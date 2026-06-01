---
title: 'Graph-GRPO: Dependency-Aware Credit Assignment for Generative E-commerce Search
  Relevance'
title_zh: Graph-GRPO：电商搜索相关性生成式推理的依赖感知信用分配
authors:
- Jiarui Che
- Yifei Chen
- Zhixing Tian
- Chenyang Wang
- Ziguang Cheng
affiliations:
- Nankai University
- JD.COM
arxiv_id: '2605.31003'
url: https://arxiv.org/abs/2605.31003
pdf_url: https://arxiv.org/pdf/2605.31003
published: '2026-05-29'
collected: '2026-06-01'
category: GenRec
direction: 生成式电商搜索相关性·图信用分配
tags:
- Graph-GRPO
- Credit Assignment
- E-commerce Search
- Generative Relevance
- LLM Distillation
one_liner: 提出图结构GRPO，将CoT推理步骤构建成依赖图，通过图传播结局奖励到节点，实现细粒度信用分配，提升电商搜索相关性。
practical_value: '- 在结构化推理任务（如电商搜索相关性）中，可将 CoT 步骤间的逻辑依赖显式建模为图，利用图传播结局奖励到局部节点，实现更精细的信用分配，比单纯使用序列级
  GRPO 或独立过程奖励更有效。

  - 可学习图系数与主策略损失联合优化，使信用传播强度自适应不同训练阶段和样本分布，这一机制可泛化到其他多步推理的 RL 微调场景。

  - CoT 随机掩码训练策略：SFT 阶段对推理 token 随机掩码但始终监督决策标签，既保留结构化推理信号又防止过拟合模板化解释，适合作为 RL 初始化。

  - 通过图节点多头蒸馏，将 LLM 的结构化推理能力迁移到轻量 Bert 模型，在满足在线低延迟要求的同时保留多维度匹配判别能力，为 LLM 在搜索中的工业部署提供可行方案。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商搜索相关性判断并非简单的文本匹配，需要解析 query 与产品的主题、属性等多维度信息，并进行结构化推理。现有基于 LLM 的方法多采用结局级奖励的 RL 优化，将整条推理链作为单一优化单元，忽略了推理步骤之间的依赖关系和错误传播，导致信用分配不准确。虽然过程奖励方法可提供更密集的监督，但它们通常将推理步骤视为独立，同样缺乏对依赖关系导致的错误传播的建模。

**方法**：
- **依赖图构建**：将相关性推理过程分解为 7 个语义节点（最终标签 y、主题匹配分 ms、属性匹配分 ma 以及 query/product 侧的主题与属性证据 qs/qa/ps/pa），并根据逻辑依赖定义有向边（如 y→ms, ms→qs 等），形成推理依赖图。
- **图信用传播**：在 GRPO 框架内，将结局级奖励沿图边传播，转化为各节点的细粒度信用信号，并引入可学习的边传播系数（φ），通过主策略损失同步更新这些系数，实现自适应责任分配。
- **节点级优势计算**：为每个节点计算组内归一化优势，映射到 token 级策略优化，使不同推理单元能独立更新。
- **训练框架**：先用标签优先 CoT 随机掩码进行 SFT 初始化，再通过 Graph-GRPO 进行 RL 优化，最后用图节点多头蒸馏将能力迁移至轻量 Bert 模型供线上部署。

**关键结果**：在京东搜索的真实标注数据（92k 样本）上，Graph-GRPO 在 Macro-F1（81.26%）和无关类 F1（84.75%）上均优于 LLM-SFT 和标准 GRPO。线上 A/B 测试将 Bad Case Rate 从基线平均 11.97% 降至 11.65%，相对降低 2.67%，模型已部署服务亿级用户。
