---
title: 'From Evidence to Action: How Tool-Using Agents Fail'
title_zh: 从证据到行动：工具型智能体如何失败
authors:
- Hongzhan Lin
- Shidong Cao
- Ziyang Luo
- Wenhao Chai
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- Hong Kong Baptist University
- Amazon Web Services
- Princeton University
arxiv_id: '2610.07753'
url: https://arxiv.org/abs/2610.07753
pdf_url: https://arxiv.org/pdf/2610.07753
published: '2026-10-05'
collected: '2026-10-07'
category: Eval
direction: 工具使用 Agent · 证据链评估
tags:
- tool-using agents
- evidence-to-action
- benchmark
- trajectory evaluation
- failure analysis
- LLM agents
one_liner: 提出 SAFEACTBENCH，用确定性轨迹评估定位工具型智能体在证据建立、动作执行与依赖传播中的失败点
practical_value: '- 在电商/客服等有状态操作（退款、订单修改、营销 push）上线前，可引入 **确定性证据链检查器**：对每个副作用动作，验证其前置证据是否已通过工具调用建立，并绑定到正确的实体和当前状态，避免只看最终结果；不要用
  LLM judge，用可重放的规则判断。

  - 分离 **静态决策与交互执行** 的监控：静态判断准确率（Legacy）可能很高，但交互执行暴露过早行动（PAR）与调查未完成（BSR）等失败模式；建议在回归测试中持续追踪这些指标，尤其多步工作流。

  - 多步 Agent 工作流中显式建模 **动作依赖 DAG**，要求下游必须使用前置动作实际返回的字段（如 refund_id），不能使用相似值或其他实体结果；在测试集中加入
  withheld/contradicted evidence 场景，验证 agent 是否仍坚持无证据行动。

  - 证据缺失时，仅增加检索次数不一定会提高行动克制；**requester 明确声明“已检查”** 比直接提供证据包更能降低无证据行动概率，提示业务中需警惕 agent
  对声明的过度信任。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
工具型 Agent 越来越多地执行改变外部状态的动作（退款、发文档、更新记录）。结果正确不代表行动有可观察的证据支持：Agent 可能查询了错误实体、未完成必要调查就执行，或在多步任务中使用了不匹配的前置结果。现有评估多聚焦最终状态或中间里程碑，却很少检查每个后果性动作是否在可观察轨迹中建立了恰当前置证据。

**方法关键点**  
- 提出 **SAFEACTBENCH**：656 个案例，覆盖 6 个业务领域，包含 1 个静态判断协议（Legacy）和 4 个交互协议：V0 调查后应停止；V1 单动作；V2 线性多动作；V3 依赖图约束多动作。  
- 设计 **provenance-bound Evidence Ledger**：记录每个事实的来源、描述的实体与状态，要求动作需求必须由正确来源在动作执行前满足。  
- 使用 **确定性轨迹评估器**：重放轨迹，验证调查完成度、工具/目标/参数正确性、执行回执、动作依赖和最终状态，不依赖 LLM judge，也不检查隐藏推理。  
- 区分“动作是否被允许”与“动作是否被已建立证据支持”：查询 C1 不能为退款 C2 提供支持，即使数值相同。

**关键实验与结果**  
在 10 个模型-harness 配置上评估，总体精确案例成功率（ECS）最高 Claude Code 67.2%，最低 GLM-ZCode 37.7%。静态 Legacy 判断普遍 >90%，但交互执行明显更弱：GLM-ZCode Legacy 97.7%，V2 仅 12.1%。失败诊断显示：V1 中过早行动（PAR）比例达 37.0–66.9%，但证据完成后的单动作执行成功率（CAS）大多在 93% 以上；V0 中停止前未完成调查（BSR）为 21.7–62.9%；多步工作流中依赖缺口与不完整执行普遍存在。受控干预发现：即使决定性证据被 withheld，Agent 仍有 46.5–53.5% 的概率继续行动；requester 明确声明“已检查”比提供证据包更能减少无证据行动。

**最值得记住的一句话**  
静态判断强不等于证据支撑的交互执行可靠，失败往往发生在行动之前——调查不完整或过早行动。
