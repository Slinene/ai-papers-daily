---
title: Are We Ready For An Agent-Native Memory System?
title_zh: 面向原生Agent内存系统的系统性评估与设计
authors:
- Wei Zhou
- Xuanhe Zhou
- Shaokun Han
- Hongming Xu
- Guoliang Li
- Zhiyu Li
- Feiyu Xiong
- Fan Wu
affiliations:
- Shanghai Jiao Tong University
- Tsinghua University
- MemTensor (Shanghai) Technology Co., Ltd
arxiv_id: '2606.24775'
url: https://arxiv.org/abs/2606.24775
pdf_url: https://arxiv.org/pdf/2606.24775
published: '2026-06-23'
collected: '2026-06-24'
category: Agent
direction: Agent 内存系统体系化评估与设计
tags:
- Agent Memory
- Memory System
- LLM Agents
- Evaluation
- Data Management
- Cost-Performance
one_liner: 从数据管理视角分解Agent内存为四模块，量化权衡并揭示局部维护成本效益最优
practical_value: '- **模块化设计**：将Agent内存解耦为表示/存储、提取、检索/路由、维护，便于针对业务瓶颈选型，例如在搜索推荐Agent中，可单独优化检索精度与动态更新。

  - **局部维护优于全局重组**：在用户画像或对话状态频繁更新的场景下，采用增量式维护（如局部索引更新）比全量重建内存成本更低，适合线上实时系统。

  - **成本-性能权衡**：通过消融实验量化了表示保真度、检索精度、更新正确性等，为资源受限的推荐Agent提供了明确的架构取舍依据。

  - **评估体系**：超越端到端指标，关注内存子系统自身的鲁棒性与稳定性，可用于指导自研Agent中上下文记忆模块的离线评测。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有 Agent 内存评估仅以端到端任务成功指标（F1、BLEU）衡量，将内部系统视为黑箱，忽略了架构选择、动态更新鲁棒性和运营成本等关键维度。

**方法**：提出一个数据管理分析框架，将 Agent 内存分解为四个核心模块：内存表示与存储、提取、检索与路由、维护。在此框架下，对12种代表性内存系统和2个基线进行评测，覆盖5类工作负载（11个数据集），并通过细粒度消融实验量化各模块对表示保真度、检索精度、更新正确性和长程稳定性的独立影响。

**关键结果**：
- 没有单一架构在所有场景中占优；效能取决于内存结构与工作负载瓶颈的对齐程度。
- 局部维护（如增量更新）比全局重组更具成本效益，在真实负载下可显著降低运营开销。
- 消融揭示：检索精度对长程任务影响最大，更新正确性直接影响时序推理的稳定。

代码已开源：https://github.com/OpenDataBox/MemoryData。
