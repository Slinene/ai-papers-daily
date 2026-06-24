---
title: 'Counsel: A Meta-Evaluation Dataset for Agentic Tasks'
title_zh: Counsel：首个面向Agent任务的元评估数据集
authors:
- Sashank Pisupati
- Henry Broomfield
- Eujeong Choi
- Antonia Calvi
- Charlie Wang
- Roman Engeler
- Max Bartolo
- Patrick Lewis
affiliations:
- Atla AI
- Cohere AI
- Mistral AI
- Google DeepMind
arxiv_id: '2606.21627'
url: https://arxiv.org/abs/2606.21627
pdf_url: https://arxiv.org/pdf/2606.21627
published: '2026-06-18'
collected: '2026-06-24'
category: Eval
direction: LLM-as-judge 评估 · Agent 过程批评质量对齐
tags:
- LLM-as-judge
- meta-evaluation
- agentic evaluation
- process critique
- human alignment
- open-source dataset
one_liner: 构建首个公开的Agent过程批评元评估数据集，量化LLM-as-judge的人类对齐度，最强judge错误位置对齐~88%
practical_value: '- **迁移标注协议**：对Agent交互轨迹的过程批评，采用“正确位置、正确理由”、“正确位置、理由差”、“不应标记”三级标注，直接用于校准电商客服或推荐Agent的自动评估器。

  - **选择LLM judge的基准**：模型能力与推理努力（如更多tokens）均提升判断对齐度，实践中可依据任务复杂度权衡成本，优先选择更强开源模型（如文中开源模型组合）。

  - **构建自有元评估数据集**：方法可复现，从已有ground-truth agent benchmark产生过程批评，然后人工评价批评质量，用于训练或微调定制化的judge模型。

  - **评估Agent系统可靠性**：在广告投放、搜索推荐多步交互流程中，可借助该范式量化自动评估的偏差，避免错误决策被放大。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Agent系统任务日益复杂，人工标注轨迹耗时且难以规模化，LLM-as-judge（LLMJ）被广泛用于自动批评过程与结果，但其批评的可靠性缺乏量化。

**方法**：构建Counsel数据集，从tau-bench（客服Agent）和DA-Code（编程Agent）两个基准中获取开源LLMJ的过程批评，由人类标注者将每条批评分为“正确位置且推理正确”、“正确位置但推理差”、“不应标记”三类，达到0.78的Krippendorff's α一致性。随后用不同能力的开源judge模型进行实验，考察模型能力和推理努力对与人类对齐度的影响。

**关键结果**：能力更强的judge模型和增加推理努力均提升对齐度；最强开源judge在错误位置对齐上达~88%，在推理质量上达~65%。数据集完全采用开源模型生成，已开放许可。
