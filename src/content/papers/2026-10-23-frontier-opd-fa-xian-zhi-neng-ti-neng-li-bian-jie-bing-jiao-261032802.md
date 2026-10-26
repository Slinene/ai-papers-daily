---
title: 'Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents
  to Go Beyond'
title_zh: Frontier-OPD：发现智能体能力边界并教会其超越
authors:
- Zheng Jiang
- Yiming Chen
- Houde Qian
- Ling Li
- Chaoyang Li
- Lifeng Sun
affiliations:
- Tsinghua University
arxiv_id: '2610.32802'
url: https://arxiv.org/abs/2610.32802
pdf_url: https://arxiv.org/pdf/2610.32802
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent 在线蒸馏 · 学习前沿
tags:
- On-policy distillation
- LLM agents
- Learning frontier
- Teacher-student
- Multi-turn agents
one_liner: 通过学习前沿动态选择教师干预点，并用学生后续行为验证指导质量，提升多智能体在线蒸馏效果
practical_value: '- 在电商/Agent 微调里，不要随机采样教师补充数据：用 on-policy 学生 rollout 计算 teacher-student
  token logprob gap，按共享状态聚合，挑『难但可救』的决策点做教师干预，比均匀采样明显提升。

  - 状态抽象可复用：把归一化 observation + available actions 哈希成 state key，合并重复访问；同时做 trajectory-balanced
  加权，避免死循环轨迹拉高节点分、占用干预预算。

  - 教师指导必须验证『学生能否接住』：只加 teacher bridge，不检查后续学生 continuation，会浪费算力；建议用 matched-window
  agreement gain（bridge+continuation vs 原轨迹等长窗口）做过滤。

  - 线上持续学习时，每轮更新后重新采样重建 frontier，让数据分布跟随当前策略；若目标是尽快达到可上线成功率，接受额外单步成本可能反而缩短总训练时间。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
多轮 Agent 蒸馏中，on-policy 反馈来自学生自己的行为，但哪些额外教师指导最适合当前学生学习仍是开放问题。只靠 teacher-student 分歧不够：某个决策可能学生已经会了，或者给了指导后学生仍无法完成后续交互。作者把『当前学生还不稳定、但短暂教师引导后能自主继续』的决策场景定义为 learning frontier。

## 方法关键点
- 构造共享状态轨迹图：把 observation + available actions 归一化哈希成 state key，合并重复状态；每个决策 occurrence 保留原始 history 用于 replay。
- 用 trajectory-balanced 聚合 signed teacher-student logprob gap，给节点打分：先对同一轨迹内多次访问平均，再跨轨迹平均，避免循环轨迹靠访问次数霸榜。
- 选 top-B distinct frontier nodes，每个节点取最高分歧的 occurrence 作为 replay representative。
- 教师短桥（默认 K=1）后恢复学生执行 H=3 步，比较 bridge+continuation 与原始等长窗口的负绝对 logprob gap 均值，gain ≥ η 才接受教师响应进入蒸馏池。
- 每次策略更新后重新 rollout 重建 graph 和 frontier，形成持续自适应。

## 实验与结果
在 ALFWorld / WebShop / ScienceWorld 上，用 Qwen3-32B 教师和 Qwen3-1.7B / 4B 学生。Qwen3-32B→1.7B：ALFWorld SR 从 OPD 22.1、FutureBridge 40.0 提升到 45.5；WebShop 从 33.7、57.7 到 58.3；ScienceWorld 从 6.2、10.2 到 14.5。Qwen3-8B-RL 教师下同样全面领先。消融显示随机选择干预点退化最大，删除 accepted bridge 数据也明显掉点；去掉 gain filtering 也有损失。效率上 Frontier 单步最贵，但在 ALFWorld 上达到 55% SR 的耗时最少。

**最值得记住的一句话**：真正有用的教师指导，既要出现在学生不会的地方，更要让学生能在之后自己走下去；这就是 learning frontier。
