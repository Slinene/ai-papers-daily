---
title: What If Chain-of-Thought Is Not Enough?
title_zh: 如果思维链还不够：训练 LLM 采用问题-选项-标准决策框架
authors:
- Marc Jansen
affiliations:
- Computer Science Institute, University of Applied Sciences Ruhr West, Germany
arxiv_id: '2611.26282'
url: https://arxiv.org/abs/2611.26282
pdf_url: https://arxiv.org/pdf/2611.26282
published: '2026-11-19'
collected: '2026-11-21'
category: Reasoning
direction: LLM 推理 · 结构化决策微调
tags:
- Chain-of-Thought
- Question-Option-Criteria
- Fine-tuning
- Decision Support
- LLM Reasoning
- Interpretability
one_liner: 用结构化 Question-Option-Criteria 替代 CoT 微调 LLM，提升决策支持的可解释性与答案质量
practical_value: '- 在推荐/搜索的决策型 Agent 中，让 LLM 显式输出「问题-选项-标准」三元组，替代自由式 CoT，便于线上校验、日志审计与可解释性保障。

  - 借鉴三代训练管线：先构建基础 QOC 决策数据集冷启动，再逐步加入答案合成与统计增强推理，用于 fine-tune 业务模型；建议先在较大模型上验证，小模型可能内部一致性不足。

  - 在广告创意优选、query 推荐、push 文案选择等场景，将候选集作为 options、业务目标/用户意图作为 criteria，让模型做结构化决策，方便后续规则干预与
  A/B 测试。

  - 注意模型规模阈值：QOC 计算需要模型可靠执行，若基座太小则内部一致性差、收益不显著，部署前需评估规模与一致性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 LLM 推理提升多依赖 Chain-of-Thought 提示或其内部化，但 CoT 对决策支持任务未必是最优 scaffold，需要更显式的决策结构以提高可靠性与可解释性。

**方法关键点**：引入 Question–Option–Criteria (QOC) 框架，将任务拆为决策问题、竞争选项和评价标准，训练模型内部遵循该结构化思考过程。开发三代微调管线：第一代构建基础 QOC 决策核心；第二代加入更丰富的答案合成；第三代用统计增强的 QOC reasoning 进一步优化。评估同时关注模型内部一致性与输出质量。

**关键结果**：QOC 微调模型的答案质量优于未微调基座；当模型规模足够大、能可靠执行底层 QOC 计算时，增益尤其显著。结果表明 LLM 的内部思考模型可被训练改变，结构化替代 CoT 有望带来更可靠、可解释且任务自适应的决策支持。论文未报告具体数值，但强调规模阈值对 QOC 执行一致性的影响。
