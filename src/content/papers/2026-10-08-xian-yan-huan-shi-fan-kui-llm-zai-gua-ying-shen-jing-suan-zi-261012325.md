---
title: Prior or Feedback? What an LLM Uses When Adapting Neural Operators
title_zh: 先验还是反馈？LLM 在适应神经算子时依赖什么
authors:
- Julian Chan
- Javier Mora Jimenez
affiliations:
- University of Surrey
- Compare the Market
arxiv_id: '2610.12325'
url: https://arxiv.org/abs/2610.12325
pdf_url: https://arxiv.org/pdf/2610.12325
published: '2026-10-08'
collected: '2026-10-11'
category: Agent
direction: LLM 科学代理决策归因
tags:
- LLM agents
- scientific agents
- neural operators
- decision attribution
- hyperparameter optimization
- PDE
one_liner: 通过干预实验证明 LLM 在神经算子调参中同时依赖任务先验与实验反馈，而非仅靠初始上下文
practical_value: '- 在 LLM 驱动的超参/策略搜索中，可利用 LLM 的领域先验作为初始配置，替代随机或贝叶斯优化冷启动，提升预算有限场景下的早期性能。

  - 评估 Agent 是否真正利用反馈时，借鉴其干预设计：重排历史反馈分数、做保值重写、冷启动基线，避免只看最终指标造成虚假归因。

  - 对搜索推荐中的自动调参/模型选择，可让 LLM 根据任务描述生成候选配置，再用反馈迭代；注意先验会随任务描述变化，如学习率需随任务调整。

  - 局限：论文面向科学计算神经算子，业务可借鉴点主要在 LLM 决策归因方法和 warm-start 思路，需自行验证在电商/推荐场景的迁移效果。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 科学代理在序贯实验中是否真的根据反馈调整决策，还是只依赖初始任务描述？终端指标无法区分行为来源，需要干预实验验证归因。

**方法关键点**：
- 在神经算子微调配置选择任务中，固定 LLM 策略在有限预算内提出/修改配置，对比随机搜索与贝叶斯优化。
- 三组干预验证归因：
  1. **冷启动**：观察任何验证分数前，检查 LLM 首提案在随机搜索池中的排名。
  2. **任务敏感**：改变 PDE 描述，观察所选基础学习率是否变化。
  3. **反馈敏感**：重分配已有验证分数，观察下一提案是否改变；用保值重写作为对照。

**关键结果**：
- LLM 在 PDE 族内和跨族迁移中，几乎每个匹配比较 held-out test nRMSE 都低于随机搜索和贝叶斯优化。
- 首配置在随机搜索池中排名接近顶部，表明有任务依赖先验。
- 改变 PDE 描述会改变所选基础学习率；重分配分数每次改变下一提案，保值重写无聚合效应。

结论：LLM 结合任务依赖先验和对实验反馈的敏感性，而非仅靠初始上下文。
