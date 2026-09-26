---
title: An Empirical Study of VLM Pipelines for Long-Document QA
title_zh: VLM 长文档问答流水线的实证研究
authors:
- Kenan E. Ak
- Jay Mohta
- Gwang Gook Lee
- Yan Xu
- Dimitrios Dimitriadis
affiliations:
- Amazon
arxiv_id: '2609.29933'
url: https://arxiv.org/abs/2609.29933
pdf_url: https://arxiv.org/pdf/2609.29933
published: '2026-09-24'
collected: '2026-09-26'
category: RAG
direction: 长文档 VLM QA 流水线实证
tags:
- VLM
- Long-Document QA
- Retrieval
- Agentic Pipeline
- Token Efficiency
- Oracle Routing
one_liner: 图像检索 top-k 页面输入是 token 效率与准确率均衡选择，Agent 收益随 VLM 规模增大才显现
practical_value: '- 在商品详情、说明书、财报等多模态长文档处理中，优先尝试图像 embedding 检索 top-k 页面/区块而不是全量文本入库，token
  可降到全页输入的 1/7 到 1/4，且准确率不降反升。

  - Agent 工具调用（page/table/figure/search）不是小模型的免费午餐：Qwen3.5-4B/9B 上落后静态页面输入，27B 才持平，Sonnet
  4.5 才领先。实际选型时先评估静态管道，再决定是否把预算花在 agentic 流程上。

  - 文本检索侧一个现成 cross-encoder rerank 就能匹配很重的多阶段 LLM 管道，工程上可用轻量 reranker 替代 LLM 重排，节省成本和延迟。

  - 最强流水线之间互补，oracle 路由能提升约13点，但证据类型路由几乎无效；说明自动路由很难，可先通过人工分析问题类型或构建更强路由特征，不要盲目上路由模型。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：长文档 QA 的输入同时包含文本、图表、表格和复杂排版，部署 VLM 时需要决定：如何把文档喂给模型、只用部分页面时选什么 retriever、用 agentic 还是静态 pipeline。这些选择影响准确率与 token 成本。

**方法关键点**：在 MMLongBench-Doc 和 LongDocURL 两个长文档 QA benchmark 上，对比 frontier API（Sonnet 4.5）与开源 VLM（Qwen3.5-4B/9B/27B）。比较静态全页输入、top-k 检索页面输入、文本检索/图像检索、以及带 page/table/figure/search 调用的六工具 agent。

**关键结果数字**：第一，agent 收益依赖 reader 规模——MMLongBench-Doc 上 Qwen3.5-4B 和 9B 落后静态页输入，27B 持平，Sonnet 4.5 领先；LongDocURL 上各 reader 均持平或领先。第二，检索模态比具体 retriever 更重要：最强图像 retriever 领先最强文本管道；文本侧一个 off-the-shelf cross-encoder rerank 基本匹配重量级多阶段 LLM 管道。top-k 图像检索在所有 reader 上 token 效率最高，约为发送每页的 1/7 到 1/4。第三，三个最强流水线在不同问题上各自成功，oracle 按题选择最佳流水线比最佳单一流水线约高 13 个点，但证据类型路由几乎无法恢复该增益。
