---
title: 'AgenticDataBench: A Comprehensive Benchmark for Data Agents'
title_zh: AgenticDataBench：面向数据代理的多领域细粒度综合基准
authors:
- Zhaoyan Sun
- Shan Zhong
- Daizhou Wen
- Jiaxing Han
- Guoliang Li
- Ying Yan
- Peng Zhang
- Yu Su
- Xiang Qi
- Baolin Sun
affiliations:
- Tsinghua University
- Ant Digital Technologies, Ant Group
arxiv_id: '2607.01647'
url: https://arxiv.org/abs/2607.01647
pdf_url: https://arxiv.org/pdf/2607.01647
published: '2026-07-01'
collected: '2026-07-03'
category: Eval
direction: 数据代理评估基准
tags:
- Data Agents
- Benchmark
- Data Science
- Skill-based Evaluation
- LLM-based Task Generation
one_liner: 覆盖15个垂直领域，基于细粒度技能定义实现数据代理的全面评估与任务生成
practical_value: '- 借鉴技能分解思路，将推荐系统开发流程（如特征工程、模型选择、A/B测试）拆解为可复用的原子技能，用于设计模块化推荐Agent。

  - 利用社区数据（如内部实验日志、技术文档）提取高频操作模式，构建面向推荐问题的诊断或调优数据集。

  - 按技能覆盖度最大化来筛选任务集合，确保离线评估时覆盖更多真实场景，避免评估偏差。

  - LLM合成任务的方法可迁移至推荐场景，用于生成低资源领域的训练数据或用户模拟查询。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：数据科学工作流的自动化需求迫切，但目前缺乏覆盖多领域、能细粒度评估LLM数据代理的基准。现有评测大多场景单一、粒度粗糙，无法反映代理在真实异构任务中的能力。

**方法**：
1. **多域真实任务收集**：从15个垂直领域（含金融科技B2B用例）采集真实数据集与任务，保证领域多样性。
2. **技能抽取与基准覆盖量化**：定义数据科学技能（如“处理缺失值”“特征编码”）为基本操作单元；利用大规模Stack Overflow解决方案，通过技能对齐的层次聚类提取代表性技能集合。
3. **任务选择与合成**：对真实任务，选择使技能组合多样性最大化的任务-解决方案对；对缺少真实任务的领域，设计基于技能的LLM流水线自动生成工作流与任务。
4. **细粒度评估**：基准提供逐技能的标注真值，支持代理在子技能层面上的性能诊断。

**结果**：在开源测试平台上评估了当前主流数据代理，获得技能级别的性能剖析，揭示了它们在“数据清洗”“多步推理”等技能上的显著能力差异。
