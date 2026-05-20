---
title: Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information
title_zh: 基于逐点互信息的抗自蒸馏推理强化学习
authors:
- Guobin Shen
- Xiang Cheng
- Chenxiao Zhao
- Lei Huang
- Jindong Li
- Dongcheng Zhao
- Xing Yu
affiliations:
- Xiaohongshu Inc.
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2605.11609'
url: https://arxiv.org/abs/2605.11609
pdf_url: https://arxiv.org/pdf/2605.11609
published: '2026-05-11'
collected: '2026-05-20'
category: Training
direction: 强化学习训练方法 · 推理优化
tags:
- Anti-Self-Distillation
- Pointwise Mutual Information
- Reasoning RL
- Entropy Gate
- GRPO
- On-Policy Distillation
one_liner: 通过逐点互信息分析揭示自蒸馏在推理任务中的失效根源，提出逆向散度与熵门控，使 GRPO 基线训练步数减少 2-10 倍，准确率最高提升 11.5
  点
practical_value: '- **信用分配改进**：传统 on-policy 自蒸馏在推理任务中会系统性压低探索性 tokens（如“Wait”“Let”）的权重，抬高结构连接词权重，AntiSD
  逆向设计可更有效分配 token 级信用，可借鉴到 Agent 多步决策训练，避免模型过早陷入确定性模式。

  - **熵门控机制**：当教师熵崩塌时自动关闭蒸馏项，防止后期训练坍缩。在电商对话或 Agent 规划中，可类似监控策略熵，动态切换训练信号，避免多样性丧失。

  - **训练加速**：将 AntiSD 作为 GRPO 的即插即用替换，可在极少量训练步内达到基线性能，适合资源受限的线上模型迭代，可直接复用到有 token
  级反馈的 RLVR 场景。

  - **超参鲁棒性**：方法对额外超参不敏感，工程落地成本低，可将“抗自蒸馏”视作一种通用的训练 trick 加入现有 RLHF/GRPO 流程。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：on-policy 自蒸馏（学生模型向自身特权上下文版本靠近）在数学推理中表现不稳定，与在其他任务的成功形成反差。本文通过逐点互信息（PMI）分析发现，特权上下文（如验证后的答案）会抬高模型对“结构连接词”和“可验证断言”的置信度，却压低对驱动多步搜索的 deliberation token（如“Wait”、“Let”）的置信度，导致自蒸馏信号与推理探索目标相悖。

方法：提出 Anti-Self-Distillation (AntiSD)，不再最小化学生与教师的散度，而是最大化散度（即 ascending divergence），从而反转每 token 的梯度符号，形成自然有界的优势函数。同时引入熵触发门控：当教师熵骤降时关闭 AntiSD 项，避免后期训练坍缩，作为默认自蒸馏的即插即用替代。

结果：在 4B 至 30B 参数规模的五个模型上，AntiSD 仅需 GRPO 基线的 1/10 到 1/2 训练步数即达到同等准确率，最终准确率最高提升 11.5 个百分点。
