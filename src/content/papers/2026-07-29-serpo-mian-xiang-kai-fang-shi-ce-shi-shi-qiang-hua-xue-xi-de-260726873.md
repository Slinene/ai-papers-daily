---
title: 'SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement
  Learning'
title_zh: SERPO：面向开放式测试时强化学习的自演化评分标准策略优化
authors:
- Jianze Wang
- Kunwang Zheng
- Ying Liu
- Yu Cao
- Qilong Zhang
- Jinlong Chen
- Hua Yang
- Qianglong Chen
affiliations:
- Huazhong University of Science and Technology
- University of Science and Technology of China
- Alibaba Group
arxiv_id: '2607.26873'
url: https://arxiv.org/abs/2607.26873
pdf_url: https://arxiv.org/pdf/2607.26873
published: '2026-07-29'
collected: '2026-07-30'
category: Training
direction: 测试时强化学习 · 评分标准自演化
tags:
- TTRL
- self-evolving
- rubric optimization
- open-ended generation
- policy optimization
- LLM
one_liner: 提出自演化评分标准闭环，替代答案投票，实现开放式文本生成下的测试时强化学习，无需外部奖励
practical_value: '- 自演化评分标准（G‑N‑B 响应进化 + 评分标准进化）可在无外部奖励的条件下构建自我评估系统，适用于电商文案生成、搜索词推荐等开放式场景，自动产生质量评分并迭代提升生成质量。

  - 测试时自我进化闭环（采样→构建评分标准→评分→更新策略）可部署为线上模型的持续微调组件，例如用于推荐系统中的 query 改写或商品描述优化，全程无需人工标注。

  - 概率化评分标准（将判定 token 的似然转化为奖励）提供了一种轻量、可解释的 reward 建模范式，可直接迁移到 Agent 决策链的自我改进，降低对昂贵奖励模型的依赖。

  - 跨基准迁移进化结果表明该方法对不同领域分布有良好泛化性，可启发多任务推荐模型在无监督下自适应新品类或新场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有测试时强化学习（TTRL）依赖答案投票，无法处理开放式生成任务，因为缺乏标准答案，无法通过多数投票构造伪标签。需要一种在推理时从模型自身输出中构建可靠奖励的方法。

**方法**：提出 SERPO 闭环，共同演化响应证据、查询特定评分标准和策略参数。核心步骤：
- Good‑Normal‑Bad 响应进化：将采样响应分档为优、中、差三个存档，保持最大分离度。
- 评分标准进化：保留能区分这些存档的评分标准。
- 概率性标准评分：将标准判定 token 的似然转化为奖励信号。
- 策略优化：用该奖励更新 actor 模型。
新轮次采样刷新存档与评分标准，形成三向演化循环，全程无需外部奖励模型或更强裁判。

**结果**：在两个模型配置、两个域内基准和四个域外基准上，SERPO 在 HealthBench 和 ResearchQA 上分别提升最多 20.63 和 20.31 分，六个基准宏平均提升最多 8.06 分，且展现出跨基准迁移和持续进化能力。
