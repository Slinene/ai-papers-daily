---
title: Defensive Boosting for Online Probabilistic Forecasting
title_zh: 防御性 Boosting：在线概率预测的双重保证算法
authors:
- Georgy Noarov
- Aaron Roth
arxiv_id: '2608.13554'
url: https://arxiv.org/abs/2608.13554
pdf_url: https://arxiv.org/pdf/2608.13554
published: '2026-08-13'
collected: '2026-08-16'
category: Training
direction: 在线 boosting 概率预测与校准
tags:
- online learning
- boosting
- probabilistic forecasting
- Brier score
- adversarial sequences
- weak learning
one_liner: Defensive Booster 同时获得在线梯度 boosting 的 Brier 竞争保证与弱学习条件下的分类误差收敛保证
practical_value: '- 在线广告 CTR/CVR 预测中可将其作为轻量在线集成/校准层：只维护一个弱学习器（如 FTRL 逻辑回归或浅层 MLP）做增量更新，不保存大型集成，同时获得与
  span 最优线性组合竞争 Brier 的保证，适合高 QPS、低延迟场景。

  - 在非平稳或可能被策略对抗影响的流量中，利用其 dual view：若预测误差持续升高，mistake weights 会形成弱学习条件失败的 hard-core
  证书，可作为线上监控信号，触发模型重训、特征回补或人工排查。

  - 强自适应变体可在任意时间区间提供局部保证，适合电商大促、突发流量等剧烈分布偏移时对近期区间单独做校准，不用等待全局历史数据积累。

  - 若目标是“任意数据下不崩”和“有利条件下快速收敛”，可直接借鉴其目标设计：把 Brier 竞争和弱学习条件两个目标纳入同一在线更新，而不是单独使用在线梯度
  boosting 或在线分类 boosting。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：在线概率预测中已有 boosting 方法只能二选一——在线梯度 boosting 在任意序列上与 H 的 span 中最优预测竞争 Brier 分数，但 span 中没有准确预测时无保证；在线弱到强 boosting 在弱学习条件下分类误差趋零，但条件失效时保证很弱。需要同时获得两种保证。

方法：Defensive Booster 采用防御性预测思想，每轮只访问一个弱学习器。若随机化分类误差持续偏高，则其 mistake weights 构成平滑重加权，使所有弱假设 edge 都很低，从而事后给出弱学习条件失败的 hard-core 证书。因此，算法能在任意自适应序列上获得与在线梯度 boosting 相同速率的 Brier 竞争保证；当 transcript 满足 smooth weak-learning condition 时，Brier 分数与随机化分类误差也获得与在线分类 boosting 相同的速率保证。进一步提出强自适应变体，在每个时间区间同时满足两种保证并提供局部 hard-core 证书。算法仅需一个弱学习器，而对比的在线 boosting 基线需维护大型弱学习器集成。

结果：在合成与真实数据流上，Defensive Booster 的预测性能强，有时显著超越所有基线，运行速度快几个数量级。
