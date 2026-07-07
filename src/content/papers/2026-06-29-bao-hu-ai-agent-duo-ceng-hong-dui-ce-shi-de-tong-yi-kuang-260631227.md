---
title: 'Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming'
title_zh: 保护AI Agent：多层红队测试的统一框架
authors:
- Yong Yang
- Xing Zheng
- Huiyu Wu
- Huangsheng Cheng
- Xiaorong Shi
- Jing Guo
- Bo Yang
- Yi Zhou
- Xiangfan Wu
- Zonghao Ying
affiliations:
- Tencent Zhuque Lab
arxiv_id: '2606.31227'
url: https://arxiv.org/abs/2606.31227
pdf_url: https://arxiv.org/pdf/2606.31227
published: '2026-06-29'
collected: '2026-07-07'
category: Agent
direction: Agent安全 · 多层红队测试
tags:
- Agent Security
- Red Teaming
- MCP
- Supply Chain
- Vulnerability Scanning
- Jailbreak
one_liner: 提出开源框架AI-Infra-Guard，分层匹配检测范式覆盖基础设施到模型的全攻击面并加入供应链审计
practical_value: '- **多层安全防护思路**：将Agent系统攻击面划分为基础设施、协议/工具、行为与模型四层，每层采用不同检测机制（规则匹配、Agent驱动审计、黑盒多轮测试、越狱攻击），可作为电商Agent安全架构参考。

  - **第三方MCP与技能包供应链审计**：在引入外部MCP服务器或Agent技能时，执行自动化漏洞扫描与代码审查，防止恶意工具调用导致数据泄露或操作风险，适合社区化Agent生态的安全控制。

  - **Agent行为红队测试**：对推荐/对话Agent进行多轮黑盒交互，模拟恶意用户诱导模型执行危险动作（如查看他人订单、修改配置），可迁移到线上Agent上线前的安全评测流程。

  - **模型层越狱防护验证**：使用框架内置的26+攻击算子和多数据集，快速构建对自研LLM的越狱测试，评估模型在敏感推荐或用户数据问答场景下的抗攻击能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：AI基础设施迅速膨胀，但安全工具缺失，尤其对Agent平台、MCP生态和模型供应链的防护不足。单一检测范式无法应对从基础设施到模型的多层攻击面。

**方法关键点**：
- 将AI Agent攻击面分为四层：基础设施层（模型服务引擎、组件漏洞）、协议/工具层（MCP服务器、Agent技能包）、Agent行为层（多轮对话滥用）、模型层（越狱攻击）。
- 为每层匹配最适检测范式：
  - 基础设施层：确定性规则匹配，覆盖75+组件、1400+漏洞规则。
  - 协议/工具层：LLM驱动的Agent自动化审计，扫描MCP服务器与技能包的供应链风险。
  - Agent行为层：多轮黑盒红队测试，模拟恶意用户交互。
  - 模型层：集成26+攻击算子与16个数据集的越狱测试套件。
- 框架名为AI-Infra-Guard，是首个开源覆盖全部层面（含供应链审计）的Agent红队测试工具。

**关键结果**：
- 实现全层覆盖的红队测试，填补AI Agent供应链安全审计空白。
- 提供统一框架供社区构建和对比，推动Agent安全实践标准化。
