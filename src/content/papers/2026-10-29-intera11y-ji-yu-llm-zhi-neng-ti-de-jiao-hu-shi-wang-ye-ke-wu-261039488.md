---
title: 'InterA11y: Interactive Web Accessibility Error Detection with LLM Agents'
title_zh: InterA11y：基于 LLM 智能体的交互式网页可访问性错误检测
authors:
- Mingyuan Zhong
- Mengqi Shi
- Davin Win Kyi
- Ajit Mallavarapu
- Xia Chen
- James Fogarty
- Jacob O. Wobbrock
affiliations:
- University of Washington
- Cornell University
- Carnegie Mellon University
arxiv_id: '2610.39488'
url: https://arxiv.org/abs/2610.39488
pdf_url: https://arxiv.org/pdf/2610.39488
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: LLM Agent 结合 rubrics 与工具审计
tags:
- Web Accessibility
- LLM Agents
- Rubrics
- Interactive Tools
- Evaluation
- WCAG
one_liner: 结合可测试规则分解与确定性交互工具，显著提升 LLM Agent 网页可访问性审计召回并保持高精度
practical_value: '- 将复杂质量标准/规则分解为可测试的 rubrics，并由 agent 逐步收集证据，可用于商品信息合规审核、广告审核、推荐理由生成等场景，降低
  agent 主观误判。

  - 用确定性工具（如 DOM 检查、焦点/错误消息提取）替代或补充 LLM 直接推理，能减少 token 消耗和幻觉，提高 precision，在需要高准确率的业务（如广告审核、商品合规）可借鉴。

  - 系统架构上采用 LLM 负责规划与证据解释、工具负责确定性检查，可隔离不同模型间的表现差异，推荐系统 agent 协同中也可采用同类混合架构。

  - 评估方法上，用专家标注案例集对比召回/精度并关注跨模型一致性，对业务上线 agent 的评测与可信度验证有参考价值。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：现有基于 LLM 的网页可访问性检查器忽视交互与动态上下文，导致覆盖有限、误报率高、跨模型表现不一致。

**方法关键点**：
- 设计 agentic 评估系统 InterA11y，结合 rubrics 与 interactive tools。
- Rubrics 将 WCAG 成功标准分解为可测试的方面，引导 agent 收集和解释证据。
- Interactive tools 通过确定性方式检查或操作页面，获取焦点外观、错误消息等证据，减少 LLM 幻觉。
- 基于 682 个精选测试用例开发，针对 10 个常见违规标准。

**关键结果数字**：
- 在 197 个专家标注案例（来自 54 个真实网页）上，召回率 79.0%，对比最强 LLM 基线 44.4% 提升 34.6 个百分点。
- 精度 93.1%，与最佳规则检查器（90.3–97.6%）相当。
- 跨模型变异显著降低；通用 web agents 装备交互工具后检测错误更多、误报更少、token 消耗更低。
