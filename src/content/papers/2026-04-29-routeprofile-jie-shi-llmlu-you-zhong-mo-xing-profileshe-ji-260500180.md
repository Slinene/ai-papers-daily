---
title: 'RouteProfile: Elucidating the Design Space of LLM Profiles for Routing'
title_zh: RouteProfile：揭示LLM路由中模型profile设计空间
authors:
- Jingjun Xu
- Hongji Pu
- Tao Feng
- Haozhen Zhang
- Jiaxuan You
- Ge Liu
affiliations:
- University of Illinois Urbana-Champaign
- Nanyang Technological University
arxiv_id: '2605.00180'
url: https://arxiv.org/abs/2605.00180
pdf_url: https://arxiv.org/pdf/2605.00180
published: '2026-04-29'
collected: '2026-05-16'
category: LLM
tags:
- LLM
- Routing
- Profiling
- Graph
- Cold-Start
- Design Space
one_liner: 定义LLM路由的profile设计空间，发现结构化、可训练profile显著提升路由与新模型泛化能力
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

在大模型生态中，不同模型在不同查询、任务和领域上表现各异，这催生了LLM路由技术，以便为每个查询动态选择最合适的模型。然而，现有工作多聚焦于路由器机制的设计，而刻画模型能力的LLM profile却长期被忽视，甚至与路由策略纠缠在一起，遮蔽了性能增益的真正来源。本文将LLM profiling重新定义为异构交互历史的结构化信息集成问题，并系统性地研究profile设计如何影响路由性能与泛化能力。

## 方法关键点

- **异构交互图**：将模型族、模型、领域、任务和查询构建为异构图，边特征包含基准测试得分，节点特征由LLM生成或从查询文本编码得到。
- **设计空间RouteProfile**：沿四个维度刻画profile构造：**组织形态**（扁平 vs. 结构化）、**表示类型**（文本 vs. 嵌入）、**聚合深度**（0~4跳）和**学习配置**（训练自由 vs. 可训练）。
- **实例化聚合器**：扁平文本拼接、基于文本的GNN（LLM消息传递）、基于嵌入的GNN（简化GCN）以及可训练GNN（HANConv + 掩码重建自监督）。
- **评估路由器**：覆盖三种代表性路由器——SimRouter（相似度）、MLPRouter（学习投影）和GraphRouter（图结构），在标准路由和新LLM冷启动两种设定下进行测试。

## 关键实验与结果

- **数据与模型**：15个数据集构建交互图，25个LLM（8个候选模型），12个下游评测数据集。
- **结构化优于扁平**：在所有路由器上，结构化profile均一致优于扁平基线。例如，SimRouter下结构文本4跳达到平均性能0.580，而扁平文本仅0.554；MLPRouter下结构文本3跳0.625；GraphRouter下结构Emb 4跳0.614。
- **查询级信号更可靠**：消融实验表明，保留查询与任务信号时性能最高（文本2跳0.578），而加入领域信号反而可能下降（0.549），说明细粒度信号是决定性因素。
- **冷启动泛化**：使用新LLM（Mistral-Small-24B）时，扁平profile几乎为零泛化，而结构化可训练profile取得显著提升。例如，Trainable GNN 3跳在SimRouter上冷启动命中率达0.452，GraphRouter下结构文本4跳冷启动命中率0.547，显示出结构化与学习能力的互补必要性。

## 一句话总结

LLM路由性能不仅取决于路由器设计，更依赖于候选模型的profile质量；结构化且可训练的profile是通向鲁棒路由和模型泛化的关键路径。
