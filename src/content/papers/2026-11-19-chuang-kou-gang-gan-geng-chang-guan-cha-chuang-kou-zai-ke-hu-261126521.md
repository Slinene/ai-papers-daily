---
title: 'The Window Lever: Longer Observation Windows Outweigh the Observed Effects
  of Data, Capacity, and Architecture in Customer Behavior Forecasting'
title_zh: 窗口杠杆：更长观察窗口在客户行为预测中压过数据、容量与架构效应
authors:
- Tara Sowrirajan
- Yanqiao Wang
affiliations:
- Amazon
arxiv_id: '2611.26521'
url: https://arxiv.org/abs/2611.26521
pdf_url: https://arxiv.org/pdf/2611.26521
published: '2026-11-19'
collected: '2026-11-21'
category: RecSys
direction: 用户行为预测 · 观察窗口长度
tags:
- customer behavior forecasting
- observation window
- sequence modeling
- long-horizon forecasting
- ablation study
one_liner: 在长周期客户行为预测中，延长观察窗口带来的提升远大于增加数据、模型容量或更换架构
practical_value: '- 在电商用户行为预测（复购、LTV、流失预警等）中，优先尝试将历史特征窗口从8周延长到16周甚至更长，可能带来 log-space
  R² +0.07~0.107 的提升，效果远超增加训练数据量或模型参数。

  - 更长窗口可覆盖最多 10% 更多的冷启动训练客户，改善对低活跃用户的预测；但窗口长度与日历覆盖存在混杂，落地时需通过匹配测试队列或特定锚点设计来控制。

  - 当资源有限时，不要盲目堆数据或换更大模型，其他杠杆（数据量、容量、架构）的观测效应量级仅 ≤0.006，比窗口效应小一个数量级，优先把窗口调长性价比最高。

  - 实验设计可借鉴其匹配测试队列方法，在同一批 customer-weeks 上比较不同窗口，避免样本偏移干扰结论。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：长周期客户行为预测中，业界常关注更多数据、更大模型和更新架构，但历史观察窗口长度往往被当作固定超参。论文在亚马逊内部数据上系统对比窗口长度与这三个杠杆的效果。

**方法关键点**：采用多个序列模型家族（含 transformer）和 ridge probe，设置 8 周到 32 周不等的观察窗口，同时控制训练数据量（1M vs 10M）、模型容量和架构。使用匹配测试队列对齐不同窗口下的 customer-weeks，并在五个公共数据集上验证方向一致性。

**关键结果**：从 8 周到 16 周窗口，log-space R² 在所有模型家族上增加 +0.070~0.107（1M 数据量下）；匹配测试队列显示该增益被低估。相比之下，数据量、容量、架构的观测效应最大仅 0.006，小一个数量级。更长窗口还能纳入最多 10% 更多及更冷启动的训练客户。但窗口长度与日历覆盖未完全分离，训练期锚点的增益在非假期保留约 72%。内部注册的四个预测中，唯一完全盲测的预测（24→32 周）失败。结论：此类任务应优先延长观察窗口。
