---
title: Training-Free Token-Level Steering for LLM Personalized Co-Writing
title_zh: 免训练的Token级引导框架：大模型个性化协同写作
authors:
- Wenhao Mao
- Chengbin Hou
- Weixiao Wang
- Jialiang Zhu
- Min Liu
- Yibin Hao
- Hairong Lv
affiliations:
- Tsinghua University
- Fuyao University of Science and Technology
- Henan Provincial People’s Hospital
arxiv_id: '2608.06069'
url: https://arxiv.org/abs/2608.06069
pdf_url: https://arxiv.org/pdf/2608.06069
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: 训练免token级引导 · 个性化写作
tags:
- training-free
- token-level steering
- personalization
- co-writing
- domain adaptation
- LLM
one_liner: 提出免训练的token级引导方法，在小数据集上实时控制LLM生成，显著降低人工编辑量
practical_value: '- 在商品标题/广告文案生成中，可借鉴 token 级引导快速适配专业领域，无需频繁微调大模型，降低算力与维护成本

  - 针对小样本商品类目（如新品），该框架基于小数据集构建引导，能有效捕捉细分用语风格，提升个性化文案质量

  - 工程上可将领域知识（如商品属性、组合搭配）编码为 token 偏置，作为轻量插件接入现有文本生成流程

  - 方法不依赖梯度更新，适合在频繁变化的电商环境中实时注入最新促销信息、季节热词等'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在专业领域缺乏领域知识，微调成本高且难以跟上频繁更新的数据；RAG 虽免训练却无法提供 token 级别的细粒度控制。现有协同写作多限于代码领域，缺乏面向专业个性化的高效方案。

**方法关键点**：提出 SteerWrite，一个免训练的 token 级引导框架。它无需修改模型参数，而是在推理时动态调整下一个 token 的概率分布，将外部专业知识注入生成过程。框架专为小数据集设计，能有效适应稀疏样本场景，通过 token 级别的实时干预使输出贴合特定领域和个性化需求。

**关键结果**：在多个数据集、不同评价指标及多种基础模型上均达到 SOTA 性能，大幅减少了人工后编辑的工作量，验证了免训练 token 级引导在个性化协同写作中的有效性和通用性。
