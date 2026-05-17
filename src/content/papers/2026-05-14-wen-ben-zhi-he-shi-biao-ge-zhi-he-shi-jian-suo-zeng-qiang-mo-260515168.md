---
title: 'Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented
  Multimodal Alignment'
title_zh: 文本知何事，表格知何时：检索增强多模态对齐实现临床时间线重建
authors:
- Sayantan Kumar
- Shahriar Noroozizadeh
- Juyong Kim
- Jeremy C. Weiss
affiliations:
- Carnegie Mellon University
arxiv_id: '2605.15168'
url: https://arxiv.org/abs/2605.15168
pdf_url: https://arxiv.org/pdf/2605.15168
published: '2026-05-14'
collected: '2026-05-17'
category: Multimodal
direction: 检索增强多模态对齐 · 时间线重建
tags:
- Multimodal Alignment
- Retrieval-Augmented
- Timeline Reconstruction
- LLM
- Clinical NLP
one_liner: 用检索到的结构化EHR表格校准临床文本时间线，多模态对齐提升绝对时间精度并发现34.8%事件仅存于文本。
practical_value: '- 检索增强校准的思路可迁移至电商用户行为时间线构建：将非结构化评论/日志中的事件与结构化交易时间戳对齐，提升用户旅程建模精度。

  - 图结构多步流程（锚事件骨架→非中心事件相对放置→外部证据校准）可泛化为通用多模态融合范式，适用于推荐系统中异构数据的时间对齐。

  - AULTC（绝对时间标签准确度）指标可直接用于评估推荐场景下用户行为序列的时间预测质量。

  - 发现大量文本事件缺失于结构化记录，提示在生成式推荐中需重视非结构化信号的独立价值，避免仅依赖结构化数据遗漏关键行为。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：临床时间线重建中，非结构化文本语义丰富但时间模糊，结构化EHR时间精确但缺失大量临床事件。单一模态均无法完整可信地还原患者轨迹。

**方法**：提出检索增强多模态对齐框架，将重建建模为图多步过程。首先从文本中提取中心锚事件构建初始时间骨架，再放置非中心事件形成相对序列，最后从EHR表格中检索相关行作为外部时间证据进行校准，输出绝对时间戳。

**结果**：在MIMIC-III/IV的i2m4基准上，指令微调LLM结合多模态管道后，绝对时间戳准确度（AULTC）一致提升，时间一致性增强，且事件匹配率未下降。分析显示34.8%的文本衍生事件完全不存在于表格记录，证明对齐两种模态比单一来源更保真。
