---
title: Training Documents Reranker with Search Rubrics for Deep Research Agent
title_zh: 用搜索评分标准训练文档重排序器以支持深度研究智能体
authors:
- Wenhan Liu
- Yu Lu
- Qiaolin Xia
- Hui Xu
- Tong Zhao
- Jian Xi
- Yutao Zhu
- Haijin Liang
- Haibo Shi
- Hao Wang
affiliations:
- 中国人民大学
- 腾讯
arxiv_id: '2608.03527'
url: https://arxiv.org/abs/2608.03527
pdf_url: https://arxiv.org/pdf/2608.03527
published: '2026-08-04'
collected: '2026-08-05'
category: RAG
direction: 搜索评分标准引导的文档重排序器训练
tags:
- reranker
- rubric-based RL
- GRPO
- deep research
- RAG
- document set selection
one_liner: 提出层级式搜索评分标准，指导文档重排序器训练，提升智能体检索质量并减少搜索调用次数
practical_value: '- **搜索评分标准可迁移至电商/推荐场景**：借鉴层级式评估（集合级：相关性、简洁性、一致性；文档级：来源权威性、时效性），为商品搜索词或推荐候选集设计
  query-specific 质量 rubrics，直接用于训练重排模型或构造奖励函数。

  - **两阶段训练范式可直接复用**：先用教师模型（如强 LLM）按 rubrics 生成伪标签做 SFT 冷启动，再用 GRPO 搭配 rubrics 加权奖励做
  RL 微调，这一范式适合商品列表、广告创意列表等需要集合整体优化的排序任务。

  - **rubric 构造方法可提升评估与训练信号质量**：用强 LLM 先合成高质量答案，再扩展出细粒度、带权重的评分标准，能够更精准地捕捉集合级别的信息需求（如多样性、覆盖度），这个方法可直接嫁接于推荐系统的离线评估或
  RL reward 设计。

  - **文档集级别重排思想可直接用于电商搜索/RAG 系统**：不按单个文档相关性排序，而是直接输出一个满足整体质量要求的子集，能够减少冗余、提升证据充分性，可降低后续
  Agent 或 LLM 生成回答时所需的搜索步数，改善时延。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
深度研究 Agent 通过多步推理与检索产生长文本回答，但传统重排序器仅按单文档相关性打分，无法保证 top-k 文档集合的整体质量——集合可能缺乏多样性、包含冗余、或来源不可靠，导致 Agent 需要更多次搜索调用且回答质量受限。现有 generation-oriented 重排方法缺乏对集合层面需求的显式建模。

**方法关键点**  
- **层级式搜索评分标准**：定义固定 meta rubrics，集合级评估相关性、简洁性、一致性，文档级评估来源权威性与时效性；对每个查询，先用 GPT-5.1 合成高质量答案，再基于 meta rubrics 扩展出带权重的 query-specific rubrics。  
- **两阶段训练**：① **Rubrics 引导 SFT**：教师模型 GPT-5.1 根据 rubrics 选择高质量文档集作为伪标签，冷启动训练 Qwen3-8B 重排序器，输入仅为查询与候选文档列表（推理时无需 rubrics）。② **Rubric 基线 RL**：用 GRPO 优化，奖励函数由 LLM Judge 对每个 rollout 按 rubrics 评分，按权重聚合集合级和文档级分数，同时加格式奖励；训练中候选文档长度随机化以提升泛化。  
- **推理时直接输出文档子集**，无需 rubrics 输入，可处理不同数量的候选文档。

**关键结果**  
在 4 个深度研究基准（HealthBench, WebWalkerQA, DRB, ResearchQA）上，RubricRanker 的平均得分为 60.1，比最优 baseline Rank4Gen 高出 2.6 分；在 5 个 RAG 基准上平均 EM 达 40.0，比 Rank4Gen 高 2 分。消融实验：去掉 RL 平均分降至 51.1，去掉 SFT 骤降至 48.3。在 HealthBench/ResearchQA 上，RubricRanker 使 Agent 平均搜索调用次数从基线 3.2–3.5 降至 2.9，相对减少约 9–17%。

**一句话总结**：用 query-specific rubrics 显式定义文档集质量标准，通过两阶段训练让重排序器内化这些要求，实现集合级优化并显著提升下游回答质量与检索效率。
