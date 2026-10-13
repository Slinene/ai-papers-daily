---
title: Self-Preservation in Language Models
title_zh: 语言模型中的自我保存
authors:
- Dongkyu Cho
- Rumi Chunara
- Ali Behrouz
affiliations:
- New York University
- Google Research
- Cornell University
arxiv_id: '2610.12602'
url: https://arxiv.org/abs/2610.12602
pdf_url: https://arxiv.org/pdf/2610.12602
published: '2026-10-07'
collected: '2026-10-13'
category: Training
direction: 持续学习 · 自生成重放防遗忘
tags:
- continual learning
- catastrophic forgetting
- replay generation
- self-preservation
- instruction tuning
one_liner: 用 Task Bank 与自生成重放实现更广泛的持续学习防遗忘，并证明模型可辅助选择重放目标
practical_value: '- 在模型周期更新（如新增品类、场景）时，不要只保存固定旧任务样本，可让冻结的旧模型根据 Task Bank 自动生成重放数据，覆盖面更广，减少对原始训练数据的依赖。

  - 用带权重/相关性的 Task Bank 选择重放目标：新任务知情的选择在 4B 模型上能提升旧能力保留率，但在小模型上不一定有效，业务小模型需谨慎验证。

  - 监控“之前回答正确的样本的保留率”，而不仅是平均准确率；推荐/广告模型更新时也建议监控老用户、长尾场景的指标，防止平均指标掩盖遗忘。

  - 在固定示例预算下，可以用少量新任务样本换取更多重放样本，以旧能力稳定为优先；对线上稳定性要求高的场景（如广告出价、搜索排序）更适用。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：持续学习（CL）旨在适配预训练模型的同时保持旧能力，但人工指定的保留任务只覆盖模型知识的一部分，遗忘可能出现在这些任务之外。近期研究表明，语言模型可以在不访问原始训练数据的情况下生成有用的重放数据。本文进一步追问：模型能否帮助选择保留目标，从而更广泛地保护自身能力？

**方法**：作者提出 Task Bank，将任务描述和示例组织成可选择的条目。冻结的旧模型根据选中的条目生成重放数据，用于后续持续指令微调。实验使用不同规模的 Qwen 模型，对比随机选择与基于新任务信息的选择策略，并追踪“之前正确回答的样本保留率”这一细粒度指标。

**关键结果**：1）新任务种类和学习率共同决定哪些旧能力退化，平均准确率会掩盖具体任务上的遗忘；2）生成重放能减少 Task Bank 之外任务的遗忘，合并多个局部 bank 可进一步增强保护，提升测试规模下的平均保留率；3）模型可辅助选择重放目标：在 4B 模型上，新任务知情的选择比随机选择带来更高的 held-out 保留率，但小模型没有相应优势；固定示例预算下，用重放替换新任务示例能提高保留率，但新任务收益变小。

**结论**：语言模型可以通过生成重放数据和选择重放目标来支持更广泛的自我保存，为实际持续更新提供了一种数据高效、不依赖原始数据的防遗忘方案。
