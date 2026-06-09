---
title: 'TrustMargin: Training-Free Arbitration between Parametric Memory and Retrieved
  Evidence in Large Language Models'
title_zh: 信任边际：大语言模型中参数记忆与检索证据的无训练仲裁
authors:
- Jingyan Xu
- Hong Shi
- Yi Shan
- Penghui Liu
- Yunhao Bai
- Ningyuan Li
- Xueyang Liu
affiliations:
- DCST, Peking University
arxiv_id: '2606.08397'
url: https://arxiv.org/abs/2606.08397
pdf_url: https://arxiv.org/pdf/2606.08397
published: '2026-06-07'
collected: '2026-06-09'
category: RAG
direction: 训练无关的RAG答案仲裁 · 参数记忆与检索置信度权衡
tags:
- RAG
- Arbitration
- LLM
- Parametric Memory
- Training-Free
one_liner: 提出TrustMargin，一种无训练即插即用的仲裁层，利用模型自身似然评分选择直接生成或RAG答案
practical_value: '- 在电商问答或商品知识查询中，可利用似然比（TrustMargin）自动判断直接回答与检索增强回答的置信度，无需额外训练，即插即用。

  - “参数先验边际”思想可迁移到推荐解释生成：检测模型对检索到的商品属性是否“熟悉”，避免将不常见的属性强行加入解释。

  - “证据绑定边际”提供了一种无监督的问题-证据相关性度量，可用于过滤噪声检索结果，提升 RAG 在电商客服、商品描述生成中的可靠性。

  - 该方法不依赖特定检索器，可集成到现有 RAG 流水线中，对生成式推荐的答案选择、多路召回结果仲裁具有参考价值。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：大语言模型在回答知识密集型问题时，参数记忆与检索证据均不可靠：RAG 能填补知识空白，但干扰段落可能覆盖原有正确答案。现有方法多在生成前或生成中整合信源，而本研究聚焦生成后的冲突仲裁——给定同一模型产生的直接答案和 RAG 答案，判断哪个信源更可信。

**方法**：提出 TrustMargin，一种无训练、即插即用的仲裁层，仅利用模型自身似然对两种候选答案进行评分。核心由两个边际组成：（1）参数先验边际（Parametric-Prior Margin）：测试模型参数记忆是否“接受”检索答案，若记忆赋予检索答案的似然远低于直接答案，则倾向于信任直接生成；（2）证据绑定边际（Evidence-Binding Margin）：衡量检索答案在给定问题与证据时的特异性支持，抑制仅靠段落语言模型就能推出的浅层答案。两路似然比结合后直接输出仲裁决策，无需微调、外部裁判或额外生成。

**结果**：在 2WIKIMQA 和 CWQA 两个多跳问答数据集上，使用 LLaMA-2-7B/13B 和 LLaMA-3-8B 三个规模的模型，TrustMargin 一致优于直接生成和 BM25-RAG，恢复了部分直接/RAG 预言机上界的差距，并泛化到多种无训练 RAG 管道（如 BGE-Reranker 增强检索）。
