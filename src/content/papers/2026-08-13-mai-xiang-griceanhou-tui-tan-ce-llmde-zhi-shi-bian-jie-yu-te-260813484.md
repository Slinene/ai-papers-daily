---
title: 'Toward a Gricean Retreat: Probing LLMs for Knowledge Boundaries and Referent
  Specificity'
title_zh: 迈向Gricean后退：探测LLM的知识边界与指称特异性
authors:
- Dananjay Srinivas
- Saksham Khatwani
- Maria Pacheco
affiliations:
- University of Colorado, Boulder
arxiv_id: '2608.13484'
url: https://arxiv.org/abs/2608.13484
pdf_url: https://arxiv.org/pdf/2608.13484
published: '2026-08-13'
collected: '2026-08-16'
category: LLM
direction: LLM知识边界与生成特异性探测
tags:
- LLM
- Hallucination
- Knowledge Boundary
- Probing
- Gricean Maxims
- Referent Specificity
one_liner: LLM内部已编码知识边界与指称特异性信号，但生成时未协调，仍倾向编造具体细节而非退回通用陈述
practical_value: '- 在商品文案生成、推荐理由或对话式电商中，对于长尾/新品等知识边界外的实体，可主动降低指称特异性：生成更通用的描述（如“某品牌运动鞋”而非具体型号），减少事实错误，提升可信度。

  - 利用论文发现：模型激活中已包含知识边界和特异性信号，可训练轻量探针或使用激活引导（steering）在解码时调整logits，对低置信度实体自动触发“通用化”策略，无需重新训练大模型。

  - 在RAG或知识增强场景中，当检索不到实体的具体信息时，可提示模型生成更笼统但真实的回复，并可将知识边界信号作为拒答或回退的触发条件。

  - 该工作为幻觉控制提供了新思路：不是直接抑制幻觉，而是引导模型退回到安全的特异性层级，这比单纯惩罚更符合合作沟通原则，可尝试作为RLHF的额外奖励信号。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM在面对知识边界外的实体时，习惯编造看似合理的细节，而非退回到更安全、更宽泛的说法。论文用Gricean合作原则解释：合作说话者在不确定指称时应在特异性层级上后退，牺牲信息量换取真实性。研究探索LLM是否具备进行这种“Gricean后退”的内部要素。

**方法关键点**：构建基于T-REx的benchmark，变化实体熟悉度（真实实体 vs 合成实体）和指称特异性（具体如城市名 vs 通用如国家/大洲）。通过探针分析模型激活，回答两个问题：(1) 激活是否编码指称是否在知识边界内；(2) 激活是否预期即将生成指称的特异性。

**关键结果**：两个问题的答案均为肯定——模型内部确实存在知识边界和指称特异性的可解码信号。但这两个信号在生成过程中并未协调：模型绝大多数情况下仍偏好生成具体指称，即使实体未知，即使被提供正确的通用替代。底层神经表征已具备Gricean后退的“底物”，但缺乏利用这些信号的生成策略。论文将此定位为Gricean alignment的第一步，即需要训练或引导目标将知识边界意识与生成时的指称特异性耦合起来。
