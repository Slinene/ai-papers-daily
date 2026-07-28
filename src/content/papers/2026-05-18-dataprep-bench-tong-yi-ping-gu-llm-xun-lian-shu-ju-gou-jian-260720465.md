---
title: 'DataPrep-Bench: Benchmarking LLMs as Training Data Preparators'
title_zh: DataPrep-Bench：统一评估 LLM 训练数据构建与质量
authors:
- Hao Liang
- Qifeng Cai
- Yibo Lin
- Jianzhuo Du
- Qifeng Xia
- Sizhe Qiu
- Linzhuang Sun
- Meiyi Qiang
- Zhaoyang Han
- Xiaochen Ma
affiliations:
- Peking University
- Institute for Advanced Algorithms Research, Shanghai
- OriginHub Technology
- Zhongguancun Academy
arxiv_id: '2607.20465'
url: https://arxiv.org/abs/2607.20465
pdf_url: https://arxiv.org/pdf/2607.20465
published: '2026-05-18'
collected: '2026-07-28'
category: Training
direction: LLM 训练数据准备基准
tags:
- Data Preparation
- Benchmark
- Data Quality
- LLM Agent
- Distributional Alignment
one_liner: 首个端到端基准评估 LLM 数据构建与质量预测，提出 DAS 评分和技能引导代理
practical_value: '- 在电商搜索/推荐场景的微调数据准备中，可借鉴 **DAS (Distributional Alignment Score)**
  评估候选数据集与目标域（如商品查询、点击日志）的分布对齐程度，通过 MMD 衡量分布差异，过滤低质量样本，提升下游模型性能。

  - **Data-Construction-Skill** 代理将复杂数据构建任务分解为技能引导的子任务，电商从业者可类似地将“查询-商品对生成”拆解为属性抽取、语义改写等技能，提升合成数据的多样性和相关性。

  - 采用 **下游驱动评估协议**：不依赖表面文本指标，而是通过实际微调验证数据价值，推荐团队在迭代数据管道时可直接用在线 A/B 指标作为数据质量的最终评判标准。

  - 基准中数据质量评估与数据构建的 **统一框架** 可迁移至推荐系统的训练数据准备流水线，将数据采集、清洗、标注和筛选环节标准化，并通过 DAS 等指标闭环优化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：训练数据质量直接决定 LLM 能力上限，但缺乏统一基准衡量 LLM、Agent 等数据准备方法的端到端效能。现有评估多基于表面特征，未与下游训练效用关联。  
**方法**：提出 DataPrep-Bench，覆盖 Math、Science、Medical、Finance、Code、General 六个领域，从两个能力维度评估：  
1. **数据构建**：将原始来源转化为监督训练数据，评分基于用生成数据与 Dolly-15k 联合微调基模型的下游任务表现。  
2. **数据质量评估**：预测候选数据集在下游训练前的价值，评分函数通过 Pearson 相关系数与实际下游性能对比。  
同时发布两个新方法：**Data-Construction-Skill**（技能引导代理，将复杂构建任务分解为多个可执行技能）和 **DAS (Distributional Alignment Score)**（基于 MMD 衡量候选数据集与域代理的分布对齐，作为质量评分）。  
**关键结果**：Data-Construction-Skill 在 Finance 领域将 Llama-3.1-8B 的 Dolly 基线提升近 20 个绝对点。DAS 在 6 个领域中的 4 个取得最强跨模型 Pearson 相关性，且是唯一在 Math、Science、Medical 三个领域同时突破 r > 0.70 的指标，超越现有质量、多样性及启发式评估方法。
