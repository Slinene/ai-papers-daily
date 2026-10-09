---
title: 'TokenRouter: Efficient Serving System for Token-Level LLM Routing'
title_zh: TokenRouter：高效 token 级 LLM 路由服务系统
authors:
- Tianyu Fu
- Tengxuan Liu
- Ruoxi Wang
- Yixin Dong
- Yi Ge
- Yichen You
- Yu Wang
affiliations:
- Tsinghua University
- Carnegie Mellon University
arxiv_id: '2610.12242'
url: https://arxiv.org/abs/2610.12242
pdf_url: https://arxiv.org/pdf/2610.12242
published: '2026-10-07'
collected: '2026-10-09'
category: Other
direction: LLM Serving · Token 级路由
tags:
- Token-Level Routing
- LLM Serving
- Delayed Batching
- Throughput Optimization
- Request-Centric Programming
- Model-Centric Execution
one_liner: 设计 TokenRouter，以请求中心编程、模型中心执行和延迟批处理调度大幅提升 token 级 LLM 路由吞吐
practical_value: '- 在电商/广告的 LLM 多模型路由场景中，可借鉴 request-centric programming, model-centric
  execution 的分层思想：策略侧只需按单个请求描述路由逻辑，由运行时为每个模型启动独立 subserver 并异步分发，避免将路由策略硬编码进模型服务，降低开发复杂度。

  - delayed-batching scheduler 通过有界延迟换取更高吞吐，适合批量生成商品描述、广告文案、搜索 query 推荐等近线/离线任务；其最优超参数可由吞吐模型推导，减少人工调参成本。

  - 异步执行和 CUDA Graph 优化在多模型异构推理中可复用，提高 GPU 利用率；若业务同时部署大小模型或专用生成模型，可参考 subserver 隔离与异步调度避免互相阻塞。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**

token 级 LLM 路由能在 token 粒度上分发推理任务，进一步优化成本-质量边界，但现有服务系统基于单模型假设，面临 step desynchronization、频繁的 batch admission delays 以及开发实现复杂度高的问题。

**方法关键点**

TokenRouter 遵循 request-centric programming, model-centric execution 原则：开发者从单请求视角描述路由逻辑，运行时为每个 LLM 启动独立 subserver，并异步分发请求。每个 subserver 采用 delayed-batching scheduler，其最优超参数由系统数学吞吐模型推导。此外，通过扩展 CUDA Graph、异步执行等工程优化进一步提升吞吐。

**关键结果**

在多种路由算法、工作负载和模型对组合下，TokenRouter 的解码吞吐达到现有系统的 2.01–64.15 倍。相对官方 R2R 实现，并发 8 时工程优化带来 1.71 倍增益，整体提升 2.76 倍；在更严格 SLO 下，吞吐提升达 18.58 倍，同时保持速度仅 1.13 倍提升。
