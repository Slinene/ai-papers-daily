---
title: Reinforcement Learning for Computer-Use Agents with Autonomous Evaluation
title_zh: 面向计算机使用代理的自主评估强化学习
authors:
- Marta Sumyk
- Oleksandr Kosovan
affiliations:
- Ukrainian Catholic University, Lviv, Ukraine
arxiv_id: '2606.24515'
url: https://arxiv.org/abs/2606.24515
pdf_url: https://arxiv.org/pdf/2606.24515
published: '2026-06-23'
collected: '2026-06-25'
category: Agent
direction: GUI代理 · 噪声奖励校正
tags:
- Reinforcement Learning
- GUI Agent
- Vision-Language Model
- Reward Modeling
- Noise Correction
- Autonomous Evaluation
one_liner: 用VLM作为不完美奖励信号的噪声校正强化学习，显著提升GUI代理任务成功率
practical_value: '- 当无法获得密级标签或手工奖励函数时，可以用 **VLM 评分作为稀疏奖励** 来微调 Agent 策略，尤其适合 UI 自动化、电商操作机器人等视觉交互任务

  - 将 VLM 评估视为带噪声的二元信道，推导出 **PPO 中噪声校正奖励估计器** 的思路，可直接复用于任何依赖不完美自动评估的 RL 训练，例如用 LLM
  评价对话质量或推荐解释

  - 实验中噪声校正明显优于直接用原始评估奖励（+5.1pp），提示在落地类似方案时，**必须对自动评估器的误差建模**，否则噪声会削弱甚至误导策略学习

  - 该方法解耦了任务评估与策略优化，意味着可以 **快速迭代评估器**（更换 VLM 或 prompt）而不必改动 Agent 架构，适合工程中渐进式优化'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：GUI 代理（CUA）通过视觉感知直接操作界面执行自然语言指令，但强化学习受制于奖励信号难以规模化——任务成功往往依赖视觉判断，难以手工编写奖励函数或获取密集人工标注。

**方法**：用视觉-语言模型（VLM）查看代理执行后的最终截图和原始指令，输出“成功/失败”二元判断作为终端奖励。由于 VLM 评估并不完美，论文将其建模为有噪声的二进制信道，并推导出适用于 PPO 的噪声校正奖励估计器。整个过程无需任务专属启发式或人工标注，实现可扩展的自主评估。

**结果**：在 macOSWorld、Windows Agent Arena 和 OSWorld 三个基准上，噪声校正的评估奖励微调比零样本代理平均成功率提高 12.6 个百分点，比直接使用原始 VLM 奖励微调提高 5.1 个百分点，证明对评估器噪声的显式建模能有效提升策略质量。
