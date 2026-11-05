---
title: Presentation Sensitivity in Typed Decision Models for Subjective Text Evaluation
title_zh: Typed Decision 模型在主观文本评估中的展示敏感性审计
authors:
- Jatin Agrawal
- Radhika Mamidi
affiliations:
- LTRC, IIITH
arxiv_id: '2611.06384'
url: https://arxiv.org/abs/2611.06384
pdf_url: https://arxiv.org/pdf/2611.06384
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: LLM 评估器的展示敏感性审计
tags:
- LLM evaluators
- presentation sensitivity
- robustness
- human alignment
- decision models
one_liner: 审计 Jev、Clef Flash、Perplexity Decider 发现展示干预显著改变主观评分，需验证评估管线
practical_value: '- 在评估管道中使用 LLM 决策模型时，务必固定选项顺序或随机化，避免位置偏差（如 Jev 摘要任务中第二位置概率优势达 6.11
  个百分点）。

  - 设计评估 prompt 时避免使用拒绝框架（如“哪个更差”），因为 Clef 在摘要任务上与人类偏好一致性下降 23.36 点；优先采用积极框架。

  - 对同一评估任务测试多种评分格式（如等级 vs 二元选择），格式可能改变分数分布；若只关心排名，格式影响较小，但需在不同格式间验证排名稳定性。

  - 将“可重复性”和“人类对齐”作为独立指标监控，定期对评估器做扰动测试（位置、标签、背书等），特别是在更换模型或 prompt 版本时。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：Typed decision models（如 Jev）提供快速低成本主观判断，但缺乏生成解释或思维链，其展示敏感性未被充分审计。评估管线若依赖此类模型，需验证其决策和分数解释的可靠性。

**方法关键点**：对 Jev、Clef Flash、Perplexity Decider 进行受控审计，覆盖 6 个数据集、9000 条多重标注的幽默、有用性、摘要项目，收集 70.2 万次判断。干预因素包括选项位置、标识符、作者声明、读者背书、决策框架、评分 rubrics，同时保持被评估文本不变。

**关键结果**：Jev 在摘要任务上第二位置概率优势达 6.11 个百分点；反转读者背书使 Perplexity 选择幽默文本在 40.40% 的配对中改变；拒绝框架使 Clef 摘要与人类偏好一致性降低 23.36 点；评分格式改变分数水平但常保留排名。结论：可重复性、展示鲁棒性、人类对齐是评估器的独立属性，可靠使用需分别验证。
