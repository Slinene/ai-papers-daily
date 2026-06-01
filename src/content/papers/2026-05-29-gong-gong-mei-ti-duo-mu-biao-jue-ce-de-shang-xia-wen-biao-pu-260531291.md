---
title: Contextual Scalarisation Thompson Sampling for multi-objective decisions in
  public media
title_zh: 公共媒体多目标决策的上下文标量化汤普森采样
authors:
- Théo Maëtz
- Luc Guillet
- Andrea Cavallaro
affiliations:
- Radio Télévision Suisse
- EPFL
arxiv_id: '2605.31291'
url: https://arxiv.org/abs/2605.31291
pdf_url: https://arxiv.org/pdf/2605.31291
published: '2026-05-29'
collected: '2026-06-01'
category: RecSys
direction: 上下文多目标Bandit · 动态权重学习
tags:
- Multi-Objective Bandits
- Thompson Sampling
- Contextual Bandits
- Dynamic Weighting
- Public Media
one_liner: 提出上下文多目标Bandit方法CSTS，根据情境动态学习目标权重，提升推荐与专家实践匹配度
practical_value: '- **多目标动态权重学习**：电商推荐中常需平衡点击、转化、GMV、多样性等指标，固定权重难以适应不同用户群或场景。CSTS将标量化权重建模为上下文的函数，可借鉴此思路用上下文特征（用户画像、时段、活动类型）动态调整目标偏好。

  - **模仿专家决策**：从历史专家策划数据中学习权重模式，适合需要自动化人工决策的场景，如运营选品、活动排期。可提取领域专家标注的目标权衡逻辑，减少人工调参。

  - **汤普森采样探索**：在在线学习中利用汤普森采样进行高效探索，适用于多臂老虎机场景的冷启动或策略迭代，比如Agent协作中的动作选择、流量分配等需要探索的多目标优化。

  - **业务可迁移性有限**：方法验证于公共媒体节目推荐，缺乏大规模电商场景实验，但核心思路（上下文驱动标量化 + Bandit探索）可作为多目标在线学习的组件集成到现有推荐框架中。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：公共媒体推荐需同时满足受众覆盖、文化价值、运营约束等多重竞争目标，现有方法依赖固定目标组合或帕累托优化，无法适应情境变化。专家手工策划虽灵活但不可扩展，需自动化且上下文感知的多目标决策方法。

**方法**：提出上下文标量化汤普森采样（CSTS），将多目标奖励通过标量化函数聚合为单目标，并让标量化权重成为观察上下文的函数。通过高斯过程对每个目标的奖励值建模，利用汤普森采样在上下文条件下同时探索奖励分布与权重函数，从而在不同情境下动态调整目标重要性。

**结果**：在瑞士广播公司Radio Télévision Suisse的真实节目编排数据上，CSTS相比固定权重和标准上下文Bandit基线，显著提升了推荐的上下文相关性，且决策结果更接近专家手工策划的分布，验证了自适应权重的有效性。
