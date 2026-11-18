---
title: 'RSI-Prime: Training Models to Train Models'
title_zh: RSI-Prime：训练模型去训练模型
authors:
- Dewu Zheng
- Yang Ye
- Hongyu Zhang
- Jun Yu
- Yanlin Wang
affiliations:
- Sun Yat-sen University
- Mind Lab
- Chongqing University
- Harbin Institute of Technology, Shenzhen
arxiv_id: '2611.23138'
url: https://arxiv.org/abs/2611.23138
pdf_url: https://arxiv.org/pdf/2611.23138
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: 递归自我改进 · 模型训练自动化
tags:
- Recursive Self-Improvement
- LLM Training
- Model Training Automation
- PostTrainBench
- Decision-level Loss Masking
- RSI-Prime
one_liner: 构建 RSI-Prime 数据集并引入决策级 loss masking，让 GLM-5.3 自主训练性能相对提升 31.95%
practical_value: '- 决策级 loss masking 可直接借鉴：训练 Agent 策略模型时，对实验轨迹中的每个决策进行质量标注，仅用高质量决策做监督，能有效避免低质量动作污染策略学习，这在推荐系统
  AutoML、自动特征工程等场景尤其适用。

  - RSI-Prime 的轨迹结构（完整实验轨迹 + 细粒度决策识别）可作为构建训练自动化 Agent 数据集的模板，推荐团队可替换为自身训练 pipeline
  的决策日志，微调内部 LLM 来自动化调参、模型选择。

  - PostTrainBench 的评估任务设计（覆盖 post-training 各环节）可作为自主训练能力的评测基准，业务中可借鉴其维度设计，评估内部训练
  Agent 的能力边界。

  - 对电商/广告推荐系统直接业务价值有限：核心贡献在训练自动化与递归自我改进，离在线推荐、召回排序等日常业务较远，主要作为长期技术储备。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
LLM 正在从“被训练”扩展到“进行训练”，但模型训练能力缺乏系统研究和专门数据。递归自我改进（RSI）需要 LLM 能自主规划、执行并迭代训练实验，而现有工作多聚焦执行 harness 或训练算法，缺少高质量决策数据。

## 方法关键点
- 构建 **RSI-Prime** 数据集：包含 **350 条完整实验轨迹**，覆盖 **7 类任务**，用于提升模型训练能力。
- 对实验轨迹做**细粒度决策识别与质量标注**：区分高质量与低质量训练决策。
- 提出**决策级 loss masking**：在训练时屏蔽低质量行为的监督信号，只让模型学习高质量决策。
- 基于 GLM-5.3 在 **PostTrainBench**（自主 post-training 基准）上微调评估。

## 关键结果
- 在 PostTrainBench 上，用 RSI-Prime 训练的 GLM-5.3 相比原始 GLM-5.3，**整体性能相对提升 31.95%**。
- 证明决策级 loss masking 能有效避免低质量实验轨迹的负面影响，为未来 RSI 系统提供了可行路径。
