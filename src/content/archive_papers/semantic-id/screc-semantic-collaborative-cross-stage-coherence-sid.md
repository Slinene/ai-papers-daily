---
title: "Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation"
authors: "Jiayi Dan (1 人)"
affiliation: "Kuaishou Technology"
date: "2026-09"
venue: "RecSys 2026"
topic: semantic-id
topic_name: Semantic ID
topic_icon: 🗂
idea: "把两阶段 SID 生成式推荐的问题概括为「跨阶段信息解耦」：tokenizer 只看文本语义、缺协同信号；生成阶段对 code 重新 embedding，又把语义先验丢了。SCRec 双向补信息：tokenize 前把 SASRec top-10 相似商品的标题拼成文本，与本商品文本一起用 sentence-T5 编码后加权（a）再做 RQ-VAE；生成阶段用门控把冻结的语义向量融进 code embedding，并加 InfoNCE 和 Poincaré 球测地距离做对齐。"
paperUrl: https://arxiv.org/abs/2609.13678
codeUrl: https://github.com/DanJiayi/SCRec
tags:
- "Textualized Collaborative Signals"
- "Semantic-Guided Generation"
- "Hyperbolic Manifold Alignment"
- "Cross-Stage Coherence"
- "Plug-in Module"
unverified: false
---
## 核心思路

SID 生成式推荐通常分两阶段：先把商品文本经 PLM 编码，再用 RQ-VAE 量化成 code 序列（tokenization）；然后让生成模型自回归地解码下一个商品的 code（generation）。作者认为这两个阶段存在**跨阶段信息解耦**：

- **tokenization 只看语义**：文本相近但协同模式差别很大的商品（跑鞋和高跟鞋）拿到相近的 code；协同上很近但文本不同的商品（跑鞋和足球）拿到差得很远的 code。下游生成因此更难学。
- **generation 丢掉语义**：生成模型对 code 重新做 embedding，只靠交互数据学习，PLM 语义先验逐渐流失，而解码目标偏偏又是「语义」code，结果是语义失真。

SCRec 的思路是**双向补信息**：tokenization 时把协同信号「文本化」后注入，generation 时把语义先验融回去；另外，code embedding（离散码本）和语义表示（PLM 稠密隐状态）的几何结构不同，所以作者在双曲空间里再做一次流形对齐。

## 整体实现思路

1. **离线**：预训练一个 SASRec，取每个商品的 top-10 相似商品。把相似商品的标题拼成 Prompt_CF，与商品自身的 Prompt_main 一起用 sentence-t5-base 编码，按 a : (1-a) 加权后送进 RQ-VAE，得到同时带有语义和协同信息的 SID。
2. **生成训练**：对历史序列中的每个 item，用语义向量生成 code 位置权重，把 l 个 code embedding 聚合成 e_code；与投影后的语义向量 e_sem 做标量门控融合，得到 e_fused，作为骨干（RPG 式 decoder-only、TIGER、LIGER 均可）的输入，预测下一个 item 的 code。
3. **正则**：L = L_gen + α·L_align（InfoNCE） + β·L_geo（Poincaré 测地距离）。
4. 推理时没有额外检索步骤，只多了门控融合和投影的计算。

## 子模块实现（可复现细节）

### 1. Collaborative-Enhanced Tokenization（CT）

- 相似商品：`{j1..jk} = Top-k cos(e_i, e_j)`，e 取自在训练集上预训练的 SASRec（也可以换成 Swing 等任意 CF 模型），k = 10。
- 商品自身 prompt：`"{title}; {brand}; {category}; {description}; ..."`。
- 协同 prompt：`"{title_j1}; {title_j2}; ...; {title_jk}"`，每个标题截取前 20 个词，避免被长文本主导。
- 融合：`ẽ_i = a·Encode(Prompt_main) + (1−a)·Encode(Prompt_CF)`，a ∈ {0.2, 0.5, 0.8}。两路用同一个 PLM 编码，作者认为它们天然处在同一空间，因此无需额外的对齐任务。
- RQ-VAE：`L_quant = Σ_i ||ẽ_i − ê_i||² + Σ_m ( ||sg(r_{i,m}) − q_{i,m}||² + γ||r_{i,m} − sg(q_{i,m})||² )`；codebook 大小 256，潜空间维度 256，γ = 0.25，训练 5000 epoch，lr 1e-3，batch 4096。
- 全部在离线完成，不增加线上训练和推理成本。

### 2. Semantic-Guided Generation（SG）

- h_i ∈ R^h：**冻结**的原始语义表示；E_i ∈ R^{l×d}：item i 的 l 个 code 的可学习 embedding。
- 位置权重：`w = W_h h_i`（W_h ∈ R^{l×h}），`w̃ = softmax(w / τ_w)`，τ_w 从 2 线性退火到 1；`e_code = E_iᵀ w̃`。权重按 item 生成、不全局共享，因此保留了层次信息。
- 门控融合：`e_sem = W_s h_i`，`g_i = σ(W_g [e_code; e_sem])`（W_g ∈ R^{1×2d}，标量门），`e_fused = g_i·e_code + (1−g_i)·e_sem`。
- 额外计算约 2(ld + dh + lh) FLOPs。门控形式可以换成按维度门控或多头门控，作者选的是复杂度最低的版本。
- 对比对齐：`L_align = −Σ_i log [ exp(sim(e_code_i, e_sem_i)/τ) / Σ_j exp(sim(e_code_i, e_sem_j)/τ) ]`，τ = 0.1。

### 3. Manifold Alignment（MA）

- e_code 先经过一个可学习线性层得到 ẽ_code，再映射到半径为 c 的 Poincaré 球：`z_code = c·tanh(||ẽ_code|| / (2c)) · ẽ_code / ||ẽ_code||`；`z_sem = ψ(e_sem)`，ψ 是可学习投影。
- 测地距离：`L_geo = Σ_i arccosh( 1 + 2c²||z_code − z_sem||² / ((c² − ||z_code||²)(c² − ||z_sem||²)) )`，c ∈ {0.2, 0.5, 1}。
- 复杂度 O(Nd)，低于 batch 内 InfoNCE 的 O(N²d)。
- 理论（附录 A.1）：假设 decoder logit 映射关于 d_D 是 L_f-Lipschitz、损失是 L_ℓ-Lipschitz，并且 E[d_D(z_s, z*)] ≤ ε_s，则超额生成误差 ≤ L_ℓ·L_f·(E[d_D(z_c, z_s)] + ε_s)。因此最小化 L_geo 可以收紧这个上界。
- 需要注意，融合本身仍在欧氏空间进行，MA 只起正则作用。

### 4. 训练配置

最多 300 epoch，batch 256，lr 0.01，按验证集 NDCG@10 做 patience = 20 的早停；主实验骨干沿用 RPG 的 decoder-only 生成器，其他设置与 RPG 一致；α、β、c、a 都按验证集 NDCG@10 调，最终取值论文没有给出。实验在单张 RTX 4090 上完成。

## 实验设置与结果

数据集为 Amazon Reviews 的 Beauty、Sports and Outdoors、Toys and Games，采用 leave-last-out 切分，指标为 Recall/NDCG@{5,10}。基线包括 7 个 ID 类方法和 13 个 SID 类方法（RecJPQ、VQ-Rec、HSTU、TIGER、LIGER、CoST、ETEGRec、LC-Rec、RPG、LLaDA-Rec、CoFiRec、S2GR、PIT），在统一环境下重跑。没有线上实验。

**主结果（节选，NDCG@10 / Recall@10）**

| 模型 | Beauty N@10 | Beauty R@10 | Sports N@10 | Sports R@10 | Toys N@10 | Toys R@10 |
|---|---|---|---|---|---|---|
| SASRec | 0.0318 | 0.0605 | 0.0192 | 0.0350 | 0.0374 | 0.0675 |
| TIGER | 0.0312 | 0.0592 | 0.0184 | 0.0346 | 0.0313 | 0.0594 |
| LIGER | 0.0368 | 0.0697 | 0.0228 | 0.0419 | 0.0370 | 0.0704 |
| HSTU | 0.0389 | 0.0704 | 0.0215 | 0.0414 | 0.0357 | 0.0669 |
| PIT | 0.0403 | 0.0783 | 0.0243 | 0.0462 | 0.0432 | 0.0839 |
| RPG | 0.0460 | 0.0795 | 0.0252 | 0.0440 | 0.0484 | 0.0857 |
| **SCRec** | **0.0546** | **0.0930** | **0.0319** | **0.0570** | **0.0582** | **0.0973** |
| 相对提升 | +18.70% | +16.98% | +26.59% | +23.38% | +20.25% | +13.54% |

**消融（NDCG@10）**

| 变体 | Beauty | Sports | Toys |
|---|---|---|---|
| 完整 | 0.0546 | 0.0319 | 0.0582 |
| w/o CT（a=1） | 0.0502 | 0.0275 | 0.0538 |
| w/o SG（g=1，同时去掉对齐） | 0.0444 | 0.0237 | 0.0463 |
| w/o MA | 0.0491 | 0.0297 | 0.0547 |
| w/o CA（InfoNCE） | 0.0509 | 0.0305 | 0.0558 |

注意：w/o SG 在三个数据集上都**低于** RPG 基线（0.0460/0.0252/0.0484），说明增益主要来自生成侧的语义融合与对齐。

**协同注入方式 / 对齐方式对比（NDCG@10）**

| 方法 | Beauty | Sports | Toys |
|---|---|---|---|
| MMGRec 式拼接 | 0.0512 | 0.0280 | 0.0557 |
| LETTER 式对比 | 0.0523 | 0.0258 | 0.0526 |
| L2 对齐 | 0.0517 | 0.0285 | 0.0551 |
| MMD 对齐 | 0.0504 | 0.0306 | 0.0573 |
| 本文（文本化 CT + Poincaré MA） | 0.0546 | 0.0319 | 0.0582 |

LETTER 式在 Sports 和 Toys 上甚至不如 w/o CT（0.0275/0.0538）；L2 对齐在 Sports 上低于 w/o MA（0.0285 对 0.0297）。

**换骨干（NDCG@10）**

| 骨干 | Beauty | Sports | Toys |
|---|---|---|---|
| TIGER → +SCRec | 0.0312 → 0.0372 (+19.23%) | 0.0184 → 0.0213 (+15.76%) | 0.0313 → 0.0366 (+16.93%) |
| LIGER → +SCRec | 0.0368 → 0.0418 (+13.59%) | 0.0228 → 0.0252 (+10.53%) | 0.0370 → 0.0417 (+12.70%) |

开销（Beauty，10 次平均）：TIGER 单步训练时间 +6.70%、推理时间 +6.19%；LIGER 分别为 +1.98% 和 +0.54%。

其他分析：α、β、c 在扫描范围内都优于所有基线（只给了图）；t-SNE 显示加 MA 后两种表示的分布明显更接近；**门控分布**方面，没有 MA 时 g 大量接近 0，即模型偏向使用稠密语义向量，加上 MA 后 g 集中在 0.5 附近，code embedding 被更充分地利用。

## 思考与可参考价值

- **最实用的是 CT**：用已有 i2i 关系取 top-k 邻居，把标题拼成第二路 prompt，同一个 encoder 编码后加权，再量化。不改 RQ-VAE 或 RQ-KMeans 的目标，也不加训练阶段，比 LETTER 式对比损失更稳（本文 Sports/Toys 上的结果支持这一点）。电商里 Swing、co-buy、co-view 都可以直接当邻居源。
- **SG 的本质**是「历史 item 输入侧再补一路冻结稠密语义特征 + 标量门」。由于 w/o SG 低于 RPG，主要增益来自这里。论文没有和「直接把 h_i 加到输入」这一最简基线比较，落地前要自己补上这个对照，判断门控和对齐是否值得引入（推断）。
- **门控诊断值得照搬**：在任何「SID embedding + 稠密特征」混合输入的系统里，都可以监控门控或注意力权重。如果模型几乎只用稠密特征，SID embedding 就会退化，进而影响 SID 解码质量。
- **双曲 MA 先复现再用**：它的动机主要来自类比，理论上界对「为什么非用双曲空间不可」没有区分力；c 的选择和 ||z||→c 附近的数值稳定性都要调。它在 Amazon 小数据集上比 L2/MMD 高约 0.001-0.004 的 N@10，放到工业规模是否成立需要自己验证。
- **上线前要核查**：(1) CT 会让 SID 随 i2i 更新而漂移，要评估冲突率、码本利用率和重训节奏；(2) 新品和冷启动商品的邻居质量差，要分冷热分桶评估；(3) 推理时要额外查语义向量表，要评估大 catalog 下的存储和延迟；(4) 论文只做了 Amazon 小数据集、没有多种子方差和线上 A/B，相对提升里有多少来自重跑基线的偏差（TIGER 在 Beauty 上 R@5 仅 0.0378）需要谨慎看待。
- 代码：https://github.com/DanJiayi/SCRec
