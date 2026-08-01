---
title: Measuring Alignment With Reader Highlights Net of Position and Length
title_zh: 去除位置和长度影响的读者高亮对齐度量
authors:
- Kazuki Nakayashiki
- Keisuke Watanabe
affiliations:
- Glasp Inc.
arxiv_id: '2607.27739'
url: https://arxiv.org/abs/2607.27739
pdf_url: https://arxiv.org/pdf/2607.27739
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: LLM上下文压缩评估 · 读者高亮对齐
tags:
- context compression
- evaluation
- reader highlights
- position bias
- length bias
- language models
one_liner: 提出剔除位置与长度偏差的评估框架，发现LLM重要性排序与读者高亮对齐接近人类个体水平
practical_value: '- 评估文档摘要/压缩模型时，常规准确率受位置和长度偏差影响，可借鉴分层匹配与合成零分布校准，对商品描述、评论摘要等场景的压缩质量进行无偏评估。

  - 语言模型重要性排序与读者高亮高度一致，可自动提取商品卖点或用户关注片段，量化模型与人类偏好对齐程度，提升内容生成效率。

  - 该方法提供消除混杂因子的通用评估框架，可迁移至推荐系统中分析用户行为数据（如点击），控制位置暴露偏差，更准确衡量模型捕捉兴趣的能力。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：上下文压缩依赖下游任务精度评估，形成模型评判重要性的循环论证。读者社交高亮提供非循环参考，但传统指标（保留高亮句子比例）被位置偏差（读者偏好前部）和长度偏差（高亮句子更长）混淆，导致虚高得分。

**方法**：提出无偏评估框架：对每个高亮句子，在同一文档中匹配相对深度和长度排名相同的未高亮句子为对照，计算富集度差异。并用仅含位置和长度的合成零分布校准，避免仅分层导致的20-36%假阳性。在120个网页（≥12位读者）上，评估LLM重要性排序与高亮对齐。

**结果**：LLM排序保留38.4%高亮句，对照19.9%，富集度+0.196 [0.148,0.239]，p=0.0005。朴素截断富集度仅+0.003，证实偏差消除。单人类读者富集度+0.182，GPT-5.4为+0.002（与人类无差异），Claude Opus 5更高。经典Luhn启发式达+0.088，可见词频部分解释读者选择，但词法中心性仅减少0.010，表明一致性不源于中心性。
