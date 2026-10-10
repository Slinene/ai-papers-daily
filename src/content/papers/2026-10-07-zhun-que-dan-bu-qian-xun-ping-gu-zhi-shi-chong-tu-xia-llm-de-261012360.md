---
title: 'Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under
  Knowledge Conflict'
title_zh: 准确但不谦逊：评估知识冲突下 LLM Agent 的认知谦逊
authors:
- Kaiser Sun
- Bernal Jimenez Gutierrez
- Hongjun Liu
- Jingyu Zhang
- Jie Gao
- Mark Dredze
- Daniel Khashabi
affiliations:
- Johns Hopkins University
- New York University
arxiv_id: '2610.12360'
url: https://arxiv.org/abs/2610.12360
pdf_url: https://arxiv.org/pdf/2610.12360
published: '2026-10-07'
collected: '2026-10-10'
category: Eval
direction: Agent 评估 · 知识冲突与不确定性
tags:
- Epistemic Humility
- Knowledge Conflict
- LLM Agents
- Evaluation
- Uncertainty
one_liner: 提出 ISE 轨迹级评估框架，发现高准确率不必然伴随认知谦逊，模型干预提升谦逊常损失准确率
practical_value: '- 在电商 RAG/Agent（商品问答、智能客服、选品助手）中，除最终准确率外，增加轨迹级 ISE 指标：是否识别冲突、是否尝试二次检索/对比解决、是否对未解决冲突升级给用户或人工；可在日志中埋点监控。

  - 构建对抗性评测集：故意注入与模型参数知识矛盾的商品属性、库存、价格信息，或构造两个上下文来源不一致的场景，检验 Agent 是否静默覆盖冲突，而不是只测端到端准确率。

  - 多步 Agent 流程中，早期检测到的冲突常在后续被覆盖；可在每步状态维护“未解决冲突”列表，并在最终回答前强制检查，或用 memory 保存冲突标记，要求输出时带上
  caveat。

  - 强制模型输出不确定性可能降低任务完成率，建议按业务风险分级：高合规/价格承诺场景启用强制谦逊与升级，低风险推荐场景只做日志监控。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 Agent 评估只看任务成功，难以回答“当检索证据与模型先验冲突时，Agent 是否会修正、承认不确定还是坚持错误”。论文提出评估认知谦逊（EH），关注 Agent 在任务执行中识别、应对和沟通不确定性的能力。

方法：将 EH 操作化为轨迹级三维度 ISE——Identify（是否识别冲突）、Solve（是否尝试解决）、Escalate（是否对未解决冲突升级沟通）。构造两类知识冲突：受控冲突（参数知识与证据冲突）和自然发生的多步执行冲突，并配无冲突对照。评估四个 Agent，观察中间轨迹和最终答案。

关键结果：高任务准确率并不必然伴随高 EH；部分高准确配置能在执行中识别冲突，但在错误最终答案中不沟通未解决的不确定性。轨迹分析显示 Agent 常在早期步骤检测到冲突，但后续未能维持或解决。模型级干预能提升 EH，但通常以任务准确率为代价，说明 EH 由 backbone、agent harness 和评估环境共同决定，不能单靠模型能力。
