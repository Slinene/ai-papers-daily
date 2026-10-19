---
title: 'GatewayBench: Unified Capability and Security Evaluation Platform for MCP
  Gateways'
title_zh: GatewayBench：MCP 网关能力与安全统一评测平台
authors:
- Yitian Zheng
- Zhaorun Chen
- Haoyu Li
- Bo Li
affiliations:
- Tsinghua University
- University of Chicago
- University of Illinois Urbana-Champaign
arxiv_id: '2610.23449'
url: https://arxiv.org/abs/2610.23449
pdf_url: https://arxiv.org/pdf/2610.23449
published: '2026-10-16'
collected: '2026-10-19'
category: Eval
direction: Agent 基础设施评估基准
tags:
- MCP gateway
- Agent Evaluation
- Tool Use
- Security
- Benchmark
- Hierarchical Architecture
one_liner: 首个 MCP 网关统一评测基准，量化扁平与层级网关在任务完成、效率与攻击韧性上的差异
practical_value: '- 在电商/广告 Agent 场景中，若需接入大量工具（商品搜索、订单、营销、报表等），优先采用层级式 MCP 网关，通过工具发现
  meta-tool 按需检索，避免将所有工具 schema 塞入 context，降低 token 消耗并提升任务完成率。

  - 评测自有 Agent 工具调用时，可借鉴 GatewayBench 注入大量无关工具，模拟真实大规模工具面，观察模型在干扰下的选择能力；工具池尽量用真实业务工具而非合成样本。

  - 安全侧：层级网关并非天然安全，需在工具发现层增加权限过滤、来源验证与工具描述审查，防止恶意工具通过检索被暴露给 agent。

  - GatewayBench 提供统一任务和可验证 judge 的评测框架，可直接复用其任务构建思路，为内部 MCP 网关选型和迭代建立可量化的回归测试。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：AI agents 越来越多依赖工具调用，MCP 成为连接异构工具的标准接口。大规模部署时，MCP 网关作为聚合、治理和塑造工具面的中间层，直接影响智能体的能力、效率和安全，但此前无系统研究。

**方法**：提出 GatewayBench，首个 MCP 网关统一评测框架。将网关架构分为扁平（一次性暴露全部工具）和层级（通过工具发现 meta-tool 按需检索）两类。包含 524 个任务、6 个领域、来自 251 个真实 MCP 服务器的 11,118 个工具。为模拟大规模部署，系统注入无关工具，基于可验证的 judge 定量评估环境状态。在 7 个广泛部署的 MCP 网关上，涵盖良性与对抗任务，评估任务完成率、工具使用效率和攻击韧性。

**关键结果**：不同网关设计在任务完成、效率与安全上存在显著差异，且与底层模型和 agent harness 强交互。层级网关在工具规模化时表现更稳健，但安全风险取决于具体实现。该工作揭示 MCP 网关是被低估的关键组件。
