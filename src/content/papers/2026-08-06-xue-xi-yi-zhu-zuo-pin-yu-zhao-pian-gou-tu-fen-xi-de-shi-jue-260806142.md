---
title: Learning visual representations for compositional analysis of artworks and
  photographs
title_zh: 学习艺术作品与照片构图分析的视觉表征
authors:
- Fatemeh Behrad
- Tinne Tuytelaars
- Johan Wagemans
affiliations:
- KU Leuven
arxiv_id: '2608.06142'
url: https://arxiv.org/abs/2608.06142
pdf_url: https://arxiv.org/pdf/2608.06142
published: '2026-08-06'
collected: '2026-08-09'
category: Multimodal
direction: 视觉构图表征 · 人类感知 vs 基础模型
tags:
- Visual Composition
- Object-centric Learning
- Graph Attention
- Interpretability
- Self-supervised Fine-tuning
- Cross-domain Generalization
one_liner: 对比人类启发的构图分析（对象分解+图注意力）与微调基础模型，前者可解释且数据高效，后者性能更强但泛化差
practical_value: '- 商品图像美感评估：借鉴对象中心分解+空间关系图注意力，构建可解释的构图评分模块，辅助自动优化商品主图布局。

  - 广告创意排序：冻结编码器+人类先验的方法在数据稀缺时泛化更好，适合冷启动的创意构图质量过滤。

  - 可解释推荐视觉特征：将区域级对象关系显式编码为图表示，替代黑盒特征，提升推荐理由中视觉部分的可解释性。

  - 多模态检索增强：构图检索任务可迁移至电商场景，支持“构图相似”的商品搜索，例如按对角线构图、三等分构图查询相似商品图。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

动机：构图是艺术品传达意义、情感与美学的核心，但缺乏可计算的形式化理解，现有方法存在语义偏差，需探索人类感知启发的方案。

方法：比较两种构图分析范式——(1) 人类启发方法：用对象中心模型将图像分解为感知区域，再通过图注意力网络建模空间关系，编码器冻结以保持可解释性；(2) 微调基础模型：在大规模构图数据集上微调自监督视觉模型。评估覆盖构图评分/分类预测、构图感知图像检索和视觉显著性检测三个下游任务。

结果：冻结编码器下，人类启发方法取得有竞争力的性能，且天然具备可解释性；当数据充足允许微调时，大自监督模型显著超越，但牺牲了可解释性和跨域泛化能力。
