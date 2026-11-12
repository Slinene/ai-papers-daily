---
title: 'Read Less, Solve More: Token-Efficient Sparse Reading of External Content
  for AI Agents'
title_zh: 少读多解：AI Agent 外部内容 token 高效稀疏读取控制
authors:
- Zedong Liu
- Jiaan Wu
- Xinyang Ma
- Le Xu
- Kai Wang
- Yuanchao Hu
- Dingwen Tao
- Guangming Tan
affiliations:
- University of Chinese Academy of Sciences
- Institute of Computing Technology, Chinese Academy of Sciences
- Songshan Lake Materials Laboratory
arxiv_id: '2608.22237'
url: https://arxiv.org/abs/2608.22237
pdf_url: https://arxiv.org/pdf/2608.22237
published: '2026-11-06'
collected: '2026-11-12'
category: Agent
direction: Agent 外部内容稀疏读取控制
tags:
- Sparse Reading
- Token Efficiency
- LLM Agents
- Read Intent
- Budgeted Reading
- Evidence Pack
one_liner: 通过 Read Intent 协议、自适应 Reader 后端和预算读门控制外部内容进入 agent 上下文，显著降 token 与延迟且保质量
practical_value: '- 在电商搜索/推荐 Agent 中，商品详情、用户评论、广告落地页等外部资源往往整体喂给 LLM，导致 token 浪费和证据稀释。可借鉴
  Read Intent Protocol：每次访问外部资源前强制结构化 intent（查询目标、需要字段、当前已覆盖证据），返回只包含 source-anchored
  证据片段与 coverage 状态，而不是全文。

  - 对结构化数据（商品表格、JSON 日志、订单信息）采用 Adaptive Reader Backends：表格用列投影或精确聚合操作（如 sum/count），JSON
  用 key-path 提取，文本用 hybrid retrieval；将“处理范围”和“模型暴露”解耦，全表计算只暴露结果，大幅降低 prompt token。

  - 引入 Budgeted Read Gate：设置完整视图预算 L，累计稀疏读取 payload 不超过 L，交付前检查即将进入 context 的 batch
  size，超预算直接 fallback 到完整视图；这保证最坏情况总曝光 <=2L，避免稀疏读取因反复查询反而更贵。

  - 工程实现上可落地为统一 Reader 接口，把不同数据源（详情页、SQL、API 响应）都实现为可插拔 Reader，协议与 agent 框架解耦，不改变模型参数就能接入现有
  agent 框架。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Web-facing AI agents 反复访问网页、文档、仓库和工具返回，但读取接口通常暴露整个对象，而单次决策往往只需少量证据。论文量化了这种 over-reading：支持证据在长文档 QA 中仅占约 3.17% 源 tokens，但 full-read agent 可能多花 17.3 倍 token 且并未提升质量。外部观察占 agent trajectory tokens 的 60-80%，且多余内容会稀释证据、诱导错误工具使用和停止失败。因此需要在外层控制“读什么”，而不是依赖事后压缩或通用检索。

**方法关键点**：SparseRead 由三部分组成，不改模型参数。
- **Read Intent Protocol**：把 artifact 访问转为结构化、有状态的阅读过程。agent 给出 access intent（优先于 session intent），返回 EvidencePack 带 source anchor、scope、coverage；agent 决定回答/精炼/验证。SHA-256 指纹失效版本变化。动作集 scout/focus/collect/refine/verify 固定。
- **Adaptive Reader Backends**：Reader 注册支持的类型、动作、成本；配置包含证据定位/处理方法 + 暴露形式，按校准的可靠性和成本选择。文本用 hybrid retrieval，表格用列投影/精确聚合，JSON 用 key-path，处理范围可与模型暴露解耦。
- **Budgeted Read Gate**：在线控制稀疏读取与 full-view fallback。固定完整视图长度 L，累积稀疏 payload E <= L；每次交付前检查实际大小，超预算则回退。保证每 episode 总曝光 <=2L，显式 fallback 防止小对象/全视图任务因稀疏读取更贵。

**关键结果**：在 6 个模型（DeepSeek-V4-Flash/Pro、Qwen3.6-Plus、GLM-5.1、Kimi-K2.5、Claude Opus 5）和 5 场景（长文档、多文件审计、结构化分析、Web deep search、AI for Science）上，tokens 减少 15.7-92.9%，wall time 减少 23-89%，中位减少 61.4%/53.7%；30 个 settings 中 29 个质量保持或提升。Web deep search 上 tokens 减 31-43%，时间减 23-37%，分数 +5-14 个百分点。对比 Naive、RAG Static、RAG Agent、ACON 和 Obs. masking，SparseRead 在 15 个设置中质量保持/提升且 token/time 更低。消融显示 intent 协议将重复读取从 4.8 降到 1.5，不可追溯证据 28% 降到 8%，有效验证从 37% 升到 89%；hybrid retrieval 证据命中率 65.3% vs BM25 60.1%；预算 gate 交付前检查使曝光控制在 1.62-1.93L，优于交付后检查的 2.10-2.33L。

**最值得记住**：外部内容要在进入 context 之前控制，而不是之后压缩；显式 Read Intent + 证据覆盖 + 预算回退是 token 高效的可复用模式。
