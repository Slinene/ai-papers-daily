---
title: "SAGE: Sequence-level Adaptive Gradient Evolution for Generative Recommendation"
authors: "Yu Xie, Xingkai Ren, Ying Qi, Yao Hu (4 人)"
affiliation: "小红书 (Xiaohongshu)"
date: "2026-01"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "把 OneRec-V2 的 GBPO 在推荐里的毛病归结为「对称保守」(Symmetric Conservatism)：正负样本共用一个保守上界，冷启动正反馈被压住、被拒绝主导的负反馈又挡不住多样性塌缩。SAGE 用三件事改它：序列级几何平均重要性比（GSPO 式）、正样本放宽上界到 1+eps_boost（DAPO Clip-Higher 式）、负样本按 slate 类目熵低于滑动均值的程度加大惩罚（BAPO 式），再加 GDPO 式先分目标组内归一化再加权聚合的 advantage。实验在 Qwen3-8B 上同时跑 Semantic-ID（OneRec-SAGE）和原生文本（TextRec）两种动作空间。"
paperUrl: https://arxiv.org/abs/2601.21452
codeUrl: null
tags:
- "Asymmetric Clipping"
- "Sequence-Level Importance Ratio"
- "Entropy-Aware Penalty"
- "Multi-Objective Advantage Decoupling"
- "Native-Text Item Generation"
unverified: false
---
## 核心思路

小红书团队把 OneRec-V2 中 GBPO（Gradient-Bounded Policy Optimization）在推荐场景的问题概括为 **Symmetric Conservatism（对称保守）**：

- GBPO 对正负样本使用对称、保守的边界（有效 ratio r ≤ 1），**罕见正信号**（冷启动 item 在旧策略下概率极低）拿不到足够的更新；
- 对负样本的静态约束在「被拒绝主导」的推荐反馈下挡不住**多样性塌缩**；
- GRPO 式把多目标 reward 加权求和后再组内归一化，会出现 **Reward Collapse**，不同表现的样本得到相同 advantage。

文中引用的现象：冷启动视频播放下降 44.7%，cluster density 上升 11.7%（论文没有给出这两个数的实验设置）。

SAGE（Sequence-level Adaptive Gradient Evolution）把 LLM-RL 里已有的几个改进拼到推荐上：GSPO 的序列级重要性比、DAPO 的 Clip-Higher、BAPO 的 Entropy-Clip（改成负样本动态惩罚）、GDPO 的多 reward 解耦归一化。为说明问题出在优化器而不在 tokenization，作者在 **Semantic-ID（OneRec-SAGE）** 和 **原生文本（TextRec）** 两种动作空间上都做了评估。

## 整体实现思路

1. **数据文本化**：用户画像与近期行为按主题聚合成按时间排序的自然语言描述；item 用标题、描述、内容理解标签和统计特征渲染成文本；label 是由后续行为（浏览时长、收藏、分享、评论、关注、点赞）构造出的 item 序列。
2. **SFT 预热**：Qwen3-8B，小规模高质量数据训 1 epoch（并回灌 RLHF 阶段的高质量样本），只求学会格式和粗粒度偏好。
3. **RLHF（SAGE）**：每个用户用旧策略采样 K 个长度 L=10 的 slate → 计算多目标 reward 与 slate 类目熵 → 解耦归一化得到 advantage → 序列级 ratio + 非对称裁剪的 PPO 代理损失 → 更新参数并 EMA 更新历史熵均值。

问题形式化：给定上下文 c，策略 π_θ 自回归生成 S=(i_1,…,i_L)，优化 max_θ E_{S~π_θ(·|c)}[Σ_m w_m R_m(S)]。

## 子模块实现（可复现细节）

### 1. 序列级重要性比

r_slate(θ) = exp( (1/L) · Σ_{t=1..L} log[ π_θ(i_t | u, S_<t) / π_old(i_t | u, S_<t) ] )

即逐 token 比值的几何平均，L=10。作者的解释是用户反馈作用在 item/列表层面，token 级 ratio 方差大；几何平均相当于「整个 slate 在新策略下的平均概率增益」。

梯度写成：

∇J = E[ r_slate/Φ(S,A) · A_SAGE · (1/L) Σ_t ∇log π_θ(i_t|u,S_<t) ]

其中 1/L 把序列级 log-prob 之和的尺度对齐到 r_slate（约等于 1），避免偏好长序列；Φ 是自适应分母。

### 2. 非对称自适应裁剪

**Case A：正样本 Boost（A ≥ 0）**

- 论文式(4)：r_slate > 1+ε_boost 时 Φ_pos = 1/(1+ε_boost)，否则为 1；文字说明是「有效梯度系数维持在 1+ε_boost」，让成功的冷启动 item 以超线性方式涨概率。
- ε_boost 建议区间 [0.2, 0.5]，实验取 **0.3**。
- 算法 1 的实现写法：下界 ε⁻ = ε_clip，上界 ε⁺ = ε_boost。

**Case B：负样本熵感知惩罚（A < 0）**

- 论文式(5)(6)：Φ_neg = max(1, (1 − r_slate)/λ(H(S)))，λ(H(S)) = 1 + β · tanh(max(0, H̄ − H(S)))。
- H(S) 为 slate 多样性分（如类目熵），H̄ 为历史多样性的滑动平均，β 为多样性温度，实验取 **0.5**。
- H(S) < H̄ 时 λ > 1，惩罚加大；否则 λ ≈ 1，退回 GBPO 边界。
- 算法 1 的实现写法：下界 ε⁻ = λ − 1，上界 ε⁺ = ε_clip。

**PPO 代理损失**：r_clip = clip(r, 1−ε⁻, 1+ε⁺)，ℓ = min(r·A, r_clip·A)，L_SAGE = −(1/(|B|·K)) Σ ℓ。

> 注意：式(4)/(5) 的分母形式和算法 1 的 clip 区间并不等价（例如按式(4) r/Φ = r·(1+ε)，并不会「锁在 1+ε」），复现时建议以算法 1 的非对称 clip 为准（推断）。

### 3. 多目标信号解耦（Decouple-then-Aggregate）

A_SAGE(S) = Norm_batch( Σ_m w_m · (R_m(S) − μ_m^group)/(σ_m^group + ε) )

对每个目标先在同一用户的 K 个采样组内做 z-score，再按 w_m 加权求和，最后在整个 batch 上再做一次 z-score，使 advantage 近似标准正态。目标示例为点击、时长、评论。

### 4. TextRec 动作空间

- 每个上下文提供候选池 I(c)，item 用标题/标签/类目关键词渲染；
- 模型输出长度 L 的 slate，只能从候选池里选，确定性解析与合法性检查，匹配不到的输出丢弃或映射为 null action；
- 采样用 nucleus sampling，温度 0.9。

### 5. 训练配置

| 项 | 取值 |
|---|---|
| Backbone | Qwen3-8B |
| Slate 长度 L | 10 |
| SFT | 1 epoch |
| RLHF 优化器 / lr | AdamW / 5e-6 |
| ε_boost | 0.3 |
| β | 0.5 |
| 组大小 K、ε_clip、RL 步数、w_m | 未报告 |

## 实验设置与结果

**数据**：Amazon Product Reviews（Beauty / Sports / Toys，1996-05 至 2014-07）；RecIF-Bench（约 1.2 亿交互、20 万用户，短视频/广告/商品三域，按用户留出 20% 测试）。

**基线**：SASRec；ReaRec、TIGER、LC-Rec-8B；OneRec-GRPO、OneRec-GBPO、OneRec-SAGE（基于 OpenOneRec 公开 checkpoint）；Only SFT (TextRec)；TextRec（SAGE）。

### Amazon 准确率（Table 1，节选 R@10 / N@10）

| 方法 | Beauty R@10 | Beauty N@10 | Sports R@10 | Sports N@10 | Toys R@10 | Toys N@10 |
|---|---|---|---|---|---|---|
| SASRec | 0.0639 | 0.0289 | 0.0389 | 0.0178 | 0.0658 | 0.0294 |
| LC-Rec | 0.0764 | 0.0424 | 0.0418 | 0.0225 | 0.0549 | 0.0285 |
| OneRec-GRPO | 0.0924 | 0.0545 | 0.0547 | 0.0310 | 0.0953 | 0.0579 |
| OneRec-GBPO | 0.0928 | 0.0550 | 0.0551 | 0.0317 | 0.0958 | 0.0581 |
| OneRec-SAGE | 0.0932 | 0.0557 | 0.0553 | 0.0320 | 0.0960 | 0.0585 |
| Only SFT (TextRec) | 0.0495 | 0.0204 | 0.0263 | 0.0139 | 0.0571 | 0.0212 |
| **TextRec** | **0.0973** | **0.0590** | **0.0575** | **0.0339** | **0.1018** | **0.0622** |
| 相对 GBPO | +4.84% | +7.27% | +4.35% | +6.94% | +6.26% | +7.05% |

### Amazon 多样性与冷启动（Table 2，Cold = 训练集交互频次最低 5%）

| 方法 | Beauty Ent@10 | Beauty Cold-R@10 | Sports Ent@10 | Sports Cold-R@10 | Toys Ent@10 | Toys Cold-R@10 |
|---|---|---|---|---|---|---|
| OneRec-GBPO | 2.285 | 0.326 | 2.274 | 0.282 | 2.315 | 0.365 |
| OneRec-SAGE | **2.551** | **0.619** | **2.528** | **0.567** | **2.574** | **0.705** |
| TextRec | 2.420 | 0.487 | 2.510 | 0.460 | 2.485 | 0.522 |
| 提升（SAGE vs GBPO） | +11.64% | +89.9% | +11.17% | +101% | +11.19% | +93.2% |

### RecIF-Bench（Table 3，节选）

| 方法 | 短视频 Pass@32 | 短视频 Recall@32 | 广告 Recall@32 | 商品 Recall@32 | Label Pred AUC | Interactive Recall@32 | Label-Cond Recall@32 |
|---|---|---|---|---|---|---|---|
| TIGER | 0.1061 | 0.0132 | 0.0581 | 0.0283 | 0.6675 | - | 0.0123 |
| LC-Rec | 0.1306 | 0.0180 | 0.0723 | 0.0416 | 0.6139 | 0.2394 | 0.0170 |
| OneRec-GRPO | 0.2122 | 0.0369 | 0.0964 | 0.0538 | 0.6912 | 0.3458 | 0.0235 |
| OneRec-GBPO | 0.2134 | 0.0377 | 0.0979 | 0.0545 | 0.6918 | 0.3481 | 0.0248 |
| OneRec-SAGE | 0.2142 | 0.0381 | 0.0983 | 0.0554 | 0.6919 | 0.3495 | 0.0254 |
| Only SFT (TextRec) | 0.0920 | 0.0107 | 0.0235 | 0.0161 | 0.6028 | 0.1660 | 0.0128 |
| **TextRec** | **0.2196** | **0.0392** | **0.1015** | **0.0568** | **0.7017** | **0.3648** | **0.0261** |

### RecIF-Bench 短视频多样性与冷启动（Table 4）

| 方法 | Entropy@10 | Cold-Recall@10 |
|---|---|---|
| OneRec-GBPO | 4.284 | 0.521 |
| OneRec-SAGE | **4.455** | **0.637** |
| TextRec | 4.317 | 0.594 |

### 消融（Amazon-Beauty，Figure 5，仅归一化柱状图）

- 去掉 Positive Boost（ε_boost=0）：Cold-Start Recall 下降最多；
- 去掉 Entropy Penalty：Entropy@10 明显下降；
- 用加权 reward 求和替代信号解耦：NDCG@10 等指标下降。

论文没有给出消融的具体数值，也没有线上 A/B。

**作者的观察**：SAGE 增加探索、提升长尾覆盖；在 SID 动作空间上强探索换来多样性，但准确率增益很小；原生文本动作空间在同样探索下更能保持准确率。

## 思考与可参考价值

**可以直接借鉴的**

- **正样本单独放宽上界**：如果 RL 阶段新品/长尾曝光被压低，把正 advantage 样本的上界从 1+ε 放到 1+0.3 左右，几乎零成本；
- **负样本按 slate 熵加权惩罚**：熵低于 EMA 的被拒 slate 罚得更重，是在 RL 目标里直接对抗同质化的轻量办法，电商可以换成叶子类目熵或店铺熵；
- **多目标先组内归一化再加权**：点击/加购/成交量级和方差差异很大，GDPO 式解耦能避免高方差目标吞掉低频目标，建议默认采用；
- **序列级几何平均 ratio**：SID 多 token 场景下减少单 token 抖动带来的裁剪噪声。

**需要警惕的**

- 公式前后不一致：式(4)/(5) 与算法 1 不等价，复现要自己定规则；
- SID 空间上 SAGE 相对 GBPO 的准确率提升在小数点后第三、四位，没有方差和显著性；
- TextRec 的优势混入了「从候选池选」与「全量 SID 生成」的任务难度差异，也没有 TextRec+GBPO 对照，主表准确率提升不能归因到 SAGE；
- 冷启动指标翻倍、准确率几乎不变，是否是热门命中换冷门命中，论文没有分析；
- K、ε_clip、reward 定义和权重都未公开，也没有代码。

**落地前建议检查**（推断）：在自己的 SID 体系里做 GBPO vs SAGE 的同空间对照；监控 Boost 对热门品的放大效应；类目分布有季节性时确认熵 EMA 不会漂移；如果考虑原生文本 + 候选池方案，要把召回候选的成本和生成延迟一起算，不能直接和 SID beam search 比。

**结论**：这篇论文本质上是把 LLM-RL 里成熟的非对称裁剪和多 reward 解耦搬到 OneRec 式生成推荐上，对冷启动和多样性有明确帮助，对准确率帮助有限。适合作为改裁剪规则的参考，结论本身证据偏弱。
