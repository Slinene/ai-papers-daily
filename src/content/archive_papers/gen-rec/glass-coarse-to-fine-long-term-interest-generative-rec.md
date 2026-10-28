---
title: "Coarse-to-Fine Long-term Interest Modeling for Generative Recommendation"
authors: "Shiteng Cao, Junda She, Bin Zeng, Ji Liu, et al. (12 人)"
affiliation: "Tsinghua University × BUPT × Kuaishou"
date: "2026-02"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "GLASS 的核心主张：生成式推荐是粗到细的生成，SID 的前缀（决定落在哪个语义簇）和后缀（在簇内定位具体 item）需要不同形态的长期兴趣信号，不能像 SIM/DualGR 那样一刀切地注入。前缀侧用 SID-Tier：利用一级码本很小（64 个码）的特点，统计长期历史与每个一级码原型的余弦相似度分布直方图，压成一个兴趣 token 拼进 encoder，给第一个 SID「冷启动」。后缀侧用 Semantic Hard Search：把已生成的第一个 SID 当作检索 key，从长期历史里捞出同簇的 item，经第二路 cross-attention + 自适应门控融合进 decoder，校准后续细粒度 token；再用语义邻居扩充或缩小一级码本解决检索结果过稀的问题。"
paperUrl: https://arxiv.org/abs/2602.05663
codeUrl: null
tags:
- "Long-term Interest"
- "Prefix vs Suffix"
- "SID-Tier"
- "Semantic Hard Search"
- "Codebook Resizing"
unverified: false
---
## 核心思路

生成式推荐（GR）是粗到细的生成：第一个 SID 决定落在哪个语义簇，后续 SID 在簇内定位具体 item。作者认为这两步需要的长期兴趣信号不同：

- **前缀（sid1）**：还没有任何路径，需要**簇级的全局偏好**，帮助选对语义分支。
- **后缀（sid2、sid3）**：簇已确定，需要**与当前意图相关的 item 级历史**，在簇内区分细节。

此前把 SIM 搬进 GR 的 DualGR 对两者一视同仁（均值池化 + 输入层硬路由）。GLASS 分别设计了两个模块：

1. **SID-Tier**：把长期历史压成一个「用户对每个一级码的兴趣强度直方图」，作为额外 token 送进 encoder，增强第一个 SID 的预测。
2. **Semantic Hard Search（SHS）**：第一个 SID 生成后，以它为 key 从长期历史中检索同簇 item，作为第二路 cross-attention 的 K/V，经门控融合后校准后续 token。

另外用 **Sparsity-Aware Augmentation**（语义邻居补齐 / 缩小一级码本）解决检索结果太少的问题。

## 整体实现思路

- **SID**：RQ-VAE 量化多模态 embedding，3 层，公开集码本 [64, 128, 128]。
- **序列切分**：最近 50 条为短期序列，更早的为长期历史（平均约 900~1000 条）。
- **Encoder**：输入 `[E_short ; e_tier]`，即短期序列的 SID token 加上 1 个 SID-Tier token。
- **Decoder**：每层先 self-attention，再并行两路 cross-attention（短期 encoder 输出 / 检索序列），门控融合后过 FFN；线性头投到当前层码本。
- **训练**：三层 code 的 NLL 之和，teacher forcing。

## 子模块实现（可复现细节）

### SID-Tier（增强第一个 SID）

1. **原型**：一级码本每个码 k 的原型 `h̃_k = mean{h_v : c0(v) = k}`，即该簇所有 item 多模态 embedding 的均值。
2. **兴趣直方图**：把相似度区间 [−1, 1] 等分为 N 档，对长期历史中每个 item 计算与 `h̃_k` 的余弦相似度并计数：`t_k[j] = Σ_{v∈H_long} I(bin(cos(h̃_k, h_v)) = j)`。
3. **注入**：`x = concat(t_0, …, t_{K0−1}) ∈ R^{K0·N}`，`e_tier = MLP(x) ∈ R^d`（MLP 维度 256），接在短期序列之后送入 encoder。

只依赖用户历史，可离线预算。一级码本只有 64 个码，所以「用户 × 每个语义簇」的交叉统计可以全量计算。

### Semantic Hard Search（增强后续 SID）

- **检索**：生成 `ĉ0` 后，`H_ret = {c(v_i) | v_i ∈ H_long, c0(v_i) = ĉ0}`，取这些历史 item 完整 SID 的 embedding 作为 `E_ret`。
- **双路 cross-attention**：
  - `X = SelfAttn(Lookup(H_dec))`
  - `Z_short = CrossAttn_θ(X, O_enc, O_enc)`
  - `Z_ret = CrossAttn_φ(X, E_ret, E_ret)`
- **门控**：`g = σ([Z_short ; Z_ret] W_g)`，`Z = (1−g)⊙Z_short + g⊙Z_ret`。
- 生成第一个 SID 时检索为空；beam search 中每条 beam 的 `ĉ0` 不同，各自检索。

### Sparsity-Aware Augmentation

论文举例：长期历史 1000 条、一级码本 128 时，平均每个桶只能检索到约 7.8 条，信息量不足且噪声大。

- **Semantic Neighbor**：用一级码 embedding 的两两余弦相似度预建 top-k 邻居表；检索长度 `< τ` 时把邻居码对应的历史 item 并入。
- **Codebook Resizing**：缩小一级码本，让每个桶装更多 item。论文把它表述为「第一层负责密度、后续层负责精度」。

## 实验设置与结果

- **数据**（只保留正反馈作为序列）：
  - Taobao-MM（点击，采样 1 万 item）：189,423 用户，26.5 万训练样本，平均历史 987。
  - KuaiRec（watch ratio > 100%）：3,790 用户，10,728 item，平均历史 884。
- **超参**：embedding 维度 96，dropout 0.1，AdamW lr 1e-4，8 头，4 个 encoder/decoder block。
- **基线**：ID 类（Caser / HGN / GRU4Rec / SASRec / Bert4Rec / S3-Rec / HSTU）；SID 类（TIGER / DualGR）。

### 主结果

| 数据集 | 模型 | R@1 | R@5 | R@10 | R@20 | N@3 | N@10 |
|---|---|---|---|---|---|---|---|
| Taobao-MM | HSTU | .0274 | .0512 | .0784 | .1023 | .0384 | .0495 |
| Taobao-MM | Tiger | .0280 | .0756 | .1076 | .1498 | .0448 | .0627 |
| Taobao-MM | DualGR | .0306 | .0781 | .1126 | .1487 | .0438 | .0653 |
| Taobao-MM | **GLASS** | **.0372** | **.0934** | **.1284** | **.1723** | **.0582** | **.0782** |
| KuaiRec | DualGR | .0445 | .0932 | .1292 | .1678 | .0632 | .0821 |
| KuaiRec | **GLASS** | **.0467** | **.0971** | **.1345** | **.1742** | **.0659** | **.0855** |

Taobao-MM 上相对最强基线：R@1 +21.57%，N@3 +29.91%，R@10 +14.03%。KuaiRec 上各指标约 +3.8%~+4.9%，作者归因于 KuaiRec 的多模态特征质量较低。

### 消融与分析

- **SID-Tier**：R@5 .0702 → .0842；acc1 .2410 → .2485；P1（top-1 beam 下第一层正确率）.1470 → .1587。
- **SHS**：主要提升 acc2 / P2；两者叠加时 R@10、N@10 最高。
- **稀疏增强**：Codebook Resizing 的 R@10 最高；Semantic Neighbor 在不缩码本时有效，与 CR 叠加时略降。
- **门控**：固定权重 0.5 在一级码本小时有效，码本变细后反而掉点；可学门控的平均值随检索长度上升。
- **CRP（beam = 20）**：第二层正确前缀的排名退化从 1.25 降到 0.98（−22%）；第三层从 0.19 降到 0.13（−31%）。

### 线上 A/B

快手短视频平台两周，实验组和对照组各 3%（约 1200 万）用户：总 App 使用时长 +0.056%，人均 +0.052%（95% 置信），召回率绝对值 +3pt。

## 思考与可参考价值

- **范式**：「用生成出的前缀当检索 key」把 SIM 的 target attention 搬进了生成过程，解决了召回阶段没有 target 的问题；检索结果是 item 级 SID，decoder 可直接 attend 到具体历史 item，比 Q-Former 的簇级 latent 更适合需要「抄写」历史目标的场景。
- **诊断**：分层看 acc_i / P_i 和 CRP，能定位收益或损失发生在哪一层，可以直接复用。
- **码本设计**：一级码本大小同时影响生成难度和按前缀检索能拿到的上下文量，与「小码本更利于泛化」的结论相互印证。
- **风险**：训练时用真实 c0 检索，推理时用生成的 ĉ0，第一步出错会把错误簇的历史喂给后续步骤；论文没有分析这一点，也没讨论 beam 内逐路检索的推理成本。实验规模小，线上收益有限，代码未给出实际地址。
