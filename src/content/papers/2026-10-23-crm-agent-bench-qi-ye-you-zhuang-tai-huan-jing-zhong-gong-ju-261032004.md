---
title: 'CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments'
title_zh: CRM-Agent-Bench：企业有状态环境中工具型Agent评测基准
authors:
- Monojit Banerjee
- Zhujun Lan
- Defu Cao
affiliations:
- Salesforce, Inc.
arxiv_id: '2610.32004'
url: https://arxiv.org/abs/2610.32004
pdf_url: https://arxiv.org/pdf/2610.32004
published: '2026-10-23'
collected: '2026-10-26'
category: Eval
direction: 企业级Agent执行与合规评测
tags:
- Agent
- Benchmark
- CRM
- Tool Use
- Stateful Environments
- Policy Compliance
one_liner: 用可执行合同严格评估多轮CRM任务中Agent的动作、状态与合规性，揭示说与做的差距
practical_value: '- 构建内部Agent评测时，不要只看最终答案，可借鉴 executable contract 思路：将业务规则拆成对动作、参数、顺序、响应、目标状态、受保护状态的检查，合成严格成功条件，自动化回归。

  - 在电商/推荐场景的Agent（如客服助手、营销文案生成、推荐解释）中，可定义受保护状态（如用户隐私字段、价格锁定、优惠券余额），确保Agent不会越权修改，直接复用其中的
  protected state 检查。

  - 评估指标必须包含 latency 和 cost，论文中领先系统虽然成功率接近，但成本和领域可靠性差异很大；业务落地前要做成本/稳定性分域分析，避免只按总体准确率选型。

  - 给任务打能力标签（工具选择、多步推理、规则遵守等），用于快速定位失败模式，指导后续 prompt 优化、模型微调或工具设计。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

动机：现有语言Agent评测多聚焦答案正确性，但真实业务中Agent需执行多步流程、遵守领域规则、与用户多轮交互，说和做的差距直接造成业务损失。CRM场景具有可变记录、操作规则和实际后果，适合全面考察。

方法关键点：推出 CRM-Agent-Bench，包含 555 个有状态多轮任务，覆盖 9 个业务领域和 36 个能力标签。每个任务提供可执行合同，检查项包括动作、参数、顺序、响应、目标状态和受保护状态；成功定义为该任务所有声明检查的严格合取。评估完整Agent系统，报告得分覆盖率、延迟和成本。

关键结果数字：在最终审计版本上评估 16 个系统，严格成功率从 64.32% 到 83.60%；得分相近的领先系统在成本与分领域可靠性上差异显著。该基准提供可审计的合同化业务事务完整性度量，结构可扩展。
