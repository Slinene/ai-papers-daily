---
title: Which Metrics Save the Most Human Annotation? Prediction-Powered Evaluation
  and Meta-Evaluation
title_zh: 哪些指标最能节省人工标注？预测驱动评估与元评估
authors:
- Mingqi Gao
- Anthony Sicilia
- Weiyan Shi
affiliations:
- Northeastern University
- West Virginia University
arxiv_id: '2608.26638'
url: https://arxiv.org/abs/2608.26638
pdf_url: https://arxiv.org/pdf/2608.26638
published: '2026-08-27'
collected: '2026-08-30'
category: Eval
direction: 预测驱动推断用于评估降本
tags:
- Prediction-Powered Inference
- Evaluation
- Meta-Evaluation
- Human Annotation
- LLM Judge
- PPSR
one_liner: 提出预测驱动评估框架，用少量人工标注结合大规模自动分数实现无偏系统比较，并定义PPSR元指标衡量指标降本效果
practical_value: '- 在模型迭代或A/B评估中，不必完全依赖昂贵人工标注：可复用prediction-powered evaluation思路，使用少量人工样本（如数百条）校准大规模LLM
  judge或业务自动指标（如CTR预估、相关性打分），获得无偏的模型版本对比，显著降低评估成本。

  - 选择自动指标时，不要只看与人工分的相关性（如Kendall tau），建议计算PPSR（Prediction-Powered Saving Ratio），直接衡量该指标能节省多少人工标注；PPSR对指标排名更稳定，适合在业务中筛选LLM
  judge或自定义评估器。

  - 注意paired vs unpaired设计：若新旧系统产出相同候选集（paired），使用paired设计通常更高效；若输出空间不同（如不同推荐策略、不同生成式模型），需要根据数据效率权衡选择，论文给出的分析可指导线上评估设计。

  - 该框架适用于非可验证任务（如文案生成、推荐理由、对话系统），可扩展至电商场景中商品描述、广告创意、搜索摘要等的自动+人工混合评估。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

在机器翻译等非可验证任务中，人工评估可靠但昂贵，自动指标（包括LLM judge）可规模化但常有偏。传统做法将自动指标当作人工评估的代理，导致要么只用人工（样本不足），要么只用自动（偏差风险）。该工作基于预测驱动推断（PPI），构建预测驱动评估框架：用少量人工标注校准大规模自动分数，实现数据高效且可证明无偏的系统对比。方法包括参数和非参数推断流程，并分析配对（paired）与非配对（unpaired）设计在效率上的权衡。进一步提出预测驱动节省比（PPSR）作为元指标，直接度量某个自动指标在该框架下能节省多少人工标注。在六个WMT数据集上的实验显示，PPSR对自动指标的排名比现有系统级元指标（如与人工分的相关性）更具判别力和稳定性。整体上，这一范式重新定位自动指标为降低人工标注成本的工具，而非替代人类判断，并可推广到各类非可验证任务。
