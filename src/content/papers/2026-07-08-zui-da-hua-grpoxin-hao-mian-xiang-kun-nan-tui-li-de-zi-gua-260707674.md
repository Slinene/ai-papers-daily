---
title: 'Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning Problems'
title_zh: 最大化GRPO信号：面向困难推理的自适应前缀控制
authors:
- Vladislav Beliaev
affiliations:
- Independent Researcher
- thinkdense.ai
arxiv_id: '2607.07674'
url: https://arxiv.org/abs/2607.07674
pdf_url: https://arxiv.org/pdf/2607.07674
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: RL训练方法 · 自适应难度调节
tags:
- GRPO
- Reinforcement Learning
- Curriculum Learning
- Prefix Control
- Reasoning
one_liner: 自适应前缀控制动态维持困难问题的50%成功率，最大化GRPO梯度信号，大幅提升推理准确率
practical_value: '- 在电商搜索/推荐中使用GRPO训练LLM策略时，常遇到困难样本组内全失败导致梯度为零，可借鉴AdaPrefix：为困难样本预先拼接部分正确输出（如人工标注的关键步骤）作为前缀，提高组内成功概率，避免梯度消失。

  - 借鉴“成功率50%噪声最大”的思想，在在线学习过程中动态调整任务难度（前缀长度），使模型始终处于最利于学习的“挑战区”，可应用于动态负采样或课程学习排序中。

  - 工程实现极为轻量：仅需在数据预处理中拼接前缀token，并在计算loss时mask掉前缀部分，训练器无需改动，适合快速实验和部署。

  - 对于多步推理的Agent训练，可在初始阶段给予部分正确推理链作为引导，随着训练逐步撤除，使Agent最终独立完成复杂任务，缓解稀疏奖励问题。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：GRPO在解决困难问题时，若一组rollout全部失败，组内相对优势为零，损失梯度消失，导致模型在最需要学习的边界问题上浪费算力且无进步。现有方法如丢弃全错组不能从根本上提供有效梯度。

**方法**：提出AdaPrefix-GRPO，为每个问题拼接长度可调的参考解答前缀作为提示，将前缀长度视为连续难度旋钮。训练中引入反馈控制器，根据问题的成功历史动态调整前缀长度，使每个问题的成功率维持在50%附近——此处GRPO的梯度信号最大。训练后期逐渐缩短前缀直至完全移除，确保最终模型在无辅助下能独立求解。实现仅需在数据准备阶段添加前缀并在损失计算时mask前缀token，不改变GRPO训练流程。

**结果**：在困难数学推理上，0.6B模型准确率提升至GRPO的2.1倍，1.7B模型提升1.6倍，AIME基准提升1.7倍，同时生成的推理轨迹长度减半。模型越小增益越大。
