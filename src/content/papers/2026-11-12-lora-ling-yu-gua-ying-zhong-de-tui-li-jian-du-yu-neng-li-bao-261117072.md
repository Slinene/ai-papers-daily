---
title: Reasoning Supervision and Capability Retention in LoRA Domain Adaptation
title_zh: LoRA 领域适应中的推理监督与能力保留
authors:
- Saleh Ashkboos
- Dhruv Desai
- Lavinia Ghita
affiliations:
- NVIDIA
arxiv_id: '2611.17072'
url: https://arxiv.org/abs/2611.17072
pdf_url: https://arxiv.org/pdf/2611.17072
published: '2026-11-12'
collected: '2026-11-14'
category: Training
direction: LoRA 领域适应训练策略
tags:
- LoRA
- Domain Adaptation
- Reasoning Supervision
- Capability Retention
- Fine-tuning
one_liner: 比较三种 LoRA 微调方案，发现 response-only 在领域性能与通用能力保留上最优，推理监督未带来增益
practical_value: '- 在电商/广告的领域分类任务（如意图识别、内容审核、query 分类）中，优先采用 response-only LoRA，避免引入
  teacher reasoning traces 增加训练复杂度和推理成本却无明确收益。

  - 若业务场景需要保留通用能力（如 Agent 的指令跟随、常识推理），response-only LoRA 已能基本保持冻结模型的泛化水平，无需额外推理监督。

  - 不要采用 dual-adapter 分离训练 traces 和 labels 的复合方案，实验显示其并未带来进一步增益，徒增工程复杂度。

  - 若团队尝试用压缩后的 reasoning traces 做蒸馏，需注意短摘要会使模型校准趋近 response-only 但无法完全达到，收益有限，建议先做小规模消融验证。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：金融领域微调 LLM 时，如何在提升领域任务性能的同时保持通用能力（指令跟随、校准、泛化）是一大挑战。现有工作常引入 teacher reasoning traces 进行监督，但缺乏系统对比。

**方法关键点**：论文在 Qwen3-8B 上用 LoRA 进行消融，对比三种训练方式：(1) response-only LoRA，监督信号仅用标签；(2) single-adapter reasoning，将 teacher traces 与标签一并加入训练损失；(3) dual-adapter composite training，为 traces 和标签分别训练独立 LoRA adapter。另将 teacher traces 压缩为摘要后训练，观察校准变化。

**关键结果**：response-only LoRA 提升领域内性能且通用能力接近冻结模型，其中 calibration 和 argmax accuracy 提升最明显；single-adapter reasoning 的领域内指标落后于 response-only，MMLU-Pro 仅轻微上升，其他 retention 基准在正常波动范围内；dual-adapter 无进一步增益；压缩 traces 后校准向 response-only 靠拢但未达到。
