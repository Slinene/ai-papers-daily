---
title: "FLUID: From Ephemeral IDs to Multimodal Semantic Codes for Billion-Scale Livestreaming Recommendation"
authors: "Xinhang Yuan, Zexi Huang, Anjia Cao, Xudong Lu, Zikai Wang et al. (9 人)"
affiliation: "TikTok × ByteDance"
date: "2026-05"
venue: "RecSys 2026"
topic: semantic-id
topic_name: Semantic ID
topic_icon: 🗂
idea: "直播间平均只播约 40 分钟，item ID embedding 在生命周期内根本学不收敛，作者因此主张：item ID 短命时，ID 主导效应是根本瓶颈，应当在候选侧彻底退役 item ID，而不是再往 ID 旁边加多模态特征。FLUID 用短视频+直播跨域联合训练的单塔多模态编码器（SigLIP2 + Qwen3-Embedding-0.6B）产出 128 维切片向量，RQ-KMeans 量化成 4×64 的 LUCID，房间级 LUCID 按层多数投票得到；两者经 prefix n-gram embedding 以独立 token 晚融合进 Zenith++ 排序器，再用三阶段 warmup（加切片、撤 ID、加房间）替换 item ID。"
paperUrl: https://arxiv.org/abs/2605.21832
codeUrl: null
tags:
- "ID-Free Ranking"
- "Livestreaming Cold-Start"
- "Late Fusion Tokens"
- "Staged Warmup"
- "Prefix N-gram SID Embedding"
unverified: false
---
## 核心思路

直播间寿命很短（中位约 40 分钟）。作者在一天的生产流量上统计了 item ID embedding 的 L2 范数随开播时长的变化：40 分钟时范数约 0.86，稳态约 1.2，低了约 28%。也就是说，大多数直播间在整个生命周期里，ID embedding 都处于欠训练状态。

已有的多模态推荐方案（冻结 embedding 当特征、对齐、离散成 Semantic ID）都把多模态信号当成 **item ID 旁边的补充**，排序器很容易走 ID 记忆的捷径，用不上多模态信号。作者的判断是：**当 item ID 短命时，ID 主导效应是根本瓶颈，应该在候选侧把 item ID 彻底退役**，而不是继续往上叠融合技巧。

FLUID（Framework for Live Universal ID-free Recommendation）的做法：

1. 用短视频 + 直播跨域联合训练一个单塔多模态编码器，借短视频更干净、更稠密的监督；
2. 用 RQ-KMeans 把 2 分钟切片 embedding 量化为 4 层、每层 64 码字的语义码 **LUCID**（Live Universal Content IDentifier），再按层多数投票得到房间级 LUCID；
3. 用 prefix n-gram 方式把 LUCID 映射为 embedding，以 **独立 token** 的形式晚融合进 token 化排序骨干（Zenith++）；
4. 用 **三阶段 warmup**（加切片 → 撤 ID → 加房间）完成从 ID 到 LUCID 的迁移。

线上（合计用户超过十亿的直播平台）：Quality Watch Duration +0.55%，Cold-Start Room Views +2.05%，Active Hours +0.05%。

## 整体实现思路

```
直播/短视频 2min 切片
  ├─ 视觉帧 → SigLIP2-base ViT → 2层MLP → T_v
  └─ 标题/OCR/ASR/作者简介/评论/贴纸标签 → T_t
        ↓  [T_v, T_t, EOS] → Qwen3-Embedding-0.6B（单塔）
        ↓  EOS 隐状态 → 线性投影 → z ∈ R^128
        ↓  RQ-KMeans (L=4, N=64)
  切片 LUCID [c1..c4]  ──逐层多数投票(累计切片)──>  房间 LUCID
        ↓ prefix n-gram 查表（切片表 / 房间表独立）
  s (slice token)            r (room token)
        ↓
  Zenith++ token 交互排序骨干：候选侧 token = {r, s}，不再有 item ID g
```

训练分两块，分别评测：多模态编码器（检索基准）和排序模型（CTR AUC + 线上 A/B）。

## 子模块实现（可复现细节）

### 1. 跨域多模态编码器

- **数据**：query-to-item（Q2I）对。query 为用户搜索词或 MLLM 合成的关键词；item 为直播和短视频的 2 分钟内容切片；正例由点赞、分享、完播等用户行为构造。很多直播间在攒够交互前就下播了，所以把短视频一起放进同一个 embedding 空间联合训练。
- **结构**：
  - Vision：SigLIP2-base（原生分辨率 ViT）+ 两层 MLP projector，输出视觉 token `T_v ∈ R^{N_v×D_h}`；
  - Text：标题、OCR、ASR 转写、作者简介、观众评论、贴纸标签，分词得到 `T_t ∈ R^{N_t×D_h}`；
  - Fusion：Qwen3-Embedding-0.6B 处理 `T = [T_v, T_t, [EOS]]`，取 EOS 隐状态线性投影到 128 维 `z`。
  - 选单塔，是为了让视觉和文本在 LLM 的每一层都发生交互，而不是只在输出层相遇。
- **损失**：InfoNCE + 假负例屏蔽。在一个 batch 内，如果两个 query embedding 的相似度高于预设阈值，就把这整对负例丢掉（阈值论文未给）。
- **两阶段训练**：(1) 对齐阶段只训练 MLP projector 和输出投影，保住 LLM 的预训练语义；(2) 联合微调阶段解冻全模型，用更低的学习率端到端训练（具体学习率未给）。

### 2. RQ-KMeans 离散化与房间级 LUCID

- 直接把 `z` 喂给排序器效果不好：通用视觉语言目标与用户-物品交互信号不对齐，而且共享 MLP 处理冻结特征时，表达力不如排序器的 embedding 查表。
- 用 RQ-KMeans 量化，`L=4`，`N=64`，得到 `[c1,c2,c3,c4]`，例如 `[33,42,63,3]`。
- **为什么不用 RQ-VAE**：在线上流式重训的节奏下，RQ-VAE 的码本会塌缩；K-means 拟合一次后分区就稳定了。
- **切片级 LUCID**：描述当前 2 分钟内容（例如主播从聊天切到唱歌）。
- **房间级 LUCID**：在每一层 `l` 上，对该房间所有 *累计* 切片取出现最多的码字。残差量化本身是粗到细解耦的，所以逐层投票不会把不同层的语义混在一起。（推断：房间 LUCID 会随开播时间推移更新，论文没有说明更新频率。）

### 3. Prefix n-gram LUCID embedding

level-wise 解码为每层建一张 `N×d` 的表 `E_l`，再把 `E_l(c_l)` 拼接起来。问题是在残差量化中，同一个 `c_l` 在不同前缀下指向完全不同的语义区域。

改用复合键（参考 Zheng et al. RecSys'25）：

```
c̄_l = Σ_{k=1..l} c_k · N^(l−k),   l = 1..L
e_LUCID = E1(c̄1) ∥ E2(c̄2) ∥ … ∥ EL(c̄L)
```

第 `l` 层的表从 `N` 行扩到至多 `N^l` 行。论文举例（取 N=4）：`[0,2]` 得 `c̄2=2`，`[3,2]` 得 `c̄2=14`，落在不同槽位。按 N=64 推算，第 3、4 层最多约 26 万和 1677 万行（推断，论文未讨论实际行数）。

切片和房间 LUCID 用同样的方案，但 **embedding 表各自独立**：如果共享，稳定的房间语义和快速变化的切片语义会被塞进同一个参数空间。

### 4. 融合方式

记 `g` 为 item ID embedding，`s`、`r` 分别为切片、房间 LUCID 的 prefix n-gram embedding。

- **早融合**（合成一个候选 token `T_early={h}`）：
  - 替换 `h = s`；拼接 `h = W[g∥s]`；门控 `h = αg + (1−α)s`，`α = σ(f(u))`，`u` 可以是 ID embedding 本身，也可以是曝光计数、ID 范数等侧信息（LARM 式门控）。
- **晚融合**：`T_late = {g, s}`，作为独立 token，由骨干学习两者的交互。
- **FLUID 最终形态**：`T_FLUID = {r, s}`，`g ∉ T_FLUID`。

### 5. 三阶段 warmup

直接切换到 `T_FLUID` 不稳定，深层原因是 **优化不对称**：短命 ID embedding 虽然泛化差，但带有很强的 item 级记忆信号，联合训练早期会被骨干先吸收，压制学得慢但更能泛化的 LUCID。所以每个阶段只改一个 item 侧组件，其余作为稳定锚点：

| 阶段 | 训练方式 | 操作 | 锚点 | 相对 AUC |
|---|---|---|---|---|
| Stage 1 切片接入 | 离线批训练 | 从收敛的 item-ID ckpt 初始化，加切片 LUCID 独立 token | item ID | +0.22% |
| Stage 2 ID 退役 | 离线批训练 | 逐步把候选侧 item ID 置零，只剩切片 LUCID | 切片 LUCID | +0.11% |
| Stage 3 房间接入 | 在线流式 | 用热的切片表初始化房间 LUCID 表，再独立训练 | 切片 LUCID | +0.23% |

Stage 3 之后，继续生产环境的流式增量训练。Stage 2 的置零节奏（线性还是阶梯、持续多少步）论文没有给出。

## 实验设置与结果

**排序数据**：生产 Zenith++ 管线，168B 样本、4,552 个特征、98 个目标。骨干和训练配置与 Zenith++ 保持一致。离线指标为 CTR 目标的 AUC/Logloss，Δ 是相对变化。

### 主结果（Table 3）

| 配置 | AUC | Logloss |
|---|---|---|
| baseline（带 item ID） | 0.7784 | 0.1264 |
| baseline + Slice LUCID | 0.7801 (+0.22%) | 0.1263 (−0.08%) |
| baseline w/o item ID | 0.7748 (−0.47%) | 0.1273 (+0.65%) |
| w/o item ID + Slice & Room LUCID (FLUID) | 0.7802 (+0.23%) | 0.1262 (−0.19%) |

### 线上 A/B（Table 4，相对生产基线，n.s. = p<0.05 下不显著）

| 指标 | +Slice | −ID | FLUID |
|---|---|---|---|
| Quality Watch Duration | +0.43% | −0.02% | +0.55% |
| Quality Watch Session | +0.39% | −0.10% | +0.51% |
| Cold-Start Room Views | +1.15% | +1.58% | +2.05% |
| Niche Room Views | +0.69% | +2.23% | +2.87% |
| Unique Watched Tags | +0.55% | +0.20% | +1.63% |
| Stay Duration | n.s. | −0.05% | +0.07% |
| Active Hours | n.s. | n.s. | +0.05% |

解读：只加 SID 能提升参与度和多样性，但留存不动，此时 SID 只是辅助信号；只去 ID 能放出被 ID 压住的长尾流量，但损失排序效率；只有 FLUID 在三组指标上都为正。

### 融合与训练配方消融（Table 7，baseline AUC 0.7784）

| 类别 | 方法 | AUC | Δ |
|---|---|---|---|
| 早融合 | 用 LUCID 替换 ID | 0.7774 | −0.13% |
| 早融合 | 拼接 ID + LUCID | 0.7785 | +0.01% |
| 早融合 | LARM 可学习门 | 0.7783 | −0.01% |
| 早融合 | LARM 特征门 | 0.7785 | +0.01% |
| 晚融合 | EM3 CIC 对齐损失 | 0.7785 | +0.01% |
| 晚融合 | 独立 token（=Stage 1） | 0.7801 | +0.22% |
| 训练配方 | 从零联合训练 | 0.7784 | +0.00% |
| 训练配方 | Stage 2（只剩切片） | 0.7793 | +0.11% |
| 训练配方 | Stage 3（切片+房间，FLUID） | 0.7802 | +0.23% |

- 看 LARM 可学习门的收敛权重（Figure 5，按 ID 范数分桶），门偏向 item ID，切片 LUCID 基本没被用到；
- 从零联合训练会塌缩成只用 ID；
- Stage 3 之后再把 item ID 加回来，AUC 没有额外提升，作者据此认为 LUCID 已经吸收了 ID 在候选侧提供的信息。

### LUCID embedding 设计（Table 5）

| 变体 | AUC |
|---|---|
| Level-wise 解码 | 0.7793 (+0.12%) |
| Prefix n-gram（本文） | 0.7802 (+0.23%) |
| 切片/房间共享表 | 0.7798 (+0.18%) |
| 独立表（本文） | 0.7802 (+0.23%) |

### 编码器消融（Table 6，内部检索基准，R@10/R@50）

| 方法 | Live Q2I | Live I2Q | Video Q2I | Video I2Q |
|---|---|---|---|---|
| CLIP-B/32 + Albert-V2 | 43.96/59.95 | 45.57/60.87 | 73.40/84.36 | 72.86/83.46 |
| + Qwen3-Embedding | 46.15/60.43 | 47.18/61.32 | 84.74/91.97 | 85.30/91.40 |
| + SigLIP2 ViT（本文） | 47.44/61.62 | 48.67/62.71 | 87.10/93.35 | 87.20/93.39 |
| 双塔（浅融合） | 45.37/59.90 | 47.00/61.42 | 83.68/90.91 | 84.59/91.52 |
| 单阶段训练 | 45.01/59.83 | 45.78/60.53 | 84.13/91.47 | 84.10/91.43 |

骨干替换的收益最大；单塔和两阶段训练在每一列检索指标上都有提升。定性案例（Figure 4）中，LUCID (39,41) 对应游泳，(17,26) 对应舞蹈，同一码下的直播切片和短视频语义一致。

## 思考与可参考价值

**值得借鉴的结论**

- **SID 进排序器要作为独立 token**：在同一骨干上，早融合各方案在 −0.13%~+0.01% 之间，独立 token 是 +0.22%。如果门控融合没效果，先按 ID 范数分桶看门权重有没有塌缩到 ID。
- **ID → SID 的迁移是训练配方问题**：从零联合训练收益为 0，分阶段热启动才能拿到收益。我们在电商里做“SID 替换商品 ID”的实验时，如果从零训练没有效果，不应直接断定 SID 无效。
- **流式场景用 RQ-KMeans**：码本稳定比重建误差更重要。
- **Prefix n-gram 键 + 粒度分表 + 粗粒度表由细粒度表热启动**，这几项都可以直接照做。
- **评估不能只看 AUC**：FLUID 的离线 AUC 与只加 SID 几乎一样，区别体现在线上的冷启、长尾、多样性和留存。

**需要保留的地方**

- 离线收益很薄（+0.23%，相对只加切片仅 +0.01%），“退役 ID 更好”主要靠线上指标支撑，而线上实验没有给出流量、时长和置信区间。
- 复现关键参数缺失：Stage 2 的置零节奏、假负例阈值、学习率、房间 LUCID 的刷新频率、编码器训练数据规模。
- 码本质量（利用率、碰撞率）和 N^l 扩表的实际开销都没有报告；只退役了候选侧 item ID，用户序列侧和作者等 ID 特征是否保留没有说清楚。
- 98 个目标只报告了 CTR。

**对电商 GR/SID 的落地建议**（推断）：直播带货商品、短期活动 SKU、新品都属于短寿命 item，可以先画出 ID 范数随曝光时长的收敛曲线，确认 ID 是否欠训练；对长寿命爆品，ID 的记忆价值可能仍然高于 SID，更合适的是按 item 生命周期分群决定是否退役 ID，而不是全量替换。
