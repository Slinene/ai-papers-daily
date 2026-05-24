---
title: 'Scene Abstraction for Lexical Semantics: Structured Representations of Situated
  Meaning'
title_zh: 场景抽象：词汇情境化意义的结构化表示
authors:
- Yejin Cho
- Katrin Erk
affiliations:
- University of Texas at Austin
- University of Massachusetts, Amherst
arxiv_id: '2605.22542'
url: https://arxiv.org/abs/2605.22542
pdf_url: https://arxiv.org/pdf/2605.22542
published: '2026-05-21'
collected: '2026-05-24'
category: LLM
direction: 基于LLM的词汇场景结构化表示
tags:
- lexical semantics
- scene abstraction
- few-shot prompting
- structured representation
- dataset
- word meaning in context
one_liner: 用LLM少样本提示从语境中提取结构化场景，捕捉词语的情境、属性和情感关联
practical_value: '- 在商品搜索和推荐中，对查询词和商品描述进行场景抽象（事件、实体、氛围、情感），可构建超越纯文本匹配的语义索引，提升长尾查询与相关商品的关联度。

  - 对话Agent在理解用户意图时，可利用场景轮廓（如“独自喝咖啡”的场景轮廓：专注、提神、清晨）生成更贴合情境的回应，避免字面匹配导致的答非所问。

  - 生成式推荐的理由生成可借鉴Expression Profile模块，将商品的场景化属性（如“静谧的冬夜”、“喜庆的节日氛围”）融入推荐文案，增强情感共鸣。

  - 构建领域场景知识库（如将电商类目top关键词的场景预先抽象并向量化），可以冷启动实时场景解析，直接用于召回或重排阶段的特征增强。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：传统词汇表示（如词向量、词典定义）忽略了词语在具体语境中唤起的情景、氛围和情感关联（如“咖啡”常关联清晨专注、提神，“乌鸦”关联寂静、不祥）。这些情境化维度对真实语言理解至关重要，却长期隐含未建模。

**方法**：提出Scene Abstraction框架，将词语在一个语境中的“场景”定义为两部分：**Contextual Scene**（事件、实体、背景氛围）和**Expression Profile**（该词参与的事件、可泛化属性、唤起的情感）。通过LLM（gpt-4o-mini）的少样本提示，从单句语境中自动提取结构化场景。基于COCA语料库，为26个关键词构建了520个使用实例的数据集COCA-Scenes。

**关键结果**：1）场景识别任务中，人类观察者能以82.4%的准确率从四个候选场景中选出文本对应的场景，比纯文本嵌入基线高11.8个百分点，表明场景表示捕获了文本中隐含的情境结构；2）场景轮廓（Expression Profile）与人类对词语在语境中的解读一致性达86.4%，显著优于基于ATOMIC知识图谱的基线，证明了结构化场景轮廓的有效性。
