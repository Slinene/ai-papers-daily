---
title: 'Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces'
title_zh: 策略其实受 Harness 秘密约束：Agent 接口的决策几何
authors:
- Jian Mu
- Ruibo Shen
- Yao Shu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2610.37255'
url: https://arxiv.org/abs/2610.37255
pdf_url: https://arxiv.org/pdf/2610.37255
published: '2026-10-26'
collected: '2026-10-29'
category: Agent
direction: Agent 接口设计与策略学习
tags:
- Agent Harness
- KL-Regularized Control
- Policy Learning
- Prompt Engineering
- Evaluation
one_liner: 训练策略会带上训练 harness 的偏好，部署收益可分解为接口天花板减策略偏差，固定模型评估接口会混淆两者
practical_value: '- 在评估 prompt / 工具 / 工作流改动时，别只拿固定模型 A/B 测试，应把表现拆成 ceiling（接口天花板）和
  mismatch（当前策略偏差）。可以用一个更强的模型（如 GPT-4 或更大开源模型）近似最优策略来估计 ceiling，再用当前模型算 mismatch，从而预测改动后重新训练/微调能带来的真实收益。

  - 如果接口只是格式变化（比如 prompt 字段顺序、工具描述顺序）而最优动作理论上不变，已微调的策略可能大幅失效（MiniWoB++ 里反转字段顺序让成功率从
  85.0% 跌到 19.2%）。这提醒我们：对 LLM 做领域微调时，训练 harness 的格式偏好会被固化，上线接口改动前要重新校准，或者在训练数据里加入字段排序、模板扰动等增强来提高鲁棒性。

  - 自动 prompt 优化工具（如 DSPy、TextGrad）常用固定模型给候选 prompt 打分，可能只选出当前模型更擅长的表达方式，而不是真正提高任务上限的接口。建议在候选
  harness 搜索中引入更强模型作为 oracle 评估 ceiling，避免陷入对当前模型的过拟合。

  - 在设计推荐/搜索 Agent 的工具调用接口、提示词模板时，接口本身的易用性和信息完整性（高 ceiling）可能比当前模型一次性表现更重要，尤其是计划后续用业务数据继续训练模型时。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Agent 通过 harness（prompts、工具、控制逻辑）部署，实际工作中 harness 常被修改并用固定模型给候选接口打分，这暗含假设——模型在旧 harness 上学的行为能迁移到新 harness。论文追问：策略到底从 harness 中学到了什么？harness 改变后什么会保留？

方法关键点：在 KL 正则化控制下，最优策略的 log odds 恰好反映 harness 对每个动作的偏好强度，因此训练出的策略会携带训练 harness 的偏好。部署回报可分解为两项：ceiling（该 harness 能提供的最好回报）减去 mismatch（策略自身次优决策造成的损失）。训练只改变 mismatch，而改变 harness 会同时移动 ceiling 和 mismatch。因此用固定模型比较不同 harness，会混淆“接口本身能提供什么”和“当前模型用得好不好”。

关键结果：在 MiniWoB++ 中，仅仅反转观察字段顺序（最优决策不变）就让训练模型的成功率从 85.0% 暴跌到 19.2%，说明策略偏好高度绑定训练 harness。反过来，所有被固定模型比较拒绝、但提高 ceiling 的新 harness，在进一步训练后都超过了原 agent；事前测得的 ceiling 和 mismatch 能预测这些收益。在 Terminal-Bench Lite 编码 agent 场景，用更强模型代替最优策略估计 ceiling - mismatch，可以复现 harness 的准确率排名，而单独看 ceiling 或 mismatch 都不行。
