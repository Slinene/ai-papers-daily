---
title: 'ANTMAN: Adaptive Need Tracking for Multi-Agent Navigation in Large Information
  Spaces'
title_zh: ANTMAN：大信息空间多智能体导航的自适应需求追踪
authors:
- Jerry Wang
- Haibo Jin
- Xiaopeng Yuan
- Peng Kuang
- Haohan Wang
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.33326'
url: https://arxiv.org/abs/2609.33326
pdf_url: https://arxiv.org/pdf/2609.33326
published: '2026-09-26'
collected: '2026-09-30'
category: MultiAgent
direction: 多智能体协作 · 需求图驱动
tags:
- Multi-Agent Coordination
- Need Graph
- Information Seeking
- Long Context
- Adaptive Routing
- RAG
one_liner: 用可修订的未解决需求图替代静态分区，使多智能体协调随查询需求而非信息空间规模增长
practical_value: '- 在电商搜索/推荐中，把用户 query 或会话意图建模为可修订需求图（如类目偏好、属性约束、缺失证据、候选商品集），用该图动态调度召回、排序、解释或
  Agent 调用；避免按商品池/内容池大小固定切分 worker，使计算随需求复杂度而非目录规模增长。

  - 借鉴 territory + WorkerCard + 两阶段路由：将商品库/内容库/代码库等 substrate 静态划分为 scope-specialized
  的 territory，先用轻量检索（稀疏+精确+稠密+RRF）召回少量 WorkerCard，再由 orchestrator 决定是否派遣；比所有 agent
  全量参与更省 token，且可跨业务 substrate 复用。

  - 每个需求节点显式记录 evidence、attempts、progress，当某条寻证/检索路径 stalled 时，优先做局部 reframe/reroute/fallback，而不是重新规划整个查询；在电商
  Agent 场景可减少长流程失败后的整体重试代价。

  - 需求驱动的局部搜索规避了超长商品列表/长上下文 prompt 里 lost in the middle 问题；在 push/推荐理由生成或大候选集重排时，可采用类似按需分段检索策略。成本敏感场景还可用小模型做
  worker 执行（ANTMAN-H 用 8B worker 保留超过 89% 性能），保留 orchestrator 用大模型。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
信息代理在超大信息空间运行时常按静态分区分配 agent，导致协调成本随空间规模增长，而查询实际所需信息很少。现有 LongAgent、CoA 等分区驱动方案在 16× 上下文增长时活跃协调增长超 15×，但查询需求并未变化。需要把运行时协调单元从“信息空间分割”改为“查询仍未解决的信息需求”。

**方法关键点**
- 将信息空间划分为确定性的 territories，每个 territory 有 WorkerCard（轻量元数据：范围/内容摘要）；worker 按 scope 特化而非按功能，共享检索接口。
- 维护可修订 Need Graph：节点为信息需求，记录 resolution status、accumulated evidence、attempt history、progress；新证据可触发 resolve/refine/introduce/reframe，支持依赖分支。
- 协调循环：选择未解决 need → 路由（先非 LLM 检索 WorkerCards，再由 orchestrator 决策）→ bounded local search → 结构化报告 → 更新图；stuck 时触发 reframe/reroute/fallback。
- 空间解耦 bound：激活 worker 数 ≤ min(M, ρH(q))，M 为总 territory 数，H(q) 为实际需求数，ρ 为单需求路由预算，因此协调随需求而非空间增长。

**关键实验**
- 多文档 QA：HotpotQA/2WikiMultiHopQA/MuSiQue 上平均 EM 0.711、F1 0.814，超过 S2G-RAG 的 0.700/0.799。
- 受控 scaling：32K→512K，活跃协调仅 1.23× 增长，LongAgent/CoA 超过 15×；成本增长 6.9× vs 14.2×/16.1×；F1 稳定在 0.840。
- 结构化导航：RepoProbe、SWE-QA-Pro、GAIA-Text-103 上相对最强非特定基线提升 15.3%/18.4%/27.9%；用 8B worker 版本保留 89.2%/93.5%/98.3% 性能。
- 消融：去掉显式 Need Graph 改用 graph-free adaptive replanning，512K F1 下降 23.82%，GAIA 下降 16.67%。
- 位置鲁棒性：ANTMAN 中间位置 gap 为 +0.015，而 full context 直接推理为 -0.181。

**最值得记住的一句话**
协调状态不应是信息空间的静态划分，而应是查询当前仍未解决的信息需求；把需求图作为 runtime state，可同时控制 worker 激活、路由和恢复，实现查询驱动而非空间驱动的计算扩展。
