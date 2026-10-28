---
title: "EGR: Embedding-Native Generative Retrieval with a Shared LLM"
authors: "Xiaodong Liu, Congfei Zhang, Hsiang-wei Chao, Siman Wang, Tong Zhao et al. (20 人)"
affiliation: "Snap Inc."
date: "2026-07"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "把生成式召回从「生成离散 SID」或「冻结物品塔后再训查询生成器」改成 embedding-native：同一个 LLM 既编码物品元数据成索引向量，又把用户行为序列编码成查询向量，两侧在同一空间里联合训练，线上直接走标准 ANN。训练用物品对对称 InfoNCE（IRL）锚定物品空间，加上带目标侧 stop-gradient 的历史到目标 InfoNCE（NIP），在 Snap DPA 广告上线拿到 CVR +2.91%。"
paperUrl: https://arxiv.org/abs/2607.23038
codeUrl: null
tags:
- "Embedding-Native Retrieval"
- "Shared LLM Dual Encoder"
- "SID-Free"
- "Stop-Gradient Contrastive"
- "Ads Retrieval"
unverified: false
---
## 核心思路

生成式召回（GR）目前有两条主线：

- **SID 路线**（TIGER、PLUM、OneRec、GR4AD、GPR）：物品编码器 → 量化器 → SID 词表 → 生成器 → grounding。四个组件，物品库一变就要给新品分配 ID。
- **Embedding 路线**（PinRec、TBGRecall）：生成稠密查询向量走 ANN，不需要 SID，但物品编码器先训好再冻结，查询侧只能事后对齐一个固定的物品空间。

EGR（Snap）的做法是 **embedding-native**：用**同一个 LLM**（Qwen3-VL-Embedding 2B + LoRA + 投影头）既把商品元数据编码成索引向量，又把用户行为序列编码成查询向量，两侧在同一空间里**联合训练**。推理时就是一次前向得到查询向量，再做最大内积检索；不预测物品 token、不量化、不 grounding。

两个损失：

1. **IRL**（Item Representation Learning）：相邻共同交互物品对的对称 InfoNCE，负责锚定物品空间；
2. **NIP**（Next Item Prediction）：用户历史到目标物品的 InfoNCE，**目标侧 stop-gradient**，防止逐样本的拉扯把索引空间搞乱。

线上作为 Snap DPA（动态商品广告）的新增召回源，CVR +2.91%，已全量。

## 整体实现思路

```
商品元数据 (title/brand/category/image)
   └─ prompt: "Represent this product for retrieval." ─┐
                                                       ├─ 共享 Qwen3-VL-Embedding 2B (LoRA) ─ last-token ─ MLP 头 ─ L2 归一化 512 维
用户历史 <view> item | <add_to_cart> item | ...        │
   └─ prompt: "Predict the next product ..." ──────────┘
物品向量 z_i  → 写入 ANN 索引
用户向量 q_u  → 每天算一次存起来，请求时实时 ANN → top-K → 下游排序
```

- 物品路径和用户路径**共享全部参数**，包括投影头。
- 训练：L = L_IRL + λ_t · L_NIP。前 10% 步只开 IRL，之后 λ_t 从 0.1 线性升到 1.0。
- 服务：物品向量离线或准实时刷入索引。新品只要编码一次就能入库，不需要重建 SID 词表或重训生成器。

## 子模块实现（可复现细节）

### 1. 物品编码（IRL 路径）

- 输入：chat template，system 为 “Represent this product for retrieval.”，user message 为 `Title: ..., Brand: ..., Category: ...`；多模态版额外把商品图送进 vision tower。
- 输出：z_i = h_φ(f_θ(x_i)) / ‖h_φ(f_θ(x_i))‖₂，直接入 ANN。
- 物品对：同一用户时间序列里**相邻**的共同交互物品 (p_a, p_b)。
- 损失：L_IRL = ½ [InfoNCE(z_a, z_b) + InfoNCE(z_b, z_a)]，其中 InfoNCE(a, b) = −log( exp(aᵀb/τ) / Σ_{b′∈{b}∪N} exp(aᵀb′/τ) )，N 是 in-batch 负样本，τ 可学习。

### 2. 用户历史编码（NIP 路径）

- 历史 H_u = (e_1, …, e_T)，每个事件是（转化类型, 物品），从旧到新排列。
- 每个事件前加转化类型 token：`<view>` / `<add_to_cart>` / `<purchase>`，事件之间用 `|` 分隔，例如：
  `<view> Title: Galaxy Watch, Brand: Samsung, Category: Electronics | <add_to_cart> Title: Coffee Maker, ... | <purchase> ...`
- system 为 “Predict the next product this user will interact with.”。
- q_u = h_φ(f_θ(H_u)) / ‖·‖₂。
- 损失：L_NIP = InfoNCE(q_u, sg(z_y))。z_y 每步由当前骨干重新计算，但对该样本不回传梯度；由于骨干共享，NIP 梯度仍会经历史分支更新参数，间接影响以后的物品向量。

### 3. 联合训练与调度

| 阶段 | IRL 权重 | NIP 权重 |
|---|---|---|
| 前 10% 步（warm-up） | 1 | 0 |
| 之后 | 1 | λ_t：0.1 → 1.0 线性 |

### 4. 训练配置

| 项 | 取值 |
|---|---|
| 骨干 | Qwen3-VL-Embedding 2B，last-token pooling |
| 投影头 | 两层 MLP（LayerNorm、GELU、dropout），从零训练，输出 512 维 L2 归一化 |
| LoRA | r=128，α=256，挂在 q/k/v/o |
| 可训参数 | 约 41M（主要是 LoRA 和投影头） |
| 优化器 | AdamW，lr 2e-5，短 warm-up 后 cosine 衰减；温度一起学 |
| 资源 | 8×H100，1 epoch，每卡 batch 64 |
| 历史长度 | 最多 20 个事件，平均约 460 token |
| 负样本 | 跨所有 DDP rank 收集，每个 anchor 有 B×W 个 |

### 5. 服务

- 线上部署是**批量加在线混合**：每个用户的查询向量每天算一次并存储，请求时取出做实时 ANN，top-K 交给下游排序。
- 对会话内意图变化大的场景，也可以在请求时在线跑用户路径，但单请求成本更高（论文未给延迟数字）。
- 向量是 L2 归一化的，所以 MIPS 等价于余弦检索，标准 ANN 设施就能用。

## 实验设置与结果

**数据**：Amazon Reviews Beauty / Sports / Toys（5-core，leave-one-out）；Snap DPA 交互日志，留出 1M 用户序列测试。Snap 数据只报相对值。指标：R@10。

### Amazon Reviews（R@10）

| 方法 | Beauty | Sports | Toys |
|---|---|---|---|
| BERT4Rec | 0.0396 | 0.0175 | 0.0332 |
| SASRec | 0.0607 | 0.0301 | 0.0626 |
| TIGER | 0.0623 | 0.0347 | 0.0547 |
| HSTU | 0.0652 | 0.0343 | 0.0566 |
| **EGR** | **0.0655** | **0.0362** | **0.0807** |

Beauty 上和 HSTU 基本持平，Sports 小幅领先 TIGER，Toys 领先次优基线（SASRec 0.0626）较多。

### Snap DPA：数据规模

训练用户从 10K 增加到 10M（4 个子集），R@10 单调上升 27%，未见饱和。

### Snap DPA：按目标物品训练频次分桶（以 >15 的头部桶为 100%）

| 训练中出现次数 | 测试样本占比 | 相对 R@10 |
|---|---|---|
| 0（冷启动） | 31.3% | 94.9% |
| 1 | 8.0% | 99.1% |
| 2 | 6.0% | 111.5% |
| 3 | 4.3% | 112.7% |
| 4 | 3.6% | 117.6% |
| 5 | 2.8% | 115.4% |
| 6–10 | 9.4% | 119.1% |
| 11–15 | 5.3% | 116.8% |
| >15 | 29.2% | 100.0% |

冷启动只比头部低 5.1%；中频桶最好，呈非单调，作者也承认这个实验没法分离其他因素。

### 多模态

| 输入 | 相对 R@10 |
|---|---|
| 纯文本 | 100.0% |
| 文本 + 图片 | 106.9% |

### 联合训练消融

| 方法 | IRL | NIP | 联合 | stop-grad | 相对 R@10 |
|---|---|---|---|---|---|
| EGR | ✓ | ✓ | ✓ | ✓ | 100.0% |
| 去 stop-grad | ✓ | ✓ | ✓ | | 95.3% |
| 只 NIP | | ✓ | — | | 93.7% |
| 只 IRL | ✓ | | — | | 26.6% |
| 两模型（IRL 训完冻结 → 训 NIP） | ✓ | ✓ | | | 86.2% |

### Loss 调度

| 变体 | IRL | NIP | 相对 R@10 |
|---|---|---|---|
| Joint（默认） | 恒为 1 | λ_t：0.1→1.0 | 100.0% |
| Balanced | 1−λ_t | λ_t | 97.9% |
| Sequential | 只前 50% | 只后 50% | 74.4% |

### 线上 A/B（Snap DPA，两周，各 10% 流量）

EGR 作为**新增召回源**，总候选配额不变，下游排序、竞价、策略、渲染都不变。

| 指标 | 相对提升 |
|---|---|
| 曝光 | +0.15% |
| CTR | +0.23% |
| CVR | +2.91% |

EGR 贡献最终曝光的 5.3%，其源级 CTR、CVR 分别是所有召回源（U2I、I2I、非个性化）平均值的 1.55 倍和 1.53 倍。实验后已在 DPA 全量。

## 思考与可参考价值

**它到底是什么**：剥掉“生成式”这个标签，EGR 就是 **共享权重的 LLM 双塔**，物品塔吃内容，用户塔吃带行为类型的内容序列，再加两个 InfoNCE。没有自回归解码，也没有多兴趣、多 token 输出。真正有信息量的是消融：**物品塔和用户塔一起训比先冻物品塔高约 16%（86.2% → 100%）**，物品对损失要全程保留（Sequential 只剩 74.4%），目标侧 stop-gradient 再多拿约 5%。

**不足**：

- Amazon 只报 R@10，基线没有同骨干的冻结 LLM 双塔，也没有 PinRec；Beauty 和 Sports 的领先非常小。
- Snap 实验全是相对值，单次运行，没有方差。
- 没有和 Snap 现有 U2I 双塔离线对比，线上也只是新增源，看不出能否替代。
- 用户向量日更，2B 模型做实时编码的延迟和成本没有报告；历史最长只有 20。

**对电商 SID 生成式推荐的参考**：

1. **当强基线用**：在讨论 SID 路线收益之前，先用同一 LLM 训一个联合双塔，看 SID 在召回上到底赢多少（推断：很多“GR 收益”可能来自 LLM 内容表示本身，而不是来自生成）。
2. **冻结 embedding 再量化有代价**：“两模型”掉 13.8% 和 SID 流程里“冻结 embedding → RQ → 训生成器”的割裂是同一类问题。可以考虑联合 tokenizer，或者至少在生成器训练里保留物品侧对比辅助损失。
3. **可直接迁移的小技巧**：全程保留物品对 InfoNCE 作为锚；目标侧 stop-gradient；行为类型 token 前缀；跨 DDP rank 汇集负样本。
4. **上线前要核实**：全量商品用 2B 模型刷 embedding 的算力和刷新频率；日更用户向量在电商实时场景下损失多少；冷启动桶的表现在自家类目分布上能否复现；和现有双塔在同配额下的离线对比。
