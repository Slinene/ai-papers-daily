---
title: Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute
  Pipelines
title_zh: 工业 Agent 管道中的时序语义缓存与工作流优化
authors:
- Alimurtaza Mustafa Merchant
- Krish Veera
- Sajal Kumar Goyla
- Shambhawi Bhure
- Dhaval Patel
- Kaoutar El Maghraoui
affiliations:
- Columbia University
- IBM
- IBM Research
arxiv_id: '2605.20630'
url: https://arxiv.org/abs/2605.20630
pdf_url: https://arxiv.org/pdf/2605.20630
published: '2026-05-19'
collected: '2026-05-21'
category: Agent
direction: Agent 执行加速与缓存优化
tags:
- temporal semantic cache
- MCP workflow optimization
- plan-execute
- industrial agent
- latency reduction
- cache failure mode
one_liner: 在 Plan-Execute 工业 Agent 中，时序语义缓存命中达 30.6 倍加速，MCP 工作流优化降低 40% 延迟，并揭示纯语义缓存在参数丰富查询中的失效模式。
practical_value: '- **依赖感知并行执行**：在电商多智体（如导购 + 库存 + 物流 Agent）的 Plan-Execute 管道中，分析工具调用间的依赖关系，并行执行无依赖步骤（如同时查询商品详情和用户画像），可直接降低端到端延迟，类似于本文的
  1.67 倍加速。

  - **带参数感知的时序缓存**：对于生成式推荐/商品问答等参数敏感场景，避免使用纯语义缓存；设计缓存键应包含时间戳、用户 ID、商品 ID 等维度，并设置合理的
  TTL，防止因忽略参数而返回过期或错误结果。

  - **工具发现结果持久化**：在多 MCP 工具场景下，将工具列表和 schema 缓存到磁盘，避免每次请求都重新获取工具清单，减少 LLM 规划前的准备开销，工程实现简单但效果明显。

  - **缓存正确性评估**：引入缓存命中时的结果验证机制（如通过工具返回的最新数据校验），确保加速的同时不牺牲答案正确性，尤其适合金融级或库存实时性要求高的 Agent
  系统。'
score: 7
source: huggingface-daily
depth: abstract
---

工业资产运营中，Agent 的 Plan-Execute 管道因工具发现、LLM 规划、MCP 工具执行与总结等环节产生高延迟，传统 KV-cache 或语义缓存无法处理时间、设备等参数敏感性。

方法上，引入两层优化：
1) **时序语义缓存**：在语义相似度基础上，将查询参数（时间戳、资产 ID、传感器代号）编码进缓存键，并设定动态过期策略，确保仅当语义与参数均匹配时才返回缓存结果。
2) **MCP 工作流优化**：包括磁盘持久化的工具发现缓存（避免重复 schema 拉取）和基于依赖图的并行步骤执行（将无数据依赖的工具调用并发执行）。

在 AssetOpsBench 基准上，MCP 工作流优化取得 1.67 倍整体加速，中位端到端延迟降低约 40.0%；时序语义缓存在缓存命中时中位加速达 30.6 倍。同时，实验暴露纯语义缓存因忽略参数维度导致输出错误，强调了工业 Agent 场景中缓存机制必须与正确性评估协同设计。
