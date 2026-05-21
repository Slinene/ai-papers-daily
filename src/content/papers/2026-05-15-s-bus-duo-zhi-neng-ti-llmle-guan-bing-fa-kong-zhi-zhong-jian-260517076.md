---
title: 'S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination'
title_zh: S-Bus：多智能体LLM乐观并发控制中间件
authors:
- Sajjad Khan
arxiv_id: '2605.17076'
url: https://arxiv.org/abs/2605.17076
pdf_url: https://arxiv.org/pdf/2605.17076
published: '2026-05-15'
collected: '2026-05-21'
category: MultiAgent
direction: 多智能体一致性中间件 · 乐观并发控制
tags:
- DeliveryLog
- Optimistic Concurrency Control
- Observable-Read Isolation
- Multi-Agent LLM
- HTTP Middleware
- SWE-bench
one_liner: 服务器端 HTTP 日志自动重构读集，实现多智能体共享 NL 状态的乐观并发控制，零 agent 改动。
practical_value: '- 对于多 agent 协作修改共享 NL 状态（如商品描述、推荐策略片段），可借鉴 DeliveryLog 自动追踪 agent
  HTTP GET 请求的版本，在提交时做跨键检查，无需 agent 侧编码读集追踪，大幅降低开发负担。

  - 采用专用 shard 拓扑（每个 agent 拥有独立的写键，只读取共享参考 shard）可天然避免写冲突，同时利用乐观锁防止跨 shard 陈旧读取。电商场景中，多个
  agent 可并行修改不同商品的详情，共享品牌规范等只读信息。

  - 对于非加法性的 NL 状态更新（如覆盖式策略修改），乐观并发控制比 CRDT 或最后写入获胜更安全；HTTP 409 冲突响应可触发 agent 重读并重新生成，保持整体一致性。

  - 该中间件对现有 agent 框架透明，可直接部署为旁路服务；在 HTTP/1.1 场景下几乎零改造，HTTP/2 下可通过 ARSI 模式强制完备读集重建。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：多智能体 LLM 并行读写共享自然语言状态时，产生结构性竞态条件（写覆盖、跨 shard 陈旧读），现有框架缺乏写所有权语义，冲突不易发现。需一种轻量一致性机制保证协作正确性。

**方法关键点**：
- 提出 **DeliveryLog**：服务端为每个 agent 记录其 HTTP GET 请求返回时的 (key, version)，在 agent 提交时自动聚合为读集，无需 agent 显式声明或改造。
- 定义一致性模型 **Observable-Read Isolation (ORI)**：基于 HTTP 可观测读集的因果一致性，防止写-写冲突和跨 shard 陈旧读，允许不可观测读集上的写偏斜。
- 实现精简中间件（Rust 950 行核心逻辑），结合原子提交锁、跨键版本校验和写前日志，提供乐观并发控制。
- 三层次形式验证：TLA+ 模型检查（N=3 下 2076 万状态 0 违反），TLAPS 证明读集单调性和提交安全性（1 个基础公理除外），Dafny 验证 9 个归纳引理。

**关键结果**：
- 在 SWE-bench 多 agent 代码协调任务上，专用 shard 下 S-Bus 的成功率与框架可比，协调开销极低（CF=0.13 vs LangGraph 6.18）。
- 与 PostgreSQL SERIALIZABLE 和 Redis WATCH 对比，在 88 万次提交尝试中零 Type‑I 破坏，安全对等。
- 数据管道设计任务中，ORI 开启时 0/638 次提交出现不一致，关闭时 590/639 次不一致。
- 可观测读覆盖率：单步 26.1%，会话累积（利用早期 GET 记录）可达 99.8%，但 agent 自报存在 29–37% 过度声明。
- 拓扑影响：专用 shard 场景 ORI 语义中性（100% 一致），单 shard 协作写作场景有害（需额外合并策略）。
- 分布式故障转移 30/30 ORI 不变式存活，仅剩 5ms 并发故障窗口。

**核心启示**：HTTP 流量本身就是隐式的读集，服务端通过 DeliveryLog 捕获它，即可在不侵入多智能体系统的前提下提供可证明的乐观并发控制。
