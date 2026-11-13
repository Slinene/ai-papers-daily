---
title: 'Evolving Infra: Agent-Adaptive LLM Serving at Scale'
title_zh: 面向 Agent 负载的自适应 LLM 推理服务系统 Evolving Infra
authors:
- Hao Kang
- Weili Xu
- Ziyang Li
- Zheng Du
- Hanchen Li
- Tian Xia
- Song Bian
- Tushar Krishna
- Huizi Mao
- Ion Stoica
affiliations:
- Georgia Institute of Technology
- University of Illinois Urbana-Champaign
- University of California, Berkeley
- NVIDIA
- OpenAI
arxiv_id: '2611.12304'
url: https://arxiv.org/abs/2611.12304
pdf_url: https://arxiv.org/pdf/2611.12304
published: '2026-11-08'
collected: '2026-11-13'
category: Agent
direction: Agent 推理服务 · 计算与 KV 缓存解耦
tags:
- Agentic LLM Serving
- Prefill-Decode Disaggregation
- KV Cache Management
- Online Adaptation
- Symmetric Engine
one_liner: 解耦 prefill/decode 计算分配与 KV cache 管理，通过 agent 上下文感知的动态规划与缓存策略大幅降低延迟并提升吞吐
practical_value: '- **对称引擎 + 共享 KV pool 实现快速 PD 切换**：在电商搜索推荐 Agent 推理服务中，负载随时间波动大（如大促、推送高峰），可采用类似的对称引擎架构，节点无需重启即可在
  prefill/decode 间切换，避免 KV 丢失和分钟级停机，降低运维成本。

  - **Agent 上下文感知的 KV 驱逐策略**：多轮对话 Agent 常涉及工具调用、上下文压缩、子任务分支，传统 LRU 会误驱逐等待复用 key 的
  KV。可借鉴引用计数目录，跟踪 active branch，优先驱逐无引用 KV，显著提升 KV 命中率，降低重复计算成本。

  - **在线迭代时间模型驱动 PD split 动态调整**：工作负载组成（如 query 改写、排序打分、生成式推荐）在 prefill/decode 资源需求上差异大，可离线拟合
  prefill/decode 单次迭代耗时模型（分离 cached/uncached tokens），在线评估平均请求工作，避免突发流量干扰，实现精准的节点角色分配。

  - **基于预测 TTFT 的负载均衡路由**：放弃 cache-aware 的 sticky 路由，改用异步 KV 预取 + 预测 TTFT 路由，可以避免热门前缀节点过载，同时保持高
  KV 复用。在大规模 Agent 推荐场景中可有效降低 P95 延迟。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Agentic workloads 已成为 LLM 推理需求的主要来源，其特性（多步交互、长前缀复用、上下文管理）使传统 PD disaggregated serving 系统暴露出严重不足：prefill/decode 节点负载失衡、KV cache 误驱逐、阶段切换代价高昂。现有系统计算分配与 KV 管理耦合，切换节点角色需重启或丢弃 KV，且粗粒度信号无法适应 Agent 动态上下文变化，导致延迟飙升和吞吐损失。

**方法关键点**：
- **解耦计算与 KV 管理**：设计对称引擎，节点可同时服务 prefill/decode，无需重启即可切换；共享 host-memory KV pool 让 KV 对所有节点始终可读，阶段切换不丢缓存。
- **Agent-aware KV 目录**：维护集群级 prefix tree，统计每个 KV block 的 active branch 引用计数，根据 fork、compaction、sub-agent 生命周期及跨节点转移更新计数，指导 eviction（零计数优先驱逐）和 transfer。
- **在线规划器**：拟合 prefill/decode iteration-time 模型（分离 cached/uncached tokens），基于滚动窗口的平均请求工作评估候选 PD split 的吞吐增益，仅当统计显著时才切换，避免短暂突发触发昂贵切换。
- **KV-reuse-aware 路由**：异步预取 KV（请求排队时完成加载），路由到预测 TTFT 最短的节点，平衡负载同时保持高缓存复用。

**关键实验结果**：在 Putnam、Claude Code、OSWorld 三个 Agent 任务上，用 GLM-5.2 和 Kimi K2.6，部署在最多 256 张 GB300 GPU 上。相比 Dynamo（NVIDIA 生产框架），Evolving Infra 将 mean E2E latency 降低最高 4.1×，P95 TTFT 降低最高 14×；在静止负载下吞吐最高 2.73× Dynamo，比最佳静态 split 高 38%；在负载组成动态变化下吞吐高于 Dynamo 2.14×，高于最佳静态 split 1.28×。阶段切换平均仅 6.2s（Dynamo 需 681s），KV 复用损失降低 81-95%。

**最值得记住的一句话**：解耦计算分配与 KV cache，加上 agent 上下文感知的缓存管理，是高效服务 Agentic LLM 工作负载的关键。
