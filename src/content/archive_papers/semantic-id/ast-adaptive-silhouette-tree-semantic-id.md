---
title: "Not All Branches Are Equal: Adaptive Semantic ID Construction for Generative Recommendation"
authors: "Guy Hadad, Haggai Roitman, Bracha Shapira (3 人)"
affiliation: "Ben-Gurion University of the Negev"
date: "2026-09"
venue: "RecSys 2026"
topic: semantic-id
topic_name: Semantic ID
topic_icon: 🗂
idea: "把 Semantic ID 重新看作树上的路径：每个 token 的含义由前缀决定，而不是各层独立的码本属性；作者用 RQ-VAE SID 的前缀/后缀相似度分析支撑这一点。据此提出 Adaptive Silhouette Tree (AST)：自顶向下递归 KMeans，每个节点按 silhouette 自适应选分叉数；并用 MILP 约束每个子分支至少拿到父节点 rho 比例的交互质量，保证长尾前缀有监督。"
paperUrl: https://doi.org/10.1145/3773078.3831756
codeUrl: null
tags:
- "Tree-Path Semantic ID"
- "Adaptive Branching"
- "Silhouette Clustering"
- "Mass-Constrained MILP"
- "Tokenizer-Only Comparison"
unverified: false
---
## 核心思路

生成式推荐把商品表示成离散 token 序列（Semantic ID, SID）。主流做法用 RQ-VAE、RQ-Means 等残差量化构造 SID，隐含假设是每一位 token 都有独立的全局语义。本文先检验这个假设，结论是 SID 更像**树上的路径**：每个 token 的含义由它的前缀决定。

作者在 Beauty 上用 TIGER 式 RQ-VAE 生成 4 位 SID，再用“精确匹配掩码”统计商品对的平均余弦相似度：

| 掩码 | 含义 | 平均余弦相似度 |
|---|---|---|
| 1000 | 只共享第 1 位 | 0.758 |
| 1100 | 共享前 2 位 | 0.874 |
| 1110 | 共享前 3 位 | 0.920 |
| 全局 | 随机商品对 | 0.554 |
| 0111 | 后三位相同、首位不同 | 0.582（该分析的全局基线 0.570） |

共享前缀越长越相似，而只共享后三位几乎等于随机。可见后位 token 只是在前缀条件下的一次分支选择。由此得出方法上的结论：与其先优化量化、指望路径结构自己“长出来”，不如直接构造一棵树，让 SID 就是从根到商品的路径。

作者据此提出 **Adaptive Silhouette Tree (AST)**：

- 自顶向下的分裂式层次 KMeans；
- 每个节点用 silhouette 系数**自适应选择分叉数**：稠密区域分得细，同质区域分得粗；
- 可选**质量约束**：每个子分支至少拿到父节点 rho 比例的交互质量，用 MILP 求解，保证长尾前缀有足够监督。

## 整体实现思路

1. 商品文本（title + categories + description）经 Qwen3-Embedding-0.6B 编码，再做 L2 归一化，所有聚类都在这个空间里进行。
2. SID 长度为 m。前 L = m-1 位由树生成，每一层用**独立词表** `<c_l_0> ... <c_l_{B-1}>`，B 为最大分叉数（base）。
3. 从根开始递归：对每个节点枚举候选 K，跑 KMeans，用 silhouette（V2 用加权 silhouette）打分，选最优的可行 K；把子簇编号写成该层 token，然后对每个子节点递归，直到生成 L 位或没有可行分裂。
4. 叶细化：共享 L 位前缀的商品组成一个桶，末位 token 取桶内按 item ID 的确定性排名，保证 SID 唯一。
5. 生成的 SID 交给统一的 T5 encoder-decoder 做下一商品生成。

与 RQ-VAE 的结构对比：

| 维度 | RQ-VAE | AST |
|---|---|---|
| 层间关系 | 全局共享码本作用在残差上 | 每个前缀是父簇在原始空间里的一个 KMeans 子簇（laminar family） |
| 码利用率 | 存在码本坍缩 | 空簇丢弃，所有码都被用到 |
| 合法序列 | B^m 的笛卡尔积，只有 N 个合法，1-N/B^m 可超 99.9% | 恰好等于商品集合 |
| 唯一性 | 需要额外处理冲突 | 容量约束保证叶桶 ≤ B，末位排名唯一 |
| 冷启动 | 逐层残差查码，误差会累积 | 逐层走最近中心，O(BdL) |

## 子模块实现（可复现细节）

### 1. 自适应分叉范围

节点 v 有 n_v 个商品，位于第 l 层，候选 K_v ∈ [K_min, K_max]：

- K_max(n_v) = min(B, n_v − 1)，保证 silhouette 有定义；
- K_min(n_v, l) = max(2, ⌈n_v / B^(L−l)⌉)。剩余 L−l 层最多只能形成 B^(L−l) 个前缀，所以大节点必须分得足够多。归纳可证最终每个叶桶不超过 B 个商品，末位 token 一定能唯一分配。

### 2. 分裂选择

- 每个候选 K 跑 KMeans（scikit-learn，最多 50 次迭代，10 次随机初始化）；
- 打分 Sil(S_v, K) = (1/|S_v|) Σ_i (b_i − a_i) / max(a_i, b_i)，其中 a_i 是簇内平均距离，b_i 是到最近其他簇的平均距离，使用欧氏距离；
- K 从小到大评估，取分数最高的可行 K，平局取较小值；连续 5 个候选不提升就早停（patience 5）；
- 大节点的 silhouette 在最多 2,000 个子样本上估计。

### 3. 理论性质

- **Telescoping 畸变分解**：总畸变 Σ_i ||ẽ_i − μ_leaf(i)||² = Σ_l Σ_v Δ_v，其中 Δ_v ≥ 0 是节点 v 分裂带来的簇内方差下降。每一项都定义在同一个原始空间里，可以逐项检查哪些分裂真正有用。
- **自适应不劣于固定分叉**：在叶子总数固定、2 ≤ K_v ≤ B 时，W*_adaptive ≤ W*_fixed，因为固定分叉树是自适应树的特例；商品分布不均匀时自适应更有表达力。

### 4. 质量约束（AST-V1 / AST-V2）

商品质量 p_i 可取交互频次，归一化后 Σ p_i = 1；没有质量信息时取均匀分布。节点内的局部质量为 π_i = p_i / Σ_{r∈S_v} p_r。约束要求每个子簇 C_j 满足 Σ_{i∈C_j} π_i ≥ rho，因此 K_v ≤ ⌊1/rho⌋，候选区间收紧为 [max(K_min, 2), min(K_max, ⌊1/rho⌋)]。区间为空时停止递归。

**AST-V1（固定中心可行性修正）**：先跑普通 KMeans，分配已经可行就保留；否则固定中心，求解 MILP：

```
min  Σ_i Σ_j ||ẽ_i − μ_j||² z_ij
s.t. Σ_j z_ij = 1            ∀i
     Σ_i π_i z_ij ≥ rho       ∀j
     z_ij ∈ {0,1}
```

求得的解是给定中心下全局最优的可行分配，W_KM ≤ W_A ≤ 任意其他可行分配的畸变。之后用普通 silhouette 打分。

**AST-V2（质量感知的约束细化）**：

- 打分用加权 silhouette WSil = Σ_i π_i Sil({i}, K)；子样本按 π_i 抽取，估计无偏；
- 从 KMeans 中心出发交替执行两步：(i) 用同一个 MILP 求最优可行分配；(ii) 中心更新为质量加权均值 μ_j = Σ π_i ẽ_i / Σ π_i。迭代固定轮数或到收敛为止；
- 两步都不会增大 W_π = Σ_j Σ_{i∈C_j} π_i ||ẽ_i − μ_j||²，所以 W(0) ≥ W(1) ≥ … ≥ 0，相当于带约束的 Lloyd 算法。高频商品得到更精细的表示，与下游训练损失的权重一致。

rho 的扫描范围是 0.001 到 0.05，最优值随数据集变化。

### 5. 冷启动

新商品编码后，在每一层走向最近的子中心，共 L 步，每步最多比较 B 次，代价 O(BdL)，与商品总数无关。作者也指出，即使拿到合法 SID，下游模型并没有在这个新序列上训练过。

### 6. 下游生成器（所有方法共用）

T5 encoder-decoder，6 层 encoder + 6 层 decoder，dropout 0.15，initializer factor 0.02，LN eps 1e-6，batch size 256，学习率 1e-3，weight decay 1e-4，bf16，early stopping patience 5，单卡 NVIDIA RTX 6000。

## 实验设置与结果

**数据**：Amazon Reviews 5-core，序列截断到 20，leave-last-out 划分，指标为 Recall/NDCG@{5,10}。

| 数据集 | 用户 | 商品 | 稀疏度 | 平均长度 |
|---|---|---|---|---|
| Beauty | 22,363 | 12,101 | 99.93% | 8.88 |
| Toys | 19,412 | 11,924 | 99.93% | 8.63 |
| Sports | 35,598 | 18,357 | 99.95% | 8.32 |
| Health | 38,609 | 18,534 | 99.95% | 8.97 |
| Home | 66,519 | 28,237 | 99.97% | 8.29 |

**基线**：RQ-VAE（TIGER）、RQ-VAE-L（LETTER）、Qinco2、RVQ（GRID）、CoST、RQ-Means、RQ-Means-B（OneRec/EAGER）、RRS、SEATER、CRVQAE（HiGR）。所有方法共用 Qwen3-Embedding-0.6B 和同一个 T5 生成器，只比较 tokenizer。

### 主结果（R@10 / N@10，%）

| 数据集 | 最强基线 R@10 | AST-V1 R@10 | AST-V2 R@10 | 最强基线 N@10 | AST-V1 N@10 | AST-V2 N@10 |
|---|---|---|---|---|---|---|
| Beauty | 6.98 (RQ-Means) | 7.31 | **7.51** | 3.86 (RQ-Means) | 4.20 | **4.28** |
| Toys | 7.07 (RVQ) | 7.75 | **7.94** | 3.72 (RVQ/SEATER) | 4.24 | **4.31** |
| Sports | 4.09 (RVQ) | 4.62 | **4.62** | 2.23 (RVQ) | **2.54** | 2.51 |
| Health | 6.30 (CoST) | 6.40 | **6.64** | 3.49 (CoST) | 3.58 | **3.68** |
| Home | 2.63 (CoST) | 2.64 | **3.02** | 1.51 (CoST) | 1.43 | **1.67** |

R@5 节选：Beauty 5.12 vs 4.63，Toys 5.27 vs 4.63，Health 4.48 vs 4.33（CoST），Home 2.06 vs 1.86（CoST）。

- AST-V2 平均 R@5 4.00、R@10 5.95、N@5 2.67、N@10 3.29；相对最强非 AST 基线分别提升 12.68% / 13.55% / 12.66% / 13.45%，整体 13.08%。
- 20 个数据集-指标组合中，AST-V2 在 19 个上最好或并列最好；Sports N@10 被 AST-V1 超过。
- 按每个格子的最强基线计算，R@10 增幅在 5.4%（Health）到 14.8%（Home）之间（推断，由表 1 算出）。

### Head / Tail

head 定义为覆盖约 80% 交互的最热商品。AST-V2 的平均 head R@10/N@10 最好，tail R@10 最好，tail N@10 第二，在 head-tail Pareto 图上位于前沿。SEATER 明显偏 tail，RRS 偏 head；AST-V2 的 rank 取向接近 0，score 取向略偏 tail。

### 敏感性

- **rho**（0.001 到 0.05）：没有统一最优值，适中的约束在部分数据集有帮助、在另一些数据集有损失。
- **SID 长度**（2 到 7）：Beauty 最优为 4 位，其余数据集为 5 位；Home/Health 在 6-7 位时仍然稳定，说明更长的 SID 需要更多数据。
- **Embedding backbone**（R@10）：

| Embedding | 方法 | Beauty | Toys | Sports | Health | Home |
|---|---|---|---|---|---|---|
| M3 | AST | 7.45 | 7.84 | 4.46 | 6.65 | 2.80 |
| M3 | SB | 7.16 | 7.07 | 4.22 | 5.94 | 2.58 |
| Qwen3-0.6B | AST | 7.51 | 7.94 | 4.62 | 6.64 | 3.02 |
| Qwen3-0.6B | SB | 6.98 | 7.07 | 4.09 | 6.30 | 2.63 |
| Qwen3-4B | AST | 7.38 | 7.81 | 4.53 | 6.34 | 2.91 |
| Qwen3-4B | SB | 6.69 | 6.85 | 4.02 | 5.99 | 2.66 |

在 Beauty 上，AST 跨 backbone 的波动只有 0.0013（相对 1.75%）。更大的 4B embedding 并没有带来更好的结果。

### 消融（R@10）

| 数据集 | AST | 去质量约束（rho=0） | 固定分叉（调过最优） |
|---|---|---|---|
| Beauty | **7.51** | 7.33 | 7.01 |
| Toys | **7.94** | 7.73 | 7.36 |
| Sports | **4.62** | 4.54 | 4.56 |
| Health | **6.64** | 6.40 | 6.48 |
| Home | **3.02** | 2.98 | 2.95 |

两个消融版本仍然普遍强于表 1 中的最强基线，说明主要收益来自“树路径”本身。自适应分叉和质量约束在小、稀疏的数据集上作用更明显，数据越大差距越小。

## 思考与可参考价值

**值得借鉴**

- **低成本诊断**：前缀/后缀掩码相似度分析几行代码就能做，可以直接拿线上 SID 检验：如果后位 token 在不同前缀下基本没有共享语义，说明残差码本的“全局共享”是浪费，可以改为每层独立词表加层次聚类。
- **自适应分叉对电商目录很自然**：类目密度极不均匀，头部类目需要细分，长尾类目粗分即可。质量约束里的 p_i 可以换成曝光、点击或 GMV 权重，防止冷门前缀样本不足。
- **结构性好处**：没有空码、不需要冲突处理、合法序列集合等于商品集合，trie 约束解码可以直接用；新商品走树就能分配 SID，不必重训 tokenizer。

**需要警惕**

- 实验规模只有 1-3 万商品，R@10 绝对值 3-8%；论文没有报告建树耗时和 MILP 求解器配置。亿级商品下逐节点 silhouette 加 MILP 很可能不可行，需要近似（如贪心约束分配、子样本选 K）。
- 13% 是按方法平均的提升，逐格看部分数据集只有 3-5%；论文只有显著性星号，没有多种子方差。
- 固定分叉消融在 Sports、Home 上只差 0.06-0.07，大数据集上自适应分叉的边际作用有限（推断：工业规模下收益可能进一步收窄）。
- 末位 token 只是桶内按 item ID 的排名，没有语义；商品上下架时 SID 会漂移，树也需要周期性重建，新旧 SID 的对齐问题论文没有讨论。
- 论文没有说明基线是否使用约束解码。“合法序列等于商品集合”的优势可能有一部分来自解码方式的差异，作者没有把它拆开分析。
- 只用了纯文本 embedding，没有协同信号，也没有在线 A/B；在已经融合行为信号的 embedding 上是否还有增益，需要自行验证。

**结论**：AST 是一个简单、可解释、可以快速复现的 SID 强基线，最值得带走的是“路径视角”和“按密度自适应分叉加质量约束”两点。想在工业场景替换 RQ-Means，要先做规模化的近似实现，再做 SID 稳定性评估。
