---
title: 'FiMI Banking: A Sovereign Model for Indian Retail Banking'
title_zh: FiMI Banking：印度零售银行主权模型
authors:
- NPCI AI Research Team
- Aman Kumar
- Asit Desai
- Chandra Bhushan
- Harsh Sharma
- Harshit Bhushan
- Hrithik Kadam
- Keyur Doshi
- Kolisetty Sai Kapardheeswar
- Krishanu Adhikary
affiliations:
- NPCI AI Research Team
arxiv_id: '2609.03960'
url: https://arxiv.org/abs/2609.03960
pdf_url: https://arxiv.org/pdf/2609.03960
published: '2026-09-03'
collected: '2026-09-06'
category: Agent
direction: Agent 后训练与工具使用优化
tags:
- LLM Agents
- Preference Optimization
- RLVR
- Tool Use
- Banking
one_liner: 用偏好优化提升安全拒答，用可验证奖励RL提升多轮工具调用与token效率
practical_value: '- 对客服/导购 Agent，把 **out-of-scope/敏感场景拒答** 单独用 preference optimization
  做后训练，能显著提升安全行为：银行场景从 52% 到 80%。电商里价格承诺、优惠券规则、保险理赔等高风险回答也可复用。

  - 多轮工具调用任务用 **RLVR（verifiable reward）** 而非只靠 SFT/偏好优化：订单状态查询、改地址、优惠核销等可自动校验的任务，既能提升
  edge-case 和顺序敏感任务成功率，又能减少 29% token，直接降低 Agent 调用成本与延迟。

  - 业务 Agent 上线前，可搭建类似 **可控评测环境**：从内部文档构建结构化 ground truth + 合成用户背景 + 真实工具接口，用来评估模型是否乱调工具、乱拒或泄漏敏感信息。

  - 偏好优化与 RLVR 互补：前者管回复层面安全，后者管多轮工具执行；业务 Agent 后训练可以考虑两阶段组合。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：银行客服 Agent 需要既回答产品问题，又能在多轮对话中安全调用工具，但通用 LLM 常出现信息不接地、工具误用、敏感场景乱答。

方法：构建 FiMI Banking，一个印度零售银行受控环境，包含审核过的银行文档、结构化 ground truth、合成客户背景和银行工具。重点对比两种后训练：偏好优化（preference optimization）优化回复级行为；可验证奖励强化学习（RLVR）优化多轮工具使用。

结果：偏好优化将 out-of-scope 拒答率从 52% 显著提升到 80%；RLVR 将 edge-case 表现从 0.509 提升到 0.718，顺序敏感任务从 0.590 提升到 0.679，同时生成 token 减少 29%。两种方法互补，前者负责安全性，后者负责工具执行可靠性。
