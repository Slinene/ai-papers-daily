---
title: Base Models Can Reason By Taking a Cue From Training Data
title_zh: 从训练数据学到的 token cue 激发基础模型推理
authors:
- Sophie L. Wang
- Amil Dravid
- Rulin Shao
- Kevin Farhat
- Sewon Min
- Alexei A. Efros
affiliations:
- MIT
- UC Berkeley
- University of Washington
- Allen Institute for AI
arxiv_id: '2610.06851'
url: https://arxiv.org/abs/2610.06851
pdf_url: https://arxiv.org/pdf/2610.06851
published: '2026-10-04'
collected: '2026-10-06'
category: Reasoning
direction: LLM 推理行为与训练数据关联
tags:
- token cues
- reasoning
- RL
- base model
- training data
- causal intervention
one_liner: 固定特定起始 token cue 可使 base model 推理性能接近 RL 模型，该效应源于训练数据关联
practical_value: '- 在搜索推荐、电商问答等提示工程中，可对输出起始 token（如 `"Alright,"`、`".\n\nOkay"`）做批量
  A/B 测试，固定有效 cue 提升 base model 的推理质量，避免依赖 RL 训练成本。

  - 若业务中 RL 训练的推荐/策略模型相比 base model 有显著提升，可分析其输出前缀 token 分布，将高频有利 cue 固定到推理流程中，部分回收性能增益。

  - 遇到模型输出不符合预期（如推荐理由弱、拒绝率异常），可通过数据干预手段在训练数据中增删特定 token 关联，低成本调整行为，无需重新预训练。

  - 安全合规场景需注意：token cue 可能被操纵以绕过拒绝行为，评测时应覆盖多种 cue 下的安全表现，避免只测试默认提示。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：训练数据如何在 base model 响应起始 token 与后续推理行为之间建立关联？为何某些起始 token（如 `"\n\nOkay"`）能显著提升推理效果，而 RL 训练似乎强化了这一现象？

**方法关键点**：
- 固定特定起始 token cue，观察对数学/编码任务的影响，对比 base model 与 RL 模型表现。
- 统计 RL 训练前后各 cue 出现概率，分析其与性能提升的关系。
- 通过因果数据干预，将任意词（如 `"chicken"`）变为有效推理 cue，或移除已有 cue 的作用；同样方法可让 `"Think duck duck goose"` 与 `"Think step by step"` 效果相当。
- 探针分析不同 cue 诱导的隐藏状态表征与训练数据中不同文档类型（如短问答、推理轨迹）的相关性。
- 扩展到安全场景，考察不同 cue 对应的拒绝/合规行为。

**关键结果**：
- 固定 `".\n\nOkay"` 使 Olmo-3-7B 在 MATH-500 pass@1 从 42% 提升至 78%；`"Alright,"` 使 Qwen3-14B 从 72% 提升至 87%。
- RL 训练使有利 cue 更可能出现，固定这些 cue 可恢复 RL 相对 base model 的大部分性能增益。
- 数据干预后，`"chicken"` 可成为有效推理 cue，固定 `".\n\nChicken"` 在 MATH-500 上达到 77% 与 `".\n\nOkay"` 的 78% 接近。
- 不同 cue 的隐藏表征与训练集不同文档类型强相关，表明行为差异可追溯到预训练语料分布。
