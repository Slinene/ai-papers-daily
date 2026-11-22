---
title: 'Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)'
title_zh: Agent 安全事件复现与审计：ROGUE-AI
authors:
- Mengxiao Wang
- Mahbub Alam
- Kalyan Nakka
- Nitesh Saxena
affiliations:
- Texas A&M University
arxiv_id: '2611.26553'
url: https://arxiv.org/abs/2611.26553
pdf_url: https://arxiv.org/pdf/2611.26553
published: '2026-11-19'
collected: '2026-11-22'
category: MultiAgent
direction: 多智能体安全事件复现与审计
tags:
- Agent Security
- Incident Replication
- Multi-Agent
- LLM Auditing
- Prompt Injection
- Safety Evaluation
one_liner: ROGUE-AI 多智能体框架离线复现 108 个 LLM Agent 安全事件，通过对照实验验证归因并量化护栏效果
practical_value: '- 为业务 Agent（选品、投放、客服、自动交易）建立“事故复现 + 缺失归因对照组”回归测试集，在每次模型/提示升级前自动跑多模型审计，量化误操作率。

  - 护栏不要只盯 prompt injection；电商 Agent 常见错误是误改共享资源、误发大额优惠券、误操作生产数据等普通风险，需要在工具输出后给出“危害类型
  + 后果”的具体警告。

  - 用不同厂商模型交叉构建和审核复现用例可降低测试偏差；是否造成危害由代码判定比 LLM 判定更可靠。

  - 安全提示必须明确危害与后果；等长的泛泛“注意安全”类提示对降低实际危害几乎无效。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent 可删文件、付款，但安全事件报道只描述结果，缺少复现与根因验证；现有基准只测是否失败，不重建事件或验证归因。

**方法**：ROGUE-AI 多智能体框架由 Claude/Gemini/GPT 基 Agent 收集报告并构建离线复现，另一厂商 Agent 审核，代码判定伤害；每个事件配一个仅去掉被归因原因的对照组，同时运行多个模型 Agent。

**关键结果**：108 次复现中 89% 复现了报道的危害；五个当前 GPT、Claude、Gemini、DeepSeek 模型在 18%–33% 运行中犯错，对照组至多 1%。72 个现实危害事件中 62 个无攻击者，多为忽略共享生产数据库等普通风险；无攻击复现比 prompt injection 造成更多危害。工具输出后给出指明危害和后果的警告能降低所有模型危害，等长但不提及危害的提示几乎无效。
