---
title: 'CapLite: Prompt-Injection Defense for Small Language Model Agents without
  Model-Written Security Artifacts'
title_zh: CapLite：小语言模型 Agent 提示注入防御，不依赖自产安全工件
authors:
- Zimo Xu
- Wenzhuo Liu
- Hideki Nakayama
affiliations:
- The University of Tokyo
- Institute of Automation, CAS
arxiv_id: '2611.17115'
url: https://arxiv.org/abs/2611.17115
pdf_url: https://arxiv.org/pdf/2611.17115
published: '2026-11-12'
collected: '2026-11-14'
category: Agent
direction: Agent 工具调用安全防御
tags:
- Prompt Injection
- Tool-Using Agents
- SLM
- Write Integrity
- Enforcement Defense
- Security
one_liner: 从工具 schema 派生写入策略并在工具结果前校验参数来源，使小模型 Agent 防注入且 token 高效
practical_value: '- 在电商/推荐/广告的 Agent 场景中，安全校验不要依赖模型自身生成策略或程序，尤其使用小模型或本地部署模型时；直接从工具
  schema 提取可写参数白名单，把写操作校验前置到代码层。

  - 对写操作（如改广告出价、发 push 文案、创建订单、修改推荐黑名单）强制参数必须来自用户原始 query，否则拒绝；这能防止 prompt 注入在工具结果中夹带未授权写入。

  - 工程上可复用“提交写调用早于读取任何工具结果”的顺序：先对写参数做来源检查再执行后续读取，阻断注入通道，同时减少无效工具调用，token 开销更低（论文中单
  episode 仅 17.1k tokens，低于 undefended agent）。

  - 评估防御时同时报告 utility under attack 和 token 消耗 / utility per token，避免只盯 ASR 导致实用性下降。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：已有 enforcement defenses（CaMeL、Progent、IPIGuard、DRIFT）要求 agent 自己的模型编写安全 artifact（程序、权限策略、依赖图、约束列表），再由代码执行。实验发现小语言模型（SLM）不可靠：15 个 open-weight 模型（13 个 1.7B-12B）中，模型写的策略在 14/13/11 个模型上可被攻击，CaMeL 程序在最多 68% episodes 中无法运行。需要不依赖模型写安全 artifact 的防御。

**方法关键点**：CapLite 从工具 schema 自动派生写入策略；在读取任何工具结果之前提交写调用校验；只有当写调用的每个决定影响对象（收件人、金额、对象、目的地）的参数都出现在用户请求中时才允许执行。这保证 write integrity：注入内容不能添加写，写不能到达用户未指定的任何目标。

**关键结果**：在 13,935 个 attacked AgentDojo episodes 中无攻击成功；utility under attack 29.0% vs CaMeL 27.2%；单 episode token 消耗 17.1k，仅为 CaMeL 的 18%，且低于 undefended agent；在所有 enforcement defenses 中 utility per token 最高。
