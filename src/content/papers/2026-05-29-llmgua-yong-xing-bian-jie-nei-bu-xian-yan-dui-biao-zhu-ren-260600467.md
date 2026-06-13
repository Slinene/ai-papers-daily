---
title: 'On the Limits of LLM Adaptability: Impact of Model-Internalized Priors on
  Annotation Task Performance'
title_zh: LLM适用性边界：内部先验对标注任务性能的影响
authors:
- Etienne Casanova
- Rafal Kocielnik
- R. Michael Alvarez
affiliations:
- California Institute of Technology
arxiv_id: '2606.00467'
url: https://arxiv.org/abs/2606.00467
pdf_url: https://arxiv.org/pdf/2606.00467
published: '2026-05-29'
collected: '2026-06-13'
category: Eval
direction: LLM零样本标注评估与分析
tags:
- LLM
- zero-shot annotation
- prior
- correction stickiness
- DSF
- toxicity detection
one_liner: 发现LLM标注错误难以通过提示纠正，定义匹配比文本记忆更关键
practical_value: '- 在电商评论分类、商品描述标注等场景，单纯通过修改提示纠正LLM错误可能无效，应优先确保标注定义的语义与模型内部概念对齐，而非依赖表层提示工程。

  - 引入DSF（Definition-Specific Familiarity）概念，可在设计标注任务时量化定义匹配度，提前评估LLM的适应性，减少后续人工修正成本。

  - 高置信度的错误尤其顽固，直接重标注难以改变，建议结合主动学习筛选低置信度样本再进行人工复核，节省资源。

  - 避免依赖文本相似度（如ROUGE-L、BERTScore）作为记忆指标去预测模型表现，可能产生误导，应转向定义层面的对齐检查。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
LLM被广泛用于零样本标注和评判任务，但其可靠性受内部先验与用户指令交互的影响。研究旨在揭示LLM在适应不同标注定义时的局限性，而非仅关注性能分数。

## 方法
- 在多样性数据集（社交媒体、游戏、新闻、论坛）上进行毒性检测实验，使用稠密和MoE模型。
- 测试三个维度：
  1. 模型对数据和定义的熟悉度影响；
  2. 通过提示中的附加信息纠正零样本错误的可能性（“决策粘性”）；
  3. 模型对错误定义的服从程度。
- 提出定义特定熟悉度（DSF），衡量模型内部概念与任务定义的对齐程度，并与多种记忆化指标（ROUGE-L、BERTScore、embedding余弦相似度）对比。

## 关键结果
- 约2/3的零样本错误无法通过提示纠正，总拯救率仅34.8%；高置信度错误尤其顽固。
- LLM会遵循错误定义，同时保持与正确定义条件下相同的置信度。
- DSF与性能呈显著正相关（偏相关系数r=+0.41），而三种记忆化指标均未表现正关联，凸显定义对齐的重要性。
