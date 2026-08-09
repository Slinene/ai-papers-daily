---
title: 'The Price of Isolation: Estimating the Ecosystem Cost of Symmetric Two-Sided
  A/B Testing'
title_zh: 隔离的代价：对称双边A/B测试的生态成本估算
authors:
- Yuanyuan Shen
- Yiren Yan
- Wenjie Li
- Chunhui Zhu
affiliations:
- Snap Inc.
arxiv_id: '2608.04432'
url: https://arxiv.org/abs/2608.04432
pdf_url: https://arxiv.org/pdf/2608.04432
published: '2026-08-05'
collected: '2026-08-09'
category: Eval
direction: 双边平台实验设计 · 极端值理论估算隔离成本
tags:
- A-B testing
- two-sided platforms
- marketplace interference
- extreme-value theory
- recommender systems
- experimentation
one_liner: 揭示双边平台隔离实验中，匹配质量重尾分布导致生态成本恒定不随规模消失，并提供预检程序
practical_value: '- 在电商/广告等双边市场进行隔离实验（如对部分卖家和买家分桶）时，需提前评估匹配质量分布的尾部特性：若为重尾，隔离造成的用户参与度损失不会随池子增大而消失，必须纳入预算。

  - 可借鉴预检流程：先在小规模探索数据上校准尾指数，利用论文公式预估隔离损失，若超过容忍阈值，改用单边消融或其它替代设计，避免无谓的生态伤害。

  - 将隔离视作有成本的实验方法，类似多臂老虎机的探索成本，实验平台应提供工具自动估算并展示预期损失，帮助团队做实验设计决策。

  - 对于推荐系统的冷启动实验或创作者侧实验，该方法可直接迁移：通过A/A测试量化隔离带来的参与度降级，并基于极值理论外推至全量场景。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：双边内容平台常采用对称隔离实验（如将创作者和观众成比例分割到独立子市场）以消除干扰，但直觉认为随着平台规模增大，隔离导致的候选内容变少、参与度下降应可忽略。本文质疑这一直觉，通过次序统计量建模发现，实际规律取决于匹配质量的尾部形态。

**方法关键点**：构建基于次序统计量的用户参与度模型，用户消费其候选池中匹配质量最高的内容。应用极值理论，推导出尾类损失定律：轻尾或有界尾分布下，损失随候选池大小增长而渐近消失；重尾分布（如Pareto尾）下，损失收敛到一个与候选池规模无关的正常数，即使池子扩大几个数量级也无法消除。

**关键结果**：在一个千万级创作者的平台上进行两项生产实验验证。纯A/A流量扫掠显示，隔离程度越深（更小比例分割），用户参与度指标显著下降。单边目录消融实验证实，仅减少每用户可触达的内容池便会导致参与度损失。用小规模探索数据校准尾指数，预测的全量目录消融效应与实际观测一致。据此，论文给出预检流程：实验前估算损失、分配流量、设定容忍度，并推荐备用方案。
