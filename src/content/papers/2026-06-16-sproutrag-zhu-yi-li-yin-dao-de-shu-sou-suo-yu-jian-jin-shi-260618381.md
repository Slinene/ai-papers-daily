---
title: 'SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document
  RAG'
title_zh: SproutRAG：注意力引导的树搜索与渐进式嵌入用于长文档RAG
authors:
- Amirhossein Abaskohi
- Issam H. Laradji
- Peter West
- Giuseppe Carenini
affiliations:
- University of British Columbia
- ServiceNow Research
arxiv_id: '2606.18381'
url: https://arxiv.org/abs/2606.18381
pdf_url: https://arxiv.org/pdf/2606.18381
published: '2026-06-16'
collected: '2026-06-23'
category: RAG
direction: RAG长文档检索 · 层级树状检索
tags:
- RAG
- Hierarchical Retrieval
- Attention-Guided Chunking
- Tree Search
- Multi-Granularity
- End-to-End Training
one_liner: 利用学习到的句子间注意力构建二叉分块树，实现无外部LLM调用的多粒度层次检索，平均信息效率提升6.1%
practical_value: '- 对于电商RAG场景（如长商品描述、用户评论聚合），可借鉴其基于句子级注意力自动构建语义树的方法，替代昂贵的LLM分块，降低索引延迟和成本。

  - 多粒度beam search在召回侧能同时捕捉细节与上下文，可应用于广告文案生成中的多尺度信息检索，提升信息覆盖度。

  - 端到端联合训练embedding与树结构的思想，可迁移到推荐系统的层级user/item表征学习，如构建多粒度的Semantic ID树，提升检索效率与效果。

  - 注意力头选择的机制暗示了在特定领域（如商品属性）可预先分析哪些注意力模式更有效，定制化剪枝或微调，避免重复推理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有RAG方法在长文档检索中面临粒度与连贯性的权衡，要么依赖昂贵的LLM进行分块或摘要，要么仅使用单一粒度扩展，造成信息丢失或成本增加。

**方法**：SproutRAG提出一种端到端的层次化框架。首先，利用预训练语言模型的句子间注意力，学习哪些注意力头与层最能捕捉语义结构，据此构建二叉分块树，将句子级片段自底向上聚合成逐渐增大的语义连贯单元，整个过程无需额外LLM调用。检索时，采用层次化束搜索，在多个粒度上召回候选，捕获跨句子的相关性。框架联合优化嵌入表示与树结构。

**结果**：在四个涵盖科学、法律、开放领域的数据集上，SproutRAG的信息效率(IE)比最强基线平均提升6.1%。相比依赖LLM分块或单粒度扩展的基线，该方法在检索质量与计算开销间取得更好平衡。
