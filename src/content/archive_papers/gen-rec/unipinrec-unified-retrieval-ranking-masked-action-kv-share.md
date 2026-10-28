---
title: "UniPinRec: Unifying Generative Retrieval and Ranking at Pinterest Scale"
authors: "Hanyu Li, Yi-Ping Hsu, Aditya Mantha, Prabhat Agarwal, Laksh Bhasin et al. (20 人)"
affiliation: "Pinterest"
date: "2026-05"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "提出“全栈统一”概念：召回和排序不仅共享模型结构，还要共享输入格式、单阶段训练和线上服务栈，并以可插入现有漏斗的方式落地。做法是在 PinRec 生成式召回主干上加 Masked Action Modeling（行为 multi-hot 沿特征维拼到 item embedding 上并随机 mask，不再像 HSTU 那样交错 action token），用“过去行为序列 + 未来 feedview 曝光页”混合样本做 sampled softmax + 多头 BCE 联合训练；线上排序进程通过 CUDA IPC 直接读召回进程的用户历史 KV cache。离线 save Hit@3 比线上排序模型高 14.7%，Recall@10 持平 PinRec；L0+L1 上线后 BMI 保存 +0.95%，推送打开 +0.91%，端到端延迟 -11.1%，QPS +63.6%。"
paperUrl: https://arxiv.org/abs/2606.00422
codeUrl: null
tags:
- "Masked Action Modeling"
- "Unified Retrieval-Ranking"
- "Cross-Stage KV Cache"
- "Feedview-Centric Training Data"
- "Drop-in L0+L1 Serving"
unverified: false
---
## 核心思路

现在召回和排序往往都是大 transformer，编码的是同一份用户行为序列，分开训练、分开部署就等于把参数、训练和推理成本都付了两遍。已有的“统一”工作只统一了其中一部分：HSTU 结构共享，但召回和排序的输入格式不同（非交错 vs item/action 交错）；OnePiece 统一了训练，但上线时只承担一个阶段；RelayGR 复用了 KV，模型却是分开训练的；OneRec 这类语义 ID 端到端方案直接替换了漏斗，很难和其他召回源组合。

UniPinRec 提出 **全栈统一（full-stack unification）**：输入格式、模型、训练、服务四个维度全部统一，同时以“可插拔”的方式放进现有漏斗。设计原则是只组合 ANN 索引、cross-attention 排序、KV cache 这些成熟部件，不引入新机制。三个关键设计：

1. **Masked Action Modeling（MAM）**：行为不再作为独立 token 交错插入，而是沿特征维拼到 item 上并随机 mask，序列长度与召回完全一致；
2. **混合训练样本**：过去行为序列 + 下一次请求的完整曝光页，召回和排序两个目标在单阶段联合优化；
3. **跨阶段 KV cache 共享**：排序直接读召回 prefill 得到的用户历史 KV，排序计算从 O(n²) 降到 O(nk)。

## 整体实现思路

- 底座是 Pinterest 的 PinRec 生成式召回（12 层 causal decoder-only，sampled softmax 预测下一个 item，自回归生成多个 query embedding 后走 Faiss ANN）。
- 输入序列为 `[过去 n 个 token || 候选 k 个 token]`。每个 token 是 (Pin, surface, action, timestamp)，行为向量随机 mask。
- 过去部分保留召回的 next-item loss；被 mask 的过去位置和全部候选位置做多行为 BCE。
- 上线时由两个 Triton 进程组成：召回进程做 prefill + 自回归 decode + Faiss 检索，把历史 KV 写入共享 GPU 显存池；排序进程读取这些 KV，只对候选 token 做一次 decode，输出各行为概率。
- 上线范围：L0（召回）+ L1（轻量排序）合成一个服务，先超量召回再排序取 top K，下游 L2（TransAct V2）不变。

## 子模块实现（可复现细节）

### 1. 底座 PinRec 与召回 loss

- item 特征：OmniSage 图嵌入 + CLIP 类多模态嵌入（PinCLIP），搜索 query 用预训练搜索嵌入（OmniSearchSage）；经 MLP 投影后 L2 归一化。BMI 场景额外加入 Board 作为一种新的序列模态。
- loss：`L_s = -log exp(s(î,i⁺)) / (exp(s(î,i⁺)) + Σ_{n∈N} exp(s(î,i_n)))`，其中 `s(î,i_c) = λ·îᵀi_c − log Q(i_c)`，Q 是用 count-min sketch 估计的采样概率（logQ 纠偏），N 为 in-batch 负样本加随机负样本。
- `L_item` 对历史中所有（未 mask 的）过去位置求平均。

### 2. Masked Action Modeling

- **输入**：行为 multi-hot `a_i` 先经线性层变成稠密向量，再与 item 表征沿特征维拼接，然后送入 input projector 映射到 hidden 维度。
- **mask 调度**：过去位置以 `p_mask` 独立 mask（消融最优为 0.2）；候选（未来）位置一律 mask，因为推理时候选上的行为未知。
- **[MASK] 类别**：在行为词表上额外加一维，用来区分“行为未知”和“没有行为”。
- **不泄漏**：在因果注意力下，`z_i` 只依赖 `Φ_i` 和 `{(Φ_t, m_t⊙a_t)}_{t<i}`。
- **相对交错方式的好处**：上下文长度不膨胀；排序模型可直接从召回 checkpoint 初始化；随机 mask 起到去噪正则的作用，迫使模型在没有行为信息时依赖 item 内容。

### 3. 注意力掩码

- M-FALCON 式：过去部分为标准因果注意力；每个候选位置可看全部 n 个过去位置，但候选之间互不可见。
- 所有候选共享相同的 position id、feedview 类型和时间戳，保证打分无偏、与批次组成无关。
- 复杂度从 O((n+k)²) 降到 O(n²+nk)，用 PyTorch flex attention 编译成 block-sparse 融合 kernel。

### 4. 联合 loss

```
L_action = Σ_c w_c [ (1/|M_past|) Σ_{i∈M_past} BCE(h_c(z_i), a_i^c)
                   + (1/k) Σ_{j=1..k} BCE(h_c(z'_j), a'_j^c) ]
L = L_item + L_action
```

- 每种行为 c（impression-only、click、save、share、hide 等）各有一个 MLP 头 `h_c`，输出标量 logit；`w_c` 为调参得到的权重，同时用来平衡与 next-item loss 的比重。
- 单阶段训练，item embedder 不冻结，同时接收两个目标的梯度。

### 5. 数据构造

- **Feedview 中心**：召回通常只用行为序列训练，排序只用曝光日志训练。这里每条样本由“过去正向行为序列 + 后续一次请求的完整曝光页（带行为标签，含无行为负例）”组成。
- 训练时无行为的 feedview 只保留 10%，以放大稀有行为类别；评测不做下采样，用随机化 replay 数据集，保持真实分布。
- 最初在 Spark 里按 user_id/timestamp 预先 join，后来升级为 **Ray 训练器内 join**：行为序列和 feedview 分别存为 Iceberg 表，按 user ID 哈希分桶，训练时在内存中 join。这样消除了历史序列的 fanout 和数据重复，context 长度、采样比例、过滤规则都变成训练时可调的参数。

### 6. 服务：跨进程 KV 共享

- 沿用 PinRec 的 Triton ensemble：拼装用户历史 → 自回归召回 → CPU 上的 Faiss（IVF-HNSW，每日构建）ANN 检索；在 Faiss 之后新增一个排序节点。
- `Faiss.search_and_reconstruct` 同时返回候选 ID 和建索引时存下的 embedder 输出向量，直接作为排序的候选 token，省掉 embedder 前向和特征拉取，也保证召回和排序对同一份表征打分。
- 召回和排序是两个独立 OS 进程（各自的 CUDA context）。每个召回副本预分配形状为 `[L, S, H, n, D]`（层、slot、KV 头、历史长度、头维度）的 GPU 显存池，开机时把 CUDA IPC handle 导出到文件；排序进程打开 handle，映射同一块物理显存，读取 KV 时不经过 CPU。
- slot 轮转复用；排序时把当前请求所在 slot 的过去 KV 拷进自己的 decode cache，只前向候选 token，代价为 O(nk)。

### 7. FP8

- 用 Transformer Engine 融合 LayerNorm + Linear + 激活；训练前向用 E4M3、反向用 E5M2；离线指标约掉 0.5%。
- 坑：TE 要求展平后的 `[B*S, D]` 首维是 8 的倍数，召回自回归步 S=1，只能攒批，导致 QPS 上升但延迟变差，所以线上暂时用 bf16。

## 实验设置与结果

离线数据为 Board More Ideas feed（论文未给规模）。Hit@3 是按 save 头排序后的 save 命中；Recall@10 是未来 feedview 中有交互的目标被任一自回归 query embedding 召回进 top10 的比例。两列使用不同评测集，主干均为 12 层。

**Table 1 联合训练 vs 基线**

| 方法 | Hit@3 ↑ | Recall@10 ↑ |
|---|---|---|
| TransActV2 + DCNv2（线上排序） | 0.088008 | N/A |
| HSTU（交错，等效长度对齐） | 0.097326 | 0.76161 |
| PinRec（线上召回） | N/A | 0.77486 |
| PinRec finetuned（冻结 embedder） | 0.095869 | N/A |
| UniPinRec w/o item loss | 0.097345 | N/A |
| **UniPinRec** | **0.10096** | **0.77659** |

- 排序：比线上 TransActV2+DCNv2 高 14.7%，也高于 HSTU 和去掉 item loss 的版本，说明召回目标反过来对排序有帮助；冻结 embedder 的“先召回后微调”方案效果最差。
- 召回：比 PinRec 高 0.2%，联合训练没有损害召回。

**Table 4 mask 比例**

| p_mask | 0.0 | 0.1 | 0.2 | 0.3 |
|---|---|---|---|---|
| Hit@3 | 0.09923 | 0.10078 | **0.10096** | 0.10075 |

**缩放**（Figure 4）：深度 2/4/8/12/24（S=1024）和序列长度 256/512/1K/2K（L=12）两条线的 Hit@3 都持续上升（约 0.097→0.103），尚未饱和；序列长度的代价是平方级，作者因此认为序列压缩值得研究。

**Table 2 单次排序前向延迟**（L40S，B=8，n=992，k=656，L=12）

| 路径 | dtype | Attn | Runtime | 延迟 ms | 加速 |
|---|---|---|---|---|---|
| Prefill | bf16 | SDPA | compile | 25.72 | 1.00× |
| Prefill | bf16 | flex | compile | 19.70 | 1.31× |
| Prefill | fp8 | SDPA | compile | 18.91 | 1.36× |
| Decode（KV 复用） | bf16 | SDPA | compile | 10.42 | 2.47× |
| Decode（KV 复用，线上使用） | bf16 | flex | compile | 8.57 | 3.00× |
| Decode（KV 复用） | fp8 | SDPA | graph | 8.77 | 2.93× |
| Decode（KV 复用） | fp8 | flex | graph | 6.56 | 3.92× |

KV 复用带来约 2.4×，fp8+CUDA graph 约 1.25×，flex attention 约 1.3×，三者基本正交。

**Table 3 线上服务**（基线为召回、排序都用 bf16 SDPA compile 各自完整前向）

| 方案 | 端到端延迟 | QPS |
|---|---|---|
| + bf16 decode flex compile（线上使用） | −11.1% | +63.6% |
| + fp8 decode flex graph | +6.7% | +109.1% |

**线上 A/B**：基线为 PinRec 召回 K(<3000) 个候选直接送下游；实验组先超量召回（BMI 约 2×，Notification 约 3×），再用 L1 头排序取 top K，下游 TransAct V2 不变。

| 场景 | 指标 | 提升 |
|---|---|---|
| Board More Ideas | surface saves | +0.95% |
| Board More Ideas | 全站 saves | +0.08% |
| Notifications | push opens | +0.91% |
| Notifications | push opens（沉默用户） | +1.72% |
| Notifications | 通知页 saves | +3.84% |
| Notifications | email clicks | +0.30% |
| Notifications | WAU | +0.09% |

## 思考与可参考价值

- **MAM 是性价比最高的部分**。如果已有基于行为序列的 transformer 召回，只需把行为类型作为特征拼到 item token 上、随机 mask、加几个 BCE 头，就能用同一个模型同时做召回和 L1 排序，序列也不需要变长。去掉 item loss、冻结 embedder 微调这两个对照都显示，联合训练本身有收益。
- **可插拔的上线策略值得学**。没有一次性替换整个漏斗，而是先把 L0+L1 合成一个服务、下游 L2 不动，这样能做干净的 A/B 和回滚，也更容易说服线上团队。
- **KV 共享走跨进程 CUDA IPC，而不是把召回和排序合成一个进程**，保留了微服务的边界。候选之间互不可见、共享 position id，排序分数就与 batch 组成无关，这是做“候选 decode 打分”时必须遵守的约束。
- **需要谨慎的地方**：(1) 线上 A/B 的基线没有 L1 排序，收益里混有“多了一层排序 + 2~3 倍超量召回”的效果，缺一个“PinRec + 独立 L1”的对照来证明统一本身的价值；(2) 离线只有一个场景，Hit@3 只报 save，没有显著性检验，模型规模也未公开；(3) 线上候选向量来自 Faiss 每日建库时的快照，而 embedder 在持续训练，两者之间存在版本差（推断）；(4) fp8 实际让线上延迟变差。
- **对电商 SID 生成式推荐的启示（推断）**：这套方法用的是稠密 embedding 加 ANN，不涉及语义 ID；论文也引用了“语义 ID 生成式召回不一定胜过稠密召回”的结论。如果走 SID 路线，可以借用同样的思路：对 beam 产出的候选 item 做“过去 KV 复用 + 候选 decode 打分”的 L1 排序，并在 SID 主干上加入 MAM 式的行为 mask 头。电商的下单行为非常稀疏，BCE 头能否学好、无行为曝光保留 10% 是否合适，都需要在自己的数据上验证。
