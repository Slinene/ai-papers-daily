---
title: 'CoSimRec: Measuring Coordinated-Content Penetration in Recommender Feedback
  Loops'
title_zh: CoSimRec：测量推荐反馈环中协同内容渗透的闭环保真评估框架
authors:
- Nan Li
- Jiahong Shao
- Jiuyang Lyu
arxiv_id: '2607.15114'
url: https://arxiv.org/abs/2607.15114
pdf_url: https://arxiv.org/pdf/2607.15114
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 推荐系统鲁棒性 · 反馈循环评估
tags:
- Coordinated-Behavior
- Feedback-Loop
- Agent-Based-Simulation
- Recommendation-Robustness
- Offline-Evaluation
one_liner: 提出基于智能体的闭环模拟框架与渗透率指标族APR，量化协调攻击通过反馈循环放大对非机器人用户的影响
practical_value: '- 电商/广告推荐中常见水军、刷单、炒信等**协调攻击**，本文的渗透率指标（APR-Lift）可直接迁移为业务安全评估指标，衡量不当内容通过反馈循环污染正常用户流量的程度。

  - 框架采用**智能体模拟非机器人用户的响应**，可替换为业务内真实的用户行为模型，离线复现“攻击→推荐→用户反馈→再推荐”的闭环，提前评估召回/排序策略的脆弱性。

  - 实验表明**基于流行度或反馈敏感的排序算法更容易放大渗透**，而同步感知的防御策略（如降低近期互动权重）能一致降低APR，可直接作为排序层加固策略的参考。

  - 闭环评估设计强调了**曝光分配与行为反馈的耦合**，建议在线上AB测试前先用此类工具评估新策略面对恶意协同时的风险，避免仅用静态攻击测试产生盲目乐观。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统推荐系统鲁棒性研究仅关注静态排名变化，忽略了攻击、推荐和用户响应在闭环中的相互放大效应。协同攻击对非机器人用户的影响需要新的度量与评估范式。

**方法关键点**：
- 提出 **CoSimRec**，一个基于智能体的离线模拟框架，同时模拟协同机器人账号、动态排序算法、非机器人用户响应及排序干预，构成闭环反馈。
- 设计 **APR（Algorithmic Penetration Rate）** 指标族：目标内容在非机器人曝光与互动中的份额、相对于无攻击基线的提升（APR-Lift）、以及单位协同互动的曝光增益（APR-Exposure per Interaction）。
- 实验覆盖随机、流行度、反馈敏感、MF、BPR-MF 等推荐器，在 MIND、MovieLens、LastFM 三数据集上运行，并采用十种子推断和最多 1000 用户的人群规模实验。

**关键结果**：
- 随机控制组未显示统计显著的渗透；流行度和反馈敏感排序在所有六个数据集-推荐器组合中产生了显著的正 APR-Lift，LastFM 上最高达 0.4505。
- 采用同步感知的防御策略（如调整时间窗口）在所有防御设置中均降低了 APR。
