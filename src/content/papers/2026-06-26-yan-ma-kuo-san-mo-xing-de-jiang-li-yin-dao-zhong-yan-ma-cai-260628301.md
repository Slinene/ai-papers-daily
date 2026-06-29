---
title: 'VGB for Masked Diffusion Model: Efficient Test-time Scaling for Reward Satisfaction
  and Sample Editing'
title_zh: 掩码扩散模型的奖励引导重掩码采样：高效测试时缩放与样本编辑
authors:
- Kijung Jeon
- Thuy-Duong Vuong
- Molei Tao
affiliations:
- Georgia Tech
- UCSD
arxiv_id: '2606.28301'
url: https://arxiv.org/abs/2606.28301
pdf_url: https://arxiv.org/pdf/2606.28301
published: '2026-06-26'
collected: '2026-06-29'
category: LLM
direction: 离散扩散模型推理缩放·奖励引导采样
tags:
- masked diffusion model
- test-time scaling
- reward-guided generation
- sample editing
- backtracking
- discrete diffusion
one_liner: 将回溯马尔可夫链扩展到掩码扩散模型，通过奖励引导的unmask/remask实现二次复杂度的推理时优化，理论上优于best-of-N
practical_value: '- 将奖励引导的重掩码迁移到广告文案、搜索词等序列生成任务中，利用可微分的过程奖励信号对生成样本进行局部编辑，避免全量重新生成，降低推理成本。

  - 在电商推荐Agent的决策序列生成中，可将业务指标（点击率、转化率）转化为奖励，通过MDM-VGB在线修复低质决策路径，提升推荐效果。

  - 理论上的二次复杂度保证，相比best-of-N采样能有效防止错误累积，适合高吞吐在线推理场景，工程实现可参考其unmask/remask动作选择逻辑。

  - 若生成任务存在硬约束（如query必须包含关键词、长度限制），可将约束作为可验证奖励，借鉴该方法在测试时生成满足约束的候选，无需重新训练模型。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：许多结构化生成任务需要满足全局约束或奖励优化，但过程验证器噪声大，常规best-of-N采样易导致错误累积，复杂度指数增长。
**方法**：针对掩码扩散模型（MDM），提出MDM-VGB采样器，将经典Jerrum-Sinclair回溯马尔可夫链从固定前缀树扩展到掩码状态图，允许在任意位置进行unmask和remask。采样时，根据当前部分配置的奖励价值，选择最优的unmask或remask动作，偏向高价值路径。理论上证明该方法对过程验证器噪声鲁棒，且计算复杂度为二次，而best-of-N可能达指数复杂度。
**结果**：在Sudoku约束满足和QM9分子生成任务上，MDM-VGB在生成高奖励样本和修复低质样本方面均显著优于已有基线，验证了其效率和效果。
