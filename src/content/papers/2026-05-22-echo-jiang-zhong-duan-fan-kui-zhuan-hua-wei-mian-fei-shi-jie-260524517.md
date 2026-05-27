---
title: 'ECHO: Terminal Agents Learn World Models for Free'
title_zh: ECHO：将终端反馈转化为免费世界模型训练的智能体强化学习
authors:
- Vaishnavi Shrivastava
- Piero Kauffmann
- Ahmed Awadallah
- Dimitris Papailiopoulos
affiliations:
- Microsoft Research
arxiv_id: '2605.24517'
url: https://arxiv.org/abs/2605.24517
pdf_url: https://arxiv.org/pdf/2605.24517
published: '2026-05-22'
collected: '2026-05-27'
category: Agent
direction: 终端智能体 · 稀疏奖励 · 世界模型
tags:
- GRPO
- world model
- terminal agents
- auxiliary loss
- environment prediction
- reinforcement learning
one_liner: ECHO在GRPO中增加环境观测token的交叉熵损失，将终端输出变为稠密监督，在TerminalBench-2.0上pass@1翻倍。
practical_value: '- 业务中若存在交互式环境（如对话Agent、推荐模拟器），可将环境返回的文本（如用户反馈、系统日志）直接作为辅助预测目标，在RL损失中加入交叉熵项，为失败样本提供稠密梯度，加速策略学习。

  - 该方法仅需修改损失掩码，重用已有前向计算，无需额外模型或rollout，工程实现成本极低，适合在现有GRPO或PPO训练流程中快速试验。

  - 在电商对话或任务型Agent中，可将用户对每次回复的直接反应（如点击、评价文本）作为“环境观测token”，训练模型预测自身行为的后果，隐式学习用户模型，从而减少对稀缺成功轨迹的依赖。

  - 入的“无验证器适应”实验表明，即使没有奖励信号，仅凭预测环境反馈也能在OOD任务上持续改进，这为在线持续学习或冷启动场景提供了思路：可在无人工标注时仅通过模拟交互提升模型。'
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机
标准GRPO在训练终端智能体时，只对助手动作施加稀疏奖励的梯度，大量失败轨迹中的终端输出（stdout、错误、文件内容）虽被模型前向计算却未参与损失，形成巨大的监督浪费。论文指出这些输出是环境对动作的直接响应，预测它们等价于学习一个隐式世界模型，能为策略提供密集反馈，尤其在仅少数rollout能成功的稀疏奖励场景下意义重大。

## 方法关键点
- **混合目标（ECHO）**：在GRPO的动作策略梯度损失上，增加一个辅助交叉熵项 `L_Env`，要求模型预测自身动作引起的环境观测token。
- **损失共享前向**：直接复用GRPO前向中已计算的logits，仅需在环境token位置收集损失，无需第二次前向或额外rollout。
- **目标选择**：仅对终端输出token（env tokens）计算损失，排除低熵的格式警告前缀，避免梯度快速消失。
- **权重与自适应**：固定系数 λ=0.05，因环境预测损失随训练下降，天然具有退火效果。
- **全训练兼容**：与GRPO的稳定化技术（如DAPO、留空过滤等）正交，可直接叠加。

## 关键实验
- **测试基准**：内部val100、ITD、TBLite及公开TerminalBench-2.0（TB2），基模型为Qwen3-8B和Qwen3-14B。
- **主要结果**：ECHO几乎使所有基模型的TB2 pass@1翻倍（Qwen3-8B 2.70%→5.17%；Qwen3-14B 5.17%→10.79%），并在内部评测上全面提升。
- **世界模型验证**：在强模型（Qwen3-32B）生成的离线轨迹上，ECHO将环境token交叉熵大幅降低（如14B模型从0.24降至0.07），GRPO几乎不变，证明学到了可迁移的终端动态。
- **降低专家示范依赖**：未使用专家SFT的Qwen3-8B+ECHO，在内部评测上追平了专家SFT+GRPO的表现，在TB2上也收复了约50%的专家初始化优势。
- **无验证器自改进**：仅用环境预测损失（λ单独作用）即可在分布内和部分OOD任务（如PyTerm）上带来+3.8pp至+10pp的提升，证明环境反馈本身就是有力的监督信号。

值得记住的核心结论：环境反馈不仅是上下文，更是密集、在线、可免费利用的训练信号，预测自身行为的后果即可将稀疏强化学习转化为更高效的深度理解任务。
