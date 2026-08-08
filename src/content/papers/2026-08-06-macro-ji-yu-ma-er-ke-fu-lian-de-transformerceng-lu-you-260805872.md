---
title: 'MACRO: Markov Chain Routing of Transformer Layers'
title_zh: MACRO：基于马尔可夫链的Transformer层路由
authors:
- Paweł Batorski
- Abtin Pourhadi
- Akylgali Aitaza
- Przemysław Spurek
- Paul Swoboda
affiliations:
- Heinrich Heine University Düsseldorf
- Jagiellonian University
- IDEAS Research Institute
arxiv_id: '2608.05872'
url: https://arxiv.org/abs/2608.05872
pdf_url: https://arxiv.org/pdf/2608.05872
published: '2026-08-06'
collected: '2026-08-08'
category: LLM
direction: 动态层路由优化推理
tags:
- LLM
- Dynamic Routing
- Markov Chain
- Transformer
- Inference Optimization
- Computation Budget
one_liner: 不修改模型参数，通过马尔可夫链学习任务特定层路由，精度+5.0%，搜索时间降低9.4倍
practical_value: '- 动态层路由可作为在线模型服务的推理加速手段，根据查询或上下文的复杂度自适应选择执行层数，在搜索推荐系统中平衡延迟与效果。

  - 路由策略以马尔可夫链形式外挂于预训练模型，无需修改原始权重，便于在已有LLM上快速实验与部署。

  - 利用top-k Viterbi解码生成高概率候选路径，可借鉴用于Agent多步推理中对执行路径的规划与剪枝。

  - 将计算预算分阶段建模，可控制推理成本，适合在流量波动下动态调整资源分配，如大促时保障核心服务。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM固定顺序执行所有层，忽略了不同输入对计算深度需求的差异。现有动态路由方法往往需要更新模型权重、高昂的逐样本搜索或依赖推理时的标签。MACRO旨在不修改模型参数的前提下，学习任务特定的层路由以提升性能并降低搜索开销。

**方法**：将层路由建模为上下文依赖的马尔可夫策略，条件包括层索引、计算预算阶段、移动方向（跳过、重复等）以及操作符上下文，支持skip、repeat、residual hidden-state addition三种操作。在训练数据上基于反馈更新路由分布，再通过top-k Viterbi算法解码出高概率的候选路由程序。整个过程冻结基座模型参数。

**结果**：在多个开源LLM的推理与知识基准上，MACRO相比无路由基线平均准确率提升+5.0%，小模型增益更显著；对比最优动态路由方法Dr.LLM，准确率高+7.2%，路由搜索时间从14.8小时降至1.6小时（9.4倍加速），实现了精度与搜索效率的双重提升。
