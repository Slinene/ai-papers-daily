---
title: 'Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling'
title_zh: 分层稀疏注意力HiLS：端到端分块选择实现无限上下文建模
authors:
- Xiang Hu
- Xinyu Wei
- Hao Gu
- Minshen Zhang
- Tian Liang
- Huayang Li
- Lei Zhu
- Yan Wang
- Sirui Han
- Yushi Bai
affiliations:
- Tencent HY Team
- ShanghaiTech University
- The Hong Kong University of Science and Technology
- University of California, San Diego
arxiv_id: '2607.02980'
url: https://arxiv.org/abs/2607.02980
pdf_url: https://arxiv.org/pdf/2607.02980
published: '2026-07-02'
collected: '2026-07-08'
category: LLM
direction: 分层稀疏注意力 · 超长上下文外推与高效推理
tags:
- Sparse Attention
- Long Context
- Extrapolation
- End-to-End Learning
- Efficient Inference
- Hierarchical Landmark
one_liner: 提出HiLS Attention，端到端学习分块选择的分层稀疏注意力，推理加速且外推超64倍训练长度
practical_value: '- 在电商推荐的长用户行为序列建模中，可借鉴HiLS的分块检索与端到端选择机制，自动关注关键历史块，突破全注意力计算瓶颈，同时保持预测性能。

  - 对于RAG或Agent长上下文场景，分层地标（landmark）压缩文档/对话历史，实现高效检索式注意力计算，既能大幅降低KV缓存，又能外推到极长序列，适合在线长对话或长文档问答。

  - HiLS提供全注意力模型的轻量级继续预训练转换方案，已有模型（如推荐系统、对话模型）只需少量训练即可获得超长上下文能力和推理加速，便于业务快速升级。

  - 推理时只缓存被选中的分块KV，降低解码内存和延迟（预填充加速9.3x，解码加速15.7x），适合在线服务对长序列实时响应的要求。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：稠密注意力平方级计算和有限长度外推制约LLM长上下文应用。分块稀疏注意力可降低计算，但现有方法因分块选择不准确而性能不及全注意力。

**方法**：提出HiLS Attention，将注意力分层分解：每个query与检索到的分块独立计算，输出通过可学习的块检索分数融合。检索分数直接参与前向计算，受语言模型损失端到端优化，实现原生稀疏训练。分块选择基于可学习的landmark表征，压缩块信息以估计相关性。

**关键结果**：HiLS-Attention在训练长度内性能与全注意力持平或更优；可外推至训练长度的64倍以上，长上下文检索准确率达90%；全注意力模型仅需50B token继续预训练即可转换为HiLS-Attention，在LongBench长短任务上保持性能，在超长任务上大幅超越基线，同时预填充速度提升9.3倍，解码速度提升13.5–15.7倍。
