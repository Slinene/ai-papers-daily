---
title: 'One Success Isn''t Reliability: Thinkingbox, a Sandbox and Benchmark for Agents
  in Stateful Business Workflows'
title_zh: 单次成功不等于可靠：有状态业务工作流的 Thinkingbox 沙盒与基准
authors:
- Zhuochun Li
- Youngmin Ko
- Ali Keramati
- Nicola Ferri
- Susana Palmaz Lopez Pelaez
- Liang-Chun Tsai
- Calvin Wang
- Mirco Milletari
- Tuhin Kundu
- Vadim Smolyakov
affiliations:
- University of Pittsburgh
- Northwestern University
- University of California, Irvine
- Microsoft
arxiv_id: '2608.19741'
url: https://arxiv.org/abs/2608.19741
pdf_url: https://arxiv.org/pdf/2608.19741
published: '2026-08-19'
collected: '2026-08-26'
category: Eval
direction: Agent 可靠性评估 · 有状态业务沙盒
tags:
- Agent Evaluation
- Stateful Workflows
- Tool Use
- MCP
- Reliability
- Benchmark
one_liner: 提出可执行的状态副作用检查沙盒 Thinkingbox，发现最强模型 pass@1 仅 65.36%，且全部 20 次成功仅 25.25%
practical_value: '- 在电商售后/订单修改/退款等有状态场景，评估 agent 不能只看回复或工具调用是否合法，应定义可执行的后端状态检查（订单、退款、优惠券记录），同时校验“必须变更”和“禁止副作用”。

  - 上线评估应同时报告 pass@1 和 pass^k（如 pass^20 全部成功），区分“偶尔能找到成功路径”和“稳定可靠执行”，避免把 pass@20 当可靠性指标。

  - 工具错误恢复是主要失效模式（平均 77.5%），建议在 prompt 或训练数据中强制 agent 在关键写操作后二次读取/校验状态，而不是假设工具成功返回即完成。

  - 模拟用户可设计为“只回答被问的信息、不主动补充”，推动 agent 学会澄清缺失字段（地址、授权、时间等），接近真实客服多轮交互。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 agent 评估集中在代码、网页、函数调用等容易执行验证的任务，但真实业务中大量工作是修改预订、处理退款、更新保险理赔等多轮、有状态、带后果的操作。仅仅输出合理回复或合法工具调用不代表成功，agent 可能改了错误记录、缺少确认、产生额外副作用。需要一个能检查最终后端状态和副作用的沙盒与基准。

**方法关键点**
- Thinkingbox 将任务定义为 (b0,g,T,U,C)：初始后端状态、用户目标、可用领域工具、模拟用户策略、隐藏可执行检查；运行中 agent 在用户对话与工具调用间切换，工具操作在隔离后端会话执行。
- 评价采用可执行检查的合取：V=∏c_i，所有必须条件同时满足才通过；检查作用于最终状态、副作用和对话，不要求与参考轨迹一致，允许不同有效路径但拒绝错改、漏改和额外改动。
- 工具通过 MCP 兼容接口暴露，支持工具发现与调用，贴近现实部署；每次尝试重置状态并隔离，保证 pass@k 可靠性。
- 30个任务额外检查最终回复的必要属性（如保密披露、与执行结果一致性），其余477个任务只看后端状态。

**关键实验**
- Thinkingbox-bench 包含507个任务，覆盖零售/电商、旅行酒店、车险、数字银行内部 IT、咨询 IT/HR 五个领域。
- 评估12个模型，每个任务重复20次，报告 pass@1、pass@20、pass^20。最强模型 GPT-5.4 pass@1 65.36%，至少成功一次的任务比例91.12%，但全部20次成功的任务仅25.25%。
- 领域差异明显：零售平均约52%，车险最难约23%；失败分析显示工具使用错误占77.5%，错误状态更新12.1%，不完整用户解决7.9%，完全无状态变更2.5%。

**最值得记住的一句话**：表面干净的工具调用和流畅回复不是可靠完成任务的代理；必须检查最终后端状态和副作用，单次成功不等于可靠。
