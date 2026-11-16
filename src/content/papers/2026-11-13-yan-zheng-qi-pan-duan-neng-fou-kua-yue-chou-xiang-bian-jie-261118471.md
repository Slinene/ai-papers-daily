---
title: Do Verifier Judgments Survive Abstraction? Measuring Verification Transport
  for LLM Agent Evaluation
title_zh: 验证器判断能否跨越抽象边界？LLM Agent 评估的验证传输测量
authors:
- Disha Sheshanarayana
- Sai Linisha Reddy Goli
affiliations:
- Manipal University Jaipur
arxiv_id: '2611.18471'
url: https://arxiv.org/abs/2611.18471
pdf_url: https://arxiv.org/pdf/2611.18471
published: '2026-11-13'
collected: '2026-11-16'
category: Eval
direction: Agent 执行验证的可靠性评估
tags:
- LLM-as-a-Judge
- Verification
- Agent Evaluation
- Abstraction
- Reliability
- Provenance
one_liner: 提出 Verification Transport 测试，量化 LLM 验证器在轨迹抽象下判决翻转，发现约31%失败并可通过恢复溯源修复85.5%
practical_value: '- 业务中若用 LLM 作为 agent 执行轨迹的自动验证器（如评估推荐对话、工具调用链），不要只优化 native view
  上的准确率：当执行证据经过工具摘要、子任务委派或历史压缩后，verifier 判决可能翻转。应在评估流水线中保留原始执行证据或 provenance，避免上游抽象造成误判。

  - 不同验证协议失败模式不同：直接验证更可能给出错误结论，evidence-grounded / deliberative protocol 更倾向弃权。高频自动评估场景建议采用证据链或审议式协议，并将弃权率作为可靠性的独立监控指标，而非只看判决准确率。

  - 可以借鉴 Verification Transport 的思路做压测：对同一批真实 agent 执行样本施加不同抽象变换（如压缩工具日志、模拟子任务委派），比较
  verifier 判决变化，定位自家评估链路中对抽象最敏感的环节。

  - 结果强调 provenance 恢复能修复 85.5% 的传输失败，说明在 agent 系统中记录原始工具调用、中间推理链和状态变化对事后审计和自动评估价值很大，尤其适用于搜索推荐
  agent 的多轮检索、筛选、排序决策审评。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
LLM-based verifier 被广泛用于评估 agent 执行轨迹，但现有可靠性测量通常在单一轨迹表示下进行。实际部署中，同一执行可能经过工具组合、委托边界、历史压缩等抽象，改变验证者可观察到的执行证据。正确判决是否跨抽象边界保持，此前不清楚。

## 方法
提出 Verification Transport 测试：对同一批冻结的 agent 执行构造 native、abstracted、restored 三种匹配视图，固定任务、真实轨迹、结果、ground truth、评价标准和 verifier，仅改变执行证据的可观察性。在 4 个 agent 评估基准、7 个 verifier backbone、4 种验证协议（direct、evidence-grounded、deliberative 等）和 3 种抽象边界上测量判决稳定性。

## 关键结果
- 抽象导致显著传输失败：在 macro abstraction 和 delegation 下失败率约 31%。
- 失败模式因协议而异：direct verification 更多产生错误判决；evidence-grounded 和 deliberative protocol 在有限可观察性下更倾向 abstain。低传输失败率不等于高可靠性。
- 恢复相应 execution provenance 可修复 85.5% 的传输失败；当 provenance 有损或不可用时恢复率更低。
- 结论：仅凭 native-view accuracy 不足以刻画 verifier 在证据跨抽象边界时的可靠性。
