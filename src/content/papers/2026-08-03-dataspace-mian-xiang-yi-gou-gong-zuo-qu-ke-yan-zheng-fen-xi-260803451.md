---
title: 'DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous
  Workspaces'
title_zh: DataSpace：面向异构工作区可验证分析的数据智能体基准
authors:
- Boyan Li
- Zhuowen Liang
- Yupeng Xie
- Xiaotian Lin
- Tianqi Luo
- Xinyu Liu
- Yizhang Zhu
- Zhangyang Peng
- Yuan Li
- Zhengxuan Zhang
affiliations:
- HKUST(GZ)
- Tsinghua University
arxiv_id: '2608.03451'
url: https://arxiv.org/abs/2608.03451
pdf_url: https://arxiv.org/pdf/2608.03451
published: '2026-08-03'
collected: '2026-08-08'
category: Agent
direction: 数据智能体多模态分析基准
tags:
- Data Agents
- Benchmark
- Multimodal
- Deterministic Evaluation
- Heterogeneous Data
one_liner: 提出首个统一异构多模态证据发现、完整表格输出与确定性评估的数据智能体基准，最佳准确率仅 66.34%
practical_value: '- 确定性评估器的列对齐、类型精度归一化方法可直接用于推荐系统生成表格结果的自动评估，避免人工对齐局限。

  - 多模态 workspace 构建流程（跨语言转换、关系采样、模态路由）可借鉴到商品多模态信息检索的测试集构造。

  - 不同 agent harness 带来的 15.36 点性能差异提示：在构建推荐对话智能体时，工具编排与框架选择对效果决定性，需谨慎对比。

  - 多模态证据集成和连接操作一致降低准确率的发现提醒：在搜索推荐系统中融合多源异构数据时需设计针对性的对齐与融合机制。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
现有数据智能体基准孤岛式评估结构化查询、检索或开放式分析，未统一异构证据发现、完整表格生成与确定性评价，难以反映真实工作区中的复杂分析需求。

**方法**
构建 DataSpace 基准，包含 410 个跨语言任务和 7,439 个文件（CSV、JSON、SQLite、Markdown、PDF、视频），总大小 15GB。通过 DataSpace-Builder 框架自动化生成 workspace：跨语言转换统一数据形态，约束感知关系采样确保表格间有意义的连接，模态路由决定证据呈现形式，并由 11 位专家审查修复任务。评估采用确定性策略：列对齐忽略表头命名差异，类型与精度感知归一化避免数值比较误差，行顺序感知比较处理无固定顺序的输出。

**关键结果**
六款前沿多模态模型结合五种智能体框架的最佳准确率仅 66.34%，固定骨干下不同 harness 带来 15.36 点差距；多模态证据整合和关系连接操作在所有骨干上一致导致准确率下降。基准远未饱和，数据智能体可靠性仍面临核心挑战。
