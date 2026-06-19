---
title: When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization
  in Streaming Retrieval-Augmented Generation
title_zh: 流式工具使用何时有效？基于工具意图稳定化的流式 RAG 延迟隐藏分析
authors:
- Elroy Galbraith
affiliations:
- SMG Labs
arxiv_id: '2606.20113'
url: https://arxiv.org/abs/2606.20113
pdf_url: https://arxiv.org/pdf/2606.20113
published: '2026-06-18'
collected: '2026-06-19'
category: RAG
direction: 流式 RAG 意图稳定化与延迟优化
tags:
- Streaming RAG
- Tool-Intent Stabilization
- Latency Hiding
- Speculative Query
- CRAG Benchmark
- BM25
one_liner: 在流式 RAG 中，通过分析工具意图稳定点，量化了可隐藏的延迟比例并揭示了早期意图形成的查询特性
practical_value: '- 搜索自动补全/对话式推荐中，可借鉴投机查询思想：在用户输入进行时并行检索，当意图稳定后利用剩余输入时间隐藏检索延迟。

  - 意图稳定点分析可指导何时触发推荐或 query 生成：早期意图稳定（如问题类型）可预测，从而提前启动计算，减少感知延迟。

  - 提供的无模型边界 H 可为系统设计提供理论最大延迟隐藏能力，评估不同配置下的收益。

  - 对于电商客服机器人，可以预测用户问题类型，在输入早期即发起商品或政策检索，提升响应速度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：流式 RAG 虽能通过并行输入与工具查询降低感知延迟，但其收益依赖于正确查询是否在用户完成输入前就已可确定。此工作隔离并测量了这一核心属性。

**方法**：定义“工具意图稳定化”为输入流中投机查询的检索结果收敛到最终答案承载结果的时间点。在 CRAG 数据集（1371 验证问题）上，使用 BM25 检索并比较不同阶段的 top-1 文档与最终黄金证据的重叠来测量稳定点。推导出模型无关的延迟隐藏边界 H，与工具延迟 L 和输入速度 δ 相关。构建实际流式流水线验证节省的延迟。

**关键结果**：在 L=600ms, δ=3词/秒, 置信度阈值 θ=0.8 的设置下，73.9% 的查询可实现显著延迟隐藏。21.3% 的问题具有容易检索的黄金证据，其中 95.2% 可流式化，稳定点 φ_suf ∈ [0.26, 0.281]，表明意图在输入前半段就确定。问题类型显著影响早期/晚期稳定（Kruskal-Wallis p=0.017），可指导何时触发投机检索。
