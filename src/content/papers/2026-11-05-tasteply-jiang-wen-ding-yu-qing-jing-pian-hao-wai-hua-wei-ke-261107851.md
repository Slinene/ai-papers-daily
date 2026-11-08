---
title: 'Tasteply: Externalizing Stable and Situational Preference as Manipulable Spatial
  Objects'
title_zh: Tasteply：将稳定与情境偏好外化为可操控的空间对象
authors:
- DaEun Choi
- Daniel Lee
affiliations:
- KAIST
- Salesforce AI Research
arxiv_id: '2611.07851'
url: https://arxiv.org/abs/2611.07851
pdf_url: https://arxiv.org/pdf/2611.07851
published: '2026-11-05'
collected: '2026-11-08'
category: RecSys
direction: 交互式推荐 · 偏好外化与控制
tags:
- Preference Elicitation
- Interactive Recommendation
- Spatial UI
- User Control
- Situational Preference
- Human-in-the-loop
one_liner: 把用户偏好拆成情境吸引子与全局场，用空间操控让用户直接引导推荐结果
practical_value: '- 可将用户偏好拆成“稳定偏好 + 情境偏好”两个层级，并在产品中可视化/可调：例如电商首页推荐设置“通勤/周末/夜间”等情境
  attractor，用户拖动位置即可切换推荐策略，而不是重新训练或只靠行为推断。

  - 在推荐 Agent / 对话式推荐中，可借鉴“空间化偏好对象”的操控隐喻，让用户直接调整模型内部状态（如用滑块调节不同类目权重、全局多样性强度），减少纯语言指令的模糊性。

  - 工程实现上，“全局场强度”类似对多样性/探索项的全局加权，可作为推荐重排的轻量参数，让用户在 feed 级实时干预排序目标，无需修改底层模型。

  - 注意该论文是 HCI 探索性研究，样本量仅 N=5，结论主要是交互形态验证；用于大规模线上系统前需要做更严格 AB 与 UX 测试。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统通常把用户偏好当作单一信号，难以处理稳定偏好与随上下文切换的情境偏好，用户也缺少直接干预推荐逻辑的入口。

**方法关键点**：Tasteply 将偏好结构外化为可操控的空间对象：每个情境偏好表示为一个 attractor，稳定偏好表示为可调节的全局场。用户通过移动空间中的当前位置、调整全局场强度来改变 feed，使隐藏在模型内部的偏好结构变成可见、可操作的对象，从而直接引导推荐算法。

**关键结果**：通过 N=5 的探索性研究，发现这种空间控制方式能有效引导推荐，同时识别出局限与未来方向。论文是 HCI 短稿，以交互机制验证为主，未提供大规模离线/在线指标。
