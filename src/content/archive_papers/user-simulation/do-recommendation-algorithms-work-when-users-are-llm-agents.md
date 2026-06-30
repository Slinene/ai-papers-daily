---
title: Do Recommendation Algorithms Work When Users Are LLM Agents? A Case Study on
  Moltbook
authors: Daming Li, Simeng Han, Jialu Zhang
date: 2026-06
venue: arXiv
topic: user-simulation
topic_name: User Simulator
topic_icon: 👥
idea: 在 LLM agent 作为用户的社交平台上，传统推荐算法中依赖用户个性化偏好的模型失效，推荐退化为基于物品共现或流行度的结构模式匹配。研究发现 agent
  用户缺乏持久的内容偏好，其行为由平台结构和会话上下文驱动，而非个人兴趣演化。
paperUrl: https://arxiv.org/abs/2606.29762
codeUrl: null
tags:
- RecommenderSystems
- LLMAgents
- Personalization
- CollaborativeFiltering
- Moltbook
unverified: true
---

## 核心思路
面对 AI agent 作为用户的社交平台，传统的假设——“用户拥有可学习的持久偏好”可能不成立。本研究首次在 Moltbook（一个纯 agent 的 Reddit 式社交平台）上系统评估八种推荐算法，发现个性化方法（如 BPR-MF）表现甚至不如简单流行度基线；相反，仅利用物品共现或图结构的 ItemKNN、LightGCN 则表现最佳。这表明对于 agent 用户，推荐系统从个性化塌缩为结构模式匹配。

## 整体实现思路
端到端 pipeline：

```
原始 Moltbook API 数据 (posts, comments, agents, submolts)
  ↓ 去重、过滤（agent >= 5 次交互）、时间划分（前9周训练，第10周测试）
构建 agent × submolt 交互矩阵（二元或 karma 加权）
  ↓ 分别训练8种模型
模型预测每个测试 agent 对候选 submolts 的得分
  ↓ 排除训练期已交互的 submolts，生成 Top-K 推荐列表
计算 Recall@K, NDCG@K, HR@K, MRR
```

训练集：第1-9周；验证集：第9周（用于超参选择）；测试集：第10周。评估时只考虑同时出现在训练和测试期的 agent 和 submolt。

## 子模块实现（可复现细节）

### 数据预处理与划分
- 数据集：Moltbook Observatory Archive（HuggingFace），包含 2,395,813 帖子、991,901 评论、175,021 agent、6,232 submolts，时间范围 2026-01-27 至 2026-03-30（10周）。
- 去重：保留每个记录的最新 fetch。
- 过滤：agent 总交互次数（帖子+评论）≥5，剩余 79,643 agent、5,406 submolts。
- 划分：
  - 训练期：周1-9，有效 agent 79,596，submolt 5,359，总交互 176,681（密度 0.041%）。
  - 测试期：周10。
- 超参选择：在周1-8训练，周9验证，优化 Recall@10。

### 交互矩阵构建
- 二元矩阵 R：`R_ij = 1` 表示 agent i 在训练期有帖子或评论发布于 submolt j，否则 0。维度 m × n = 79,596 × 5,359，稀疏度 0.041%。
- Karma 加权矩阵 `R^κ`：`R^κ_ij = log(1 + Σ_t κ(i,j,t))`，其中 κ(i,j,t) 为 agent i 在 submolt j 的某次交互获得的 karma（类似 upvote 数）。矩阵同样非常稀疏。

### 评估指标
对每个测试 agent，生成长度为 K 的推荐列表（排除训练期已交互的 submolts），与其实际测试期交互的 submolt 集合 `S_test_i` 比较。
- Recall@K：`1/|U_test| Σ_i |(rec_list_i ∩ S_test_i)| / |S_test_i|`。
- NDCG@K：归一化折损累计增益。
- Hit Rate@K：`1/|U_test| Σ_i 1(|rec_list_i ∩ S_test_i| > 0)`。
- MRR：第一个相关结果排名倒数的均值。
评估 K ∈ {5,10,20,50}。

### 模型实现细节

#### Random（随机基线）
- 为每个 agent 随机推荐未交互过的 submolts。

#### TopPopular（流行度基线）
- 统计训练集中所有 submolts 的总交互次数，降序排列，排除已交互项后推荐前 K 个。

#### BPR-MF (Bayesian Personalized Ranking)
- 输入：二元矩阵 R。
- 输出：agent i 对 submolt j 的得分 `ŕ_i,j = u_i^T v_j`，u_i, v_j ∈ R^d，d=64。
- 损失：贝叶斯个性化排序（BPR），对每个用户采样正负例对 (j, j')，优化 `ln σ(ŕ_i,j - ŕ_i,j') - λ||θ||^2`。
- 超参：学习率 0.001，正则化 λ=0.0001，迭代 100 轮。
- 训练：每轮对每个正交互采样一个未交互项作为负例。

#### HybridMF（混合矩阵分解）
- 首先用 ALS 分解 R：`ŕ_ALS_ij = u_i^T v_j`，d=16，正则化 0.01，迭代 30 次。
- 内容嵌入：使用 all-MiniLM-L6-v2 对所有帖子生成 384 维嵌入。
  - Agent 嵌入 `e_i^agent`：其所有帖子的嵌入质心（中心点）。
  - Submolt 嵌入 `e_j^submolt`：该 submolt 内所有帖子嵌入的均值。
- 最终得分：`ŕ_ij = (1-α) * ŕ_ALS_ij + α * cos(e_i^agent, e_j^submolt)`，α=0.1。得分先各自 min-max 归一化至 [0,1] 再混合。
- 说明：ALS 部分学习交互隐式信号，内容部分补充语义。

#### ContentBased（纯内容推荐）
- 仅使用内容嵌入，`ŕ_ij = cos(e_i^agent, e_j^submolt)`，无训练参数。

#### ItemKNN（物品协同过滤）
- 输入：二元交互矩阵 R（行：agent，列：submolt）。
- 计算 submolt 间的余弦相似度：`S_j,k = (R[:,j]^T R[:,k]) / (||R[:,j]|| ||R[:,k]||)`。
- 对每个 submolt j，保留相似度最高的 K'=50 个邻居。
- 推荐打分：`ŕ_i,j = R_i,: · S_j`，将 agent i 的历史交互向量与 j 的相似近邻向量点积。
- 无需训练，仅计算相似矩阵。

#### LightGCN（图协同过滤）
- 输入：从二部图 G=(U∪V, E) 构建归一化邻接矩阵 `ᵬ`。
- 嵌入传播：`E^{(ℓ+1)} = ᵬ · E^{(ℓ)}`，初始 `E^{(0)}` 随机初始化，维度 d=64。
- 层数 L=3。
- 最终嵌入：`E_final = (1/(L+1)) Σ_{ℓ=0}^L E^{(ℓ)}`（各层均值）。
- 得分：`ŕ_i,j = e_final_i^T e_final_j`。
- 训练：BPR 损失，Adam 优化器，学习率 0.001，L2 正则化 1e-4，batch size 1024，epoch 20。

#### SASRec（自注意力序列推荐）
- 对每个 agent，构建其交互 submolts 的时序序列（按 created_at 排序），截断至最近 20 个。
- 模型：单层 Transformer decoder，d_model=64，d_ffn=256，2 个 attention heads，dropout 0.2。
- 位置：可学习位置嵌入。
- 输入：序列 `[s1, s2, ..., s_t]`，经 embedding 和 self-attention（causal mask）后，取最后位置的隐状态 h_i。
- 得分：`ŕ_i,j = h_i^T v_j`，v_j 为 submolt j 的嵌入（随机初始化或由 MiniLM PCA 投影到 64 维初始化，但等效果）。
- 训练：自回归交叉熵损失（预测下一个 submolt），Adam 优化器，学习率 0.001，batch size 512，10 个 epoch。

### 代理描述特征实验
- Agent 描述字段（63% agent 非空，中位长度 33 字符）通过 MiniLM 计算嵌入。
- 三种用法：
  1. DescriptionBased：仅基于描述嵌入与 submolt 内容嵌入的余弦相似度推荐。
  2. DescItemKNN：混合 ItemKNN 得分与描述相似度，权重 α ∈ {0.1,0.3,0.5}。
  3. DescriptionHybridMF：将 HybridMF 中的 agent 嵌入替换为描述嵌入（而非帖子质心）。
- 结果：描述特征几乎无预测能力，注入 ItemKNN 或 HybridMF 不提升性能，高权重时有害。

### 时间衰减实验
- 固定训练窗口 4 周，测试窗口 1 周，不断增加训练-测试间隔（1-4 周）。
- 所有模型（TopPopular, ItemKNN, LightGCN, SASRec, BPR-MF, HybridMF, ContentBased）均未出现系统性的性能下降，表明 agent 的交互模式在时间上是平稳的，无偏好漂移。

## 实验设置与结果

### 主要结果（二元交互矩阵）
| 模型 | Recall@10 | NDCG@10 | HR@10 | MRR |
|------|-----------|---------|-------|-----|
| Random | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| TopPopular | 0.0232 | 0.0136 | 0.0436 | 0.0155 |
| BPR-MF | 0.0165 | 0.0083 | 0.0321 | 0.0088 |
| HybridMF | 0.0117 | 0.0070 | 0.0239 | 0.0096 |
| ContentBased | 0.0056 | 0.0033 | 0.0110 | 0.0041 |
| ItemKNN | **0.0236** | **0.0169** | **0.0450** | **0.0229** |
| LightGCN | 0.0242 | 0.0159 | 0.0454 | 0.0196 |
| SASRec | 0.0234 | 0.0167 | 0.0463 | 0.0224 |

ItemKNN 整体最佳，LightGCN 与 SASRec 略逊但同属第一梯队；BPR-MF 低于 TopPopular；HybridMF 和 ContentBased 最差。个性化方法失效。

### Karma 加权效果
| 模型 | 加权 | Recall@10 | NDCG@10 | HR@10 | MRR |
|------|------|-----------|---------|-------|-----|
| TopPopular | 二元 | 0.0232 | 0.0136 | 0.0436 | 0.0155 |
| TopPopular | Karma | 0.0530 | 0.0377 | 0.0936 | 0.0465 |
| ItemKNN | 二元 | 0.0236 | 0.0169 | 0.0450 | 0.0229 |
| ItemKNN | Karma | **0.0558** | **0.0417** | **0.1009** | **0.0561** |
| HybridMF | 二元 | 0.0125 | 0.0069 | 0.0252 | 0.0093 |
| HybridMF | Karma | 0.0381 | 0.0304 | 0.0748 | 0.0427 |
| BPR-MF | 二元 | 0.0149 | 0.0080 | 0.0294 | 0.0094 |
| BPR-MF | Karma | 0.0159 | 0.0083 | 0.0312 | 0.0092 |

Karma 大幅提升结构类模型 TopPopular (2.3-3.2×)、ItemKNN (2.2-2.6×) 和 HybridMF (2.5-5.2×)，但 BPR-MF 几乎不变。说明 karma 强化了物品质量信号，但无法挽救个性化学习。

### 消融：Agent 描述特征
| 模型 | Recall@10 | NDCG@10 | HR@10 | MRR |
|------|-----------|---------|-------|-----|
| ItemKNN | 0.0236 | 0.0169 | 0.0450 | 0.0229 |
| DescItemKNN (α=0.1) | 0.0238 | 0.0169 | 0.0454 | 0.0229 |
| DescItemKNN (α=0.5) | 0.0224 | 0.0151 | 0.0436 | 0.0205 |
| HybridMF (无用户内容特征) | 0.0133 | 0.0072 | 0.0252 | 0.0093 |
| DescriptionHybridMF | 0.0110 | 0.0063 | 0.0229 | 0.0084 |
| DescriptionBased | 0.0011 | 0.0006 | 0.0041 | 0.0010 |

描述特征几乎没有预测力，甚至稀释有效信号。

### 时间衰减
- 随着训练-测试间隔从 1 周增至 4 周，所有模型的 Recall@10、NDCG、HR、MRR 均未下降，甚至略有上升（因测试群体变小带来的方差）。表明 agent 兴趣无漂移，进一步否定了个性化建模的必要性。

## 思考与可参考价值
### 局限
1. **数据稀疏**：交互密度仅 0.041%，远低常规推荐数据集，绝对指标偏低。但此稀疏性本身就是 agent 行为特征的一部分。
2. **无暴露日志**：无法区分 agent 未交互是未见还是不喜欢，只能以发帖/评论作为代理，可能引入偏差。
3. **配置不可见**：无法获知 agent 的 LLM 后端和配置文件内容，难以验证“缺乏偏好”的直接原因，分析停留在现象层面。
4. **平台特化**：针对 Moltbook 架构，若 agent 设计进化出持久记忆，结论可能变化。

### 对搜索推荐/Agent 方向的启发
- **用户建模的边界**：在人类与 agent 混合的平台上，个性化模型可能因 agent 的“噪声”交互而崩塌。需引入 agent 检测与过滤机制，清洗训练数据，或设计鲁棒模型区分人与 agent 的交互模式。
- **评价体系的扰动**：若测试集混入 agent，其随机/结构化的行为会拉低个性化模型的指标，导致模型对比失真。应分层评测或在业务指标中排除 agent。
- **推荐新范式**：在 agent 为主的平台上，推荐应从偏好匹配转向环境/结构匹配，例如基于会话上下文、任务驱动或平台热度的推荐。
- **多智能体社会模拟**：该工作为研究 agent 社群提供新的入口，可反向探索如何通过推荐塑造 agent 群体行为，用于模拟实验或调控。
