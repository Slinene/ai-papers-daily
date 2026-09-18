---
title: 'Learn Your Own Thoughts: Abstract Token Curriculum'
title_zh: 学习自己的思考：抽象 Token 课程
authors:
- Khashayar Gatmiry
- Avrajit Ghosh
- Parsa Mirtaheri
- Jason D. Lee
- Nika Haghtalab
- Emmanuel Abbe
- Peter Bartlett
affiliations:
- UC Berkeley
- UC San Diego
- EPFL
- Google DeepMind
arxiv_id: '2609.19717'
url: https://arxiv.org/abs/2609.19717
pdf_url: https://arxiv.org/pdf/2609.19717
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: 课程学习训练隐式思维表示
tags:
- Abstract Token Curriculum
- curriculum learning
- chain-of-thought
- continuous thoughts
- reasoning
- LLM training
one_liner: 提出抽象 Token 课程（ATC），无需显式思维链监督，通过课程学习在连续表示空间形成内部抽象思考
practical_value: '- 在训练推荐/Agent 的规划与推理能力时，可采用课程学习思路：按任务难度（如多跳路径长度、图规模、算术复杂度）从易到难组织样本，让模型在连续隐藏状态中隐式形成推理步骤，省去逐条标注
  CoT 的成本。

  - 若业务需要多步推理但显式 CoT 延迟高或标注贵，可尝试在 Transformer 中间层引入可训练的抽象 token，配合渐进课程，将中间推理压缩到连续表示空间，降低推理时的
  token 开销。

  - 理论分析提示注意力会自然聚焦于上下文中提供“最容易路径”的 token；构造课程样本时可在早期保留关键捷径 token，帮助模型更快收敛，后期再逐步移除捷径以强化内部推理。

  - 当前验证集中在图可达性与算术任务，属理论性实验；迁移到大规模电商/推荐场景前，需要先在真实多跳推理任务上做小规模验证。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：LLM 借助思维链（CoT）提升推理能力，但 CoT 需要显式监督中间思考 token，依赖大量任务特定数据，标注成本高。现有连续思考训练方法仍缺乏有效引导。

方法关键点：ATC（Abstract Token Curriculum）通过一系列分布逐步增加问题复杂度，训练模型在连续表示空间中形成内部抽象“thought”，无需直接监督或手工 scratchpad 设计。理论部分证明，在单层 softmax attention 学习 parity 函数时，ATC 使注意力自然聚焦于上下文中提供“最容易路径”的 CoT token。实验在 graph reachability 和 arithmetic learning 任务上进行。

关键结果：ATC 在两个任务上均展现有效性，并优于先前训练连续思考的方法；理论分析解释了注意力聚焦机制，说明模型会利用上下文中更易预测下一步的 token 作为隐式推理路径。
