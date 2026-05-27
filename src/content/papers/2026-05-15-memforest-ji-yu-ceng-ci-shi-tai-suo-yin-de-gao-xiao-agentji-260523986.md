---
title: 'MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing'
title_zh: MemForest：基于层次时态索引的高效Agent记忆系统
authors:
- Han Chen
- Zining Zhang
- Wenqi Pei
- Bingsheng He
- Ming Wu
- Jason Zeng
- Michael Heinrich
- Wei Wu
- Hongbao Zhang
affiliations:
- National University of Singapore
- Zero Gravity Labs
arxiv_id: '2605.23986'
url: https://arxiv.org/abs/2605.23986
pdf_url: https://arxiv.org/pdf/2605.23986
published: '2026-05-15'
collected: '2026-05-27'
category: Agent
direction: Agent记忆系统 · 层次时态索引
tags:
- Agent Memory
- Temporal Indexing
- Write-Efficient
- Hierarchical Retrieval
- LLM Agents
- MemTree
one_liner: 通过并行提取与层次时态索引，实现Agent记忆的局部更新与时间感知检索，大幅提升写入吞吐
practical_value: '- **时态树组织用户状态**：将用户偏好、行为轨迹等记忆按时间组织为MemTree，天然支撑“状态演变查询”，避免扁平向量检索丢失时间顺序，适合电商场景中用户偏好迁移、行为序列推断。

  - **局部更新与惰性刷新**：修改仅影响脏节点路径，避免全量重写Profile或Summary，大幅降低在线更新成本，适合高并发会话流下的实时记忆维护。

  - **并行提取提升写入吞吐**：将长会话切分为短块并行调用LLM，再通过事实规范化合并，可迁移到推荐系统中对用户长行为序列的实时摘要生成，加速记忆构建。

  - **多粒度检索平衡效率与精度**：从粗粒度树摘要快速召回，再细粒度浏览，避免全库向量搜索开销，适合多智体系统的上下文召回或检索增强生成中的高效证据定位。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM Agent需在长周期交互中维护持久记忆，但现有系统在写入路径存在严重瓶颈——粗粒度状态管理（如全量重写Profile）和顺序LLM提取导致更新延迟随记忆累积而增长，且难以保留时间维度的状态演进，影响历史查询与多步推理。

**方法关键点**：
- **并行chunk提取**：将新会话切分为固定大小的短块（默认2轮），并发调用LLM提取记忆候选，打破串行瓶颈。
- **规范事实（Canonical Facts）**：合并去重后的稳定记忆单元，作为写入和路由的基础，避免直接改写累积状态。
- **MemTree层次时态索引**：以时间有序树组织每个记忆域（实体、场景、会话），叶子存储局部证据，内部节点总结时间区间，支持局部插入与惰性脏路径刷新，维护成本与受影响路径相关而非总记忆规模。
- **多粒度检索**：森林级召回后从根节点到叶子逐级浏览，可选嵌入驱动或LLM引导，保持时间连续性，避免语义相似但时间错误的检索。

**关键实验**：
- 基准：LongMemEval‑S（500实例）和LoCoMo；对比EverMemOS、Mem0、MemoryOS等有状态记忆基线。
- 效率：在LongMemEval‑S上，MemForest写入耗时178s（30B模型），约为MemoryOS的13.7倍速，EverMemOS的5.9倍；写吞吐显著提升。
- 质量：LongMemEval‑S达到79.8% pass@1（30B），优于所有基线；LoCoMo上68.4%，接近最强基线（69.6%），但写成本大幅降低。
- 迁移实验：合并已构建记忆比顺序写入快2.4‑2.7倍。

**核心洞见**：将Agent记忆维护从全量重写转为基于时态树的局部增量更新，是打破写入瓶颈、同时保留时间感知能力的关键路径。
