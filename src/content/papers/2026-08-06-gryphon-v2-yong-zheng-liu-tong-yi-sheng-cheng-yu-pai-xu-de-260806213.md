---
title: 'Gryphon-v2: One Model in Place of a Cascade - Generate-and-Rank Recommender
  with Rollout Distillation'
title_zh: Gryphon-v2：用蒸馏统一生成与排序的单模型级联替代方案
authors:
- Anna Lipkina
- Daria Tikhonovich
- Viktor Yanush
- Mariia Ulianova
- Oleg Sorokin
- Vladislav Dodonov
- Ilya Murzin
- Denis Burshtein
- Nikolay Savushkin
affiliations:
- Yandex
arxiv_id: '2608.06213'
url: https://arxiv.org/abs/2608.06213
pdf_url: https://arxiv.org/pdf/2608.06213
published: '2026-08-06'
collected: '2026-08-07'
category: GenRec
direction: 生成式推荐 · Semantic ID · 蒸馏统一级联
tags:
- Generative Recommendation
- Semantic IDs
- Knowledge Distillation
- Rollout Distillation
- Generate-and-Rank
- Unified Cascade
one_liner: 通过Rollout Distillation将高成本排序教师蒸馏到生成式推荐 Ranking 模块，单一模型替代多阶段级联并获在线收益
practical_value: '## 可借鉴点

  - **用蒸馏替代强化学习注入精排信号**：将高成本但离线可计算的 Teacher Ranker 作为监督信号，通过 MAE 蒸馏到轻量 Ranking Module，避免
  RL 的不稳定，适合稳定上线的电商/广告场景。可借鉴 Rollout Distillation：用当前 beam search 生成的候选 + 曝光日志候选双源蒸馏，对齐服务时分布。

  - **统一生成与排序的共享编码器架构**：用户历史编码一次，既用于 SID 候选生成，也用于 item 级排序，大幅减少推理延迟。在电商推荐中，可复刻此设计：用轻量
  cross-attention Ranking Module 对生成候选打分，完全省去独立精排模型。

  - **候选预算与 beam 截断策略**：生成 SID 候选后通过碰撞类扩展，并用 item 预算（如 1200）截断低分 beam 候选；该机制在保证召回的同时严格控制精排候选集大小，适合在线延迟敏感的业务。

  - **Teacher Ranker 可按需扩大容量**：Teacher 模型可上线级不可用（如 8000 事件长历史），但蒸馏后可用 2048 事件 student
  实现 4 倍吞吐，节省 GPU；电商业务可训练一个超大排序模型作为 teacher，蒸馏到线上轻量模块。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业推荐系统通常由多级级联构成（候选生成、预排、精排），带来重复用户历史处理、复杂特征工程和多阶段服务开销。Semantic ID 生成式检索可简化流程，但仅依赖下一项预测无法捕捉生产排序目标的细粒度偏好。现有方案通过 RL 后训练或统一生成-排序架构部分解决，但前者不稳定，后者缺乏精准排序监督。

## 方法关键点
- **统一架构**：沿用 Gryphon 的共享编码器 + 自回归 SID 解码器 + item 级 Ranking Module。编码器仅运行一次，SID 解码器生成候选集，Ranking Module 利用相同编码状态对候选打分。
- **Rollout Distillation**：使用一个训练时仅用的 Teacher Ranker（大模型，离线验证优于生产排序器，但无法在线服务）作为监督，蒸馏到 Ranking Module。Teacher 对两类候选打分：① 当前 decoder 在训练步同步生成的 rollout 候选（占蒸馏候选 90%+），② 曝光日志候选。蒸馏损失为多任务 MAE，每个候选源归一化后等权重组合。
- **候选生成与解析**：SID 基于分层码本，束搜索生成 1024 个有效 SID，碰撞类扩展后通过 item 预算（1200）截断低分束，最后用 Ranking Module 的多目标加权分排序。

## 关键实验
- 数据集：Yandex Music 大规模音乐推荐服务两周交互日志，时序分割。
- 基线：纯生成检索（按束分排序）、Gryphon（用下一项监督训练 Ranking Module）。
- 离线结果：Gryphon-v2 保持 R@1000 持平（0.8615），TeacherRecall@10 从 0.04 提升至 0.5654，WPA 从 0.5528 提升至 0.5892，恢复与生产排序器差距的 59%。
- 在线 A/B：单一 Gryphon-v2 模型替代 15+ 候选生成器、预排、精排的整个级联，活跃用户数提升 +1.41%，总收听时间 +1.62%，点赞 +7.12%，延迟相当。

> 核心结论：通过在生成式推荐内部蒸馏大 Teacher 的排序知识，可以既保持生成召回又获得精排级准确性，实现单一模型端到端替换多级级联，并获得在线指标收益。
