---
title: 'RREDCoT: Segment-Level Reward Redistribution for Reasoning Models'
title_zh: RREDCoT：面向推理模型的段级奖励再分配
authors:
- Mykyta Ielanskyi
- Kajetan Schweighofer
- Lukas Aichberger
- Sepp Hochreiter
affiliations:
- Johannes Kepler University Linz
- Cognizant AI Lab
- NXAI GmbH
arxiv_id: '2606.06475'
url: https://arxiv.org/abs/2606.06475
pdf_url: https://arxiv.org/pdf/2606.06475
published: '2026-06-04'
collected: '2026-06-05'
category: Training
direction: RL微调中的信用分配与奖励再分配
tags:
- Credit Assignment
- Reward Redistribution
- GRPO
- Chain-of-Thought
- Reinforcement Learning
- Language Model
one_liner: 利用语言模型自身近似最优奖励再分配，无需额外生成，提升GRPO等强化学习的样本效率。
practical_value: '- **多步推理Agent的奖励塑形**：可直接利用策略模型自身预估中间状态价值，避免额外价值网络或MC采样，适合长序列在线训练。

  - **高效分割策略**：混合关键词–熵合并的分割方法可为长文本生成任务（如商品描述生成、对话策略）提供廉价且有效的片段级奖励分配。

  - **自助奖励再分配**：当缺少参考解时，可用模型自身产生的正确答案进行奖励再分配，适配真实业务中无完美演示的场景。

  - **轻量实现**：仅需一次前缀前向传播即可获得片段级信用，KV复用使峰值显存不变，适合在现有GRPO等RL管线中快速集成。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
当前推理语言模型的RL微调普遍使用GRPO等蒙特卡洛方法，但面对长Chain-of-Thought（CoT）时，奖励仅在序列末尾给出且均匀分布，导致高方差和低样本效率。现有信用分配方案或需额外judge模型，或需昂贵的MC采样，难以在训练时大规模应用。

**方法关键点**  
- 将RUDDER的返回分解思想迁移到CoT生成MDP，推导出最优奖励再分配等价于相邻片段间价值函数之差，再由模型自身预估值函数进行近似。  
- 设计混合熵分割策略：先按关键词（如换行）初分段，再迭代合并总熵最低的相邻段，使片段间尽可能解耦，降低价值估计偏差。  
- 片段级立即价值估计：利用参考解（或模型自身正确回答）下的PR估计量，计算片段添加前后答案概率的变化，作为该片段的贡献；值项部分亦用同一模型快速计算，无需额外生成。  
- 将再分配权重嵌入通用策略梯度目标，保证返回等价，不影响最优策略。

**关键结果**  
- 在Numina‑CoT上使用Qwen3‑4B，最大生成长度25k token，RREDCoT在AIME24上从GRPO的0.850提升至0.908，MATH500从0.804提升至0.823，Minerva从0.915提升至0.935。  
- 小型实验（Qwen2.5‑1.5B，上下文1024）：RREDCoT‑Nano在AIME24得0.333，优于open‑rs的0.366，且训练步数更少。  
- 分析表明RREDCoT与昂贵MC采样的相关性高，但GPU耗时仅为MC的约1/10；其计算开销约为朴素GRPO的1.5‑2倍，但仍远低于MC。  
- 梯度归因与留一法归因高度相关，但与RREDCoT分配的相关性较低，证明纯归因方法不适合用作训练期的显式信用分配。

**一句话总结**  
RREDCoT利用语言模型自身的预估值函数，以极低计算代价将末端奖励有效分解到CoT片段，为长程推理RL训练提供了实用且高效的细粒度信用分配。
