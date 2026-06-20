---
title: 'Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore
  for Low-Latency, Small-Batch, On-Device Physical-AI Serving'
title_zh: 执行状态胶囊：面向低延迟设备端物理AI服务的图绑定检查点与恢复
authors:
- Liang Su
arxiv_id: '2606.20537'
url: https://arxiv.org/abs/2606.20537
pdf_url: https://arxiv.org/pdf/2606.20537
published: '2026-06-18'
collected: '2026-06-20'
category: LLM
direction: 图绑定执行状态复用 · 低延迟LLM推理
tags:
- LLM serving
- state checkpoint
- low-latency
- on-device
- CUDA graph
- execution reuse
one_liner: 提出图绑定执行状态胶囊，将LLM推理复用从KV片段提升至全状态边界，实现亚毫秒级快照/恢复与27倍TTFT加速
practical_value: '- 若业务中存在实时Agent交互（如对话式推荐），可借鉴胶囊机制实现亚毫秒级状态分支与回滚，降低用户感知延迟

  - 在需要维护会话级推理状态（如探索式推荐对话）时，全量状态快照可确保回溯一致性，避免仅KV缓存导致的状态发散

  - 边缘设备推荐场景可参考静态图 + 连续缓冲区的设计，消除动态块表开销，提升小批量推理的确定性延迟

  - 工程上，若自研推理系统，可考虑将可恢复状态抽象为封闭缓冲集，以实现更高效的状态管理；但目前需深度CUDA集成，落地依赖未来框架支持'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：传统LLM服务通过分页或radix KV缓存实现前缀复用，但在低延迟、小批量、设备端的交互式Agent、语音或机器人场景中，频繁的分支、中断与重入需要更彻底的状态管理与快速恢复。KV缓存仅管理执行状态的单一片段，无法保证递归状态（如Mamba的隐藏状态）的一致性，导致符号差异与延迟波动。

**方法**：作者提出执行状态胶囊（Execution-State Capsules），一种图绑定（graph-bound）的检查点与恢复机制。核心是FlashRT运行时，它使用捕获的CUDA图在静态连续缓冲区上执行推理，消除块表间接寻址。由于所有活状态是一个封闭的命名缓冲集，胶囊可以在任何提交的令牌边界对整个状态（KV缓存、递归状态、卷积状态、MTP状态及元数据）进行一次快照、恢复、分支或回滚。这从根本上将复用从令牌寻址的KV片段转向图绑定的执行状态边界。

**结果**：在RTX 5090上，胶囊恢复实现字节精确与贪婪解码下的令牌一致，而仅KV消融实验出现发散，验证了递归状态的关键性。GPU驻留快照与恢复延迟均小于1毫秒，冷TTFT加速比从2k token时的3.9倍提升至16k token时的27倍。该设计在Jetson AGX Thor和DGX Spark上也保持了相同的正确性与结构特性，为延迟优先的服务场景提供了全新的复用基点。
