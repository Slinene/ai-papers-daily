---
title: Advancing Relevance Measurement with Vision-Language Models for Web-Scale Search
title_zh: 利用视觉语言模型提升网络搜索相关性评估的工业实践
authors:
- Han Wang
- Alex Whitworth
- Pak Ming Cheung
- Zhenjie Zhang
- Krishna Kamath
- Xi Chen
- Roberto Konow
- Kurchi Subhra Hazra
affiliations:
- Pinterest
arxiv_id: '2608.02446'
url: https://arxiv.org/abs/2608.02446
pdf_url: https://arxiv.org/pdf/2608.02446
published: '2026-08-03'
collected: '2026-08-04'
category: Eval
direction: 视觉语言模型 · 搜索相关性自动评估
tags:
- VLM
- Relevance Evaluation
- A-B Testing
- Stratified Sampling
- Multimodal Search
- Pinterest
one_liner: 用微调VLM替代人工标注，结合分层采样，将搜索A/B实验的MDE降低6倍且成本降至近零
practical_value: '- 用开源VLM（Qwen3-VL-4B）微调替代人工相关性标注，达到94.2%±1级一致性，可将标注成本降低超99%、周期从2天缩至2小时，适合电商/广告搜索中快速评估排序实验。

  - 分层采样设计（按查询兴趣类别×流行度分层）能大幅缩减相关性指标的方差，使MDE降低6倍（从~1.4%到≤0.25%），对检测微小却重要的排序变化极有价值。

  - 保留配对的实验组查询，用配对差异消除个体偏差，使得VLM标签的系统性误差在差值中被抵消，可作为Agent评估或多模态搜索中LLM裁判的校准手段。

  - 多语言微调通过单一多语言VLM支持非英语市场，虽相关性略降但配对差异仍稳健，可复用到跨境电商搜索的自动化评估。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
搜索相关性评价是A/B实验的关键守卫指标，但传统人工标注成本高、周期长（2天）、规模受限，导致实验只能检出大幅度的相关变化，无法捕捉细粒度的异质性处理效应。Pinterest搜索需要低成本、快速、可扩展的自动化相关性评估方案。

## 方法关键点
- **模型选择与微调**：基于Qwen3-VL系列，用约80万条人工标注的query-Pin对进行微调，预测5级相关度（1-5）。输入融合Pin图像、标题/描述、落地页文本、用户策展的Board标题和历史高互动查询等丰富多模态特征。
- **分层采样设计**：利用VLM低成本，从简易随机采样（SRS）升级为按查询兴趣类别×流行度分层的采样，配合分层估计量，大幅度降低查询间方差，从而缩小MDE。
- **配对实验评估**：抽取实验组和对照组的配对查询，分别用VLM标注后计算query级sDCG@25，取配对差异作为度量，有效消除标注偏差。

## 关键结果
- **人机对齐度**：VLM与人类标签精确匹配率82.9%，相差≤1级占比94.2%，QWK为0.507；query级sDCG平均误差<0.03，配对差异误差均值几乎为0。对比纯文本模型，VLM误差分布更集中。
- **实验敏感性**：引入分层采样与VLM标签后，MDE从1.3-1.5%降至≤0.25%，缩减约6倍，其中分层贡献了主要方差消减。
- **效率与规模**：单张A100 2小时可标注数十万对，成本降低99.98%，速度提升20倍；部署后相关性评估作业量增长4倍。
- **多语言迁移**：在法、德、巴葡市场，相关性排序系数为中等至强，配对差异误差接近0，体现跨语言可用性。

## 一句话精要
分层采样是降低MDE的关键杠杆，而微调VLM只是消除规模瓶颈的催化剂，二者结合让在线搜索实验能可靠捕捉细微的相关性变化。
