---
title: Amortizing Sequential Experimental Design in Reasoning LLMs
title_zh: 将序贯实验设计摊销到推理LLM中
authors:
- Anita Kriz
- Antonin Berthon
- Nicolás Astorga
- Mihaela van der Schaar
affiliations:
- University of Cambridge
arxiv_id: '2610.20832'
url: https://arxiv.org/abs/2610.20832
pdf_url: https://arxiv.org/pdf/2610.20832
published: '2026-10-13'
collected: '2026-10-30'
category: Agent
direction: Agent 自适应信息收集与提问策略训练
tags:
- Sequential Experimental Design
- Bayesian Experimental Design
- Information Gain
- LLM Agent
- Reinforcement Learning
one_liner: 用信息增益奖励训练LLM进行自适应信息收集，在低计算成本下超越BED基线并跨域迁移
practical_value: '- 对话推荐/澄清场景中，可用信息增益作为 reward 训练 LLM 生成提问，快速锁定用户偏好，减少冗余交互。

  - 将实验生成模型与 LLM 自身信念解耦，避免依赖 LLM 可能校准差的后验，用外部模型计算期望信息增益更稳定。

  - 摊销策略使推理时无需在线规划或重采样，直接生成下一个问题，显著降低计算成本，适合线上实时对话系统。

  - 从简单游戏（Twenty Questions）训练的策略能迁移到临床对话，说明信息收集技能可跨域迁移；电商中可在模拟环境预训练提问策略再迁移到真实对话。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 拥有大量先验知识和推理能力，但在序贯实验设计（如临床诊断中逐步询问症状）中难以自适应地收集信息。现有 BED 方法通常在线规划成本高，或依赖 LLM 自身不佳的概率校准。

**方法**：提出将序贯贝叶斯实验设计（BED）摊销到 LLM 中，显式训练其推理过程以信息增益作为 reward 来指导动作选择。关键技术点：将实验生成模型与 LLM 自身信念解耦，使优化目标基于选定模型下的期望信息增益，而非 LLM 内部概率；研究了生成模型构造、奖励估计、假设空间规格、多步目标等设计选择。

**结果**：在 Twenty Questions 任务上，训练后的策略显著提升信息获取和任务性能，优于推理时和训练时 BED 基线，且计算成本大幅降低；同时能泛化到未见类别。进一步，从 Twenty Questions 训练的策略正向迁移到真实临床对话基准 Medi-Q，证明信息收集可被学习为 LLM 中可泛化的推理技能。
