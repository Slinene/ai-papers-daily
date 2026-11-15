---
title: 'Cortex-FL: Agent-Mediated Collaboration for Federated Learning'
title_zh: Cortex-FL：面向联邦学习的智能体协作系统
authors:
- Rui Sun
- Jinfeng Peng
- Zehua Cheng
- Jiahao Sun
- Zhipeng Wang
affiliations:
- Newcastle University
- FLock.io
- University of Oxford
- The University of Manchester
arxiv_id: '2611.17186'
url: https://arxiv.org/abs/2611.17186
pdf_url: https://arxiv.org/pdf/2611.17186
published: '2026-11-12'
collected: '2026-11-15'
category: MultiAgent
direction: Agent 多智体协作优化去中心化训练
tags:
- Federated Learning
- Multi-Agent Systems
- Agentic Web
- Natural Language Delegation
- Incentive Management
one_liner: 用自然语言表达联邦学习目标，由多个 Agent 完成协作者发现、任务拆解、合同协商与链上激励结算
practical_value: '- 可将“自然语言需求 → 任务拆解与协作者匹配”的 Agent 编排逻辑迁移到广告主投放需求解析：让用户描述目标（如“拉新+控
  ROI”），由 Agent 自动匹配数据方、模型训练与出价策略。

  - 借鉴其“协调权与数据/执行权分离”架构：在电商多主体联合建模（品牌、平台、服务商）中，Agent 只负责协商与调度，原始数据、模型参数或用户画像留在本地，降低合规风险。

  - 合约治理与自动结算思路可用于数据合作/模型市场：对联合训练或特征共享约定贡献度与验收指标，用智能合约或可验证凭证自动结算，减少人工扯皮。

  - 四节点轻量闭环证明小规模多方数据合作可由 Agent 完成协作形成和交付，适合业务中快速验证 PoC；但链上结算额外复杂度需权衡。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：联邦学习虽能让多个数据所有者在不集中原始数据的情况下协同训练，但识别协作者、准备训练任务、协调执行和激励结算等环节需要专业知识，阻碍组织采用。

**方法关键点**：Cortex-FL 是一个 agent-native 联邦学习系统。用户以自然语言表达学习目标，多个 Agent 将目标翻译成共享任务、发现协作者、协商参与协议，并把协作形成与分布式训练、激励管理连接起来。架构上明确分离 Agent 协调与本地执行权限：所有者可以委托协调，但仍保留对数据、计算和财务承诺的控制。

**关键结果**：在四节点部署中演示完整工作流——从自然语言请求模型，经历协作形成、合约治理训练、验证模型交付，到在区块链测试网上通过 x402 完成结算。
