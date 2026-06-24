---
title: Scaling Laws for Task-Specific LLM Distillation
title_zh: 任务特定LLM蒸馏的缩放定律
authors:
- Lavinia Ghita
- Dhruv Desai
- Ioana Boier
affiliations:
- NVIDIA
arxiv_id: '2606.24747'
url: https://arxiv.org/abs/2606.24747
pdf_url: https://arxiv.org/pdf/2606.24747
published: '2026-06-23'
collected: '2026-06-24'
category: LLM
direction: LLM蒸馏缩放定律与监督格式
tags:
- knowledge distillation
- scaling laws
- model compression
- chain-of-thought
- iterative pruning
- LLMs
one_liner: 量化了领域特定LLM压缩中数据集大小、压缩比、监督格式的缩放规律，发现思维链监督能恢复剪枝损失的通用知识。
practical_value: '- 若对电商搜索/推荐中的 LLM 进行压缩（如商品分类、意图识别），使用**思维链（CoT）监督**可以显著恢复结构化剪枝损失的通用知识，避免模型变成纯粹的领域专家而丧失泛化能力。Label-only
  蒸馏（直接 logit KD 或 LoRA fine-tune）会导致通用能力塌陷。

  - **迭代剪枝+蒸馏**（每步剪枝后重新蒸馏）明显优于一次性剪枝，更匹配生产环境中逐步压缩模型的工程流程；该策略可迁移到实时服务对延迟敏感的场景。

  - 缩放定律给出明确的**数据量-压缩比关系**，实践中可据此预估：要将模型压缩到目标大小，需要准备多少领域数据；数据集过小时，CoT 监督的数据效率优势更明显。

  - LoRA 蒸馏在 label-only 设定下保留了比直接 logit KD 更多的通用知识，如果由于成本无法生成 CoT 标注，优先选用 LoRA 蒸馏作为折中方案。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：大模型部署受延迟和成本限制，需要对领域任务做压缩，但缺乏系统性的缩放规律指导如何在压缩比、数据集大小、监督格式之间权衡。本文以金融新闻标题多分类（35类）为特定领域任务，研究任务特定蒸馏的缩放行为。

**方法**：通过迭代结构化剪枝结合知识蒸馏，对比了两种蒸馏方法（logit-based KD 与 LoRA 蒸馏）及三种监督格式：仅 label、思维链（CoT）、混合 CoT（blended chain-of-thought）。提出了混合 CoT 损失，在 KL 散度蒸馏中加入推理轨迹的监督，以稳定训练。实验系统变化数据集大小、压缩比、监督格式和剪枝调度，拟合缩放定律。

**关键结果**：
- 领域内任务质量随压缩比呈可预测下降，但通用知识基准在远未达到相同压缩比时已快速塌陷。
- **监督格式是控制这一权衡的主要杠杆**：CoT 监督不仅提升数据效率，还能主动恢复剪枝抹去的通用知识；label-only 方法（直接 logit KD）则进一步损害通用能力，LoRA 蒸馏勉强维持剪枝后水平。
- 迭代剪枝+蒸馏比一次性剪枝效果好，混合 CoT 损失在三类监督中取得最佳的数据效率和知识保留。论文公开了 FinHeadlineMix 数据集及一整套实操建议，为其他领域的压缩决策提供了可复用框架。
