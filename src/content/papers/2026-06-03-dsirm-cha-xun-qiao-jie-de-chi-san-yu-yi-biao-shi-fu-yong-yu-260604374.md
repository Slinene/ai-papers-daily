---
title: 'DSIRM: Learning Query-Bridged Discrete Semantic Identifiers for E-commerce
  Relevance Modeling'
title_zh: DSIRM：查询桥接的离散语义标识符用于电商相关性建模
authors:
- Bokang Wang
- Xing Fang
- Mingmin Jin
- Jing Wang
- Zhentao Song
- Guangxin Song
- Jianbo Zhu
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2606.04374'
url: https://arxiv.org/abs/2606.04374
pdf_url: https://arxiv.org/pdf/2606.04374
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: 搜索相关性 · 离散语义ID
tags:
- Discrete Semantic Identifiers
- Contrastive RQ-VAE
- LLM for Query Understanding
- E-commerce Search
- Relevance Modeling
one_liner: 通过查询桥接对比学习训练RQ-VAE生成相关性感知的离散语义ID，并利用LLM预测查询SID，以层次匹配分数增强排序模型
practical_value: '1. **将离散SID作为排序模型的补充特征**：物品侧用RQ-VAE离线量化成层级码，查询侧用小尺寸LLM在线生成可能的SID，通过层级前缀匹配得到一个离散匹配分数，即插即用到任意DNN排序模型中，有效弥补连续嵌入在细粒度属性区分上的不足。

  2. **查询桥接的对比量化训练**：用InfoNCE损失强制匹配的query-item对在量化空间中靠近，把无监督聚类转成有监督的搜索相关性分区，并配合类别感知的一级码本分配（按类目固定码本索引）缓解类别不平衡，这一范式可迁移至其他需要查询感知离散表示的场景（如推荐中的用户意图聚类）。

  3. **LLM解码意图多义性**：微调自回归LLM根据查询文本生成Top-K个SID，以beam search得到多条候选，显式建模查询的多义意图，再与物品SID做层级匹配，该方法可复用到查询改写、意图识别等模块，比单一向量表示更灵活。

  4. **离线在线混合部署方案**：物品SID预计算并存入KV缓存，查询侧对历史查询做缓存（88%流量命中），仅12%实时流量走LLM推理，0.6B模型平均延迟17.9ms，P99
  24.3ms，几乎不增加主链路耗时，为高性能系统中引入生成式LLM特征提供了低成本的工程样板。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商搜索相关性建模中，连续嵌入虽然泛化能力强，但同类目下仅在关键属性上有差异的商品在嵌入空间中过于拥挤，难以精确区分。离散语义标识符（SID）通过层级码本赋予物品结构化离散表示，但现有方法（如DSI、TIGER）多用于检索且依赖无监督聚类，缺乏查询-物品交互的显式监督，导致语义分区与搜索相关性脱节。

**方法
1. **物品SID学习（查询桥接对比RQ-VAE）**：
   - 使用预训练的双塔模型获取查询与物品的嵌入，送入共享的层次RQ-VAE（3层码本，大小分别为216/512/512）。
   - 训练时对正负样本对施加对称InfoNCE损失，强制匹配的查询-物品在量化空间拉近，使SID分配受搜索相关性驱动。
   - 为应对类目不均衡，第一层码本直接按天猫一级类目划分（216个类目对应216个码字），用EMA更新该类目码矢；后续层级由标准量化过程决定。
   - 总损失 = 对比损失 + 量化承诺损失 + 重建损失。

2. **查询SID生成（LLM微调）**：
   - 用物品SID作为监督标签，微调Qwen3-0.6B自回归模型，输入查询文本，预测对应的物品SID序列。
   - 推理时用beam search产生Top-K（K=5）条SID，显式建模查询的多重意图。

3. **SID层次匹配与排序集成**：
   - 对查询生成的K个SID与物品SID逐层比较，最深匹配层级转化为离散特征（0.0/0.25/0.5/1.0），作为新特征拼入原MLP排序模型。

**实验**
- 离线：训练数据8000万query-item对，排序用160万Qwen3-30B标注的高质量样本。DSIRM AUC 0.9356，较无SID基线提升+1.54%，优于DSI（0.9312）和TIGER（0.9323）。
- 消融：去掉对比学习AUC降0.09%，去掉类别约束降0.07%，验证各组件有效性。
- 在线A/B：UCTR +0.13%，UCTCVR +0.25%，部署后低延迟（缓存命中率88%，实时RT 17.9ms）。

**核心洞察**
“将无监督离散化转变为查询桥接的对比量化，使SID真正成为搜索相关性的结构化特征，再结合LLM解码查询多义性，是低成本提升排序细粒度区分能力的有效范式。”
