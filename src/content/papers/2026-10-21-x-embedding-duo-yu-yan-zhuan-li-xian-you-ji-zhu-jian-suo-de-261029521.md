---
title: 'X-Embedding: Two-Stage Training for Multilingual Patent Prior-Art Retrieval'
title_zh: X-Embedding：多语言专利现有技术检索的两阶段训练框架
authors:
- Wentao Wu
- Xu Wang
- Linqing Chen
- Fenhong Zhu
- Hanmeng Zhong
- Yuanxiang Huangfu
affiliations:
- Patsnap
arxiv_id: '2610.29521'
url: https://arxiv.org/abs/2610.29521
pdf_url: https://arxiv.org/pdf/2610.29521
published: '2026-10-21'
collected: '2026-10-25'
category: RecSys
direction: 检索排序 · 两阶段训练
tags:
- retrieval
- embedding
- two-stage training
- Matryoshka
- multilingual
- hard negatives
one_liner: 提出两阶段训练框架 X-Embedding，先做专利结构与多语言对齐预训练，再用 X 类引用微调，64 维 Hit@100 达 89.09%
practical_value: '- 两阶段训练：先做领域/结构对齐的预训练（如商品标题、描述、属性、用户评论等多视图对齐；跨语言商品对齐），再做任务微调，比直接
  SFT 提升显著（+3.19 Hit@100），在低资源语言上增益更大。

  - hard negatives 构造：用检索候选和弱相关（A 类）作为负样本，提升区分度；推荐系统可用曝光未点击、同类目但低相关、历史负反馈物品作为 hard
  negatives。

  - Matryoshka 表示学习：一个模型输出 64/1024 维 embedding，低维保持高精度（89.09%），便于线上存储和检索成本控制，推荐召回可动态调整向量维度。

  - 多语言对齐：对齐不同语言家族成员，可扩展到跨境电商/多语言用户场景，用跨语言正样本对增强语义一致性。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：多语言专利现有技术检索需要识别 X 类引用（单独影响新颖性/创造性），不仅跨语言还跨文档视图，要求超越主题相似性。

方法：X-Embedding 两阶段框架。第一阶段专利域表示学习：对齐专利内部互补章节（如权利要求、说明书）和不同语言专利家族成员对应章节，学习专利结构和多语言表达。第二阶段任务适配：用审查报告 X 引用作为正样本，从检索候选和 A 类引用中采负样本，优化 X 类相关性排序。使用 Matryoshka 表示学习（MRL）在一个模型内提供 64 和 1024 维 embedding。

关键结果：在包含中英日三种语言、四种查询视图的评测集上，64 维嵌入总体宏观 Hit@100 达 89.09%，超过 Qwen3-Embedding-0.6B 和 RoBERTa 分别 21.25 和 3.68 个百分点。在相同第二阶段训练与评测条件下，两阶段训练比直接监督微调提升 3.19 个百分点，英文和日文分别提升 5.34 和 4.72 个百分点，12 个语言-视图组合中有 9 个更高；Hit@10 和 Hit@20 分别提升 3.71 和 3.79 个百分点。验证了先专利域适应再任务适配的顺序训练对提升 X 类检索有效。
