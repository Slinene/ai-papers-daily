---
title: 'A Good Self-Teacher Meets the Student Where They Are: Joint On-Policy Learning
  and Teaching'
title_zh: 自教师与学生同步：联合在策略学习与教学
authors:
- Randy Ardywibowo
- Arnav Dalal
- Jiantao Jiao
affiliations:
- Perplexity
- NVIDIA
arxiv_id: '2610.10447'
url: https://arxiv.org/abs/2610.10447
pdf_url: https://arxiv.org/pdf/2610.10447
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: LLM 强化学习 · 自蒸馏训练
tags:
- On-Policy Distillation
- Self-Distillation
- Reinforcement Learning
- LLM Training
- Privileged Information
- KL Regularization
one_liner: 提出JOLT联合训练特权教师与无特权学生，使蒸馏梯度与奖励梯度一致，提升样本效率和最终性能
practical_value: '- 在训练LLM-based推荐/搜索/Agent模型时，若存在特权信息（如用户真实反馈、人工标注、高质量参考），可采用JOLT模式：同一模型联合训练特权教师和无特权学生，教师用KL正则化向学生，避免教师走捷径导致蒸馏信号与奖励梯度相悖。

  - 对于稀疏奖励的长程任务（如多轮对话推荐、会话转化优化），JOLT的密集token级监督可大幅提高样本效率；教师可接收用户反馈摘要、历史成功策略等作为privileged
  context。

  - 工程实现简单：共享参数的教师和学生分别生成轨迹，使用logprob ratio作为token权重，结合group advantage归一化，无需额外教师模型。

  - 超参数经验：教师KL β_T 和学生蒸馏 β_S 宜设较小值（如β_T=0.001~0.03, β_S=0.1），过大会训练不稳定；学生奖励可用时，JOLT+补充直接RL可进一步提升。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
LLM强化学习常依赖稀疏终局奖励，在长程、困难任务上样本效率低。On-Policy Distillation (OPD) 提供密集token级监督，但自蒸馏（privileged self-distillation）容易失败：特权信息可能让教师走捷径，其产生的监督与学生当前行为不匹配，即使教师自身表现更好，蒸馏更新也可能降低学生期望奖励。

**方法关键点**  
- 将教师质量定义为“奖励一致性”：推导出教师local OPD更新与学生奖励梯度成正比的充要条件；点态充分构造表明理想教师是学生策略的advantage指数加权（相当于KL正则化策略改进）。  
- 提出JOLT：共享参数的单一模型扮演两个角色——特权教师（接收privileged context c）用outcome reward + KL正则化向学生；无特权学生用on-policy蒸馏学习教师logprob ratio。两角色从各自生成的轨迹学习，保持on-policy。  
- 教师训练目标：最大化期望advantage 减 β_T·KL(teacher||student)；学生目标：β_S·(teacher logprob - student logprob)；JOLT+额外加入学生outcome reward advantage。实际使用group-based reward centering降低方差。

**关键实验**  
在GSM8K、MATH、LiveCodeBench-v6、AppWorld、Terminal-Bench上与GRPO、OPSD、π-Distill对比。MATH上JOLT无直接学生奖励，用13×更少completion tokens、6.5×更少processed training tokens达到GRPO匹配精度；JOLT+绝对提升：MATH +4.2%、LCBv6 +3.0%、AppWorld +9.9%、Terminal-Bench pass@32 +4.5%。训练中教师-学生KL下降，梯度bias-variance分析显示JOLT低方差低偏差。

**最值得记住的一句话**  
好的自教师应当“meets the student where they are”：教师不仅要在任务上表现好，还要保持与学生当前策略接近，这样产生的密集蒸馏信号才与学生的奖励梯度方向一致。
