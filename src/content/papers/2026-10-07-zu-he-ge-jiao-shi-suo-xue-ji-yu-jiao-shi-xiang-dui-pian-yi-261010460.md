---
title: 'Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation
  through Teacher-Relative Shifts'
title_zh: 组合各教师所学：基于教师相对偏移的多教师在线蒸馏
authors:
- Hejian Sang
- Zhengze Zhou
- Shayan Mohajer Hamidi
- Xiaomin Li
- Rohit Jain
- Alborz Geramifard
affiliations:
- Iowa State University
- LinkedIn
- Harvard University
arxiv_id: '2610.10460'
url: https://arxiv.org/abs/2610.10460
pdf_url: https://arxiv.org/pdf/2610.10460
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: 多教师在线蒸馏 · 目标构建优化
tags:
- Multi-Teacher Distillation
- On-Policy Distillation
- Teacher-Relative Shift
- LLM Post-Training
- Distillation Geometry
one_liner: 提出教师相对基座 logit shift 作为多教师在线蒸馏目标，消除基座偏好，提升组合信号均衡与效率
practical_value: '- 多教师信号融合（如多域专家蒸馏到统一推荐/Agent 策略）时，不直接聚合教师输出，而计算每个教师相对其基座模型的 logit
  偏移（teacher-minus-base），再统一锚定到学生初始化 logits，消除基座偏好，避免单一教师主导。

  - 工程上需为每个教师保存/加载基座 checkpoint 做额外前向，单步开销增加 12%-27%，但可节省总 GPU 小时（本实验 35% H100-hours）；基座可得且推理成本可接受时优先采用该目标。

  - 在多教师蒸馏前，用 norm ratio、cancellation、cosine 等几何指标监控教师项是否均衡；若 norm ratio > 5，说明某个教师的基座偏好显著主导，需做
  shift 归一化或校准（如温度调节）再组合。

  - 多阶段课程（如先搜索、后推荐、再 Agent 指令）或多域路由训练中，shift 目标能降低训练顺序对结果的影响（顺序差距从 10.50 降到 6.42 pp），对迭代流程更鲁棒。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多教师在线蒸馏（MOPD）通常直接传输每个教师的 endpoint 策略，但 endpoint 混合了后训练阶段的变化与该教师基座模型继承的偏好。当教师基座与学生初始化不同（cross-origin），这些继承偏好会污染组合目标，导致教师信号被单一教师主导，蒸馏效率下降。教师选择已受关注，但目标构建（target construction）作为独立设计轴未被检验。

### 方法关键点
- 提出 ∆-MOPD：目标 logits 定义为学生锚点 A 加上各教师相对其基座 B_i 的 logit shift δ_i = z_Ti - z_Bi，即 z_C = z_A + Σ_{i∈S} δ_i。
- 端点控制为 z_E = z_A + Σ_{i∈S} (z_Ti - z_A)；同一 origin 教师下两者相同，仅 cross-origin 项有差异。
- 在 common-domain composition（多教师同时评分同一 rollout）与 routed-domain distillation（按域分配教师）两种设置下比较，保持教师选择固定。
- 诊断指标：教师项 norm ratio、cancellation、cosine、target–student KL。
- 支持跨 tokenizer via overlap projection（仅投影重叠 token 坐标）。

### 关键实验与结果
- 机制：端点监督下，cross-origin 教师 Polaris 的 base-reference pull 梯度范数约为 shift 的 2 倍；移除后教师项 norm ratio 5.2:1 → 1.44:1，target–student KL 0.152 → 0.031，目标近 5 倍。
- 单教师跨源蒸馏：∆-MOPD 在 step 100 达到 47.90% 英文数学宏均值，超过 endpoint 最佳 46.54% (step 195)，节省 35% H100-hours。
- 三教师组合：Math macro +4.11 pp，五套件 +1.95 pp；两教师时两者相当。
- 跨 tokenizer 投影添加第四个 shift：所有三个数学基准提升，Math macro 再 +3.32 pp，五套件 +1.85 pp。
- 分阶段路由：两种顺序下 shift 均更高，顺序差距从 10.50 降到 6.42 pp；交错路由两者相当。

最值得记住的一句话：目标构建是 MOPD 中与教师选择正交的设计轴；用 teacher-minus-base shift 重新锚定到学生初始化，能消除继承的基座偏好，让多教师信号组合更均衡、更易跟踪，尤其在多个教师信号在状态上组合时收益最大。
