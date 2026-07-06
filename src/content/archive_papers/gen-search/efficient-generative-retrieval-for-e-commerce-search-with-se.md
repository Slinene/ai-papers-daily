---
title: Efficient Generative Retrieval for E-commerce Search with Semantic Cluster
  IDs and Expert-Guided RL
authors: Jianbo Zhu, Xing Fang, Jing Wang, Mingmin Jin, Bokang Wang, et al. (8 人)
date: 2026-05
venue: arXiv
topic: gen-search
topic_name: 生成式搜索
topic_icon: 🔎
idea: 将生成式检索定位为召回补充，用类别约束和查询-商品对比学习构建语义聚类ID（CQ-SID），大幅降低beam search成本；通过四阶段渐进训练与专家引导GRPO（EG-GRPO），在稀疏奖励下对齐下游排序目标，取得线上GMV等显著提升。
paperUrl: https://arxiv.org/abs/2605.14434
codeUrl: null
tags:
- Generative Retrieval
- E-commerce Search
- Semantic ID
- RQ-VAE
- GRPO
unverified: true
---

## 核心思路
解决电商搜索召回阶段中传统生成式检索面临的三大挑战：1) 全量端到端不切实际；2) 细粒度唯一ID导致beam search开销大；3) 与下游排序目标不匹配。核心idea是用**语义聚类ID（CQ-SID）**替代唯一ID，通过类别先验和查询-商品对比学习构建层次化语义簇，减少beam大小；并设计**四阶段渐进训练**将查询映射到SID，最后用**专家引导GRPO**在稀疏点击/购买信号下对齐排序目标，实现召回质量与效率的双赢。

## 整体实现思路
```
输入: 用户查询 + 用户画像
    ↓
[1. CQ-SID 语义ID构建] (离线)
  - 商品特征 → RQ-VAE (类别引导量化 + 查询-商品对比学习) → 三层语义ID
  - 后处理: 控制每簇商品数，过大时拆分并加后缀
    ↓
[2. 渐进式查询到 SID 映射训练] (离线)
  Stage1: (商品标题, SID) → Qwen2.5-0.5B SFT
  Stage2: (查询, 多个SID) → 继续SFT
  Stage3: (用户画像 + 查询 + 近线点击商品SID, 个性化SID) → 继续SFT
  Stage4: EG-GRPO 对齐排序信号
    ↓
[3. 在线推理]
  - 用户查询+画像 → 模型beam search → top-K SID
  - SID → 商品查找表 → 高效商品池过滤 → 候选商品
    ↓
输出: 召回商品集合
```

## 子模块实现（可复现细节）

### CQ-SID 语义ID构建
- **输入**: 商品特征 `x`（如标题、类别等embedding），部分商品有已知类别标签；查询特征 `q`。
- **输出**: 三层的语义ID `(s1, s2, s3)`，每个商品对应一个SID。
- **模型架构**: 基于RQ-VAE，三层残差量化，codebook大小 `K1×K2×K3 = 2048×1024×1024`。

#### 类别引导的第一层量化
- 第一层codebook大小2048，但实际有效类别数约1711（电商顶级类目）。
- 对于已知类别的商品 `i`，第一层索引强制为 `CategoryID(i)`；否则最近邻量化：
  ```
  k_i^(1) = CategoryID(i)               if i ∈ I_known
          = argmin_j || r_i^(0) - e_j^(1) ||^2   otherwise
  ```
  其中 `r_i^(0)` 是商品编码器输出embedding，`e_j^(1)` 是第一层codebook向量。
- 后续第二、三层使用标准最近邻量化。

#### 查询-商品对比学习
- 利用用户搜索-点击-购买日志构建正样本对 `(e_i, e_q)`，双向InfoNCE损失：
  ```
  L_Bi-InfoNCE = -1/2 [ log exp(sim(e_i,e_q)/τ)/∑_{q'}exp(...) + log exp(sim(e_q,e_i)/τ)/∑_{i'}exp(...) ]
  ```
  `sim` 为余弦相似度，温度 `τ=0.1`，批次内对比样本数 `b=128`。无查询关联的商品对该损失mask掉。

#### 总体训练目标
- 重建损失：`L_recon = ||x - x̂||^2`
- 承诺损失：`L_commit = Σ_{l=1}^3 ||z_l - sg[ẑ_l]||^2`
- 总损失：`L = L_recon + β L_commit + γ L_InfoNCE`，其中 `β=1.0, γ=0.001`。
- Codebook向量用EMA更新，`λ=0.99`，使用codebook重启防止坍缩。

#### SID后处理
- 设置每簇商品上限 `Tmax=50`，最大分组数 `Gmax=100`。
- 若一个SID对应商品数 `c > Tmax`，则随机分成 `G = min(⌈c/Tmax⌉, Gmax)` 组，第三级索引后拼接3位组号，形成新SID如 `⟨s1, s2, s3_base + group_id⟩`。
- 这样保持层级前缀结构，同时避免热门簇过大。

### 渐进式查询到SID映射训练
- **基础模型**: Qwen2.5-0.5B，四阶段微调。
- **Stage1 商品标题→SID**:
  - 训练数据: 37.5M样本中抽2100万商品标题-SID对。
  - 输入: 商品标题文本，输出: 对应SID token序列。
  - SFT，batch size 128，learning rate 1e-4，2000 steps。
- **Stage2 查询→SID**:
  - 数据: 9030万查询-SID对，每个查询随机采样3个关联SID（来自点击/购买商品）。
  - 输入: 查询文本，输出: 三个SID序列（用特殊分隔符）。
  - SFT，batch size 256，lr 4e-5，2500 steps。
- **Stage3 个性化(用户+查询)→SID**:
  - 数据: 7370万条，包含用户性别、年龄段、近线点击商品SID序列（相关类目）。
  - 输入: “用户画像 + 查询 + 历史SID序列”，输出: 个性化SID列表。
  - SFT，batch size 64，lr 4e-5，5000 steps。
- **Stage4 EG-GRPO 排序对齐**（见下）。

### EG-GRPO 专家引导强化学习
- **动机**: 稀疏点击/购买奖励下，标准GRPO易产生mode collapse，牺牲曝光覆盖率。
- **奖励设计**:
  ```
  R(o) = 1.0   if o in P_pay (购买商品SID集合)
         1.0   else if o in P_clk (点击)
         0.5   else if o in P_exp (曝光)
         0.1   else if o in S_valid (有效SID)
         0.0   otherwise
  ```
- **优势计算**: 组内标准化 `A(o_i) = (R(o_i) - mean({R(o_j)})) / (std({R(o_j)}) + ε)`
- **GRPO目标**:
  ```
  L_GRPO = -1/G Σ_i min( P_θ(o_i|x)/P_θold(o_i|x) A(o_i), clip(...) A(o_i) )
  ```
- **专家注入**: 在每组 `G` 个采样输出中，额外加入 `K` 个真实点击/曝光SID作为“专家”样本，与模型生成样本混合形成新组，共同计算奖励和优势，更新时对所有样本进行梯度。
- **超参**: rollout batch size 512, group size 8 (包含K个专家，则采样8-K个)，KL权重1.0，lr 1e-6，1000 steps。
- **效果**: K=2时click和exposure指标均提升，避免标准GRPO的指标分化。

### 在线推理与过滤
- 在线：动态beam size ∈ [20,50,100]，8 GPU，200+ QPS，平均延迟40ms，生成top-K SID。
- 通过SID→商品倒排索引召回实际商品。
- 商品池：从数亿全量筛选约2100万高效率商品，每日更新，新商品推理加入池。

## 实验设置与结果
### 数据集
- 来自某大型电商平台搜索日志。
- CQ-SID训练：3750万样本（2110万查询-商品对，1640万仅商品）。
- 渐进训练：I2SID 2100万，Q2SID 9030万，UQ2SID 7370万。
- 测试集：Q2SID 201k，UQ2SID 170k。

### 基线
- 标准RQ-VAE (TIGER, 3层codebook [2048,1024,1024])。
- 消融：去掉类别约束 (CQ-SID w/o Cate)，去掉对比学习 (CQ-SID w/o QI)。

### 主要指标
- **Hitrate**: 召回SID覆盖目标物品的比例。
- **beam@N**: 相同beam大小下的hitrate。
- **top-1K截断**: 生成不同beam数，按效率分截断到1K后评估。

### 语义召回结果 (Table 1)
| Method | beam@1 | beam@10 | beam@100 |
|--------|--------|---------|----------|
| RQ-VAE | 0.0598 | 0.2579  | 0.5199   |
| CQ-SID (w/o Cate) | 0.0680 (+13.71%) | 0.2870 (+11.28%) | 0.5578 (+7.29%) |
| CQ-SID (w/o QI) | 0.0596 (-0.33%) | 0.2691 (+4.34%) | 0.5652 (+8.71%) |
| **CQ-SID** | **0.0758 (+26.76%)** | **0.3161 (+22.57%)** | **0.6181 (+18.89%)** |

CQ-SID在极小beam下优势最大，类别和对比学习互补。

### 个性化召回结果 (Table 3)
| Method | beam@1 | beam@100 |
|--------|--------|----------|
| RQ-VAE | 0.1359 | 0.7513   |
| CQ-SID | 0.1510 (+11.11%) | 0.8062 (+7.31%) |

Top-1K截断下，CQ-SID在beam=160时hitrate 0.7984，较RQ-VAE在195时0.7607高4.96%，且节省17.95% beam。

### 排序对齐 (EG-GRPO) 结果 (Table 4)
| Method | clk@1 | clk@10 | exp@1 | exp@10 | pvr@10 |
|--------|-------|--------|-------|--------|--------|
| CQ-SID | 0.1510| 0.5206 | 0.5056| 0.8693 | 0.4371 |
| + GRPO (K=0) | 0.1519| 0.5196 | 0.5077| 0.8702 | 0.4360 |
| + EG-GRPO (K=2) | **0.1524** | **0.5221** | 0.5091 | 0.8703 | 0.4377 |
| + EG-GRPO (K=4) | 0.1523 | 0.5219 | 0.5087 | **0.8711** | 0.4378 |
标准GRPO导致top-10 click下降和pvr下降 (mode collapse)，EG-GRPO稳定提升所有指标。

### 在线A/B测试
- 两周，统计显著：**GMV +1.15%**，**UCTCVR +0.40%**。生成式召回渠道曝光占比50.25%，点击58.96%，购买72.63%。

## 思考与可参考价值
### 局限性
- **领域依赖**：类别引导依赖电商完善的类目体系，迁移需考虑先验结构。
- **RL提升有限**：文章指出SFT已接近局部最优，EG-GRPO主要矫正偏差，对绝对hitrate提升微小，收益体现在指标协调。
- **商品池维护**：需筛选高效商品池并日更新，新增商品需在线推理分配SID，运维复杂。
- **非单调hitrate**：beam增大后top-1K截断下hitrate下降，离线模拟与线上粗排仍有不一致风险。

### 可借鉴点
- **生成式检索作为召回补充**：不替代全漏斗，而是新增一个高质量召回通道，是工业落地可行路线。
- **语义聚类ID设计**：牺牲ID唯一性换取推理效率，通过后处理控制簇大小，对大规模商品库尤其适用。
- **渐进训练策略**：从商品描述到查询再到个性化、RL对齐，逐步注入知识，适合LLM微调落地。
- **EG-GRPO缓解稀疏奖励坍塌**：在电商搜索等稀疏正反馈场景下，注入专家样本是简单有效的稳定RL训练技巧。
- **多指标权衡**：显式通过奖励函数设计同时优化点击和曝光，防止召回过于集中热门商品。
