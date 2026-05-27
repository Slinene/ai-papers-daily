---
title: 'Learning to Act under Noise: Enhancing Agent Robustness via Noisy Environments'
title_zh: 噪声环境下行动学习：通过带噪交互增强智能体鲁棒性
authors:
- Yuxin Chen
- Xiaodong Cai
- Junfeng Fang
- Zhuowen Han
- Yu Wang
- Yaorui Shi
- Yi Zhang
- Qi Gu
- Xunliang Cai
- Xiang Wang
affiliations:
- National University of Singapore
- Meituan
- Tsinghua University
- Tianjin University
- University of Science and Technology of China
arxiv_id: '2605.27209'
url: https://arxiv.org/abs/2605.27209
pdf_url: https://arxiv.org/pdf/2605.27209
published: '2026-05-26'
collected: '2026-05-27'
category: Agent
direction: Agent 鲁棒训练 · 噪声注入与课程调度
tags:
- Agent
- Robustness
- Noise Injection
- Reinforcement Learning
- GRPO
- Curriculum Learning
one_liner: 在 Agent RL 训练中模拟用户与工具侧噪声，结合混合轨迹与课程调度，显著提升现实噪声下的性能与泛化能力。
practical_value: '- 在训练电商客服或推荐 Agent 时，可人工构造**模糊/不一致/冗余的用户指令**，以及**工具返回错误、不完整或误导信息**，让模型在训练中就接触真实噪声模式。

  - 采用**混合轨迹训练**：每 batch 中保留一部分干净轨迹，部分加入噪声，并在组内分别归一化优势，避免噪声样本主导梯度更新。

  - 按**性能差距（∆）动态调整噪声**：当模型在噪声与干净环境下的成功率差低于阈值时，增大噪声比例与难度，形成平稳的课程学习，防止初期训练崩溃。

  - 即使最终只关心干净环境下的表现，这种训练仍可作为**隐式数据增强**，提升 Agent 的泛化推理与纠错能力，在标准 benchmark 上也能获得稳定增益。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
现有 LLM Agent 训练依赖理想化的指令和稳定的工具执行，但在真实部署中，用户提问常带模糊、冲突或冗余，工具也可能失败或不完整，导致性能大幅下降。作者指出，这种训练与部署之间的噪声差距是 Agent 鲁棒性不足的关键，亟需在训练中显式建模环境噪声。

**方法**  
提出 NoisyAgent，包含：  
1. **自动噪声注入**：识别两类噪声——**用户侧**（意图模糊、不一致、冗余）和**工具侧**（失败、结果截断、误导、冗余），用模板或模型生成扰动后的指令和工具响应。  
2. **混合训练与组内归一化**：每个任务并行采样 N 条轨迹，其中 N_noise 条注入噪声，其余保持干净。在 GRPO 中，对噪声组和干净组分别计算优势与均值方差，防止噪声轨迹稀释优化信号或引发训练震荡。  
3. **自适应课程调度**：用干净与噪声轨迹的成功率差 ∆ 衡量模型对当前噪声的适应度，当 ∆ < θ 时，逐步提高噪声比例（上限 50%）和扰动强度，形成从易到难的课程。  

**关键实验**  
在 AgentNoiseBench 和标准基准 τ²-Bench/VitaBench 上评估，覆盖零售、航空、电信等 6 个领域，基座为 Qwen3-8B/32B。与 GRPO、DAPO、GSPO 对比：  
- NoisyAgent 在噪声环境下（AgentNoiseBench）显著领先，例如在 8B 模型上，Retail 域 Avg@4 提升至 36.40%（GRPO 为 30.48%），Pass@4 从 50.88% 升至 61.40%；在 32B 模型上，Retail 域 Avg@4 从 38.16% 升至 43.20%。  
- 在理想化基准上同样有增益：8B 模型在 Retail 域 Avg@4 从 46.05% 升至 47.59%，Pass@4 从 73.68% 升至 77.19%；32B 模型 Retail 域从 58.11% 升至 60.31%。  
- 消融表明，取消混合训练（全噪声）导致最大性能下降，证明受控注入的必要性；课程调度也进一步带来提升。  
- 行为分析显示，噪声训练后 Agent 在工具调用次数上减少 18%，回复长度增加 2.1 倍，交互更高效、清晰。  

**核心洞察**  
在训练过程中谨慎引入结构化噪声并动态调整，不仅能提升 Agent 对真实世界扰动的鲁棒性，还能通过隐式难度增强提升其在干净环境下的通用能力。
