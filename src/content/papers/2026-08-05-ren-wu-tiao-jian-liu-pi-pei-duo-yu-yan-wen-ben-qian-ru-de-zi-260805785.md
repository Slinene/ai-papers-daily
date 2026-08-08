---
title: Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptation
title_zh: 任务条件流匹配：多语言文本嵌入的自适应平衡训练
authors:
- Tirth Bhatt
- Naren Kumar S
- Mayank Singh
affiliations:
- LINGO Research Group, Indian Institute of Technology Gandhinagar
arxiv_id: '2608.05785'
url: https://arxiv.org/abs/2608.05785
pdf_url: https://arxiv.org/pdf/2608.05785
published: '2026-08-05'
collected: '2026-08-08'
category: Training
direction: 多语言嵌入任务自适应训练范式
tags:
- Flow Matching
- Multilingual Embedding
- Task-Conditional
- Curriculum Learning
- Teacher-Guided
- Embedding Adaptation
one_liner: 提出任务条件流匹配，对翻译任务用流匹配，其他任务用匹配目标，结合教师引导与课程学习，多语言嵌入达 SOTA
practical_value: '- **多任务嵌入微调避免冲突**：在处理翻译、检索、分类等混合任务时，可借鉴 TCFM 对不同任务家族采用不同的训练目标，例如翻译用流匹配（适合连续对齐），检索/分类仍用对比学习/交叉熵，避免单一目标造成性能跷跷板。

  - **教师引导与课程学习稳定适应**：通过冻结原始模型做教师，加蒸馏损失保持旧知识，再配合三阶段课程（先教师引导，再逐步引入新任务），可有效防止灾难性遗忘，适用于业务中持续更新多语言嵌入模型的场景。

  - **多语言搜索/商品检索**：若业务涉及跨语言商品搜索、query 理解，可借鉴 TCFM 对平行语料（翻译对）使用流匹配直接对齐表示，提升多语言 embedding
  的一致性，而不损伤其他任务指标。

  - **工程实现参考**：流匹配模块轻量，可与对比学习头并存，通过 task-conditioned 开关选择路径；课程学习的分阶段训练策略可直接嵌入现有 ML
  pipeline，无需大幅改动架构。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多语言文本嵌入模型需同时适应翻译、检索、分类等不同性质的任务，但单一训练目标（如对比学习）在处理翻译时易产生冲突信号，导致某些任务提升而其他任务下降。

**方法**：提出任务条件流匹配（TCFM），根据任务类型选择性应用目标：对翻译任务使用**流匹配**（Flow Matching），学习从源语言到目标语言的连续向量场变换，更适合细粒度双语对齐；对检索、分类、配对分类等任务，保留更适配的对比学习或分类目标。同时引入**教师引导**（冻结初始模型作为教师，加蒸馏损失）和**三阶段课程学习**（先蒸馏、再逐步混合多任务），保证稳定适应，防止遗忘。

**结果**：在 Indic Massive Text Embedding Benchmark 上，TCFM 在多语言检索、分类、STS 等多个任务上均超越基线，总体性能建立新的 SOTA，并且在不同模型家族（如 LaBSE、XLM-R）上均表现出泛化提升，验证了任务条件目标选择和课程策略的有效性。
