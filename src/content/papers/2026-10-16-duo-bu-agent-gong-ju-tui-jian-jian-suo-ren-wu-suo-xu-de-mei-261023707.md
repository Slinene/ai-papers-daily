---
title: 'Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs'
title_zh: 多步 Agent 工具推荐：检索任务所需的每一个工具
authors:
- Sam Partee
- River Stevens
- Thierry Damiba
- Valerie Fanelle
affiliations:
- Arcade.dev
arxiv_id: '2610.23707'
url: https://arxiv.org/abs/2610.23707
pdf_url: https://arxiv.org/pdf/2610.23707
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 工具检索与推荐 · 成本优化
tags:
- Tool Recommendation
- MCP
- Agent
- Retrieval
- Cost Efficiency
- RAG
one_liner: 部署的 Tool Recommendation 系统用固定三工具接口为多步 Agent 提供全目录 8200+ 工具，实现工具链完整性与端到端成本双赢
practical_value: '- **固定接口 + 检索重排替代静态工具列表**：当 agent 需要触达大量 API/工具/技能时，不要把所有 schema
  塞进 context，而是暴露 `SelectTools`、`UseTool`、`ListApps` 等少数元工具，按需检索并执行；权限过滤放在 gateway
  层，保证推荐结果符合用户 scope，可直接迁移到电商导购/客服 agent 管理商品查询、订单、优惠券等海量工具。

  - **评估指标用 Completeness@K 而非 Recall@K**：多步任务缺一个工具就失败，例如“查库存→比价→下单”三工具缺一不可；在内部工具检索
  benchmark 上加入 Completeness 指标，能更好反映端到端成功率，而不是平均召回。

  - **成本优化必须看实际账单（含 prompt cache）而非仅输入 token**：输入 token 减少不代表账单同比例下降，因为缓存输入便宜得多；应明确
  caching 规则、用美元账单对比，并识别静态列表与动态检索的盈亏平衡点（约 25-28 个工具，或搜索频率 >0.63 次/工具调用时静态列表更便宜）。

  - **多步 agent 失败主因常是 agent 没发起搜索/任务拆解不清，而非排序错误**：可在 prompt 中显式引导 agent 每个任务只搜索一次、一次搜索一个动作，并监控首次推荐覆盖率与未发起搜索占比，针对性迭代提示词。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机** 多步 agent 任务失败往往因为缺少一个所需工具，而企业环境中工具数量巨大——Arcade 平台有约 8,200 个工具，定义总达 1.76M tokens，超过任何模型的上下文窗口。传统静态工具列表要么限制任务范围，要么每轮重复发送全部定义，成本高且选型准确率下降；微调固定工具集则无法跟上每日变化的目录。系统需要在全目录触达与低上下文成本之间取得平衡。

**方法关键点**
- **固定三工具接口**：agent 不接收工具列表，只暴露 `SelectTools`（输入任务描述，返回排名靠前的工具定义）、`UseTool`（执行工具，走用户授权）和 `ListApps`（查看可用应用及连接状态）。
- **两阶段检索**：第一阶段用 BM25+密集检索融合（加权 RRF，θ=0.5）召回候选；第二阶段用 cross-encoder 重排（90% 以上请求触发）。模型总参数量 1.2B，索引包含工具名、描述和参数文档。
- **Gateway 层权限过滤**：推荐只在 eligible scope（allowlist ∩ access policy）内排序，执行时双重检查用户 consent 和工具 scope，凭证不出 Arcade。

**关键结果**
- 在 ToolRet 基准（7,961 queries / 44,453 tools）上，Completeness@10 为 45.2%，比 BM25 的 28.8% 相对提升 57%；Recall@10 为 55.2% vs 37.0%。在 web/code 类别上优于 7-10B 参数的已发布系统。
- 端到端 Codex 多步工作流中，首次推荐覆盖全部所需工具的比例为 93%（304/327 会话）；配对实验中对 100 工具静态列表，输入 tokens 降低 17%（Codex）/ 40%（Claude Code），总账单 14 次全部更低，整体降 13.6%，任务完成率无差异。
- 成本模型预测：典型会话输入成本节省 18-21%；静态列表仅在工具数 <25-28 或搜索频率 >0.63 次/工具调用时更便宜。

**最值得记住的一句话**：给 agent 全部可用工具而不是固定百个，通过检索式推荐反而成本更低，但真正的节省取决于 agent 搜索频率和 prompt cache 对账单的影响。
