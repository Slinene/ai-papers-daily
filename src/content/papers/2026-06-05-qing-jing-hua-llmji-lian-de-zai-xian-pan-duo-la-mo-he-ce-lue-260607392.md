---
title: Online Pandora's Box for Contextual LLM Cascading
title_zh: 情境化LLM级联的在线潘多拉魔盒策略
authors:
- Alexandre Belloni
- Yan Chen
- Yehua Wei
affiliations:
- The Fuqua School of Business, Duke University
arxiv_id: '2606.07392'
url: https://arxiv.org/abs/2606.07392
pdf_url: https://arxiv.org/pdf/2606.07392
published: '2026-06-05'
collected: '2026-06-08'
category: LLM
direction: LLM推理 · API级联优化
tags:
- LLM Cascading
- Online Learning
- Pandora’s Box
- Contextual Bandits
- API Selection
one_liner: 提出在线学习算法，在LLM API级联中自适应决定查询顺序和部署选择，实现~O(√T)后悔界。
practical_value: '- 在电商广告文案生成或客服多LLM服务成本优化中，可借鉴「两阶段决策」框架：先按预留指数顺序查询API生成候选，再根据下游奖励选择最优输出，无需事先知道不同API的确切质量分布。

  - 对每个API不建完整输出分布，而是直接学习上下文相关的「预留指数」函数，结合GMM型估计与UCB探索，在业务中可大幅降低参数估计负担，特别适合API频繁迭代或输出分布复杂的场景。

  - 算法保证了后悔界与上下文维度成正比，工程实现时可通过选择合适的参数化形式（如线性函数）和滑动窗更新策略，平衡实时性与收敛性，适合大规模高并发请求。

  - 在多智能体系统里分配不同能力LLM Agent处理子任务时，也能使用类似思路：动态决定调用哪些Agent、调用顺序，以及最终采纳哪个Agent的输出，从而在预算约束下最大化任务成功率。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：企业需在多个不同成本与质量的LLM API间做选择，以低成本获取高质量输出。现有级联策略往往依赖已知的API表现分布，难以适应上下文变化和在线学习。

**方法**：将问题建模为在线情境潘多拉魔盒，每个请求上下文先顺序查询API（产生成本并暴露输出），再从中选一个输出部署并观测最终奖励。不直接估计API的输出完整分布，而是参数化「预留指数」函数——传统Weitzman策略中的关键量，采用GMM式估计和UCB置信界联合学习查询策略和输出评价器。

**关键结果**：在合理假设下，策略累积后悔为维度依赖的~O(√T)，接近在线学习理论下界，证明该自适应查询-选择策略能在长期运行中逼近最优API调用方案。
