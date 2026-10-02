---
title: 'ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization'
title_zh: ActiveSaddler：Agent 外壳优化的自动课程学习
authors:
- Sungho Park
- Wonjoong Kim
- Jue Zhang
- Wook-Shin Han
- Pengfei Gao
- Chanyoung Park
- Yongqiang Yao
- Rao Fu
- Elsie Nallipogu
- Qingwei Lin
affiliations:
- POSTECH
- KAIST
- Microsoft
arxiv_id: '2610.00906'
url: https://arxiv.org/abs/2610.00906
pdf_url: https://arxiv.org/pdf/2610.00906
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: Agent harness 自动课程学习
tags:
- Automated Curriculum Learning
- Agent Harness Optimization
- LLM Agents
- Non-stationary Bandit
- Failure-Pattern Arms
- Adaptive Exploration
one_liner: 将 Agent harness 优化的训练场景选择建模为非平稳 bandit，动态构造 failure-pattern arm 并自适应调度，在
  GAIA2/Terminal-Bench 2.0 分别提升 4.4/7.5 个百分点
practical_value: '- **把训练样本选择纳入 LLM Agent 自动优化**：在自动调 prompt / tool / control logic
  时，不要只按固定类目或场景顺序滚动训练集；先对失败执行轨迹做诊断，按同一底层缺陷聚成 failure-pattern arm，再作为后续优化目标。类目粒度太粗会掩盖未解决弱点，单场景粒度太细会分散同类失败，论文中两类替代
  arm 导致 GAIA2 下降 3.0/3.6pp，TB2 下降 10.8/6.7pp。

  - **用 LLM 对失败模式打学习潜力分并随机采样，不贪心**：打分参考 severity / fixability / breadth / side-effect
  risk 四维，再做 softmax 采样（温度 0.15）。分数随 harness 和证据更新而重算，让优化预算持续重分配到仍可修复的高价值弱点；移除自适应打分导致
  4.5/7.5pp 下降。

  - **显式设置 exploration / exploitation 控制器**：每轮先做二值决策 DRAW（探索未见样本）vs PULL（复用已知 arm），依据当前已知
  arm 剩余价值；固定每 5 轮探索的变体下降 4.5/8.3pp。在搜索/推荐 Agent 优化中，当已知失败模式已被基本修复时再切换新 task 采样。

  - **用 pattern registry + CLI 管理动态 arm，而不是把历史全塞进 prompt**：提供 scoped view 和读写命令，工程上可复用到长周期迭代的
  agent 优化系统。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有自动 harness 优化主要聚焦「如何更新 harness」（prompt、tool 接口、控制逻辑），而训练场景通常预先固定。随着 harness 演化，最有价值的反馈场景会变化：未被修复的失败需要更多曝光，已修复失败继续占用 rollout 是浪费；固定顺序无法响应这种变化，在有限 rollout 预算下尤其低效。

**方法关键点**
- 将训练场景选择建模为非平稳多臂 bandit，arm 不是预先定义的场景，而是从失败执行记录中动态提取的 failure-pattern arm：将同一底层缺陷跨场景、跨轨迹聚合，构成可复用的优化目标。
- 三个核心组件：Failure-Pattern Extractor 把失败诊断抽象为症状、规范化并注册 arm；Arm Prioritizer 用 LLM 估计每个 arm 的学习潜力分，综合 severity / fixability / breadth / side-effect risk 四维，并通过 softmax 采样选择下一次优化目标（τ=0.15）；Exploration Controller 做二值决策 DRAW vs PULL，动态平衡探索未见场景与复用已知弱点。
- 通过 pattern CLI 为优化 agent 提供 scoped view 和读写接口，持续更新 arm 状态、证据和优先级；训练成功场景在 arm 池耗尽后可重新参与回归检查。

**关键结果**
- GAIA2 test Pass@1 达 59.8%，相比 AutoSaddler 固定顺序 55.4% 提升 +4.4pp；Terminal-Bench 2.0 达 80.0%，相比 72.5% 提升 +7.5pp。
- 相比 category / scenario 难度课程，GAIA2 分别提升 +3.9pp / +4.1pp，TB2 分别提升 +9.2pp / +6.7pp。
- 跨优化器通用：将 ActiveSaddler 应用到 GEPA 后，平均 Pass@1 从 54.2% 提升到 57.2%（+3.0pp）。
- 消融：去掉自适应 arm 打分或去掉自适应探索，GAIA2 均下降 4.5pp，TB2 分别下降 7.5pp / 8.3pp；用 category / scenario arm 替代 failure-pattern arm 也带来 3.0～10.8pp 下降。

**最值得记住的一句话**
优化反馈的数据顺序与优化器本身同等重要：把失败聚类为可复用模式并动态调度，能显著提升有限 rollout 预算下的 Agent harness 质量。
