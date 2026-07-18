---
title: Where Does the Noise Come From? A Variance-Components Decomposition of Non-Determinism
  in LLM Brand Answers
title_zh: LLM 品牌回答的噪声从何而来：方差分量分解
authors:
- Dmitrij Żatuchin
affiliations:
- Estonian Entrepreneurship University of Applied Sciences
- Rankfor.AI
arxiv_id: '2607.13304'
url: https://arxiv.org/abs/2607.13304
pdf_url: https://arxiv.org/pdf/2607.13304
published: '2026-07-14'
collected: '2026-07-18'
category: Eval
direction: 方差分量分解 · 可靠度优化
tags:
- variance components
- reliability
- LLM evaluation
- brand recommendation
- generalizability theory
- multiverse analysis
one_liner: 将 LLM 品牌推荐的非确定性分解为语言、模型、提示改写和重采样四类方差，指出扩展语言和模型比重复采样更有效提升可靠性
practical_value: '- 评估 LLM 生成推荐（如品牌/商品推荐）的可靠性时，不要只重复多次提问：重复采样的方差贡献大但边际收益低；优先增加语言变体、模型种类可显著降低相对误差。

  - 品牌排名可靠性极低（单次回答 ICC 仅 0.01），若用 LLM 做品牌健康度监测或竞品分析，必须设计多语言多模型交叉采样方案，否则结果几乎无区分度。

  - 该方法可直接移植到电商搜索推荐评估：通过 G 研究分解方差分量，再通过 D 研究优化样本预算，确定需采样多少 prompt、语言、模型以获得目标可靠度。

  - 品牌-语言交互（8.6% 方差）意味着多语言评估时品牌得分随语言变化，提示需要统一语言基准或加入语言控制，避免双语偏差。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：业界用 LLM 监测品牌推荐时，发现重复提问结果不稳定，但普遍只做简单重复采样（如 5 次）后平均，未系统分解噪声源。该论文旨在分离并量化导致回答变动的各个因素，以指导采样策略。

**方法**：采用概化理论（generalizability theory）的交叉随机效应分解，将一次品牌回答的情感极性得分的方差分解为品牌、查询语言、模型、提示改写、重采样及其交互效应。实验覆盖 20 个中欧品牌、8 种语言、3 个模型（GPT-5.2、Gemini 3 Flash 参数模式、Perplexity 检索模式），构建全交叉语料 12,933 条回答，并设置重复采样稳定性子集（每单元约 5 次）。通过 REML 拟合方差分量，计算泛化系数和 D 研究下不同样本分配方案的相对误差方差。

**关键结果**：查询语言是最大系统方差源（占总方差 26.5%），品牌主效应仅占 1.5%（ICC=0.0146），说明单次回答几乎无品牌区分力。在稳定性子集中，重采样占 34.8%，品牌-情境交互占 29.6%，品牌-语言交互 8.6%（存在双语惩罚），品牌-模型和品牌-提示交互接近零。预算相同时，增加语言和模型数量对降低相对误差的效果远优于增加重复次数（第 5 次以上重复仅降低 0.0003）。品牌排名的可靠性始终很低：单次回答约 0.01，即使全交叉设计也仅约 0.36，可靠度需通过广度而非深度采样获取。
