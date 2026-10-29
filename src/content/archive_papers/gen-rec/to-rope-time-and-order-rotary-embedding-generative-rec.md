---
title: "Beyond Index-Only RoPE: Integrating Time and Order for Generative Recommendation"
authors: "Xiaokai Wei, Jiajun Wu, Daiyao Yi, Reza Shirkavand, Michelle Gong (5 人)"
affiliation: "Roblox × University of Maryland"
date: "2025-10"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "把生成式推荐里的「位置」拆成两种含义：事件在序列里的序号（order）和发生的墙钟时间（time），主张两者都应作为 RoPE 的旋转角来源，而不是把时间塞进额外 embedding 或注意力偏置。TO-RoPE 在角度域把 index 角和 time 角线性融合，并给出 early fusion、split-by-head、split-by-dim 三种实例；关键发现是同一旋转平面内混合两种角度会互相干扰，按头或按维度硬切分更稳。"
paperUrl: https://arxiv.org/abs/2510.20455
codeUrl: null
tags:
- "Rotary Position Embedding"
- "Temporal Encoding"
- "Time-Aware Attention"
- "Positional Encoding Ablation"
- "Roblox"
unverified: false
---
## 核心思路

生成式推荐（GR）把用户历史当作 token 序列做 next-item 预测，位置编码大多照搬 LLM：只编码 token 在序列中的序号。但推荐序列和文本不同，每个事件同时有**序号（order）**和**发生时间（time）**两个坐标，用户行为有短时突发、长期节律和日/周周期。现有做法用时间差特征、分桶时间 embedding 或注意力上的相对时间偏置（HSTU、TiSASRec）来补时间信息。

这篇 RecSys 2026 短文（Roblox）的主张是：**RoPE 本身就能做时间编码**，只要把旋转角的来源从序号换成（或加上）时间戳。难点在于如何同时保留序号和时间。作者提出 Time-and-Order RoPE（TO-RoPE），在角度域统一表达两种来源，并指出把两者加在同一个旋转平面里会互相干扰，因此推荐按**维度**或按**头**硬切分：一部分平面/头只转序号，另一部分只转时间。

## 整体实现思路

1. 把每个事件的原始时间戳归一化成标量 tau_i。
2. 为 time 构造一组多尺度频率 omega^t_k（对应从 session 级到长期的周期），与原有的 index 频率 omega^p_k 并存。
3. 每个旋转平面的角度 = 门控加权的 index 角 + time 角；门控 lambda_k 取值决定实例：全 0 为 index-only，全 1 为 time-only，共享软门为 early fusion，按平面或按头取 0/1 为 split。
4. 只对 Q、K 做旋转，V 不变，注意力 kernel 不变，因此兼容 FlashAttention，几乎不加参数。
5. 骨干为 GPT-2 式自回归 decoder-only，12 层、约 85M 参数，所有位置编码方案共用该骨干对比。

## 子模块实现（可复现细节）

### 1. 时间标量与 Time RoPE

- 时间归一化：`tau_i = (u_i - u_ref) / s`，u_ref 是任意锚点，s 让时间量级与 index 范围接近（秒或天视业务而定）。注意力只依赖 Delta tau，因此与时区、锚点无关。
- 时间角：`theta^t_{i,k} = tau_i * omega^t_k`，或乘一个正的可学尺度 `alpha^t_k`。
- 每个平面的贡献相当于时间核 `cos(Delta tau * omega^t_k)`，周期 `2*pi / omega^t_k`。高频平面关注短间隔（突发），低频平面关注长程 recency。
- 头内相似度 `S(Delta tau) ∝ sum_k w_k cos(Delta tau * omega^t_k)`：当两次交互的时间差接近日周期、周周期的整数倍时，多个频带同相，内积变大，从而表达周期性。

### 2. 时间频率库的两种构造

- **Base 形式**：`omega^t_k = base_t^(-2(k-1)/d)`，`base_t` 取 1e3 到 1e5，可再乘 alpha 适配单位。
- **按波长指定**：选定 `[lambda_min, lambda_max]`（以 tau 的单位计），令 `omega_max = 2pi/lambda_min`、`omega_min = 2pi/lambda_max`，对数等距插值 `omega^t_k = omega_max * (omega_min/omega_max)^((k-1)/(N-1))`。
- 与 index RoPE 一样需保持频率单调（对数间隔），防止频带交换；omega_min 要覆盖最长节律，omega_max 要能响应 session 级突发。

### 3. 统一形式

对一个旋转维度为 d 的注意力头，有 N = d/2 个平面，平面 k 的角度：

`theta_k(i) = (1 - lambda_k) * alpha^p_k * i * omega^p_k + lambda_k * alpha^t_k * tau_i * omega^t_k`，其中 `lambda_k ∈ [0,1]`（可用 sigmoid 学习），alpha 为正尺度（如 softplus）。

两个 token 的相对相位：`Delta theta_k = w~^p_k * Delta i + w~^t_k * Delta tau`，其中 `w~^p_k = (1-lambda_k) alpha^p_k omega^p_k`，`w~^t_k = lambda_k alpha^t_k omega^t_k`。也就是说每个平面在角度空间是一个双特征线性模型，(w~^p_k, w~^t_k) 决定该平面对序号和时间的敏感度；也可直接学习这两个非负有效频率，并对 k 加单调约束以保留多尺度覆盖。

### 4. 三种实例

| 实例 | 门控约束 | 特点 |
|---|---|---|
| Index-only / Time-only | 全部 lambda_k = 0 / 1 | 单源 RoPE |
| Early fusion | 全局或每头共享 lambda、alpha | 两种角度在同一平面相加；角度不一致时余弦项衰减、正弦干扰项增大，大的时间相位会抵消序号对齐 |
| Split-by-dim | 每平面 lambda_k ∈ {0,1} | 部分平面只转 index，其余只转 time，消除平面内干扰；切分比例是显式容量旋钮（如 70% time / 30% index） |
| Split-by-head | 同头内所有平面共享 lambda_h ∈ {0,1} | 头专精于 order 或 time，交互靠多头混合 |

文中还提到 split-by-layer、按 GQA 的 KV 组切分等变体，但未做实验。

### 5. 训练与评测设置

- 骨干：GPT-2 式 decoder-only，12 层，约 85M 参数，item 作为词表，next-item 预测。
- 论文**未给出** base_t、s、波长范围、lambda/alpha 是否可学、序列长度、优化器等超参，复现需自行扫描。

## 实验设置与结果

**数据**：MovieLens-20M（5-core，leave-one-out）；Roblox 游戏平台内部数据（数千万用户、一年交互，最后一天为测试、倒数第二天为验证）。**指标**：HR@10/50、NDCG@10/50。**基线**：Index APE、Index APE + 分桶 time APE、HSTU 式相对偏置（时间间隔与序号偏置加到 logits），以及单源 RoPE。

### 主结果（Table 1）

| 方法 | 内部 HR@10 | 内部 NDCG@10 | 内部 HR@50 | 内部 NDCG@50 | ML HR@10 | ML NDCG@10 | ML HR@50 | ML NDCG@50 |
|---|---|---|---|---|---|---|---|---|
| Index APE | 0.5493 | 0.3805 | 0.7588 | 0.4273 | 0.3318 | 0.2007 | 0.5729 | 0.2540 |
| Index APE + time APE | 0.5510 | 0.3818 | 0.7605 | 0.4286 | 0.3335 | 0.2023 | 0.5739 | 0.2554 |
| Relative Bias (HSTU) | 0.5513 | 0.3820 | 0.7604 | 0.4287 | 0.3341 | 0.2023 | 0.5727 | 0.2550 |
| Index-only RoPE | 0.5537 | 0.3841 | 0.7612 | 0.4305 | 0.3347 | 0.2026 | 0.5737 | 0.2555 |
| Time-only RoPE | 0.5568 | 0.3865 | 0.7653 | 0.4331 | 0.3341 | 0.2027 | 0.5746 | 0.2559 |
| Index RoPE + time APE | 0.5547 | 0.3848 | 0.7627 | 0.4313 | 0.3353 | 0.2031 | 0.5746 | 0.2561 |
| TO-RoPE Early fusion | 0.5562 | 0.3855 | 0.7648 | 0.4321 | 0.3362 | 0.2037 | 0.5765 | 0.2569 |
| TO-RoPE Split head | **0.5582** | **0.3875** | **0.7663** | **0.4340** | 0.3388 | 0.2048 | 0.5767 | 0.2574 |
| TO-RoPE Split dim | **0.5582** | 0.3874 | **0.7663** | 0.4339 | **0.3406** | **0.2059** | **0.5791** | **0.2587** |

要点：(1) RoPE 系整体优于 APE 和 HSTU 式相对偏置；(2) 内部数据上 time-only RoPE 明显优于 index-only，ML-20M 上两者接近；(3) early fusion 在内部数据上低于 time-only，印证平面内干扰；(4) split 变体在两个数据集都最好。幅度上，split-dim 相对 index-only RoPE 在 ML-20M HR@10 约 +1.8%、内部数据约 +0.8%（推断，由表中数值计算）；相对 time-only RoPE 在内部数据只多 0.0014。

### 注意力行为（RQ2）

在内部数据上按层统计注意力加权的 query-key 距离和注意力熵（对头平均）。RoPE 系在中间层显著高于 APE，TO-RoPE 在所有层都高于 index-only RoPE，说明它会看更远、更多的历史事件。作者把这解释为收益来源，但明确说是推测，图中也没有给出数值。

### 切分比例（RQ3，Table 2，内部数据，比例越高 time 侧越多）

| 方法 | 0.1 | 0.3 | 0.5 | 0.9 |
|---|---|---|---|---|
| Split head HR@10 | 0.5580 | 0.5582 | 0.5579 | 0.5577 |
| Split head NDCG@10 | 0.3873 | 0.3875 | 0.3871 | 0.3871 |
| Split dim HR@10 | 0.5572 | 0.5578 | 0.5582 | 0.5574 |
| Split dim NDCG@10 | 0.3866 | 0.3871 | 0.3874 | 0.3868 |

0.3 到 0.5 最好，可作为默认值；整体对比例不敏感（HR@10 波动在 0.001 以内）。论文没有线上 A/B。

## 思考与可参考价值

**值得拿走的**：时间作为 RoPE 角度源是几乎零成本的改动，不碰 kernel、不加 token、不加特征工程。对电商来说，日内节律、周末效应、大促、复购周期都是天然的多尺度周期，按波长指定 time 频率库可以把这些先验直接写进频带，事后还能检查哪个频带被用得多。split-by-dim/head 比 early fusion 更稳这一点也有明确机理：同一平面里两个角度相加，相位不一致就会互相抵消。

**需要警惕的**：
- 增益在千分位，且没有方差或显著性检验；内部数据上 split 相对 time-only 只多 0.0014，真正的大头是「用时间」本身，而不是「怎么组合」。
- 骨干 85M、item-ID 词表、ML-20M，没有 Semantic ID 实验。SID 场景一个 item 展开为多个 code token，它们共享同一时间戳，time 平面无法区分层级，只能靠 index 平面，切分比例和效果都可能不同（推断）。
- 关键超参（s、base_t、波长范围、门控是否可学）没写，周期性论点也没有用学到的频带去验证。
- 推理时 target 位置的时间戳应取请求时刻，需要和训练口径一致；论文没讨论。
- 对比的是在 GPT-2 骨干上加 HSTU 式偏置，不是完整 HSTU，迁移到 HSTU 类架构的结论未知。

**落地建议**：已有 RoPE 的 GR 模型可以把 30% 到 50% 的平面（或头）改为按时间旋转作为一个低风险 A/B 臂；先离线多 seed 验证，并检查与已有相对时间偏置是叠加还是替换。SID 模型要额外设计层级 token 的时间处理（例如同 item 的 code token 共享时间、层级只走 index 平面）。
