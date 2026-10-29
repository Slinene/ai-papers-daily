---
title: "Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation"
authors: "Ruizhong Qiu, Yinglong Xia, Dongqi Fu, Hanqing Zeng, Ren Chen et al. (10 人)"
affiliation: "University of Illinois Urbana-Champaign × Meta"
date: "2026-06"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "把「物品的兴趣归属」从单一硬类目改成「分布式兴趣画像」：在稀疏化的 item-item 共同交互图上做可微软聚类，每个物品得到一个对 C 个兴趣原型的稀疏概率分布 p_i，并据此算出一个连续的兴趣画像 token y_i。用户序列改写成 [x_i1, y_i1, x_i2, y_i2, ...] 交替格式，LLM 同时预测下一物品和以 p_i 为软标签的兴趣原型；公开集在 1+99 采样评测下全面领先，Meta 线上多指标 +0.06%~0.19%。"
paperUrl: https://arxiv.org/abs/2606.20554
codeUrl: null
tags:
- "Co-Engagement Graph Sparsification"
- "Soft Modularity Clustering"
- "Continuous Interest Profile Token"
- "Interleaved Item-Profile Sequence"
- "Soft-Label Interest Prediction"
unverified: false
---
## 核心思路

G2Rec（Sparse Co-Engagement Graph Schema for Generative Recommendation）想解决的是：生成式推荐的 item tokenization 只编码内容语义，缺少「用户会把哪些东西放在一起交互」的协同兴趣结构；而直接用图（序列化或 GNN）要么太贵，要么只看局部。

它的做法分三步：

1. 用 **item-item 共同交互图** 承载用户行为，并按用户采样把边数从 O(M^2) 压到 O(M log M)，同时证明图 Laplacian 近似保持；
2. 在这张图上用 **可微的期望模块度** 做软聚类，每个簇是一个「兴趣原型」，每个物品得到一个稀疏的兴趣隶属分布 p_i（物品兴趣画像）；
3. 把 p_i 变成连续的 **画像 token** y_i，用户序列改为物品与画像交替，LLM 同时学「下一物品」和「当前物品属于哪些兴趣原型」。

关键概念转变：物品的兴趣归属不是一个硬类目，而是一个分布；这个分布来自全局共现结构，不需要人工兴趣标签。

## 整体实现思路

- 离线：交互日志 → 每用户采样 m 对共现 → 稀疏共现图 G → Leiden 初始化 → 梯度最大化 Q_soft 得到稀疏 P → 计算原型嵌入 V 和画像 token Y。
- 训练：序列 [BOS, x_i1, y_i1, ..., x_iN, y_iN] 输入 LLM（公开集为 Llama 2 13B + LoRA），在 y 位置之后预测下一物品、在 x 位置之后预测兴趣原型分布。
- 在线：画像 token 离线周期更新，在线只是查表拼接；论文报告的额外开销为训练 +0.043s/batch、推理 +0.0027s/batch。

## 子模块实现（可复现细节）

### 1. 稀疏共现图

- 全量共现边：E* = ∪_u (I_u × I_u)。Observation 1 指出用户序列在 G* 上是一条路径，所以边编码了兴趣转移。
- 稀疏化：E = ∪_u sample(I_u × I_u, m)，有放回均匀采样 m 对，构成无向图，边权 N(N−1)/(2m)，使每个用户贡献的总权重仍为 C(N,2)，L_E 是 L_E* 的无偏估计。
- Theorem 2：每用户 N 次交互时，取 m = ⌈2N(1/(3ε) + 1/ε^2)·log(2|I|/δ)⌉，则以概率 ≥ 1−δ 有 (1−ε)L_E* ⪯ L_E ⪯ (1+ε)L_E*，总边数 |E| = |U|m = O(M log M)。
- 证明要点：同一用户团 K_N 内任意两点的有效电阻 = 2/N，加边只会让电阻变小（Rayleigh 单调性），于是每个采样项的范数 ≤ N/m，再用矩阵 Bernstein 不等式。

### 2. 软模块度聚类

- 参数化：p_i = softmax(z_i) ∈ R^C，用 Leiden 结果初始化并稀疏化，每行最多 ρ 个非零。
- 硬模块度：Q_hard(h) = (1/|E|) Σ_{i,j} (A_ij − γ k_i k_j / |E|) · 1[h_i = h_j]。
- 软模块度（Proposition 3，对 h ~ P 取期望的闭式）：

```
Q_soft(P) = (1/|E|) * [ Σ_{(i,j)∈E} p_i^T p_j  −  γ * ||P^T k||_2^2 / |E| ]
```

- p_i^T p_j 是两物品落在同一原型的概率；第二项是 Newman–Girvan 零模型惩罚，防止所有物品都挤进一个簇。
- 复杂度（Proposition 4）：O(ρ|E|) = O(ρM log M)，可 GPU 加速。
- 分辨率 γ：Beauty/Toys 取 0.8，Sports/Yelp 取 1。C、ρ、优化器、迭代次数论文均未给出。

### 3. 兴趣画像 token

- 原型嵌入：v_a = Σ_i p_{i,a} x_i / Σ_i p_{i,a}，即按隶属度加权的物品嵌入均值。
- 画像 token：y_i = Σ_a p_{i,a} v_a，矩阵形式 Y = P V。
- x_i 在公开集上是 d=64 的 SASRec 嵌入。因此 y_i 是一个连续向量，是 x_i 在「兴趣子空间」里的平滑版本（推断：相当于在共现簇内做了一次加权平均的图平滑）。

### 4. 序列格式与训练目标

```
R_u = [BOS, x_i1, y_i1, x_i2, y_i2, ..., x_iN, y_iN]
L_item^t    = −log F(i_{t+1} | R_u[≤2t+1])          # 看到 y_it 之后预测下一物品
L_profile^t = −Σ_a p_{i_t,a} · log F(a | R_u[≤2t])   # 看到 x_it 之后预测其兴趣原型（软标签）
L = L_item + λ · L_profile
```

- 训练配置（公开集）：Llama 2 13B，LoRA rank 16、dropout 0.05，3 epoch，Adam lr 3e-4，cosine 调度 + 100 步 warmup，Xavier 初始化，最大序列长度 50。
- 最终 λ 未给出；消融在 λ ∈ [0, 1] 上扫。

### 5. 工业部署

- 在 Meta 多个产品面上线（文中举例 Instagram Reels 的规模）。
- 自研分布式高性能图处理引擎离线周期性运行图聚类，文中引用的是 Louvain（Blondel et al. 2008），在线响应不受影响。各产品面有内部改动，细节因公司政策未披露。

## 实验设置与结果

数据集（5-core，leave-one-out，测试为 1 正例 + 99 随机负例）：

| 数据集 | 用户 | 物品 | 交互 | 稀疏度 |
|---|---|---|---|---|
| Beauty | 22,363 | 12,101 | 198,502 | 99.93% |
| Sports | 25,598 | 18,357 | 296,337 | 99.95% |
| Toys | 19,412 | 11,924 | 167,597 | 99.93% |
| Yelp | 30,431 | 20,033 | 316,354 | 99.95% |

主结果（摘录 Table 2，含最强的几个基线）：

| 数据集 | 指标 | GRU4Rec | SASRec | LightGCN | HeLLM | EAGER | G2Rec |
|---|---|---|---|---|---|---|---|
| Beauty | Recall@10 | 0.4696 | 0.4739 | 0.4042 | 0.3413 | 0.3663 | **0.4892** |
| Beauty | NDCG@10 | 0.3156 | 0.2975 | 0.2596 | 0.2474 | 0.2278 | **0.3334** |
| Beauty | MRR | 0.2852 | 0.2614 | 0.2340 | 0.2359 | 0.2060 | **0.3034** |
| Sports | Recall@10 | 0.4622 | 0.4722 | 0.3855 | 0.2946 | 0.2232 | **0.5093** |
| Sports | NDCG@5 | 0.2497 | 0.2341 | 0.2056 | 0.1641 | 0.0906 | **0.2869** |
| Sports | MRR | 0.2520 | 0.2378 | 0.2133 | 0.1750 | 0.1078 | **0.2867** |
| Toys | Recall@10 | 0.4663 | 0.4493 | 0.3721 | 0.3375 | 0.3777 | **0.4691** |
| Toys | NDCG@10 | 0.3136 | 0.2698 | 0.2374 | 0.2359 | 0.2319 | **0.3225** |
| Toys | MRR | 0.2842 | 0.2338 | 0.2154 | 0.2228 | 0.2075 | **0.2942** |
| Yelp | Recall@1 | 0.2375 | 0.2405 | **0.2696** | 0.2148 | 0.0976 | 0.2558 |
| Yelp | Recall@10 | 0.7373 | 0.7597 | 0.6756 | 0.4909 | 0.4088 | **0.7736** |
| Yelp | NDCG@10 | 0.4642 | 0.4778 | 0.4566 | 0.3436 | 0.2343 | **0.4927** |

平均排名：G2Rec 1.04、GRU4Rec 2.46、SASRec 2.83、LightGCN 4.50、Caser 5.23。注意 Yelp Recall@1 上 G2Rec 输给 LightGCN，与正文「全面领先」的说法不一致。

效率（Beauty，每 batch 秒数）：

| 方法 | 训练 | 推理 |
|---|---|---|
| Item-Only | 0.763 | 0.0534 |
| G2Rec | 0.806 | 0.0561 |
| 增量 | +0.043 | +0.0027 |

软聚类消融（模块度，越高越好）：

| 方法 | Beauty | Sports | Toys | Yelp |
|---|---|---|---|---|
| Hard (Leiden) | 0.419 | 0.365 | 0.437 | 0.691 |
| Soft (Ours) | 0.499 | 0.452 | 0.550 | 0.757 |

λ 消融（Beauty）：λ 从 0 增到 1，MRR 大约从 0.287 升到 0.293（读图，纵轴范围 0.287–0.293）。

线上 A/B（7 天 + 长期）：in-session 指标 > +0.03%，总时长、点赞、分享等多项互动指标 +0.06%~+0.19%；同时称内容多样性和 serving 效率有提升，具体设置未披露。

## 思考与可参考价值

**值得拿走的部分**

- 软模块度 Q_soft 是一个干净、可微、近线性复杂度的软社区发现目标，适合给 SID 加一层「协同兴趣」语义：例如用 argmax 簇作为第一层粗码，用 p_i 作为第一层 code 的软标签，补足 RQ-VAE 只看内容、看不到互补关系（手机和手机壳）的短板。
- 「先预测兴趣、再预测物品」的辅助损失不需要人工标签，可直接迁移到意图层或粗粒度 SID 的监督上。
- 每用户采样 m 对共现、带权重修正的构图方式在亿级商品上可行，且有 Laplacian 保持的理论保证。

**需要警惕的部分**

- 评测用 1+99 随机负采样，与全库检索指标不可比；基线多是小模型，而 G2Rec 用 Llama 2 13B，缺少同主干只用 x_i 的效果对照，增益有多少来自主干本身不清楚。
- 软聚类的价值只用模块度证明，没有给出软 vs 硬在推荐指标上的对比；λ 消融幅度很小、只在一个数据集上做。
- 部署段写的是 Louvain（硬聚类），线上是否真用了软聚类存疑；C、ρ、λ 等关键超参缺失，复现成本高；没有开源代码。
- 这里的 tokenization 是连续向量注入，不是可解码的离散 SID；序列长度翻倍在长序列（如 last100）场景下的开销会明显高于论文的 5%（推断）。

**落地前建议验证**：在全库指标（order@50/@512、qAUC）上对比「同主干 + 是否加画像 token / 兴趣损失」；比较软聚类与 Leiden 硬聚类做第一层 SID 的差异；评估簇周期重算带来的画像漂移对增量训练的影响。
