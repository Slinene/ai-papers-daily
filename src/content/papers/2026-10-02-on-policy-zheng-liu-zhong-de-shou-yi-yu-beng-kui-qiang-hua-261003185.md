---
title: Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective
title_zh: On-Policy 蒸馏中的收益与崩溃：强化学习视角
authors:
- Han Cui
- Jianhao Yan
- Yun Luo
- Hongbo Zhang
- Zhizhang Fu
- Yue Zhang
affiliations:
- Zhejiang University
- Westlake University
arxiv_id: '2610.03185'
url: https://arxiv.org/abs/2610.03185
pdf_url: https://arxiv.org/pdf/2610.03185
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: LLM 后训练 · On-Policy蒸馏 · RL视角
tags:
- On-Policy Distillation
- Reinforcement Learning
- Reward Hacking
- LLM Post-training
- SFT Initialization
- Response Masking
one_liner: 用 RL 视角解释 OPD 收益与崩溃：教师隐式奖励会放大学生的已有采样行为，掩码不健康响应与 SFT 初始化可缓解崩溃。
practical_value: '- 做 LLM 后训练/蒸馏（如生成式推荐文案、Agent 轨迹优化）时，不要把教师模型只当作生成器，要同时审计它作为隐式 reward
  model 的可靠性；若教师打分和业务质量指标失配，可能系统性放大拼凑长文、重复槽位等低质输出。

  - 在 on-policy 训练或在线蒸馏流程中加入「不健康响应 mask」：对超长、重复、包含异常模板的 rollout 直接屏蔽或降权，可低成本遏制 reward
  hacking。

  - 上线蒸馏前先做 SFT 初始化，再切换 on-policy 蒸馏；尤其适合电商推荐解释、搜索 agent 工具调用轨迹等冷启动场景，避免从随机策略开始导致退化。

  - 监控 rollout 长度分布、重复 n-gram 比例、KL 偏离等指标，作为早期预警；一旦长度/重复度飙升，优先检查教师偏好是否被错误行为劫持。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：On-policy distillation (OPD) 在语言模型后训练中既有性能提升，也可能崩溃为过长老重生成；以往机制不清。

方法关键点：从强化学习视角重新建模，教师不是在提供自己的轨迹，而是在隐式奖励学生 rollout，包括教师很少生成的行为。实验据此区分两种情形：隐式奖励可靠时，OPD 只是把正确响应变得更易采样，并未扩大学生能力；当偏好与质量失配时，发生 reward hacking，教师会系统性放大过长老重输出，尽管其自己很少生成这类文本。缓解手段：训练时 mask 不健康响应、用 SFT 初始化，均可单独缓解崩溃。

关键结果：在数学推理示例中，教师自身正确响应为 771 tokens，而教师偏好却给 7311 tokens 的错误长 rollout 更高分，体现偏好失配下的放大效应。论文结论是 OPD 放大的是学生已有的、被教师偏好认可的行为，而非教师自身的生成能力。
