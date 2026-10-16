---
title: 'Towards Continual Learning: Mitigating Forgetting With Subspace Tuning'
title_zh: 面向持续学习：通过子空间调优减轻遗忘
authors:
- Arnav Chavan
- Kusha Sareen
- Rishabh Tiwari
- Abhranil Chandra
- Johan Obando-Ceron
- Kurt Keutzer
- Scott Niekum
- Inderjit S Dhillon
- Devvrit Khatri
affiliations:
- UC Berkeley
- Mila
- McGill University
- Université de Montréal
- UMass Amherst
arxiv_id: '2610.22293'
url: https://arxiv.org/abs/2610.22293
pdf_url: https://arxiv.org/pdf/2610.22293
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: 持续学习 · 子空间约束微调
tags:
- Catastrophic Forgetting
- Subspace Tuning
- Continual Learning
- Fine-tuning
- SVD
- Optimizer
one_liner: 通过将权重更新限制在低能量奇异子空间，SST 有效减轻 LLM 微调中的灾难性遗忘
practical_value: '- 在业务中微调 LLM 以适应新领域或任务时，可引入 SST 保护已有通用能力，避免上线后基础能力下降，尤其适用于需要持续更新的推荐/广告模型。

  - SST 与优化器无关，只需对优化器最终更新做投影，可直接嵌入现有 SFT/RLHF 流程，无需修改损失函数或数据，工程实现成本低。

  - 保护主导奇异方向可显著减少对基模型的 KL 漂移（2-4 倍），有助于保持输出分布的稳定性，对在线学习或 A/B 测试更友好。

  - 在顺序学习多领域任务时，SST 能够累积能力而非互相覆盖，适合构建多能力融合的模型或专家合并场景。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：
LLM 通过微调获取新技能时常导致灾难性遗忘，尤其是 SFT 会严重损害已有能力。现有 on-policy 方法（如 RL、SDFT）间接缓解遗忘，但在长推理等场景下仍存在明显遗忘。作者假设保护预训练权重的主导奇异子空间可以保留已有能力，同时低能量子空间有足够容量学习新任务。

方法关键点：
1. SST (Subspace Tuning) 对每个权重矩阵 W 的优化器更新 ΔW 进行双边投影：Π(ΔW) = (I - UkUk^T) ΔW (I - VkVk^T)，其中 Uk, Vk 为 W 的 top-k 左右奇异向量。投影移除所有涉及主导方向的更新分量。
2. 投影作用于优化器最终更新而非原始梯度，因为 Adam 等有状态优化器会使投影梯度泄漏到受保护方向。控制实验表明，仅投影更新可实现零泄漏且对基模型影响最小。
3. 使用 refresh 机制：每 K 步重新计算当前权重的 SVD 并更新保护基底，平衡适应性与保留性。默认 r=0.99（保护 99% 方向），可配合 R10/R100 等刷新频率。
4. 方法优化器无关，可组合 SFT、SDFT、Muon 等常见微调配方。

关键实验与结果：
在 Qwen3-8B 等模型上，对 Science、Finance、Pathology、Medicine 四个领域进行微调。即使保护 99% 的奇异方向，SST 仍匹配无约束微调的新任务准确率，同时先前能力退化从 SFT 的 30-40 点降至约 1-5 点。模型规模从 1.7B 到 14B，SST 遗忘进一步减少，8B 以上几乎消除。数据规模扩展下，SST 保持稳定而 SFT 持续退化。SST 使模型 KL 漂移减少 2-4 倍，并在顺序微调（两/三阶段）中实现能力累积。与 Sculpting、OPLoRA 等方法相比，SST 保护更彻底，遗忘更少。

核心结论：灾难性遗忘并非学习的必然代价，通过约束更新到权重的低能量子空间，可以在学习新任务的同时有效保留已有能力。
