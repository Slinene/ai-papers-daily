---
title: 'Beyond Knowledge Transfer: How User Overlap Shapes Diversity in Cross-Domain
  Recommendation'
title_zh: 超越知识迁移：用户重叠如何塑造跨域推荐多样性
authors:
- Yuhan Zhao
- Weixin Chen
- Shu Chen
- Li Chen
affiliations:
- Hong Kong Baptist University
- Shenzhen University
arxiv_id: '2611.30156'
url: https://arxiv.org/abs/2611.30156
pdf_url: https://arxiv.org/pdf/2611.30156
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 跨域推荐 · 多样性优化
tags:
- Cross-Domain Recommendation
- Diversity
- Overlapping Users
- Negative Sampling
- Model-Agnostic
one_liner: 提出 model-agnostic 的 Push-Pull 框架 DivCDR，通过拓宽重叠用户桥与推开非重叠用户表示提升跨域推荐多样性
practical_value: '- 跨域/多业务推荐中，重叠用户桥常偏向头部口味。可借鉴 Pull 的 confidence-gated virtual positives
  + exposure-entropy gain 做训练期多样性正则：对重叠用户目标域稀疏交互生成虚拟正样本，并约束曝光熵，避免高分 item 集中在少数头部类目。

  - Push 的 overlap-density-guided negative sampling 可迁移到召回/粗排：对非重叠用户或新用户负采样时，优先采样重叠用户高密度区域的
  item，把个性化表示从大众偏好中心推开，缓解热门淹没。

  - DivCDR 是 model-agnostic 插件，可在已有双塔/Graph CDR backbone 上低成本叠加；若业务已有跨域用户映射，不必更换主模型，只需在
  loss/采样层改造。

  - 上线跨域模型时，建议同时监控 accuracy 与 diversity（如曝光熵、类目覆盖率），并区分重叠/非重叠用户分别看指标；重叠用户比例低时更要注意“桥太窄”带来的多样性塌缩。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：跨域推荐常通过源域和目标域共享的重叠用户传递知识，该桥能提升精度，但其对推荐多样性的影响此前不清晰。文章识别出两个瓶颈：一是桥太窄，重叠用户覆盖的目标域口味有限；二是桥太响，共享信号会淹没非重叠用户稀疏的个人证据。

**方法**：提出 DivCDR，一个 model-agnostic 的 Push-Pull 框架。Pull 模块为重叠用户构造 confidence-gated virtual positives，并优化 exposure-entropy gain，从而拓宽桥所携带的偏好；Push 模块使用 overlap-density-guided negative sampling，将非重叠用户表示从重叠密集区域推开。该框架可叠加在多种 CDR backbone 上。

**结果**：在三个数据集和五种代表性 CDR backbone 上，DivCDR 提升推荐多样性，并在多数设置下保持或提升 accuracy；实现已公开。
