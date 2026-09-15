---
title: Online Learning with LLM Experts from Limited Feedback
title_zh: 有限反馈下面向 LLM 专家的在线路由学习
authors:
- Wang Wei
- Soumyabrata Pal
- Koyel Mukherjee
- Franck Dernoncourt
- Ryan A. Rossi
- Branislav Kveton
- Hoda Eldardiry
affiliations:
- Virginia Tech
- Adobe Research
arxiv_id: '2609.05820'
url: https://arxiv.org/abs/2609.05820
pdf_url: https://arxiv.org/pdf/2609.05820
published: '2026-09-04'
collected: '2026-09-15'
category: LLM
direction: LLM 路由 · 在线 bandit 学习
tags:
- LLM routing
- online learning
- bandit
- limited feedback
- regret minimization
one_liner: 将多 LLM 路由建模为有限反馈 bandit，给出 full-info 与 bandit 设置下的次线性遗憾界及路由算法
practical_value: '- 在电商搜索/推荐 Agent 链路中，多个 LLM 承担意图识别、query 改写、商品文案生成等任务时，可把路由建模为上下文
  bandit：action 是候选 LLM，d 维特征直接复用现有 prompt/query embedding，reward 用点击率、转化率或人工审核通过率。

  - 反馈预算 m 通常远小于流量 T；该文的 regret 界（full-info O(dT/√m)、bandit O(dT√(K/m))）说明只需对少量流量进行人工评估或用户反馈采集，就能保证学习效率，可据此设计稀疏反馈采集机制。

  - 当候选模型能力/成本差异大且无全局最优时（文中 win rates 仅 0.073-0.319），动态路由比固定使用最强模型更优；上线前可先做离线 win
  rate 分析模型互补性，再用 bandit 路由做在线调优。

  - 若业务已有较完整的反馈日志，可先采用 full-information 变体快速冷启动；后续切换 bandit 决策降低标注成本。'
score: 7
source: huggingface-daily
depth: abstract
---

不同 LLM 能力与成本差异显著，公开数据集上多个模型 win rate 均不超 1/3，说明固定选一个模型并非最优；但实际中用户对响应质量的反馈通常缺失。该工作将 prompt 到 K 个 LLM 专家的自适应路由建模为 T 轮上下文 bandit：每轮到达一个 prompt，用 d 维特征编码，选择某个 LLM 专家，产生响应并关联未观察 reward；系统只在有限反馈预算 m≪T 下获得部分 reward 观测。

方法关键点：在 full-information 设置下，策略性地选择并观察反馈以最小化遗憾，达到 O(dT/√m)；在 bandit 设置下达到 O(dT√(K/m))。实验在多个 LLM 上验证，能从非常有限的反馈中高效学到高质量路由策略，跨模型路由优于任意单一专家。
