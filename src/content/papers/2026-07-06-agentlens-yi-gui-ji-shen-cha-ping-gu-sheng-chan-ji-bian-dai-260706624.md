---
title: 'AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation'
title_zh: AgentLens：以轨迹审查评估生产级编程代理
authors:
- Andrey Podivilov
- Vadim Lomshakov
- Sergey Savin
- Matvei Startsev
- Roman Pozharskiy
- Maksim Parshin
- Sergey Nikolenko
affiliations:
- Explyt
- St. Petersburg Department of the Steklov Institute of Mathematics
- St. Petersburg State University
arxiv_id: '2607.06624'
url: https://arxiv.org/abs/2607.06624
pdf_url: https://arxiv.org/pdf/2607.06624
published: '2026-07-06'
collected: '2026-07-11'
category: Eval
direction: 代理评估 · 轨迹审查
tags:
- Agent Evaluation
- Trajectory Review
- LLM-as-Judge
- Production Benchmark
- Nightly Regression
one_liner: 提出基于LLM审查完整交互轨迹的编程代理评估基准，提供可解释评价用于诊断与回归检测。
practical_value: '- **从结果评估转向过程评估**：在电商对话Agent（如导购助手）中，不仅评估最终推荐商品是否准确，还需审查对话轨迹的指令遵循、工具调用、错误恢复，以提升用户体验。

  - **LLM轨迹审查用于回归检测**：借鉴nightly评估管道，用LLM编写审查脚本，自动对比新旧版本Agent的轨迹，捕捉产品回归（如回答风格变差、幻觉增加）。

  - **形式化验证+LLM审查混合策略**：对可客观验证的部分（如商品ID有效性、API调用格式）用形式化检查，对主观质量（解释流畅性、推荐理由合理性）用LLM审查，兼顾准确性和灵活性。

  - **开放任务评估**：对于生成商品描述、推荐文案等没有唯一正确答案的任务，采用整体轨迹质量评分，替代简单的pass/fail。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有编码代理基准仅关注任务最终成功与否，忽略交互过程中指令遵循、工具使用、错误恢复等实际体验要素，尤其不适合文档撰写等无二元结果的开放性任务。

**方法关键点**：
- 提出AgentLens基准，评估完整执行轨迹。
- 结合形式化验证（对可客观检查的步骤）与LLM驱动的轨迹审查及并排比较，生成可读的评分解释。
- 已部署于nightly评估管道，用于诊断模型行为、对比代理版本、检测产品回归。

**关键结果**：该基准能有效区分模型表面成功与真实可靠度，帮助团队发现细粒度行为退化；已在真实生产环境中用于捕捉回归。
