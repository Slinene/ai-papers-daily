---
title: "DPGFlow: Decoupled Preference Guided Flow Matching for Cross Domain Sequential Recommendation"
authors: "Xiaoxin Ye, Chengkai Huang, Hongtao Huang, Shoujin Wang, Lina Yao (5 人)"
affiliation: "University of New South Wales × Macquarie University × University of Technology Sydney × CSIRO's Data61"
date: "2026-09"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "把 Flow Matching 的起点从高斯噪声换成「跨域不变偏好」g_c，再用按时间步对齐的「域特定偏好」g_d 加域 embedding 作为条件，让确定性 ODE 只负责把可迁移兴趣搬运到目标 item 表征。结构上是三分支 Transformer 编码器（跨域 / X 域 / Y 域）+ 条件 Flow Transformer + 三视图对比学习，打分时把生成表征与域特定表征相加后点积 item embedding。"
paperUrl: https://doi.org/10.1145/3773078.3831749
codeUrl: https://github.com/seanye93/DPGFlow
tags:
- "Flow Matching"
- "Cross-Domain Sequential Rec"
- "Informative Prior Initialization"
- "Domain-Aware Guidance"
- "Disentangled Preferences"
unverified: false
---
## 核心思路

跨域序列推荐（CDSR）的难点在于，一条跨域行为序列里同时混着三类信号：可以跨域迁移的**域不变兴趣**、只属于某个域的**域特定意图**，以及误点、突然切换域带来的**噪声**。判别式 CDSR 方法（C2DSR、DREAM、C2DREIF 等）靠解耦加对比学习处理前两类；扩散式推荐（DiffuRec、DCRec）能建模多兴趣与去噪，但只在单域，且从高斯噪声出发、随机多步去噪，推理不稳定、开销大。Flow Matching（FMRec、FlowCF）给出了确定性、少步的替代方案，但也只有单域版本，并且默认偏好轨迹是平滑的，而跨域切换恰好会破坏这一点。

DPGFlow 的做法是：

- **换起点**：流的源端 x1 不再是高斯噪声，而是跨域编码器输出的域不变偏好 g_c。向量场只需把「可迁移兴趣」搬到目标 item 表征，传输距离更短。
- **加条件**：把两个域各自编码出的域特定偏好按原始时间步拼回统一序列 g_d，与域 embedding 一起作为 Flow Transformer 的条件。
- **加约束**：在生成表征、域感知引导、增强序列三个视图之间做对比学习。

## 整体实现思路

1. 从用户的完整跨域序列 s_c 中拆出 X 域子序列 s_x 和 Y 域子序列 s_y（保持顺序），另外构造一个增强序列 s_aug。
2. 三个 Transformer 编码器分别得到 g_c、g_x、g_y。
3. 用二值域指示把 g_x、g_y 按位置对齐，融合成 g_d。
4. 训练时在 x0（目标 item embedding）与 x1 = g_c 之间线性插值得到 x_t，由 DPG Flow Transformer 预测速度场，用 CFM 的 MSE 回归 x1 - x0。
5. 联合优化 L_CFM + L_rec（四路 CE）+ L_tri-cl。
6. 推理时从 ĝ_c 出发做 20 步 Euler 积分得到 x̂0，每个域用 (x̂0 + ĝ_域) 与该域 item embedding 做点积取 Top-k。

整体复杂度 O(n²d)，和 SASRec、DREAM 同阶，没有图传播带来的 O(|E|d) 开销。

## 子模块实现（可复现细节）

### 嵌入层

- 每个域一张独立的 item embedding 表 E_x、E_y，维度 d = 256。
- 共享位置编码 Pos：h_y = Emb(s_y) + Pos(s_y)，h_x、h_c 同理。

### Tri-Branch Contextual Encoder

- g_x = Encoder_x(h_x)：只看 X 域子序列的时序依赖。
- g_y = Encoder_y(h_y)：只看 Y 域子序列。
- g_c = Encoder_c(h_c)：看完整跨域序列，作为域不变 / 可迁移偏好。
- 论文没有给出层数和头数（需看代码）。

### 位置对齐（Positional Alignment）

每个时间步 t 只属于一个域，所以用二值指示 m_t^x、m_t^y ∈ {0,1}：

```
g_d^t = m_t^x · g_x^t + m_t^y · g_y^t
```

这样得到一条和原交互顺序一致的引导序列 g_d = {g_d^1, …, g_d^T}，保留了域边界，避免把不同域的意图混到同一个位置。

### DPG-FM 与 Flow Transformer

- 训练对：x0 = 目标 item embedding，x1 = g_c。
- 路径：x_t = (1 − t)·x0 + t·x1，t ~ U(0,1)；目标速度 u_t = x1 − x0。
- 损失：L_CFM = E ||v_Θ(x_t, t) − (x1 − x0)||²。
- 向量场：

```
v_Θ(x̂_t, t | g_d, emb_d) = Decoder(x̂_t + emb_d, g_d + emb_d)
```

emb_d 是统一序列中每个 item 所属域的 domain embedding，同时加在被生成量和条件上。论文比较了三种域引导方式：不加域 embedding、门控融合、加法融合，加法最好。

### Tri-view 对比学习

- 三个视图：h_c = x̂0（flow 生成的跨域表征）、h_d = ĝ_d（融合引导）、h_aug = Encoder_c(s_aug)。
- 增强：Crop、Mask、Reorder、Substitute、Insert 五种。
- 正对：同一用户的 (h_c, h_d)、(h_c, h_aug)、(h_d, h_aug)；batch 内其他用户为负。
- 损失：L = −log( exp(h_iᵀh_j) / (exp(h_iᵀh_j) + Σ_{h⁻} exp(h_iᵀh⁻)) )，文中没有写温度系数。

### 训练目标与推理

- L_rec = CE(x̂0, i_x) + CE(x̂0, i_y) + CE(ĝ_x, i_x) + CE(ĝ_y, i_y)。
- L_total = L_CFM + L_rec + L_tri-cl，三项等权，没有调权重。
- 推理：x1 = ĝ_c，积分得到 x̂0（Eq.8：x̂0 = x1 + ∫₀¹ v dt；与第 2 节 dx/dt = −v 的符号写法不一致，以代码为准）。
- 打分：î_y = Top-k((x̂0 + ĝ_y)ᵀ E_y)，X 域同理。
- 优化：Adam，lr = 0.001，batch 512，最多 100 epoch，按验证 NDCG 早停；FMRec、DiffuRec、DPGFlow 都用 20 步采样。

## 实验设置与结果

### 数据与评测

沿用 C2DREIF 的预处理：过滤交互少于 10 次的用户和 item，去掉只在单域交互、或某一域少于 3 个 item 的用户，leave-one-out 切分。

| 场景 | 域 | #Items | #Train | #Valid | #Test | 平均长度 |
|---|---|---|---|---|---|---|
| Food-Kitchen | Food | 29,207 | 34,117 | 2,722 | 2,747 | 9.91 |
| | Kitchen | 34,886 | | 5,451 | 5,659 | |
| Movie-Book | Movie | 36,845 | 58,515 | 2,032 | 1,978 | 11.98 |
| | Book | 63,937 | | 5,612 | 5,730 | |

评测：每个测试样本 1 个正例 + 999 个随机负例，报 N@5/10、H@5/10，5 次重复取均值，配对 t 检验 p < 0.05。

### 主结果（%，节选 N@10 / H@10）

| 方法 | Movie N@10 | Movie H@10 | Book N@10 | Book H@10 | Food N@10 | Food H@10 | Kitchen N@10 | Kitchen H@10 |
|---|---|---|---|---|---|---|---|---|
| SASRec | 3.69 | 5.20 | 1.71 | 2.75 | 7.79 | 11.68 | 3.93 | 6.62 |
| DiffuRec | 6.94 | 11.17 | 2.89 | 4.80 | 9.13 | 13.21 | 4.55 | 7.67 |
| FMRec | 7.43 | 12.64 | 2.66 | 4.35 | 11.46 | 16.67 | 5.69 | 9.45 |
| C2DSR | 5.76 | 9.55 | 2.45 | 3.75 | 9.71 | 14.54 | 4.94 | 8.18 |
| ABXI | 6.31 | 10.41 | 2.18 | 3.61 | 10.50 | 14.63 | 5.75 | 9.12 |
| C2DREIF | 7.14 | 12.08 | 2.71 | 4.11 | 10.93 | 15.54 | 5.31 | 8.67 |
| DREAM | 10.58 | 16.49 | 4.87 | 7.34 | 11.74 | 17.29 | 6.37 | 10.73 |
| **DPGFlow** | **13.66** | **22.24** | **6.31** | **9.20** | **13.16** | **19.18** | **7.13** | **11.56** |
| 相对提升 | 29.13% | 34.83% | 29.59% | 25.32% | 12.11% | 10.95% | 11.95% | 7.71% |

N@5 / H@5 上 DPGFlow 分别为 Movie 11.79 / 16.48、Book 5.62 / 7.05、Food 12.08 / 15.87、Kitchen 6.20 / 8.66。Movie-Book 上提升明显大于 Food-Kitchen。

### 消融（N@10）

| 设置 | Movie | Book | Food | Kitchen |
|---|---|---|---|---|
| DPGFlow | 13.66 | 6.31 | 13.16 | 7.13 |
| −DPG | 12.35 | 5.50 | 12.91 | 6.93 |
| −Tri-CL | 11.27 | 4.46 | 12.18 | 6.32 |
| −DPG −Tri-CL | 11.09 | 4.33 | 11.64 | 6.27 |
| Flow（纯 flow 基线） | 7.43 | 2.66 | 11.46 | 5.69 |

| 域引导方式 | Movie | Book | Food | Kitchen |
|---|---|---|---|---|
| 不加域 embedding | 13.15 | 6.12 | 12.37 | 6.87 |
| 门控 | 13.62 | 6.29 | 12.91 | 7.12 |
| 加法（本文） | 13.66 | 6.31 | 13.16 | 7.13 |

几点读法：

- Tri-CL 的贡献大于 DPG（Movie 去 Tri-CL 掉到 11.27，去 DPG 掉到 12.35）。
- 「−DPG −Tri-CL」到「Flow」的大落差（Movie 11.09 → 7.43）被作者归因于解耦编码器，这是全模型里最大的一块增益。
- 「Flow」一行与主表 FMRec 的 N@10 完全相同，应是直接复用 FMRec（推断）。

### 鲁棒性与效率（只有图，无表格数字）

- 维度：64 → 256 持续上升，512 略降。
- 采样步数：10 至 50 步表现稳定；和 DiffuRec、FMRec 相比，各步数下都更好，步数很少时依然有效。
- 噪声：推理时随机插入无关 item、随机替换 item，噪声比例上升时 DPGFlow 的 NDCG@10 下降最慢。
- 冷启动：目标域 ≤4 次交互为冷用户，DPGFlow 在冷、暖两组均最优，冷组优势最大。
- 域切换：目标域和上一次交互所在域不同的样本上，单域模型明显掉点，DPGFlow 最稳，Book 域增益最大。
- 无线上实验。

## 思考与可参考价值

**值得借的点**

1. **用先验替代噪声作为生成起点。** 生成式推荐里，无论是 flow 还是扩散生成用户 / 目标表征，都可以把起点设为编码器给出的用户表征，生成过程退化为少步的「残差精修」。电商里多体裁共用一个生成头时（商品、视频、直播），可以用体裁无关的共享编码当起点，体裁专属编码当条件。
2. **按时间步对齐的域条件。** 把每个位置替换成该位置所属域的专属编码，再整体作为 cross-attention 条件，是一种便宜又保留时序的多域条件注入方式，适合商品和视频混合的行为序列。
3. **域 embedding 用加法即可。** 门控没有带来额外收益。

**需要警惕的点**

1. **生成部分的真实贡献没有被单独证明。** 消融中去掉 DPG 和 Tri-CL 后 Movie 仍有 11.09，远高于 FMRec 的 7.43，且最终打分是 x̂0 + ĝ_y，域特定分支直接参与排序。缺一个关键对照：去掉 flow，直接用 ĝ_c + ĝ_y 加四路 CE 和对比学习打分。若这个对照接近 13.66，那么本文本质是「解耦多任务编码器 + 对比学习」，flow 只是锦上添花（推断）。
2. **采样评测。** 1 正 999 负的 sampled metric 会扭曲方法排序，作者自己引用了 Krichene & Rendle 的批评文章。在工业里要用全量召回或曝光负样本复评。
3. **规模。** 只有两个 Amazon 双域数据集，训练序列 3 到 6 万，没有超过两个域的设置，没有线上验证。最强基线 DREAM 出自同一作者组。
4. **文本细节。** 主表有疑似录入错误（TCSR Kitchen N@10 = H@10 = 5.66；PCDSR Book H@10 = 2.31 < H@5 = 2.60）；推理 ODE 的符号前后不一致；结论写「从噪声到数据」，与正文「以 g_c 初始化」矛盾。

**对 Semantic ID 生成式推荐的关系**

DPGFlow 在连续 embedding 空间里生成，再与 item embedding 点积召回，不涉及 SID 或自回归解码。如果想接到 SID 体系，可以考虑把 x̂0 作为 SID 解码器的前缀条件或 soft token，或者在 SID codebook embedding 空间里做 flow（推断，论文未涉及）。上线前还要单独测 20 步 Decoder 前向的延迟。
