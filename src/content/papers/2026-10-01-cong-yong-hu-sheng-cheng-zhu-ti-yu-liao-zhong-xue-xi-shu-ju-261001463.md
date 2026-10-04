---
title: Learning to structure data from user-generated thematic corpora
title_zh: 从用户生成主题语料中学习数据结构化
authors:
- Elishay Avram
- Oren Glickman
- Elad Yom-Tov
affiliations:
- Bar-Ilan University
arxiv_id: '2610.01463'
url: https://arxiv.org/abs/2610.01463
pdf_url: https://arxiv.org/pdf/2610.01463
published: '2026-10-01'
collected: '2026-10-04'
category: LLM
direction: LLM 驱动的语料属性 schema 自动归纳
tags:
- LLM
- Schema Induction
- Information Extraction
- Ontology
- User-Generated Content
- Cost-Accuracy Trade-off
one_liner: 用 LLM 全自动迭代发现领域属性 schema，无需预定义本体即可抽取结构化数据
practical_value: '- 用户生成内容（评论、社区帖、客服对话）中自动发现隐性属性：不用预设 taxonomy，先让大模型从语料归纳候选属性，再合并语义重叠、分配结构类型，快速搭建商品/内容属性体系，适合冷启动或长尾品类。

  - 成本控制：schema 发现用大模型，值抽取用较小指令微调模型；可根据模型 scale 评估精度-成本曲线，选择合适模型，对百万级评论抽取能明显省成本。

  - 属性集在 10 轮内稳定，说明迭代流程可产品化：可周期性对新语料运行，自动维护和增量更新属性字典，减少人工梳理。

  - 结构类型分配与值抽取 F1 0.8，可用于生成推荐/搜索特征，例如抽取用户提到的具体症状、偏好、使用场景，丰富用户画像和 query 扩展。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：主题语料（社交媒体/论坛）含大量非结构化用户描述，但相关属性隐式、领域相关且事先未知，难以批量结构化。

**方法关键点**：全自动迭代框架。给定语料，LLM 诱导候选属性；顺序合并语义重叠属性；为每个属性分配结构类型（类别/数值/文本等）；据此构建本体并填充值；值抽取可换用较小 LLM，并估计相对大模型的精度损失。

**关键结果**：在 5 个健康相关 Reddit 社区，发现属性与人工标注一致率 61%，接近标注者间一致率 62%；3/5 社区在 10 轮内收敛；结构类型准确率 82%；值抽取 F1=0.80；四个 LLM 家族中，指令微调小模型性能随规模显著提升，支撑成本-精度权衡。
