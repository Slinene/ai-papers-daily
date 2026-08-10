---
title: Rhetorical-Role-Aware Retrieval-Augmented Generation for Legal Question Answering
  over Indian Supreme Court Judgments
title_zh: 修辞角色感知的领域RAG：面向印度最高法院判决的法律问答
authors:
- Sayed Ayaan Ahmed Sha
- Sangeetha Sivanesan
- Anand Kumar Madasamy
- Navya Binu
affiliations:
- National Institute of Technology, Tiruchirappalli
- National Institute of Karnataka, Surathkal
arxiv_id: '2608.06828'
url: https://arxiv.org/abs/2608.06828
pdf_url: https://arxiv.org/pdf/2608.06828
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: 领域增强RAG · 修辞角色分块
tags:
- RAG
- Rhetorical Chunking
- Hybrid Retrieval
- Query Rewriting
- Legal QA
- Domain Adaptation
one_liner: 提出修辞角色分块、混合检索与查询改写的领域RAG框架，提升法律多轮问答的上下文召回与答案相关性
practical_value: '- **修辞角色分块可迁移至电商内容理解**：对商品标题、详情、评论按修辞角色（属性、评价、场景）分块，提升检索与生成相关性。

  - **多轮查询改写增强对话Agent**：利用历史与意图分类进行查询改写，可解决电商导购、客服场景中的指代消解与意图漂移。

  - **结构感知提升专业领域检索**：提取文档中的实体（如法官姓名）类似电商中的品牌、规格，可作为稀疏特征加入检索或重排序。

  - **混合检索与交叉编码器重排序**：在商品搜索或推荐Agent中直接复用，融合稠密与稀疏检索信号，再用交叉编码器精排，成本可控且效果提升明显。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：印度最高法院判决书结构复杂、术语密集，通用RAG难以精准定位相关段落，多轮对话下的意图理解尤其困难，需要领域特定优化。

**方法**：提出修辞角色感知的RAG框架，核心包括：（1）**修辞角色分块**——按文档中的论证、事实、裁决等语义角色拆分，而非固定窗口；（2）**混合检索**——融合稠密与稀疏检索结果，增强覆盖；（3）**交叉编码器重排序**——进一步精排候选块；（4）**多轮对话管理**——利用对话历史、查询分类与改写处理指代与意图变迁；（5）**结构感知**——提取法官姓名等元数据，作为附加信号辅助检索。

**结果**：使用DeepEval评估，在上下文召回和答案相关性等指标上表现强劲，验证了领域适配对法律问答有效性的重要提升。
