---
title: Generative Conversational Recommender System
title_zh: 生成式对话推荐系统：语义ID与结构化生成统一框架
authors:
- Sixiao Zhang
- Mingrui Liu
- Cheng Long
affiliations:
- Nanyang Technological University
arxiv_id: '2605.21987'
url: https://arxiv.org/abs/2605.21987
pdf_url: https://arxiv.org/pdf/2605.21987
published: '2026-05-21'
collected: '2026-05-22'
category: RecSys
direction: 生成式对话推荐 · Semantic ID · 结构化生成
tags:
- Conversational Recommendation
- Generative Retrieval
- Semantic ID
- Structured Generation
- LLM Fine-tuning
- Constrained Decoding
one_liner: 将对话推荐统一为自回归生成任务，通过语义ID和结构化分解实现端到端优化，召回提升达29%
practical_value: '- **语义ID替代自然语言标题**：在电商对话推荐中，可对商品建立语义ID（通过RQ-VAE量化商品文本描述），将推荐动作转化为ID生成，避免标题幻觉和词汇表爆炸。

  - **结构化生成范式**：将对话回复分解为“意图（推荐/闲聊）→ 目标商品ID → 自然语言回复”的因果依赖，可在多轮Agent中显式控制推荐决策，提升一致性和可控性。

  - **受限解码保证ID忠实性**：在推理时通过beam search约束生成有效的商品ID，杜绝“推荐不存在商品”的问题，对电商场景的幻觉控制有直接借鉴。

  - **仅微调新token的LoRA策略**：保持LLM主干冻结，只训练语义ID、模式等新引入token的嵌入，实现参数高效适配，适合业务中快速迭代多个商品库。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有对话推荐系统多采用检索式流水线，将对话理解和推荐分离优化，导致次优推荐且语言生成缺乏个性化；LLM重排序或微调方式仍依赖外部召回或存在标题幻觉、扩展性差等问题。本工作旨在完全生成式框架下统一对话与推荐，消除模块割裂。

**方法关键点**：
- 商品表示：用预训练文本编码器编码商品元数据（如标题、描述），经RQ-VAE量化为离散语义ID（4层×64码本），并通过碰撞解决确保唯一性。
- 结构化生成范式：将系统回复分解为<MODE>意图标记（REC/CHAT）、<BOI>SID<EOI>商品ID段、<RESP>自然语言回复三段，模型按此顺序自回归生成，强制解耦决策与表达。
- 训练：利用QLoRA仅微调新增token的嵌入，冻结原始LLM参数，在对话序列上做下一token预测，联合优化推荐与生成。
- 推理：可自主决定模式或外部指定，通过受限beam search搜索合法商品ID，保证生成商品存在。

**实验结果**：在ReDial和Inspired数据集上，推荐Recall@1分别达6.88%（提升21.8%）和14.56%（提升29.1%），NDCG、MRR等均显著提升；对话流畅性（PPL）大幅改善，且多样性（Distinct）在Inspired上最优。消融显示结构化生成和语义ID均关键，仅微调新token比全参数微调更优。不同LLM和编码器下性能稳健。
