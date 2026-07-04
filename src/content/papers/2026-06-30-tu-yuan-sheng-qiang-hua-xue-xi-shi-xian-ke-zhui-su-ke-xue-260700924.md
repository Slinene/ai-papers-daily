---
title: Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis
  Generation through Conceptual Recombination
title_zh: 图原生强化学习实现可追溯科学假设生成
authors:
- Subhadeep Pal
- Shashwat Sourav
- Tirthankar Ghosal
- Markus J. Buehler
affiliations:
- Massachusetts Institute of Technology
- Washington University in St. Louis
- Oak Ridge National Laboratory
- Lawrence Berkeley National Laboratory
arxiv_id: '2607.00924'
url: https://arxiv.org/abs/2607.00924
pdf_url: https://arxiv.org/pdf/2607.00924
published: '2026-06-30'
collected: '2026-07-04'
category: Reasoning
direction: 图增强推理 · 强化学习微调
tags:
- GRPO
- Graph Reasoning
- Hypothesis Generation
- Traceability
- Semantic Diversity
- RL Fine-tuning
one_liner: 通过图结构与强化学习将推理显式阶段化，实现可解释、可追溯的多步假设生成
practical_value: '- 将多步推理拆分为显式阶段（机制探索→图构建→模式提取→假设综合），每个阶段输出结构化中间结果，可直接用于构建推荐系统的可解释推理链路（如商品推荐理由追溯）。

  - 用图结构链接概念实体，实现因果关系的构建与检查，可迁移到电商知识图谱推理、搜索查询扩展中的概念关联验证。

  - 采用GRPO对分阶段输出进行奖励优化（例如，对图构建正确性、最终假设与中间步骤的一致性打分），能有效提升Agent链式思考的连贯性。

  - 测试时图扩展（增加计算量）可以在不扩大语义空间的情况下提升长程概念重组的质量，这为生成式推荐的多样性-相关性平衡提供了新的控制思路。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
标准LLM在开放材料设计问题上能生成流畅回答，但中间推理过程缺乏透明度和可追溯性，无法判断最终结论是否得到前后一致的推理支撑。

### 方法
提出Graph-PRefLexOR，将推理过程显式组织为四个阶段：机制探索、图构建、模式提取、假设综合。核心包括：
- **图原生推理**：模型在推理过程中动态构建概念图，用符号化关系结构链接实体，使因果连接可构造、可检查、可复用。
- **GRPO（Group Relative Policy Optimization）微调**：设计阶段性的奖励信号（如图结构的合理性、最终假设与中间步骤的对齐度），端到端优化整个推理链条。
- **测试时图扩展**：在推理时通过增加计算量扩展图结构，侧重提升长程概念重组能力。

### 结果
在100个材料科学开放问题上：
- 相较基座模型，综合性能提升40–65%，其中推理可追溯性提升最显著。
- 嵌入分析显示语义多样性约为基线的2–3倍。
- 层间隐藏状态分析证实结构化推理与最终答案的强对齐。
- 测试时增加计算主要增强语义空间内的远程概念重组，而非简单扩展覆盖范围，表明该架构更擅长深入挖掘概念间的间接关联。
