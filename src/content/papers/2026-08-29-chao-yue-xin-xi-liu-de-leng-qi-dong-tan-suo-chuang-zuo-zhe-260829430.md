---
title: 'Content Exploration Beyond the Feed: Creator Supply and the Shared Corpus'
title_zh: 超越信息流的冷启动探索：创作者供给与共享语料库
authors:
- Yuanyuan Shen
- Yiren Yan
- Wenjie Li
- Chunhui Zhu
affiliations:
- Snap Inc.
arxiv_id: '2608.29430'
url: https://arxiv.org/abs/2608.29430
pdf_url: https://arxiv.org/pdf/2608.29430
published: '2026-08-29'
collected: '2026-09-01'
category: RecSys
direction: 冷启动探索 · 双边效应测量
tags:
- cold-start
- content exploration
- creator economy
- two-sided marketplace
- A-B testing
- corpus effect
one_liner: 用四项随机实验证明冷启动探索有显著创作者供给效应，但共享语料库效应在短窗口和单边 A/B 中被结构性抵消或不可识别
practical_value: '- 现有冷启动曝光预算目标通常只含 CTR、discoverability 等快变量；可以把创作者后续发布响应作为 offline
  先验收进预算目标，用历史 creator experiments 和 corpus-age 数据估计 delayed posting response 与 corpus
  turnover。

  - 单边 viewer-side A/B 会结构性 cancel 掉 shared corpus effect；要衡量长期语料库价值，需用 co-diverted
  A/B，同时隔离 creator 和 viewer submarket。但该设计受 corpus turnover 时钟限制，短窗口只能汇报 finite-horizon
  increment，不能轻易外推 asymptote；增加样本量无法缩短所需 horizon。

  - 在固定曝光预算下把曝光分散到更多视频，能提升创作者参与且短期无 viewer 侧损失，可作为低风险冷启动 allocation 策略。

  - 若业务看到短期 A/B 混合或负向，建议拆分 direct feed effect 与 corpus-mediated effect 汇报，并用 cohort
  分析观察探索期结束后自然分发的 organic lift，例如视频 views/time 的 cohort slice 对比。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
信息流平台上，新内容冷启动探索是大多数新视频触达用户的主渠道。但工业界常用的曝光预算目标只基于 CTR、discoverability 等即时 viewer 信号，忽略创作者后续发布行为和共享语料库长期价值。这导致单边 viewer A/B 经常出现混合甚至负向消费结果，无法评估探索机制对双边生态的真实回报。

## 方法关键点
- 建立双边生态线性动态模型：supply \(\Lambda_{t+1}=\Lambda_0+R\Lambda_t\)，corpus \(K_{t+1}=(1-\omega)K_t+q(B)\Lambda_t\)。其中 R 是供给循环增益，\(\omega\) 是语料库周转率。
- 将单次曝光价值分解为 direct view、organic take-up、induced creator supply 三个通道；供给乘数为 \(1/(1-R)\)。
- 四种随机化设计对应不同识别目标：viewer ablation 识别 direct feed effect；creator ablation 识别 supply response；budget-matched reallocation 识别同预算下分配边际效应；co-diverted A/B 保留 shared corpus effect。
- 理论上给出 horizon blindness：t 周期实验最多表达 \(\omega t\) 的渐近 corpus 效应；样本量增大只降低噪声，不加速语料库周转；低于 curvature threshold 时，asymptote 的置信区间可能没有有限上界。

## 关键实验数字
- 8 个月 creator ablation：相对 minimal floor，生产探索让每 creator 发布视频数 +8.55%，至少发布一次的创作者 +7.10%。
- 1 年 viewer ablation：video views +1.74%，但 view time -2.13%，<1.5s views +7.49%，favorites -2.32%，呈现代价分化的 direct feed trade-off。
- budget-matched reallocation：创作者参与 +0.77%，viewer 指标 CI 全部包含 0，说明低风险提升供给侧参与。
- 3 周 co-diverted probe：direct step 为 video views +0.43%、view time -1.02%；corpus asymptote 在 36/360 天 turnover 设定下均无法确定符号；cohort 分析测得探索结束后自然分发 organic view time +37.9%，对应 whole-cell 0.1–0.2pp。

## 最值得记住的一句话
短窗口单边 A/B 只能识别 direct feed effect；共享语料库价值必须靠 co-diverted 设计且受 corpus turnover 时钟限制，增加用户无法缩短该 clock。
