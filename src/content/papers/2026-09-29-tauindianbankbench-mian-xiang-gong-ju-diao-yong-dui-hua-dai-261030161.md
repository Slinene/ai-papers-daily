---
title: 'TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using
  Conversational Agents'
title_zh: TauIndianBankBench：面向工具调用对话代理的过程感知行动导向评估基准
authors:
- Krishanu Adhikary
- Prashant Devadiga
affiliations:
- National Payments Corporation of India (NPCI)
arxiv_id: '2610.30161'
url: https://arxiv.org/abs/2610.30161
pdf_url: https://arxiv.org/pdf/2610.30161
published: '2026-09-29'
collected: '2026-10-31'
category: Eval
direction: 过程感知的行动导向评估基准
tags:
- evaluation
- conversational agents
- tool use
- procedure adherence
- banking
- action-oriented
one_liner: 提出银行客服对话代理评估基准，除最终记录外检查必需步骤执行与未请求变更，暴露仅看结果的假阳性
practical_value: '- **评估不能只看最终状态**：在电商客服或推荐对话场景中，很多关键动作（如查询库存、确认地址、风控校验）不改变最终记录但影响服务质量。建议在评估
  Agent 时增加"过程步骤检查"，防止模型跳过合规步骤却得到正确结果。

  - **构建 action-oriented 测试集**：用模拟用户 + 工具调用日志的方式，将业务规则编码为"必需步骤"和"禁止变更"，可复用于电商售后、广告投放审核等
  Agent 的回归测试，尤其适合有 SOP 的流程。

  - **关注未请求的变更**：模型有时会主动执行用户未要求的操作（如擅自修改订单、发送通知），这类错误在结果导向评估中难以发现。应单独统计 unrequested
  change 的比例，作为安全指标。

  - **低资源领域适配**：该 benchmark 针对印度零售银行这类非英语主流、流程固定的场景，提示我们在垂直业务中自建轻量级评估集，比通用 benchmark
  更能反映真实风险。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：银行客服从 FAQ 脚本转向 LLM 驱动的工具调用代理，但现有评估只看对话结束后的最终记录，忽略过程中必须执行但无痕的步骤（例如关闭存款前获取报价）。这导致模型跳过关键流程仍被判为成功。

**方法关键点**：提出 TauIndianBankBench，包含 1,000 个印度零售银行任务，由代理协助模拟客户完成操作。评估时除了对比最终数据库记录，还从转录和工具调用日志中检查两件事：是否执行了所有必需步骤（procedure adherence），是否做出了用户未请求的变更（unrequested change）。任务覆盖常见银行业务，如冻结卡片、预订存款等。

**关键结果数字**：对多个模型评测发现，仅按最终记录判断时，有 6.5%–12.0% 的会话被误判为成功，实际上模型跳过了必需步骤或执行了未请求的操作。同时引入过程检查后，能更准确地区分模型在印度零售银行领域的实际表现，为训练前后对比提供可靠指标。
