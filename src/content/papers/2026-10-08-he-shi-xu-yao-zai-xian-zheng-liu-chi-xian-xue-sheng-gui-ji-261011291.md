---
title: When Do We Need On-Policy Distillation? Distilling on Offline Student Rollouts
  Is Often Better
title_zh: 何时需要在线蒸馏？离线学生轨迹蒸馏常更优
authors:
- Siyan Zhao
- Yonggan Fu
- Jindong Jiang
- Shih-Yang Liu
- Song Bian
- Byung-Kwan Lee
- Sharath Turuvekere Sreenivas
- Wenliang Dai
- Hanrong Ye
- Aditya Grover
arxiv_id: '2610.11291'
url: https://arxiv.org/abs/2610.11291
pdf_url: https://arxiv.org/pdf/2610.11291
published: '2026-10-08'
collected: '2026-10-13'
category: Training
direction: LLM 蒸馏策略 · 在线 vs 离线 rollout
tags:
- knowledge distillation
- on-policy distillation
- offline rollouts
- LLM
- training efficiency
one_liner: Semi-OPD 用初始学生离线 rollout 蒸馏，在 17 对模型上 14 对优于 OPD，最高 +13.6% 精度、11.4 倍加速
practical_value: '- 做 LLM teacher→student 蒸馏（如 query 改写 / 商品文案 / Agent 策略小模型）时，先别默认
  OPD。用一批 hold-out prompt 统计初始师生输出的 top-64 token overlap；若 overlap 不高（论文中多数 < 90%），直接用初始学生离线
  rollout 的 Semi-OPD，精度更稳且省 GPU。

  - 离线 rollout 可以预生成、缓存、复用，训练时只用固定数据，天然适合电商/广告的离线训练流水线；Semi-OPD 相对 OPD 最高 11.4 倍加速，H100
  成本明显下降。

  - 若业务必须用 OPD（如需要在线探索），先做 warm start 让学生与老师输出分布接近；否则学生 rollout 随上下文增长会越来越 off-policy，蒸馏信号退化。

  - 可以把 token overlap ratio 作为轻量监控指标，在启动蒸馏前判断 OPD 是否值得，避免盲目投入 GPU。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
On-policy distillation (OPD) 被广泛用于把大模型能力迁移到小模型，但并非对所有 teacher-student pair 都更优。作者质疑：是否总是需要在线采样？

**方法关键点**  
提出 Semi-OPD：用初始学生生成的离线 rollout 蒸馏，训练过程中不更新采样；与 OPD、FastOPD、Relay-OPD 对比。提出用输出 token overlap ratio 量化初始 teacher 与 student 的对齐程度。

**关键结果**  
在 17 对 1.5B 到 235B 模型上，Semi-OPD 在 14 对中优于 OPD，最高提升 +13.6% 精度、11.4 倍训练加速。OPD 仅在 teacher-student 初始高度对齐（overlap 高）时有益。深层分析显示：有效蒸馏需要同时对 student 和 teacher 保持 on-policy；错配时学生 rollout 随上下文增长越来越偏离 teacher，削弱蒸馏信号；Semi-OPD 在较短上下文上覆盖完整轨迹，暴露更多 teacher-preferred tokens，因此更稳定。
