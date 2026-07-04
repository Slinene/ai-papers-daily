---
title: 'ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning'
title_zh: 递归证据重放：提升LLM长上下文推理的免训练方法
authors:
- Yanjun Zhao
- Ruizhong Qiu
- Tianxin Wei
- Yuanchen Bei
- Zhining Liu
- Lingjie Chen
- Ismini Lourentzou
- Hanghang Tong
- Jingrui He
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.02509'
url: https://arxiv.org/abs/2607.02509
pdf_url: https://arxiv.org/pdf/2607.02509
published: '2026-07-02'
collected: '2026-07-04'
category: Reasoning
direction: 长上下文推理 · 证据重放增强
tags:
- Long-Context Reasoning
- Evidence Replay
- Training-free
- Attention Relevance
- Inference Optimization
one_liner: 通过递归选择与问题相关的上下文证据并重放，无需训练即提升LLM长上下文推理的证据利用率
practical_value: '- 可将ReContext集成到现有LLM推理管线，用于处理长用户对话历史、多文档召回等场景，无需额外训练或外部存储。

  - 在搜索推荐Agent中，当需要从大量上下文（如用户长期行为日志、多篇商品评论）抽取关键证据时，使用递归重放可显著提升LLM回答相关问题的准确性。

  - 方法基于模型自身的注意力分数选择证据，可适配不同LLM架构，避免了硬截断上下文带来的信息丢失，适合在端侧或低资源推理中应用。

  - 理论框架将上下文视为联想记忆存储体，对优化检索增强生成（RAG）系统的内部证据利用机制有启发，可指导设计更有效的上下文选择策略。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：
现有LLM即使支持128K上下文窗口，仍常常忽略上下文中已存在的相关证据，导致长上下文推理能力不足。需在不增加训练成本的情况下，提升模型对长上下文中证据的利用效率。

**方法关键点**：
ReContext是一种免训练的推理时方法，通过递归证据重放增强LLM长上下文推理。具体过程：①利用模型自注意力权重计算每个上下文token与查询问题的相关性并排序；②递归迭代选择与查询最相关的token，构建证据池；③在最终生成答案前，将证据池插入上下文重放，同时保留完整原始上下文，不进行任何修剪。该方法将证据组织与答案生成分离，无需外部记忆或额外训练。理论上，模型被视为联想记忆体：上下文是记忆痕迹，问题是检索线索，注意力是线索-痕迹关联，重放是痕迹再激活。

**关键结果**：
在8个涵盖多文档问答、长对话等任务的长上下文数据集上测试（上下文长度128K），在Qwen3-4B、Qwen3-8B和Llama3-8B三个模型上均取得最佳平均排名，显著提升了证据利用率。分析表明，仅需0.1%的上下文token（128个）就能覆盖约50%-80%的累积相关性得分，表明少量关键证据即可支撑推理。
