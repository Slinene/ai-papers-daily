---
title: 'SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated
  Multi-Agent Systems'
title_zh: SSR：面向 LLM 编排多智能体系统的结构化信号检索器
authors:
- Giancarlo Maldonado Cárdenas
- Carlos A. Astudillo
- Nelson L. S. da Fonseca
affiliations:
- Institute of Computing – State University of Campinas, Brazil
arxiv_id: '2610.21113'
url: https://arxiv.org/abs/2610.21113
pdf_url: https://arxiv.org/pdf/2610.21113
published: '2026-10-15'
collected: '2026-10-18'
category: MultiAgent
direction: 多智能体 Agent 发现的确定性检索
tags:
- Agent Discovery
- Agent Card
- Inverted Index
- LLM Orchestration
- Candidate Context Scaling
- Training-free Retrieval
one_liner: 用 Agent Card 结构化字段 + IDF 权重 + 倒排信号索引，在不训练的情况下压缩候选上下文，实现可扩展 Agent 发现
practical_value: '- 在多 Agent 推荐/搜索编排中，Agent 注册表规模增长时，不要把所有 Agent Card 都塞进 LLM 上下文：可提取
  capability-bearing 字段（如技能、工具描述）构建结构化倒排索引，先做确定性候选预筛，只把 top-k 卡片交给 orchestrator，能直接降低
  token 成本、延迟和上下文超限风险。

  - 对电商/广告场景中的工具或子 Agent 路由，IDF 加权的结构化稀疏检索比 embedding 检索更轻量、可追溯、无训练成本，适合需要审计和冷启动的服务发现模块；可用类似方式给商品类目、服务能力字段建索引。

  - 论文的 Inverted Signal Index 思路可复用到 RAG 或推荐召回：只对高区分度字段/信号显式打分，避免全量候选逐一过模型，在保证效果的同时减少计算量；其
  MS MARCO 实验中显式打分段落减少 96.8% 的结果说明了这一点。

  - 端到端编排中维持紧凑候选上下文是工程上的关键约束：即使上游检索指标不变，控制送入 LLM 的候选数量也能避免全量 catalog 带来的 operational
  failure，这对生产级 Agent 系统和高并发广告出价/推荐链路都有参考价值。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：大规模多 Agent 生态中，LLM 编排器需要发现合适 Agent，但把完整注册表暴露给 LLM 会导致 prompt 过长、推理成本上升、延迟增加，甚至超过上下文窗口。论文把该问题定义为 candidate-context scalability，目标是既找到相关 Agent Card，又保持紧凑候选上下文。

方法关键点：提出 SSR，一个确定性、免训练的 Agent Card 检索方法。它从 Agent Card 中提取承载能力的字段，构造结构化词法信号；用逆文档频率 IDF 对信号加权；再通过倒排信号索引 ISI 进行选择性候选打分，避免对所有候选逐一显式评分。整个过程不需要训练，利用 Agent Card 的原生结构，可追踪、可解释。

关键结果：在 1,000 个 Agent 的合成基准上，SSR 相比全量 catalog 编排减少 98.8% 的 LLM 输入，降低 70.9% 编排延迟。在 MS MARCO 适配任务上，IDF 改进了结构化表示下的检索效果；ISI 在保持检索效果的同时，将显式评分的段落数减少 96.8%。端到端实验表明，候选预筛能在注册表规模增长时维持紧凑上下文，并避免全量编排中出现的运行失败。
