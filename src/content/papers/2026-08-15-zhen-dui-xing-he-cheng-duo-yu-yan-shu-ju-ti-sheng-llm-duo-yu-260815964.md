---
title: LLMs Get Smarter from Targeted Synthetic Multilingual Data
title_zh: 针对性合成多语言数据提升 LLM 多语言推理能力
authors:
- Ishika Agarwal
- Arkajyoti Charaborty
- Tanner Sorensen
- Neha Gupta
- Andreas Stolcke
affiliations:
- UIUC
- Uniphore
arxiv_id: '2608.15964'
url: https://arxiv.org/abs/2608.15964
pdf_url: https://arxiv.org/pdf/2608.15964
published: '2026-08-15'
collected: '2026-08-22'
category: Training
direction: 多语言 LLM 定向数据生成与训练优化
tags:
- Multilingual LLM
- Synthetic Data
- Data-Centric AI
- Language-Specific Competency
- Fine-tuning
- X-Lingual Reasoning
one_liner: 提出 HOTFIXR 数据框架，自动探测多语言弱点并生成合成数据，ID 提升 6.2%、OOD 语言提升 7.1%
practical_value: '- 迁移到多语言搜索/推荐：在不同语言 query 下，LLM 表现不一致会影响搜索结果排序和相关性判断；可借鉴 HOTFIXR
  思路，先用 teacher model 自动找出模型在哪些语言/任务上最容易出错，只对薄弱语言做定向合成数据微调，避免全量 language-balanced
  数据造成主语言性能下降。

  - 困难样本生成与筛选：把“难度优化”用于 query 改写、意图分类、内容理解等模块；让 teacher LLM 生成当前模型易混的合成 query（如相近语言、低资源语言、口语化表达），并保留学生模型答错的样本作为高质量微调数据，减少人工标注。

  - 评估指标：引入跨语言一致性 spread 指标，监控线上多语言推荐/搜索在不同语言之间的效果差异，避免只看总体指标掩盖局部退化。

  - 工程实现：可搭建自动化的“弱点探测 → 定向生成 → 迭代微调”流水线；每轮用教师模型生成候选数据，根据学生模型 loss/错误率筛选 top-hard 样本，控制数据规模和训练成本。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：多语言 LLM 存在语言特定能力（LSC）不一致，同一语义 query 在不同语言下效果不同；现有“先翻译成英语”会损失非英语言表达，而“语言平衡训练”会拉低整体性能。
方法关键点：HOTFIXR 采用数据为中心视角，用 teacher model 主动探测 student model 的多语言弱点，基于难度优化生成定向合成数据；不是简单平衡语言分布，而是针对模型在特定语言/任务上的 failure 生成训练样本。
关键结果：在 3 个 in-distribution 任务、3 个 OOD 任务、4 个 OOD 语言上，HOTFIXR 平均提升 ID 6.2%，减少 fine-tuning 导致的 OOD 任务灾难性遗忘 3.7%，提升 OOD 语言 7.1%；在训练类 baseline 中 ID 与 OOD 最佳，同时 cross-lingual spread 保持一致。
