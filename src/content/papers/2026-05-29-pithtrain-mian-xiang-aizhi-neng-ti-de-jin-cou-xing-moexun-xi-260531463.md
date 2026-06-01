---
title: 'PithTrain: A Compact and Agent-Native MoE Training System'
title_zh: 'PithTrain: 面向AI智能体的紧凑型MoE训练系统'
authors:
- Ruihang Lai
- Hao Kang
- Haozhan Tang
- Akaash R. Parthasarathy
- Zichun Yu
- Junru Shao
- Todd C. Mowry
- Chenyan Xiong
- Tianqi Chen
affiliations:
- Carnegie Mellon University
- Xlue
- NVIDIA
arxiv_id: '2605.31463'
url: https://arxiv.org/abs/2605.31463
pdf_url: https://arxiv.org/pdf/2605.31463
published: '2026-05-29'
collected: '2026-06-01'
category: Training
direction: Agent原生MoE训练框架设计
tags:
- MoE
- Agent-native
- ATE-Bench
- training framework
- coding agents
- throughput
one_liner: 提出Agent原生设计原则构建MoE训练框架，在保持吞吐量的同时显著提升AI编程智能体的任务效率
practical_value: '- 框架接口设计可借鉴“Agent-native”原则：显式数据流、最小化间接调用、优先Python实现，降低AI编程工具理解与修改成本。

  - 评估训练框架时，除吞吐量外应纳入Agent Task Efficiency（ATE）指标，量化开发迭代效率。

  - 在维护或扩展内部训练框架（如推荐模型分布式训练）时，避免过度使用插件系统与编译扩展，能加速新架构的适配。

  - ATE-Bench任务设计思路可复用于评估其他ML基础设施对AI辅助开发的友好程度。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：生产级MoE训练框架经过多年工程堆叠，架构复杂（Python分层+编译扩展），导致AI编程智能体难以理解、修改和扩展代码。现有评估仅关注吞吐量，忽略了开发效率，作者提出Agent Task Efficiency（ATE）衡量智能体操作框架的成本。

**方法**：基于四条Agent-native设计原则——显式数据流、最小化间接调用、避免编译扩展、Python优先——构建了紧凑的PithTrain框架。通过减少抽象层级和统一代码路径，降低智能体定位核心逻辑的难度。同时引入ATE-Bench，包含真实场景下的训练框架开发任务（如添加新算子、修改并行策略）。

**结果**：PithTrain在常用吞吐量基准上与生产框架持平，且代码量更少。在ATE-Bench上对比现有框架，PithTrain使智能体完成任务的Agent Turns减少62%，Active GPU Time减少64%，证明了Agent-native设计的有效性。
