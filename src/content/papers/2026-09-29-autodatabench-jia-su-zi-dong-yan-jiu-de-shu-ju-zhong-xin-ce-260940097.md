---
title: 'AutoDataBench: A Data-centric Testbed for Accelerating Auto Research'
title_zh: AutoDataBench：加速自动研究的数据中心测试平台
authors:
- Ruifeng Yuan
- Yizhi Li
- Yaxin Du
- Fengyu Cai
- Yiqi Liu
- Hou Pong Chan
- Chenghua Lin
- Yun Chen
- Jian Yang
- Bryan Dai
affiliations:
- The Hong Kong Polytechnic University
- IQuest Research
- Shanghai Jiaotong University
- TU Darmstadt
- The University of Manchester
arxiv_id: '2609.40097'
url: https://arxiv.org/abs/2609.40097
pdf_url: https://arxiv.org/pdf/2609.40097
published: '2026-09-29'
collected: '2026-10-02'
category: Eval
direction: 评估Agent数据智能能力
tags:
- Data Intelligence
- Benchmark
- LLM Agents
- Data-centric AI
- Mid-training
one_liner: 构建受控测试床隔离数据智能，评估LLM改进训练数据的能力及数据效应推理，并将轨迹复用于mid-training
practical_value: '- 将数据诊断、数据组织、数据构建三阶段框架用于电商推荐数据飞轮：固定模型与超参，单独度量数据改动的增益，避免归因混淆。

  - 借鉴迭代实验设置：在资源预算约束下让LLM自动做特征筛选、样本去噪、知识注入（如商品属性补全），可降低人工数据工程成本。

  - 引入“训练前预测 vs 训练后结果”对比审计LLM的数据理解能力，识别Agent是否只是试错而非真正推理数据效应，可用于内部Agent评估。

  - 收集Agent的数据干预轨迹用于mid-training，提升下游任务性能，说明高质量数据操作过程本身可作为合成数据，适合电商场景的持续预训练或指令微调。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有auto-research基准将训练框架、超参、算力与数据等多种改进来源混杂，难以归因frontier agent的优势。为单独探究数据智能（理解和改进数据的能力），需要受控测试环境。

**方法关键点**：AutoDataBench固定非数据因素，基于数据诊断、数据组织、数据构建三层框架，设计三个高度策划的优化任务。在工具使用、检索、知识注入三类场景下，评估前沿LLM在任务特定资源预算内的迭代实验能力。除优化效果外，还比较训练前预测与训练后观测，判断LLM是否具备数据效应推理，并考察迭代反馈的作用。

**关键结果**：前沿LLM能通过迭代实验改善训练数据，但数据效应推理能力有限；迭代反馈对理解数据变化有一定帮助；将AutoDataBench轨迹作为mid-training数据可提升下游代码任务性能（具体数值未报告）。
