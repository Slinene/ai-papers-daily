---
title: 'On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification'
title_zh: 自改进智能体的脆弱性：方差、任务顺序与欠规约
authors:
- Qinyuan Ye
- Yu Li
- Yada Pruksachatkun
- Jiaxin Zhang
- Chien-Sheng Wu
affiliations:
- Salesforce AI Research
arxiv_id: '2608.18066'
url: https://arxiv.org/abs/2608.18066
pdf_url: https://arxiv.org/pdf/2608.18066
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: 自改进Agent 可靠性评估
tags:
- self-improving agents
- memory-based agents
- evaluation
- variance
- task order
- underspecification
one_liner: 重评估揭示内存型自改进Agent存在高方差、强任务顺序依赖及任务/环境欠规约导致的脆弱性
practical_value: '- 评估自改进 Agent 或带记忆的 LLM 系统时，务必报告多次运行方差；观察到最佳与最差运行差距可达 10 个百分点，单次结果不可靠。

  - 任务顺序会隐式形成课程学习，默认顺序可能掩盖真实性能；上线前应在随机打乱的任务流上做压力测试，否则提升可能来自顺序而不是模型能力。

  - 内存条目若缺少任务/环境规约，容易生成看似合理但不适用的策略；可在记忆构造时注入详细 rubrics、环境反馈或约束条件，降低欠规约带来的误导。

  - 即使加入额外规约信息，性能仍存在明显 gap，说明现有自改进循环内部有不稳定因素；业务场景中建议引入人工审核或护栏，防止 Agent 在不可预见场景下产生错误记忆并持续放大。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
内存型自改进 Agent 通过在任务流中维护文本记忆库实现持续提升，但已有工作关注提升幅度，很少评估可靠性。

## 方法关键点
作者对两种主流的 memory-based 方法做系统性重评估，从两个维度扩展评测：
- **多轮运行**：量化同一实验在不同随机种子下的方差；
- **随机打乱任务顺序**：移除默认顺序隐含的课程效应，观察真实改进能力。

此外，手动检查 Agent 记忆发现任务与环境的欠规约是脆弱性来源之一，于是尝试在记忆构造时引入更明确的任务指标和执行环境反馈。

## 关键结果
- 自改进循环会放大评测噪声：71% 的情况下跨运行方差增大，同一实验最佳与最差运行差距可达 10 个百分点。
- 任务顺序高度影响提升效果：默认顺序下平均提升 +1.5%，但随机打乱后变为 -4.5%。
- 加入详细 rubrics 和环境反馈后，随机顺序下的性能退化得到部分修复，但仍存在显著 gap，说明还有其他未被刻画的脆弱因素。

结论：需要建立更严格的评估协议，包括多轮运行和压力测试，并为自改进系统设计有效的人工监督接口，防止不可预见的失败。
