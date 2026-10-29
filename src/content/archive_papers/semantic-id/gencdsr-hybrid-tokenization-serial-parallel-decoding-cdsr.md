---
title: "Empowering Cross-Domain Sequential Recommendation with Hybrid Tokenization and Serial-Parallel Decoding"
authors: "Yuxuan Hu, Yuhao Wang, Tianbo Huang, Chao Zhang, Ziwei Liu et al. (7 人)"
affiliation: "City University of Hong Kong × ByteDance"
date: "2026-07"
venue: "RecSys 2026"
topic: semantic-id
topic_name: Semantic ID
topic_icon: 🗂
idea: "把跨域生成式推荐的 SID 拆成「共享-专属混合的粗层 + 纯域专属的细层」两段：前 L1 层由共享编码器和域专属编码器各自做 RQ，再用 Gumbel-Softmax 门按物品选择走哪一支；残差进入第二阶段，每个域独立做 L2 层 RQ。解码端顺着这个两段结构做「两次 LLM 前向」：第一次用占位符一次性拿到所有位置的隐状态，前 L1 个 token 以状态累加方式串行出；第二次填回前段 token 后，后 L2 个 token 并行出。在三组 Amazon/Douban 跨域数据上，精度比 GenCDR 平均高约 1.5%，比 Beam Search 平均降延迟 85.1%。"
paperUrl: https://arxiv.org/abs/2607.28659
codeUrl: https://github.com/Applied-Machine-Learning-Lab/RecSys2026_GenCDSR
tags:
- "Cross-Domain Sequential Rec"
- "Shared-Specific Hybrid Tokenizer"
- "Gumbel-Softmax Codebook Routing"
- "Serial-Parallel SID Decoding"
- "Domain LoRA Adapters"
unverified: false
---
## 核心思路

GenCDSR 针对**跨域序列推荐（CDSR）**中的生成式推荐，分别在两处做了改动：

- **分词端**：现有做法要么每个域独立训一个 RQ-VAE（语义空间碎片化），要么所有域共享一个（抹平域差异）。GenCDSR 把 SID 切成两段：前 L1 层在「共享码本」和「域专属码本」之间由 Gumbel-Softmax 门选择，承担跨域共性；后 L2 层对残差做每域独立量化，承担域内细节。
- **解码端**：Beam Search 逐 token 解码慢，MTP/NEZHA 全并行又丢掉前缀依赖。GenCDSR 顺着两段 SID 结构做**两次 LLM 前向**：第一次前向后，前 L1 个 token 在轻量 head 上靠状态累加串行生成；第二次前向把它们填回，后 L2 个 token 并行生成。

结果：三组公开跨域数据上，精度比最强基线 GenCDR 平均高约 1.5%，推理延迟比 Beam Search 平均低 85.1%。

## 整体实现思路

1. 物品文本用 LLaMA-7B / Qwen2.5-7B 最后一层隐状态 mean-pooling 得语义向量 x_d。
2. **跨域混合分词**（多塔 RQ-VAE）：Stage 1 共享/专属两路各做 L1 层 RQ，Gumbel 门融合；Stage 2 对残差每域独立做 L2 层 RQ，域解码器重建。每个物品得到 `[t_1..t_L1 | t_L1+1..t_L]`。
3. **统一推荐训练**：在按时间合并的跨域混合序列 S̄_u 上，以 T5 或 Qwen3-0.6B 为主干，用两段 head 做 token 级交叉熵。
4. **域专属微调**：冻结主干 Φ，每个域训一个 LoRA Θ_d。
5. **推理**：激活目标域 LoRA，在该域 Trie 约束下做串并行解码，SID 映射回物品。

## 子模块实现（可复现细节）

### Stage 1：共享-专属分词（SST）

- 编码：`z_sh = Enc_sh(x_d)`（所有域物品共用），`z_d^sp = Enc_d(x_d)`（只用本域物品）。
- 两路各进一个独立的 L1 层残差量化，得量化结果 `z'_sh`、`z'_d^sp`。
- 路由：`π_d = f(x_d)`（MLP），`(g_sh, g_d^sp) = GumbelSoftmax(π_d; τ)`，融合 `z'_d = g_sh·z'_sh + g_d^sp·z'_d^sp`。框架图里标为 Hard Gate，即每个物品近似二选一。
- 至此前 L1 个 SID 确定。

### Stage 2：细粒度专属分词（FGST）

- 残差输入：`z''_d = (g_sh·z_sh + g_d^sp·z_d^sp) − z'_d`，即融合后的连续向量减去量化输出。
- 每域独立做 L2 层 RQ 得 `ẑ_d`，由域解码器 `x̂_d = Dec_d(ẑ_d)` 重建。
- 损失：`L = Σ_{d∈{A,B}} ||x_d − x̂_d||² + L_RQ^sh + L_RQ^{sp,A} + L_RQ^{sp,B}`，各 RQ 损失为标准形式 `||sg(r) − c||² + β||r − sg(c)||²`。
- 超参：L1=2，L2=2；每层 256 个 128 维码字；AdamW，lr=1e-3，batch 1024。

### 串并行解码（two-pass state-carry）

- Prompt 中目标 SID 位置放 L 个占位符 `<SP_1>..<SP_L>`。
- **Step 1**：一次前向得到前缀隐状态 h_0 与占位位置 h_1..h_L1。令 `s_1 = h_0`，对 l = 1..L1：
  `p_l^(1) = softmax(Head1(h_l, s_l))`，`s_{l+1} = s_l + Emb_l(t_l)`。
  串行只发生在 head 上，不重复跑主干。
- **Step 2**：把前 L1 个占位符替换为已选 token 再前向一次，得到 h^2；对 l = L1+1..L，统一以携带状态 `s_{L1+1}` 为条件并行预测：
  `p_l^(2) = softmax(Head2(h_l^2, s_{L1+1}))`。
- 打分：Trie 约束集合 T_d 内取 `Σ_{l≤L1} log p^(1) + Σ_{l>L1} log p^(2)` 最大者；beam size = 20。

### 训练两阶段

- **统一训练**：混合序列上最大化上式对数似然（参数 Φ）。
- **域专属微调**：冻结 Φ，每域 LoRA Θ_d，用该域自己的序列 S_u^d。
- T5：同 TIGER 设置，AdamW lr=5e-4，batch 256，LoRA r=8、α=32。
- Qwen3-0.6B：AdamW lr=1e-4，batch 128，LoRA r=8、α=16。
- 硬件：8×RTX PRO 6000，结果为 3 次平均。

## 实验设置与结果

### 数据集

| 数据 | 用户 | 物品 | 稀疏度 | 重叠用户 | 平均长度 |
|---|---|---|---|---|---|
| Clothing | 9,933 | 3,278 | 99.70% | 3,962 | 10.71 |
| Sports | 4,263 | 1,021 | 99.04% | 同上 | 同上 |
| Electronics | 20,728 | 10,492 | 99.93% | 11,698 | 8.30 |
| Phone | 11,762 | 2,246 | 99.88% | 同上 | 同上 |
| Book | 1,381 | 12,426 | 99.88% | 1,265 | 68.30 |
| Movie | 2,213 | 16,537 | 99.92% | 同上 | 同上 |

前两组来自 Amazon，Book–Movie 来自 Douban。leave-one-out 评测。

### 主结果（Table 2，节选 H@10 / N@10）

| 域 | TIGER | LLM4CDSR | GenCDR | GenCDSR |
|---|---|---|---|---|
| Clothing | 0.5961 / 0.5269 | 0.5818 / 0.5428 | 0.6076 / 0.5420 | **0.6097 / 0.5447** |
| Sports | 0.4667 / 0.4513 | 0.5038 / 0.3826 | 0.5182 / 0.4718 | **0.5207 / 0.4735** |
| Electronics | 0.0596 / 0.0437 | 0.0567 / 0.0384 | 0.0648 / 0.0482 | **0.0677 / 0.0491** |
| Phone | 0.0786 / 0.0537 | 0.0731 / 0.0457 | 0.1045 / 0.0691 | **0.1061 / 0.0702** |
| Book | 0.1390 / 0.1222 | 0.0745 / 0.0444 | 0.1452 / 0.1296 | **0.1469 / 0.1308** |
| Movie | 0.2473 / 0.1311 | 0.2216 / 0.1344 | 0.2622 / 0.1408 | **0.2671 / 0.1445** |

判别式 SDSR（SASRec 等）明显更弱，例如 Book 上 SASRec H@10 只有 0.0208。注意 Movie N@5 上 GenCDSR 为 0.1189，低于 TriCDR 的 0.1295。

### 解码效率（Table 3，H@10 / LT ms）

| 域 | 主干 | MTP | NEZHA | Beam Search | Ours |
|---|---|---|---|---|---|
| Clothing | T5 | 0.5833 / 0.18 | 0.5811 / 0.31 | 0.6227 / 4.60 | 0.6097 / 0.48 |
| Electronics | T5 | 0.0463 / 0.15 | 0.0316 / 0.31 | 0.0675 / 4.56 | 0.0677 / 0.44 |
| Book | T5 | 0.1062 / 0.40 | 0.0585 / 0.64 | 0.1420 / 5.03 | 0.1469 / 0.81 |
| Clothing | Qwen3-0.6B | 0.6052 / 0.57 | 0.6082 / 1.32 | 0.6348 / 47.30 | 0.6209 / 6.44 |
| Book | Qwen3-0.6B | 0.1241 / 2.21 | 0.1132 / 1.67 | 0.1658 / 50.64 | 0.1519 / 6.92 |
| Movie | Qwen3-0.6B | 0.2131 / 1.99 | 0.2454 / 1.47 | 0.3336 / 50.26 | 0.3481 / 7.09 |

- 相对 Beam Search 平均降延迟 85.1%（T5 87.5%，Qwen3-0.6B 82.7%）。
- 精度相对 MTP 平均 +21.9%，相对 NEZHA +37.9%（所有指标、两个主干平均）。
- 单位置 Hit@1：Electronics 上 MTP 0.0538、NEZHA 0.0499、Ours 0.0598；Phone 上 0.0964、0.0955、0.0969。

### 消融与分析

- **去 SST / 去 FGST**（Book–Movie，T5 与 Qwen3）：两者都掉点，去 SST 掉得更多。论文只给了柱状图，没有数值表。
- **特征保真度**：`max(0, 1 − ||[x_A;x_B] − [x̂_A;x̂_B]|| / ||[x_A;x_B]||)`，三组数据上 Ours 高于 Sh-RQ-VAE（单一共享）和 Sp-RQ-VAE（每域独立）。
- **码本分配**：总层数 4 时，SST:FGST = 2:2 最好；0:4、1:3 共享不足，3:1、4:0 细化不足。

## 思考与可参考价值

**可借鉴的点**

- **SID 分层承担不同语义**：粗层共享（或可选共享）、细层私有。这个结构可以直接迁移到「商品 / 视频 / 直播」多业务共用一个生成式召回主干的场景：比单一全局 RQ-VAE 更能保住业务内区分度，比每个业务一套独立 SID 更利于跨业务迁移。
- **解码与 SID 层级对齐**：主干只跑两次前向，串行只发生在轻量 head 上。它在 MTP（快但前缀无关）和 beam（准但慢）之间提供了一个可调的中间点，L1/L2 的切分就是旋钮。
- **统一训练 + 每域 LoRA**：多域部署的成本低，主干只维护一份。

**需要警惕的点**

- 数据集很小（Book 只有 1,381 个用户），平均 +1.5% 的增益接近噪声水平；没有工业数据和线上 A/B。
- 表格之间不一致：Table 2 的 Movie 列与 Table 3 的 T5-Ours 对不上（H@5 0.1875 vs 0.1793），Movie N@5 没有赢却被标了星号。
- Step 2 的各位置共用同一个携带状态，后段 token 之间相互独立。L2=2 时问题不大；推断：SID 更长时，后段会逐渐出现 MTP 式的一致性问题。
- 延迟是单请求的 ms 量级，beam=20 如何与两次前向、Trie 约束配合，以及 batch 吞吐，论文都没说清。Qwen3 上 Ours 仍比 MTP/NEZHA 慢 3–10 倍。
- Gumbel 门让一部分物品的前缀落在共享码本、另一部分落在专属码本，前缀空间是混合的。路由比例、码本利用率和碰撞率都没有报告，大物品池下需要自行验证。

**落地前建议核对**：在自有数据上对比「单一共享 SID + 业务前缀 token」这种更简单的基线；统计路由选择分布；在真实 serving 框架上测吞吐，而不只是单请求延迟。
