---
title: 'OPTED: On-Policy Fine-Tuning for End-to-End Driving using a Render-Free Teacher'
title_zh: OPTED：基于无渲染教师的端到端驾驶在线策略微调
authors:
- Damiano Da Col
- Maximilian Igl
- Peter Karkus
- Kashyap Chitta
- Boris Ivanovic
- Marco Pavone
- Konrad Schindler
- Christos Sakaridis
arxiv_id: '2609.20756'
url: https://arxiv.org/abs/2609.20756
pdf_url: https://arxiv.org/pdf/2609.20756
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 特权教师 on-policy 蒸馏
tags:
- on-policy fine-tuning
- privileged teacher
- policy distillation
- end-to-end driving
- RL
- 3DGS simulation
one_liner: 用RL训练矢量输入特权教师，在闭环中蒸馏至摄像头学生模型，大幅减少模拟器交互成本
practical_value: '- 特权教师蒸馏可迁移到推荐/广告：实际线上受限于特征获取延迟或算力，可训练一个输入全量特征（如用户画像、后验转化、上下文）的教师模型，再将知识蒸馏到实时轻量学生模型；在日志回放模拟器中做
  on-policy 更新，比直接在线 RL 成本低几个数量级。

  - 用离线数据重建用户交互模拟器：类似 3DGS 从真实驾驶日志重建场景，推荐系统可基于离线日志构建用户状态转移模拟器，用于策略微调；能部分替代高成本线上 A/B，缓解行为克隆的开环偏差和状态分布偏移。

  - on-policy 微调优于纯行为克隆：推荐/排序策略仅在离线日志上训练，线上易出现 compounding error；在模拟器中进行 on-policy
  蒸馏或 RL 微调可改善鲁棒性，且教师提供密集监督信号，避免直接 RL 稀疏奖励难训练的问题。

  - 教师可以无渲染（render-free）：若学生需要处理高维原始特征（文本、图像），教师仅使用结构化特征训练并在闭环中生成监督，可避免昂贵的前向模拟，降低训练成本；对
  Agent 或生成式推荐中的策略蒸馏有借鉴意义。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：端到端驾驶策略通常用行为克隆在开环人类演示上预训练，但闭环部署时自身的动作会导致状态漂移，累积误差可能引发安全风险。闭环后训练（如强化学习）可缓解此问题，但传感器策略需要昂贵的仿真渲染，直接 RL 交互成本极高。

**方法关键点**：OPTED 将 RL 与端到端策略后训练解耦。先训练一个特权教师：输入矢量化 HD 地图和边界框，在闭环中用 RL 优化，教师不依赖摄像头渲染，因此称为“无渲染”。随后，教师在一个基于 3DGS 神经重建真实驾驶日志的模拟器 AlpaSim 中，为预训练的摄像头学生模型（TransFuser、VaVAM）提供闭环监督，进行 on-policy 微调。学生接收教师的动作或轨迹作为监督信号，在整个闭环状态序列上蒸馏，无需额外传感器仿真。

**关键结果**：两个摄像头模型驾驶分数分别提升 1.6× 和 9.5×；与直接 RL 后训练相比，OPTED 以约三个数量级更少的模拟器交互达到相当闭环性能，同时保持更接近人类先验的驾驶行为。
