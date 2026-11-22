---
title: A Statistical Framework for Training Data Auditing of Large Language Models
title_zh: 大语言模型训练数据审计的统计框架
authors:
- Shengjie Niu
- Yeheng Ge
- Jian Huang
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2611.26264'
url: https://arxiv.org/abs/2611.26264
pdf_url: https://arxiv.org/pdf/2611.26264
published: '2026-11-19'
collected: '2026-11-22'
category: Eval
direction: LLM 训练数据审计 · 成员推断
tags:
- training data auditing
- membership inference
- Cauchy combination
- multiple testing
- FDR control
- LLM
one_liner: 统一统计框架，用Cauchy组合聚合chunk级证据做文档级成员推断，并控制全局审计与子集识别的错误率
practical_value: '- 在LLM微调电商推荐文案或搜索改写模型时，可将用户评论、商品描述等长文本切分chunk做成员推断，再用Cauchy组合得到文档级p值，避免局部泄露信号被稀释，适合审计特定商品/用户数据是否进入训练集。

  - 对一批候选商品、商家广告文案或评测集做合规审计时，可复用其校准后的文档p值 + 多重检验（FDR控制）识别可疑子集，控制误报；能迁移到“模型是否偷记竞品文案/平台敏感数据”的场景。

  - 框架不依赖重采样，Cauchy组合计算轻量，适合大规模语料预训练/微调审计，可作为LLM上线前的数据合规检查环节。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：LLM训练数据不透明，审计特定数据是否被用于训练对隐私、版权、基准污染检测很重要，尤其是书籍、论文、合成文本、医疗QA等。训练成员信号可能集中在长文档的少数片段，需要文档内聚合且不稀释局部信号；审计目标集合则需要整体判断。

方法关键点：提出统一统计框架，覆盖文档级成员推断、集合全局审计、可疑子集识别三个层次。具体做法是将文档切分为chunk，获取互补的chunk级成员证据，用Cauchy组合构造文档分数；文档分数及其校准后的p值再用于全局审计与可疑子集识别（多重假设检验）。在可交换条件下，文档级p值具有有限样本有效性，全局审计控制type-I error，子集识别控制FDR。

结果：在BookTection、Pile-arXiv、Cosmopedia、HealthCareMagic四个案例上验证了框架在预训练和微调数据审计中的有效性与可靠性。
