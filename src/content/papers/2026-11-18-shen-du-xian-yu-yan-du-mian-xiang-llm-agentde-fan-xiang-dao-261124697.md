---
title: 'Depth Before Breadth: Reverse-to-Forward Curriculum with Advantage Decomposition
  for LLM Agent'
title_zh: 深度先于广度：面向LLM Agent的反向到正向课程与优势分解
authors:
- Siyuan Du
- Yuxin Liu
- Meng Tang
- Haoran Li
- Yechao Bai
- Feiyang Pan
- Jia He
affiliations:
- 南京大学
- 北京大学
- University of Wales, Aberystwyth
arxiv_id: '2611.24697'
url: https://arxiv.org/abs/2611.24697
pdf_url: https://arxiv.org/pdf/2611.24697
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent强化学习 · 反向课程与信用分配
tags:
- LLM Agent
- Reinforcement Learning
- Credit Assignment
- Curriculum Learning
- GRPO
- Long-horizon
one_liner: 用Paired Advantage拆分前缀与后缀优势，配合反向-正向课程，在ALFWorld/WebShop显著提升长程LLM Agent训练
practical_value: '- 在电商购物Agent的RL训练中，先截取成功交易轨迹的最后几步作为训练起点，等成功率达到阈值再逐步向前移动起点；这比直接从头训练能更快建立可靠的成交能力，缓解搜索-加购-下单长链路中的稀疏奖励。

  - 借鉴Paired Advantage做细粒度信用分配：同一批rollout按前缀到达的context去重分组，对前缀用端点价值差异做优势，对后缀用同端点续写收益差异做优势；相比GRPO的trajectory-level广播，能减少策略过早收敛到单一高奖励路径。

  - 工程上，对每个去重端点固定采样2条suffix并复用于所有到达该端点的前缀，交互预算可控，同时暴露同一状态下的成功/失败方差；这在WebShop这类可重置中间状态的电商模拟环境中容易实现。

  - 课程推进可以参考其自动信号：reverse阶段用参考轨迹上的成功率阈值η，forward阶段用prefix端点多样性|E|是否plateau决定加长前缀，无需手工标注过程奖励。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
LLM Agent在长程任务上通过RL训练时，稀疏终端奖励导致信用分配与探索困难。标准reverse curriculum虽能把起点靠近目标，但仍有两个缺陷：起点后移使终端反馈被摊薄到更长序列，早期动作仍难被区分；起点锚定在参考轨迹上，限制了off-reference状态的覆盖。论文引入policy-induced capability region，指出在能力边界附近，只需少数动作就能进入已可完成任务的区域，因此长程任务可被拆成“进入能力区域”和“从区域内部完成任务”两个子问题。

**方法关键点**
- 定义能力区域 Cη(π)={c:pπ(c)≥η}，训练上下文来自能力边界附近。
- Paired Advantage：每组采样n=8个prefix，按端点context去重分组；每个端点采样NR=2个suffix，估计端点价值 bV(e)。左优势比较不同端点价值，用于prefix信用分配；右优势比较同端点suffix收益，用于suffix信用分配。更新目标对prefix和suffix分别做clip。
- 两阶段课程：reverse阶段沿成功参考轨迹从尾部逐步回退起点（stride d=3），先掌握局部执行；forward阶段从原始起点采样policy自身rollout的prefix，逐步增加prefix长度，扩展到off-reference状态。课程推进由成功率阈值η或端点多样性|E| plateau触发。

**关键结果**
- ALFWorld：Qwen2.5-1.5B/7B-Instruct成功率分别达90.1%/96.1%，较GRPO提升17.3/18.5个百分点，较GiGPO提升3.4/5.3个百分点。
- WebShop：1.5B/7B分别获得score 88.6/92.5、success 80.2%/82.6%；7B score超GiGPO 8.1分，success超CRPS 8.6个百分点。
- 消融：reverse-only成功68.8%，加forward达74.7%，再在reverse和forward中加入PA分别提升至76.6%和80.2%，验证各组件有效。
- 分析显示PA保留更多高价值端点，避免GRPO下的winner-takes-all收缩。

**最值得记住的一句话**：Paired Advantage把长轨迹拆成prefix与suffix，分别回答“走到哪里”和“从那里怎么完成”，为稀疏奖励长程Agent提供更细的信用信号。
