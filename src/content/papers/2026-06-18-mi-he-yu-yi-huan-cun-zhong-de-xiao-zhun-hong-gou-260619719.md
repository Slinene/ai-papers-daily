---
title: Closing the Calibration Gap in Semantic Caching
title_zh: 弥合语义缓存中的校准鸿沟
authors:
- Aditeya Baral
- Radoslav Ralev
- Iliya Sotirov Zhechev
- Srijith Rajamohan
- Jen Agarwal
affiliations:
- New York University
- Redis
arxiv_id: '2606.19719'
url: https://arxiv.org/abs/2606.19719
pdf_url: https://arxiv.org/pdf/2606.19719
published: '2026-06-18'
collected: '2026-06-19'
category: LLM
direction: 语义缓存校准与评估指标
tags:
- semantic caching
- calibration
- evaluation metrics
- LLM serving
- PR-AUC
- precision-recall
one_liner: 指出语义缓存评估重排名轻校准导致部署性能差，提出缓存感知的校准指标P-CHR AUC与CRR
practical_value: '- 语义缓存选型时，不要只看PR-AUC，应优先评估分数的校准度（如使用P-CHR AUC或CRR），否则线上高排名模型可能给出不可靠的阈值，导致过多误命中。

  - 部署前做分数截断阈值扫描时，直接使用P-CHR AUC曲线观察不同缓存利用率下的精度，平衡成本与质量；CRR能快速估算离线排序指标有多少能迁移到线上。

  - 校准差距主要由训练目标（如对比损失 vs. 交叉熵）决定，而不是数据规模，因此改进语义相似度模型的训练目标比堆数据更有效；已有模型可通过温度缩放、直方图分桶等后校准手段部分弥补，但不能完全消除差距。

  - 设计缓存系统时，将缓存命中决策视为二元分类问题，显式考虑正样本率（查询重复率）带来的结构性上限，避免在低重复率场景下盲目追求高召回。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：语义缓存通过返回相似查询的缓存答案降低大模型推理成本，但现有评估仅使用PR-AUC衡量排序质量，忽略分数是否可直接用于阈值截断，导致离线最优的模型在线上常表现最差。

方法：提出两个实用指标——Precision–Cache Hit Ratio (P-CHR) AUC，测量不同缓存利用率下的精度，直接反映部署时精度与成本的权衡；Calibration Retention Rate (CRR)，量化离线排序性能在部署后能保留多少。将线上下性能差距分解为可恢复的校准部分和由数据集正样本率决定的结构性不可约部分。

关键结果：校准差距受训练目标影响远大于数据规模；后校准（如Platt缩放、温度调节）只能部分弥合差距；模型选择本质是校准问题而非排序问题，使用P-CHR AUC和CRR可以更准确地预测线上表现，避免传统PR-AUC的误导。
