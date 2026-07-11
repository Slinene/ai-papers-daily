---
title: 'Feedback Manipulation Regularization: Enabling Offline Agent Alignment for
  Imitation Learning'
title_zh: 反馈操纵正则化：实现离线模仿学习 Agent 对齐
authors:
- Benjamin Poole
- Minwoo Lee
affiliations:
- University of North Carolina at Charlotte
arxiv_id: '2607.07859'
url: https://arxiv.org/abs/2607.07859
pdf_url: https://arxiv.org/pdf/2607.07859
published: '2026-07-08'
collected: '2026-07-11'
category: Agent
direction: 离线 Agent 对齐 · 模仿学习正则化
tags:
- offline RL
- alignment
- imitation learning
- feedback regularization
- Safety Gymnasium
one_liner: 将评估反馈作为纠正信号融入模仿学习，在序列决策环境中实现离线对齐，最多减少 98% 未对齐行为
practical_value: '- 在离线推荐策略学习中，可将用户行为序列视为演示，将显式反馈（如评分、停留时长）作为纠正信号，通过类似 FMR 的正则项微调模仿学习模型，提升策略与真实偏好的对齐度。

  - FMR 的算法无关设计可作为插件直接嵌入现有离线 RL 推荐框架，无需改动原算法结构，降低工程落地门槛。

  - 论文在有限数据和噪声演示下的鲁棒性结果，对稀疏反馈或冷启动推荐场景有借鉴意义，可尝试在数据匮乏时引入反馈正则化稳定训练。

  - Safety Gymnasium 中定义的对齐评估指标（如约束违反率）可启发推荐系统设计安全约束，避免推荐内容越界（如低质、违规内容），在 Agent 辅助的对话推荐中尤为重要。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：现有方法将人类演示和评估反馈割裂使用，且多局限于语言生成的 bandit 场景，尚未充分挖掘二者在完全序列决策中的协同信号。本文希望将这两种模态统一为离线训练中的互联纠正信号，提升模仿学习策略的对齐水平。

**方法**：提出算法无关的 Feedback Manipulation Regularization (FMR)，在模仿学习的损失函数中引入一个反馈驱动的正则项：对收集到的反馈（如偏好标签）进行建模，将其作为策略偏离期望行为的惩罚，从而在离线阶段直接修正策略。该方法无需在线交互或多阶段管线，可直接作用于各类模仿学习算法。

**结果**：在 Safety Gymnasium 环境中（适配为对齐测试床），FMR 使多种模仿学习算法的 misalignment 最高降低 98%，同时保持或提升任务完成能力；在只有少量对齐演示和大量噪声演示的有限数据设置下，FMR 仍能稳定减少未对齐行为，表现出良好的数据效率。
