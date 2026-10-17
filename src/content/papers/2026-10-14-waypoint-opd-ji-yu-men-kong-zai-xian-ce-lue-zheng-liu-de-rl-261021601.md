---
title: 'Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation'
title_zh: Waypoint-OPD：基于门控在线策略蒸馏的 RL 策略偏移迁移
authors:
- Bingxi Hou
- Guochao Jiang
- Guofeng Quan
- Weiqing Li
- Wenfeng Feng
- Guohua Liu
- Yuewei Zhang
affiliations:
- Alibaba Cloud Computing
arxiv_id: '2610.21601'
url: https://arxiv.org/abs/2610.21601
pdf_url: https://arxiv.org/pdf/2610.21601
published: '2026-10-14'
collected: '2026-10-17'
category: Training
direction: RL 策略偏移蒸馏 · 门控迁移
tags:
- RL distillation
- on-policy distillation
- policy shift
- gated transfer
- reasoning
- LLM training
one_liner: 用中间检查点方向一致性门控教师 RL 前后策略偏移，提升数学与代码推理蒸馏效果
practical_value: '- 在 RL 蒸馏中保留中间 checkpoint 成本低：只需额外一次 frozen-teacher 打分，即可按 early/late
  偏好方向一致性过滤噪声，适合线上小模型蒸馏。

  - 门控思想可迁移到排序/Agent 策略蒸馏：teacher 策略在训练中迭代不稳定时，不要直接用最终参数差，而是用中间检查点检测方向冲突，抑制相互抵消的 policy
  shift。

  - 对用 RL 微调 LLM 做 query 生成、生成式推荐或 Agent 决策的业务，可以借鉴 on-policy 蒸馏方式：让学生自生成轨迹，teacher
  打分并计算 early/late log prob 差，只把方向一致的策略偏移作为监督，避免把探索期噪声传给学生。

  - 论文在数学与代码推理验证，迁移到电商场景需适配奖励和动作空间，但“方向一致性 gating”是通用 trick。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 policy-shift distillation 只用教师 RL 前、后两个 checkpoints 的 log prob 差值（endpoint shift）监督学生生成轨迹，但 endpoint shift 无法反映局部动作偏好在训练中是否一致，可能掩盖早期和晚期相互抵消或冲突的变化。

**方法关键点**：Waypoint-OPD 引入同一 RL run 的中间教师 checkpoint，在 student-visited prefixes 上比较早期 shift（中间-初始）与晚期 shift（最终-中间）的相对动作偏好方向。根据方向一致程度对 endpoint shift 做门控：方向相反时抑制该偏移传递，方向一致时保留。相比 endpoint-only 蒸馏，只多一次 frozen-teacher scoring pass。

**关键结果数字**：用 Qwen3-4B RL 教师，在 Qwen3-8B/14B/30B-A3B 三个学生上覆盖数学与代码推理共 6 个 domain-student 设置，Waypoint-OPD 均取得最高 domain-average score。数学推理 mean@32 比 Direct-OPD 分别提升 2.18、1.59、1.89 个百分点；消融显示移除或打乱 gate 会降低数学推理性能。
