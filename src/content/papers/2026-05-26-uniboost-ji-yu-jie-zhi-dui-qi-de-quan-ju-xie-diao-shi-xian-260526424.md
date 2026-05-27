---
title: 'Uniboost: Global Coordination with Value Alignment for Fair and Efficient
  Traffic Allocation'
title_zh: Uniboost：基于价值对齐的全局协调实现公平高效流量分配
authors:
- Ge Fan
- Nan Zhao
- Kai Meng
- Cong Luo
- Yang Fu
- Huiping Chu
- Jialin Liu
- Yuning Jiang
- Bo Zheng
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2605.26424'
url: https://arxiv.org/abs/2605.26424
pdf_url: https://arxiv.org/pdf/2605.26424
published: '2026-05-26'
collected: '2026-05-27'
category: RecSys
direction: 流量分配 · 价值对齐 · 混排优化
tags:
- Traffic Allocation
- Blending
- Value Alignment
- Linear Boosting
- Recommendation System
- Online A-B Test
one_liner: 提出统一框架 Uniboost，通过后验价值对齐和独立线性提升，解决混排分数膨胀和不可解释问题，提升推荐效率。
practical_value: '- **后验价值对齐**：选择一个稳定且与业务一致的后验指标（如有效完成率）作为锚点，对原始分进行均值缩放，让分数具备物理意义，便于加权干预和可解释性。

  - **独立线性提升**：将广告保量、冷启探索等目标解耦为独立线性项直接相加，保证可加性和归因性，可计算每个策略的精确成本和 ROI。

  - **统一加权范式**：用线性加权+偏置统一 PID 控制、boost 等不同机制，实现简单，易于在线部署和离线分析。

  - **归因驱动宏观优化**：通过离线统计各计划的流量消耗和业务提升，识别低效策略并移除，实现数据‑驱动迭代。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统混排阶段需要同时处理广告保量、冷启动、运营活动等多业务目标，传统方法将多个加权方案耦合，导致分数膨胀、丧失物理语义、策略间相互干扰，且难以评估各策略的真实贡献。

### 方法关键点
- **后验价值对齐**：选取一个稳定、分布均匀的后验指标「有效完成率」作为锚点，用全局均值缩放映射原始模型分，使分数转化为预期完成率，具备业务可解释性。
- **独立线性提升**：对每个业务计划 p，计算独立 boost：`s_{p,v} = 1_p(v)*(w_p*y_v+b_p)`，其中 y_v 为对齐后的值；最终排序分 `r_v = y_v + Σ s_{p,v}`，保证可加性，支持精确归因。
- **统一框架**：兼容 PID 保量（令 w=0 用 b 传递 PID 输出）和传统 boost（令 b=0），将各类机制统一为线性加权+偏置。
- **近离线闭环**：实时跟踪分布、缓存分数，对各计划汇总成本与提升，计算 ROI 指导线上调参和策略下线。

### 关键实验
- 在线 A/B 测试，对照组为原始加权管线（分数对齐在加权后），实验组为 Uniboost，锚指标选「有效完成率」。
- 核心指标全线上涨：VV +1.69%，有效播放 VV +3.07%，消费时长 +0.65%，综合价值分 +2.54%。
- 加权分数大幅缩减（广告降 92.2%，有机内容降 95.8%），但曝光份额稳定，证明分数膨胀有效缓解。
- ROI 分析发现 Plan‑A 成本高收益低，移除后进一步带来有效播放 VV +2.83%，时长 +3.49%，综合分 +4.13%。

**最值得记住**：Uniboost 通过后验价值对齐和独立线性提升，将抽象分数转化为可解释的业务价值，并精确量化每个策略的贡献，实现了从微观效率到宏观指导的闭环优化。
