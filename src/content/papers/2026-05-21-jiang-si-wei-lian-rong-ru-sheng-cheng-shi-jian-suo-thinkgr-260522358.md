---
title: 'Integrating Chain-of-Thought into Generative Retrieval: A Preliminary Study'
title_zh: 将思维链融入生成式检索：ThinkGR 初步探索
authors:
- Wenhao Zhang
- Ruihao Yu
- Yi Bai
- Zhumin Chen
- Pengjie Ren
affiliations:
- Shandong University, Qingdao, China
arxiv_id: '2605.22358'
url: https://arxiv.org/abs/2605.22358
pdf_url: https://arxiv.org/pdf/2605.22358
published: '2026-05-21'
collected: '2026-05-23'
category: RecSys
direction: 生成式检索 · Chain-of-Thought 集成
tags:
- Generative Retrieval
- Chain-of-Thought
- Multi-hop Retrieval
- Hybrid Decoding
- Reinforcement Learning
- Semantic Triples
one_liner: 首次在生成式检索中实现思考与文档ID生成交错进行，通过混合解码和检索奖励的强化学习取得SOTA。
practical_value: '- **思考-检索交错范式**：在生成式推荐中，可让模型先生成推理步骤（如需求拆解），再生成候选 item ID，缓解复杂意图与商品之间的语义鸿沟，适用于多步推理的购物场景。

  - **混合解码策略**：使用 FM-index 等约束解码保证生成的 item ID 合法，避免推荐不存在的商品，同时保留自由文本思考的灵活性，实现端到端可靠生成。

  - **检索奖励驱动的思考优化**：用业务指标（如点击率、转化率）作为奖励信号，通过 KTO 等 RL 方法优化模型思考质量，无需人工标注思考步骤，适合线上持续学习。

  - **结构化标识表示**：以知识三元组作为文档/商品 ID，增强关系推理能力，可借鉴为商品属性三元组，提升生成式推荐中的可解释性与检索效率。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有生成式检索（GR）直接将查询映射为文档 ID，缺乏中间推理过程，导致在需要多步信息跳跃的复杂查询上表现不佳。受思维链（CoT）启发，本文探索如何让 GR 模型在生成文档 ID 的同时显式地逐步思考，以缩小复杂查询与目标文档之间的语义鸿沟。

**方法关键点**：
- **语义三元组 doc ID**：将文档表示为知识三元组 (头实体, 关系, 尾实体)，使模型能通过关系追踪进行语义跳跃，并利用预训练 LLM 的语义知识进行泛化。
- **混合解码策略**：在自回归生成过程中动态切换非受限思维生成与受限 doc ID 解码。用 FM-index 保证生成的 doc ID 存在于语料库，避免幻觉，同时允许自由文本思考。
- **两阶段训练**：先用强 LLM 生成的思考-检索链进行 SFT，对齐行为；再用检索准确率作为奖励信号，通过 KTO 强化学习优化思维质量，无需人工标注。

**关键结果**：在四个多跳检索基准（HotpotQA, 2WikiMultihopQA, MuSiQue, MoreHopQA）上，ThinkGR 平均召回提升 **6.86%**，取得 SOTA；消融实验验证了混合解码和两阶段训练的必要性；在下游 QA 任务中准确率亦最高；推理延迟仅为多步 LLM 驱动检索方法的 **1/50 到 1/5**，在效率与效果间取得良好平衡。
