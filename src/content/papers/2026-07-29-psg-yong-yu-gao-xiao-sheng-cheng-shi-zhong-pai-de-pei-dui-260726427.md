---
title: 'PSG: Pair-Space Generation for Efficient Generative Reranking'
title_zh: PSG：用于高效生成式重排的配对空间生成
authors:
- Chao Feng
- Li Ma
- Xiancheng Gao
- Chenghao Zhang
- Yuanhao Pu
- Xiang Li
affiliations:
- Kuaishou Tech
arxiv_id: '2607.26427'
url: https://arxiv.org/abs/2607.26427
pdf_url: https://arxiv.org/pdf/2607.26427
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 生成式重排·Pair-Space 解码加速
tags:
- Generative Reranking
- Pair-Space Generation
- Autoregressive Decoding
- GRPO
- Industrial Deployment
one_liner: 将生成式重排的原子从单品提升为有序物品对，解码步数减半，实现1.83倍加速且性能显著提升
practical_value: '- 生成式重排中，将物品级自回归解码改为物品对级，直接减少解码步数，可无缝集成到现有 Generator-Evaluator 框架中，降低推理延迟。

  - 预训练的对级表示（Pair-Token Representation）模块可在每次请求中动态构建词汇表，避免静态词汇表的数据稀疏问题，适用于电商/广告中候选集动态变化的场景。

  - 强化学习阶段使用 GRPO 进行探索，不依赖外部过程奖励模型，实现简单且有效，可直接迁移到其他序列生成的推荐任务。

  - 工程上，Pair-Token 表示编码与用户上下文编码可并行执行，隐藏额外开销；k=2 是工业场景下延迟与效果的甜点，候选集规模 n≤400 时可实现约 1.5×
  以上加速。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现代推荐系统的重排阶段常采用生成器-评估器框架，生成器自回归地逐物品生成序列，然后评估器打分筛选。但自回归解码的复杂度随序列长度线性增长，在严格延迟约束下只能生成少量序列，限制了探索空间；同时 teacher-forcing 训练与 free-running 推理的偏差导致错误累积，序列越长质量越差。本文提出将生成的基本单元从单个物品提升为有序物品对，将解码步数从 L 减少到 L/2，在不牺牲表达力的前提下显著提升效率并减少错误。

## 方法关键点
- **配对空间生成**：将生成字典定义为请求内的所有有序物品对 (v_i, v_j)，生成器自回归地生成 L/2 个对 token，最后展开为 L 长的物品序列。理论证明该映射是双射，与物品空间生成等价，无表达力损失。
- **动态配对表示**：使用预训练的 Pair-Token Representation 模块，通过可学习的角色嵌入和 MLP 融合物品特征，在线计算每次请求的配对嵌入，避免 n² 级静态词汇表的数据稀疏问题。
- **模型架构**：Transformer 编码器-解码器结构，编码器建模用户行为序列，解码器通过交叉注意力生成配对 token。推理时 Pair-Token 表示与用户编码并行执行，隐藏额外开销。
- **训练策略**：三阶段训练——(1) 利用曝光日志预训练配对表示，近似 pair 级点击标签；(2) 下一 token 预测（NTP）保持顺序生成能力；(3) 采用 GRPO 强化学习，以评估器打分为奖励进行探索，无需过程奖赏模型。
- **理论保证**：复杂度分析显示，解码 FLOPs 的固定项减少 2 倍，KV-cache 读取减少 4 倍；错误累积分析表明最坏情况次优性界从 O(L²¯ϵ) 降至 O((L/2)²¯ϵ)，在典型部署下可实现约 4 倍改进。

## 关键结果
- **离线实验**：在 ML-1M、Amazon-Books 和工业数据集 RecFlow 上，PSG 对比多种生成器-评估器基线（GoalRank、JDRec 等）在所有指标上取得显著提升，RecFlow 上 NDCG@6 提升 8.38%，Precision@6 提升 8.70%。
- **在线 A/B**：部署于快手主应用（日活超 4 亿），带来 0.178% 人均停留时长提升，单容器 QPS 从 734 提升至 1320（+79.8%），生成器延迟从 38.42ms 降至 20.99ms，实现 1.83 倍加速。
- **效率分析**：k=2 时，在 n≤100 的候选集规模下，延迟基本保持 1.5× 以上优势，k=3 则因词汇表过大而不可行，验证了配对粒度为工业实践的甜点。
- **消融实验**：移除预训练、NTP 或 GRPO 任一阶段均导致性能下降，其中 NTP 影响最大，说明 token 级自回归监督对生成稳定性至关重要。

**最值得记住的一句话**：将生成式重排的解码原子从单品提升为有序对，可在不损失列表分布表达力的前提下，将解码步数减半，理论错误界降低约 4 倍，并在线上实现 1.83 倍加速与显著的业务指标提升。
