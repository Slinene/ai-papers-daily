---
title: 'CERA-MoA: Co-Evolving Routing Mechanisms with Continually Learning LLM Agents'
title_zh: CERA-MoA：路由与持续学习智能体协同演化框架
authors:
- Jiaxuan Jiang
- Liyuan He
- Zhixuan Fang
affiliations:
- IIIS, Tsinghua University
- School of Artificial Intelligence, Shanghai Jiao Tong University
- Shanghai Qi Zhi Institute
arxiv_id: '2609.18779'
url: https://arxiv.org/abs/2609.18779
pdf_url: https://arxiv.org/pdf/2609.18779
published: '2026-09-16'
collected: '2026-09-17'
category: MultiAgent
direction: 多智能体路由与持续学习协同
tags:
- Mixture-of-Agents
- Routing
- Continual Learning
- Reinforcement Learning
- LLM Agents
one_liner: 提出 CERA-MoA，让 MoA 中动态路由器与智能体策略通过强化学习协同演化，并用隐藏状态预测熟悉度实现高效路由
practical_value: '- 在电商/搜索的多智能体架构中，路由策略不应固定：可借鉴 CERA-MoA 让 router 与专家 agent 在线/离线同步更新，将用户
  query 分发逻辑与各领域专家（如类目导购、价格对比、营销文案）的真实能力变化对齐。

  - 用中间层隐藏状态做“熟悉度”估计，避免完整 rollout 才能判断 agent 是否适合处理某类请求；实际在线系统可训练 lightweight 打分器，毫秒级实现动态路由和成本控制。

  - 累积阈值激活最小 agent 子集，可移植到集成推理/多模型打分场景，按 query 难度动态调用 1~N 个模型，在效果与 latency/成本间自动权衡。

  - 按 evolving competence 主动分配训练样本可促进专家差异化，适合多领域商品推荐或意图分类中的专家持续训练，防止 cold-start 和同质化。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**

当前 Mixture-of-Agents (MoA) 把 query 路由与 agent 微调割裂：路由策略无法适配 agent 训练后的能力变化，agent 也难以形成数据驱动的专门化，导致多智能体系统在复杂任务上的泛化瓶颈。

**方法关键点**

提出 CERA-MoA，一个迭代强化学习框架，让动态路由器与独立 agent 策略协同演化。

- 设计 **predictive familiarity estimator**：利用中间层隐藏状态评估各 agent 对当前 query 的语义胜任度（familiarity score），避免完整 rollout 的高开销。
- 基于 familiarity scores，采用 **cumulative-threshold adaptive routing**：动态激活一个定制的最小 agent 子集，在任务效果与计算效率之间取得平衡。
- 根据 agent 不断变化的能力，主动分配针对性训练样本，促进能力差异化，实现数据驱动的专门化。

**关键结果**

在多个领域的实验中，CERA-MoA 显著优于静态 agent 路由和固定工作流微调等 state-of-the-art 基线，验证了路由与智能体共同演化对多智能体系统的收益。
