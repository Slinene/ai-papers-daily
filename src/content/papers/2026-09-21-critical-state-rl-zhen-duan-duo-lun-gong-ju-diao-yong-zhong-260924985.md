---
title: 'Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use'
title_zh: Critical-State RL：诊断多轮工具调用中的可训练状态
authors:
- Zixiang Chen
- Wenting Zhao
- Zhepeng Cen
- Akshara Prabhakar
- Jielin Qiu
- Jianguo Zhang
- Zhiwei Liu
- Tulika Manoj Awalgaonkar
- Liangwei Yang
- Shelby Heinecke
affiliations:
- Salesforce AI Research
arxiv_id: '2609.24985'
url: https://arxiv.org/abs/2609.24985
pdf_url: https://arxiv.org/pdf/2609.24985
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: 多轮工具调用 · 局部 RL 训练
tags:
- Critical-State RL
- multi-turn tool use
- credit assignment
- nested sampling
- contextual bandit
- BFCL
one_liner: 用训练前嵌套采样分离动作相关方差与续采样噪声，定位多轮工具调用中真正值得训练的单个模型调用，再做局部 RL
practical_value: '- 多轮 agent（电商导购、客服、工具调用）不要直接用 trajectory-level reward 训练所有 turn：先在一个
  frozen policy 上做训练前诊断，估计每个候选 turn 的 action-dependent variance，选出真正可训练的 occurrence。

  - 局部 occurrence-level RL 只对选中的 response 计算 loss，其他 turn 只提供 context 或 reward、不接收梯度。这能减少无关
  turn 的梯度污染，适合从线上 logged interactions 中做低成本优化。

  - 对工具调用类场景，可以按任务结构构造 occurrence-local label：如 `no_write(adec) × consequence(yrec)`、keyword
  retention proxy 或 `repeat_of_history`；用参考策略 headroom 过滤已经饱和的状态，避免在无改进空间的地方浪费训练。

  - 工程实现上，嵌套采样用 `S_between^2 - S_within^2 / m` 估计 V_act，训练前无需训练 critic；对每个 candidate
  采 n 个 actions × m 个 continuations 即可。负值估计保留，只做排序选择，成本低且可跨模型/任务迁移。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
多轮工具调用任务中，失败往往取决于某一个模型调用，但 trajectory-level reward 不能识别哪个调用值得训练。后续交互的随机性会让 reward 波动，和当前动作质量混在一起。固定角色地训练某个 turn（例如总是训练决策轮或恢复轮）在不同模型/任务上不稳定。

## 方法关键点
- Critical-State RL 将候选 phase / occurrence 定义为任务结构相关的具体模型调用，并用 occurrence-local label 作为局部 reward。
- 训练前在冻结 base policy 上做嵌套采样：固定 prefix，采样多个 action，每个 action 固定后重采样 reward-only continuation；用 `S_between^2 - S_within^2 / m` 估计动作相关方差 V_act，消除 continuation noise。
- 三个门槛筛选 critical state：action-sufficiency（`R⊥a|(x,z)`）、headroom（相对参考策略有可改进空间）、trainability（`V_act>0`）。候选 occurrence 按平均 V_act 排序，选最大者。
- 只对选中调用做 occurrence-local RL / contextual-bandit 训练：该调用的 generated tokens 接收梯度，前后调用仅提供 context 或 reward。
- label 随任务构造：缺函数任务采用 `no_write(adec) × consequence(yrec)`；记忆任务采用行为/内容加性 reward + GPT-4o 关键词 proxy；重复调用采用确定性的 `repeat_of_history` label。

## 关键实验
BFCL v4 multi_turn 四格研究，no-think Gemma-4-26B-A4B。诊断选择 miss_func 的 recovery turn、miss_param 的 decision turn。训练选中 turn：miss_func `0.14→0.283±0.015`（+14.3pp），miss_param `0.435→0.473±0.010`（+3.8pp）；训练替代 turn 分别 -4.5pp 和 +1pp。换成未见过的 bridge 表达仍然 +13.0pp。与 Monte-Carlo RTG 全轨迹训练相比，RTG gym 0.997 但 BFCL 仅 0.45，低于 Critical-State RL 0.473；targeted-SFT 在 miss_func/recovery 上比 base 还低 6pp，因过度偏向调用工具。跨任务：logged repeat-call avoidance 一致性 `37%→约75%`；Nemotron missing-function +4.4pt；memory xLAM `34.54%→50.54%`，Gemma memory `38.1%→52.7%`。

## 最值得记住的一句话
多轮 agent 中“哪个 turn 值得训练”本身是一个需要诊断的问题；动作相关方差比 reward 是否 mixed 更能反映可训练信号。
