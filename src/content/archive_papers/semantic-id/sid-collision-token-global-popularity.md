---
title: "Don't Waste the Last Token: A Quantizer-Agnostic Quality Boost from Semantic ID Collision Resolution"
authors: "Anna Volodkevich, Anton Klenitskiy, Artem Fatkulin, Darya Denisova, Alexey Vasilev (5 人)"
affiliation: "Sber AI Lab × AI Center × HSE University"
date: "2026-09"
venue: "RecSys 2026"
topic: semantic-id
topic_name: Semantic ID
topic_icon: 🗂
idea: "把 SID 冲突消解从实现细节变成设计选择：TIGER 式追加码本的最后一个 token 通常只是组内计数器，白白浪费一个码本。作者在量化器、生成模型、SID 长度都不变的前提下，把计数器换成全局流行度分位桶（Global Popularity）或组内随机排列（Random），在 Amazon Toys 上 NDCG@10 最高 +12.7%。"
paperUrl: https://doi.org/10.1145/3773078.3841287
codeUrl: https://github.com/sb-ai-lab/sid-collisions/tree/recsys_2026
tags:
- "Semantic ID Collision"
- "Disambiguation Token"
- "Popularity Signal"
- "Quantizer-Agnostic"
- "Short Paper"
unverified: false
---
## 核心思路

单阶段生成式推荐要求 SID 与 item 一一对应，而 RQ-VAE、残差 K-means 量化总会产生冲突。业界最常用的 TIGER 做法是追加一个消歧码本，在冲突组内按 0,1,2… 编号：非冲突 item 和每组第一个 item 都拿到 0，这一层 token 分布极度偏斜，也不携带信息。

论文的观点是：**冲突消解是一个设计选择，不是实现细节**。在量化器、生成模型、SID 长度都不变的前提下，把这个计数器 token 换成既能消歧、又有意义的 token，就能免费拿到效果提升（Toys 上 NDCG@10 最高 +12.7%）。

## 整体实现思路

- 先用任意量化器得到 L 层前缀 p_i，冲突组 G_p = {i : p_i = p}，最大组大小 g_max。
- 给**每个** item（不只是冲突 item）追加一个 token z_i ∈ {0..C_c−1}，保证同一前缀内互不相同，最终 SID = (p_i, z_i)。
- 不同策略只在 z_i 的填法上有差别；生成器照常做下一个 token 预测并用 beam search 解码。

| 策略 | 信号 | 与量化器无关 | 跨组含义一致 | C_c 可调 | C_c | 额外信息 |
|---|---|---|---|---|---|---|
| Sequential [TIGER] | 计数器 | ✓ | — | ✗ | g_max | 无 |
| In-group pop. [MMGRec] | 组内排名 | ✓ | ✗ | ✗ | g_max | 流行度 |
| ZCR | 内容 | ✗ | ✓ | ✗ | C_q ≥ g_max | 量化器内部状态 |
| Random（本文） | 打散（类哈希） | ✓ | — | ✓ | C_c ≥ g_max | 无 |
| Global pop.（本文） | 流行度分位 | ✓ | ✓ | ✓ | C_c ≥ g_max | 流行度 |

## 子模块实现（可复现细节）

### Random
对每个前缀组（包括大小为 1 的组）生成 {0..C_c−1} 的一个随机排列，取前 |G_p| 个值依次分给组内 item。token 本身没有语义，但每个 token 值被更少 item 共享，作用接近随机哈希 ID。作者假设这能给模型留出更多学习协同模式的容量，同时把它作为对照组，用来拆分“分布更均匀”和“引入有用信号”两种效应。

### Global Popularity
1. 全体 item 按训练集交互次数排序，切成 C_c 个等频桶，桶号 b_i 就是首选 token（0 = 最热门）。
2. 非冲突 item 直接取 z_i = b_i。
3. 冲突组内从最热门的 item 开始依次处理，每个 item 取离 b_i 最近的空闲 token。

这样，末位 token 在所有前缀下都近似表示同一个全局流行度分位，模型可以显式看到并沿序列传递用户偏热门还是偏长尾的偏好。

### 基线
- **Sequential**：组内任意顺序编号，C_c = g_max。
- **In-group pop.**：组内按流行度排名，同一个 token 在不同组里代表不同的流行度水平。
- **ZCR**：不追加 token，而是把冲突 item 重新分到失真最小的末层质心，SID 仍完全由语义决定；需要质心和残差，且 g_max ≤ C_q，否则要重新量化。实验中用 4 层量化，保证末码本大小和 SID 长度与其他方法一致。

### 训练配置
- FAISS 残差 K-means，3 层 × C_q=256（ZCR 用 4 层）；Random/GlobalPop 的 C_c = 256；所有方法都是 4-token SID。
- GPT-2 风格 decoder-only，共 8 层、8 头、d=512，beam search。
- 代码：https://github.com/sb-ai-lab/sid-collisions/tree/recsys_2026

## 实验设置与结果

数据为 Amazon 2014 三个子集，5-core，去掉连续重复；采用全局时间切分（0.9 时间分位，以最后一个 item 为目标），避免 leave-one-out 的时间泄漏对流行度策略不公平；5 个种子取平均。

| 数据集 | #Users | #Items | #Inter. | 冲突率 | 平均组大小 | 最大组大小 |
|---|---|---|---|---|---|---|
| Beauty | 22,363 | 12,101 | 198,502 | 0.128 | 1.452 | 28 |
| Sports | 35,598 | 18,357 | 296,337 | 0.162 | 1.649 | 33 |
| Toys | 19,412 | 11,924 | 167,597 | 0.117 | 1.585 | 23 |

NDCG@10（括号内为相对 Sequential 的变化）：

| 策略 | Beauty | Sports | Toys |
|---|---|---|---|
| Sequential | 0.0182 | 0.0131 | 0.0243 |
| In-group pop. | 0.0181 (−0.8%) | 0.0129 (−1.7%) | 0.0233 (−3.9%) |
| ZCR | 0.0174 (−4.6%) | **0.0138 (+5.6%)** | 0.0242 (−0.3%) |
| Random | 0.0182 (−0.3%) | 0.0134 (+2.1%) | 0.0247 (+1.8%) |
| Global pop. | **0.0191 (+5.1%)** | 0.0134 (+2.7%) | **0.0274 (+12.7%)** |

HR@10 上 Global pop. 在 Beauty 为 +6.0%，在 Toys 为 +14.1%（0.0514 vs 0.0450），在 Sports 为 +0.5%。

结论：Sequential 在每个数据集上都至少被一种策略超过；Global pop. 在三个数据集上都优于 Sequential，也优于 Random，说明流行度信号本身有用；但没有在所有数据集上都最优的策略（Sports 上 ZCR 最好）。

## 思考与可参考价值

- **几乎零成本的 ablation**：只改离线 SID 映射表。工业 SID 管线如果还在用组内序号消歧，值得直接试一下，把末位换成流行度、价格带、类目等全局一致的分桶 token。
- **要注意的地方**：数据规模很小，Sports/Beauty 上的差异接近标准差；只验证了残差 K-means 一种量化器；流行度是静态的，没有讨论漂移、新品冷启动和 SID 定期重建的问题；也没有按头部/长尾分组拆指标。收益是否只是给 beam 加了流行度先验，需要自己检验（推断）。
- **在电商场景落地前建议检查**：自己的冲突率与 g_max；SID 重建周期是否与模型重训周期对齐；按长尾分组的指标和覆盖率；与“只在打分时加流行度先验”的对照。也可以把末 token 换成协同信号（例如协同 embedding 的聚类 ID）（推断）。
