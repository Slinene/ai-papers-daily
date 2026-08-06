---
title: 'Reasoning Core: Designing Broad Procedural Data for Completion-Supervised
  Reasoning Training'
title_zh: 程序化推理数据设计：Completion-Supervised微调下的广泛生成器集合
authors:
- Damien Sileo
- Valentin Lacombe
- Dimitri Kachler
affiliations:
- Univ. Lille
- Inria
- CNRS
- Centrale Lille
- CRIStAL
arxiv_id: '2608.05148'
url: https://arxiv.org/abs/2608.05148
pdf_url: https://arxiv.org/pdf/2608.05148
published: '2026-08-05'
collected: '2026-08-06'
category: Training
direction: 程序化数据生成 · 推理训练
tags:
- Procedural Generation
- Reasoning Training
- Completion Supervision
- Synthetic Data
- Data Quality
one_liner: 构建50个生成器的Reasoning Core，揭示紧凑目标和校准难度对完成监督推理训练的关键作用
practical_value: '- 为Agent训练构建程序化推理数据：可借鉴其生成器框架，创建电商购物助手所需的多步决策、约束满足等合成样本，通过难度控制逐步提升模型推理能力。

  - 训练数据设计原则：优先保证目标的紧凑性（减少冗长输出）和难度校准，避免模型学习表面模式；在搜索推荐场景中生成query改写或解释时，可据此过滤低质样本。

  - 数据质量审计流程：将模型辅助审查、人工裁决和回归测试组合，用于保障搜索/推荐系统的合成训练数据质量，快速发现生成与标注错位。

  - 验证数据效用的方法论：不依赖单一的语义合理性，而是直接在下游任务（如DROP/ARC）上评估数据贡献，业务中可据此建立快速反馈循环，筛选真正有效的训练数据。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：程序化生成器能大规模产出可验证的推理问题，但其作为完成监督微调的数据源尚未被充分探索。现有工作多关注强化学习奖励，缺乏对监督微调中数据设计原则的系统分析。

**方法关键点**：构建**Reasoning Core**库，包含50个生成器，覆盖数学、逻辑、规划、状态跟踪、形式语言、结构化数据、游戏、因果和代码等九大类任务。每个生成器配置语义评分器、难度控制和评估器，确保样本可验证和多样性。在3B参数模型上，采用匹配的完成监督协议，与Procedural Warmup、Reasoning Gym、SynLogic三个程序化数据集进行横向对比。训练后在下游推理基准DROP、LogiQA、ARC-Challenge上评估。

**关键结果**：Reasoning Core在三个基准上平均得分最高，显著超越无程序化数据的基线及其它三个集合。分析发现：语义有效性不能保证训练效用；紧凑的生成目标和校准的难度是提升性能的关键。此外，通过模型辅助、人工裁决和回归测试的审计管道，揭示了各数据集在生成、渲染、目标、评分间存在隐蔽错配，提示仅靠程序化生成不能确保正确性。
