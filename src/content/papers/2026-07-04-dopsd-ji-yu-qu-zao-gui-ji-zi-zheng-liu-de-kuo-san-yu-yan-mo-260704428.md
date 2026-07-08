---
title: 'dOPSD: On-Policy Self-Distillation for Diffusion Language Models'
title_zh: dOPSD：基于去噪轨迹自蒸馏的扩散语言模型训练方法
authors:
- Phuong Tuan Dat
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2607.04428'
url: https://arxiv.org/abs/2607.04428
pdf_url: https://arxiv.org/pdf/2607.04428
published: '2026-07-04'
collected: '2026-07-08'
category: Training
direction: 扩散语言模型 · 在线策略自蒸馏
tags:
- diffusion language model
- on-policy self-distillation
- privileged information
- trajectory-based distillation
- masked diffusion
- Jensen-Shannon divergence
one_liner: 将去噪轨迹的后续步骤作为特权信息进行在线自蒸馏，提升扩散语言模型的推理与泛化能力
practical_value: '- **为生成式推荐中的扩散模型提供训练思路**：若采用扩散模型生成Semantic ID或物品序列，可将解码轨迹的后续更“确信”状态作为教师信号，在掩码位置进行蒸馏，无须外部标注，实现纯在线自蒸馏，缓解曝光偏差。

  - **通用在线蒸馏技巧**：学生状态取随机真实解码步（非随机掩码完成序列），保证训练分布与推理一致。前向KL做主散度比反向KL更有效，因为可覆盖教师分布全貌，针对序列生成任务可优先选用。

  - **无标注场景也可用**：即使没有答案验证器，只从所有rollout中蒸馏仍能带来提升；验证器仅用于进一步筛选正确轨迹，可显著增加收益，但非强制，适用于推荐中缺乏强监督信号的情形。

  - **可迁移至Agent动作序列训练**：若将Agent行为建模为掩码序列去噪过程，可利用轨迹内后续步骤呈现的“全局视野”对早期动作提供弱监督指导，无需外部环境奖励或标注。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：扩散语言模型（dLLM）通过迭代去噪生成文本，具有并行解码和双向上下文的优势，但后训练提升推理能力困难。监督微调离线且受曝光偏差影响，强化学习奖励稀疏且难以适配无序列似然的扩散模型。在线自蒸馏（OPSD）虽能提供稠密、在线的逐token监督，但依赖外部参考解作为特权信息（PI），学生无法在推理时获知，最终蒸馏出的策略是各PI教师最软弱的“共识”，对数学推理这类实例特异性任务几乎无效。同时，简单将自回归OPSD的随机掩码方式移植到dLLM会导致训练失配。

**方法关键点**：
- 从学生模型自身的去噪轨迹中采样，将去噪过程中间步骤（掩码率高于阈值τ）作为学生输入，保证训练噪声分布与推理一致。
- 教师特权信息来自同一轨迹的后续步骤：对每个仍被掩码的位置，用未来步骤的预测分布取平均作为教师目标，构成一种“预瞄”优势，无需外部标签。
- 蒸馏损失采用广义Jensen-Shannon散度（前向KL为默认），仅正确rollout参与梯度更新（可选的答案验证器）。

**关键结果**：
- 在Dream-7B-Instruct和LLaDA-8B-Instruct上，dOPSD在GSM8K、MATH500上均获提升（Dream：83.04 vs 81.41, 42.20 vs 38.97；LLaDA：72.87 vs 71.23, 36.00 vs 31.24），且唯一在分布外代码生成（HumanEval、MBPP）上同时获得正收益。
- 对比SFT、GRPO、OPSD（仅答案/完整解）四种基线，所有基线均未提升甚至严重退化，其中OPSD（完整解）GSM8K暴跌15点以上。
- 消融实验证实：使用完整未来轨迹优于截断窗口；前向KL优于反向KL；即使去掉验证器，dOPSD仍能提升表现，说明轨迹自蒸馏信号本身即有效。
