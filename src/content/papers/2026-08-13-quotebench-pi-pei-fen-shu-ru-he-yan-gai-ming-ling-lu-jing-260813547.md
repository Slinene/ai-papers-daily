---
title: 'QuoteBench: How Matched Scores Can Hide Command-Path Failures'
title_zh: QuoteBench：匹配分数如何掩盖命令路径失败
authors:
- Shangao Li
- Yao Zhang
- Volker Tresp
- Yuanyuan Yang
affiliations:
- Stony Brook University
- LMU Munich
- Munich Center for Machine Learning
arxiv_id: '2608.13547'
url: https://arxiv.org/abs/2608.13547
pdf_url: https://arxiv.org/pdf/2608.13547
published: '2026-08-13'
collected: '2026-08-15'
category: Eval
direction: LLM Agent 命令执行评估
tags:
- LLM agents
- Bash quoting
- evaluation
- execution transport
- command generation
- final-state validation
one_liner: 通过控制执行传输中的解析器，揭示匹配执行分数掩盖的 Bash 引用失败与边界适应差异
practical_value: '- 在构建 command-issuing agent（如自动数据管道、文件处理、脚本调用）时，不要只看最终执行是否匹配，应显式记录生成契约、执行路径和
  final-state validator，区分生成错误与执行层转义错误。

  - 通过 prompt 或系统提示向模型披露执行传输边界（如是否经过 shell 转义层），通常能显著恢复成功率，但需在具体配置下验证，部分场景披露无效甚至负向。

  - 工程实现上，建议在命令插值点统一转义，避免 raw model output 直接进入 shell 解析；同时用 exact final-state 校验替代简单字符串匹配。

  - 评估多家 LLM 或选型 agent 时，应固定同一回复在不同执行传输配置下 replayed，避免 matched score 掩盖真实差距，尤其关注边界适应能力而非单纯生成质量。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**
LLM coding agent 输出 Bash 命令时，接口可能序列化、包装并重新解析模型输出。仅看匹配执行分数无法区分命令生成错误与生成后执行传输引入的失败，尤其 Bash 引用/转义问题常见且隐蔽。

**方法关键点**
QuoteBench 用 56 个 one-shot 任务（来自 14 个 incident-derived families）交叉生成契约与执行传输，围绕一个故意未转义的 added parser。通过在插值点转义，可复现每个 replayed reply 的原始路径结果；若在披露边界下仍有恢复，说明模型改变了生成方式。对比同一回复在 8 个 same-window 配置下的成功率。

**关键结果数字**
经过 added parser 后，成功率下降 55.4–73.2 个百分点；披露边界后 6 个配置恢复 30.4–60.7 点，其余 2 个配置恢复为零或略负。GPT-5.6-sol 的 matched gap 仅 -3.6 点，却隐藏 -64.3 点损害和 +60.7 点补偿。部署配置会重新排序模型，26 个可比对中有 1 个明确反转，另有 4 个处于单任务边缘。结论：评估 command-issuing agent 必须报告模型配置、生成契约、执行路径、operating point 和 final-state validator，不能把 matched score 当作模型固有属性。
