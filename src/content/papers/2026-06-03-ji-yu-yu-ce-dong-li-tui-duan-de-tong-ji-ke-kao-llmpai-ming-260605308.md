---
title: Statistically Reliable LLM-Based Ranking Evaluation via Prediction-Powered
  Inference
title_zh: 基于预测动力推断的统计可靠LLM排名评估
authors:
- Abhishek Divekar
affiliations:
- Amazon
arxiv_id: '2606.05308'
url: https://arxiv.org/abs/2606.05308
pdf_url: https://arxiv.org/pdf/2606.05308
published: '2026-06-03'
collected: '2026-06-06'
category: Eval
direction: LLM评估的统计偏差校正
tags:
- PPI
- LLM-as-Judge
- Bias Correction
- Precision@K
- Ranking Evaluation
- Hierarchical Metrics
one_liner: 利用预测动力推断对LLM评判进行偏差校正，实现无偏且更精确的排序指标估计
practical_value: '- **低成本高可靠评估**：用30~100条人工标注（黄金集）配合大量LLM判断，即可获得无偏估计并将标准误差降低21%，适合电商搜索、推荐系统等需要频繁A/B测试的场景，显著节省人力成本。

  - **层次化指标的稀疏化技巧**：对Precision@K这类每个query汇总评分的指标，通过将输出空间从指数级降为2^K（K通常≤10）的联合分布，使PPI可实际工程化，可直接复用到NDCG@K、MAP等排序指标。

  - **区分系统微小改进**：生产系统中，LLM判断的原始偏差会淹没不同系统变体的差异；引入偏差校正后，仅需100条人工标注即可正确预测最优变体，日销售额提升407bps，适用于模型迭代中的离线快速决策。

  - **可推广到Agent评估**：方法可延伸至基于LLM的critic信号校准（如对话质量、事实准确度），用少量人工judge校正Agent自我评估的偏差，为多智体系统提供可信的自动化优化信号。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
人工评估成本高昂，小标注集导致宽置信区间，难以区分系统真实改进与噪声；LLM-as-a-Judge方案虽有成本优势，但存在系统性偏差。以往做法多通过提示工程、微调等方法打造更公正的裁判，本文另辟蹊径：接受LLM评判的偏差，并用统计方法加以校正，从而在保证无偏性的同时降低方差。

**方法关键点**  
- **PPI++ 估计框架**：结合少量人工标注的黄金集和大量LLM判断的未标注集，通过黄金集测量LLM评判的系统偏差并在估计中进行校正，估计量为无偏且λ可调以最小化方差。
- **层次化指标适配**：对Precision@K等query级指标，传统PPI的输出空间为全集大小（|C|），计算不可行。论文观察到Precision@K仅依赖Top-K文档，将输出空间压缩为{0,1}^K；假设文档间条件独立，构建K维二值向量的联合分布，计算期望时只需遍历2^K种可能（K≤10可承受），使PPI得以高效运行。
- **成本与方差折衷**：自动搜索最优λ，并发现未标注量在达到黄金集的100倍后收益递减，可据此规划标注预算。

**关键实验**  
- 在ESCI检索基准上，用30条黄金标注和60K条Claude 3 Sonnet判断，将Precision@4的标准误差从4.45降至3.50（相对降低21%），偏差保持较低（0.70）。Haiku模型以1/12的成本实现相近效果（SE=3.86，偏差最低0.29）。
- 生产搜索系统A/B测试：用100条人工标注和8400条LLM判断，PPI方法正确预测出三个系统变体的优劣（T1 > T2 > Control）；实际在线A/B确认T1带来日销售额+407bps、点击率+571bps的提升，而原始LLM评分无法区分变体。

**核心启示**  
用少量可靠标注纠正大规模LLM判断的偏差，是获得经济且可靠离线评估的可行路径，特别适用于需要精确区分候选系统的推荐与搜索场景。
