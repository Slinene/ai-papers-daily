---
title: Generalizable VLA Finetuning via Representation Anchoring and Language-Action
  Alignment
title_zh: 通过表示锚定和语言-动作对齐实现可泛化的VLA微调
authors:
- Dwip Dalal
- Shivansh Patel
- Chahit Jain
- Jeonghwan Kim
- Utkarsh Mishra
- Alex Baratian
- Hyeonjeong Ha
- Heng Ji
- Svetlana Lazebnik
- Unnat Jain
affiliations:
- University of Illinois Urbana-Champaign
- Texas A&M University
- University of California, Irvine
arxiv_id: '2607.13429'
url: https://arxiv.org/abs/2607.13429
pdf_url: https://arxiv.org/pdf/2607.13429
published: '2026-07-14'
collected: '2026-07-25'
category: Agent
direction: 具身Agent微调：表示蒸馏与动作离散化
tags:
- Vision-Language-Action
- Behavior Cloning
- Representation Anchoring
- Language-Action Alignment
- Catastrophic Forgetting
- Robot Manipulation
one_liner: 提出Anchor-Align，用表示锚定和语言-动作对齐防止VLA微调中的灾难性遗忘，提升机器人操作泛化能力
practical_value: '- **多模态对话Agent的连续动作离散化**：可将连续动作空间（如推荐系统中的出价、调价）转化为离散方向标签，与语言生成任务联合训练，提升策略的对齐性和解释性。

  - **微调中防止预训练表示遗忘**：在电商搜索LLM微调时，可引入表示锚定损失（蒸馏冻结模型的中间层），保留通用语义知识，提升OOD泛化能力。

  - **离线强化学习/模仿学习的稳定性**：对于从日志数据模仿推荐的Agent，该方法可防止分布漂移，尤其适用于长期序列决策的推荐场景。

  - **主要用于具身智能，电商直接迁移有限**：核心贡献在机器人控制，但其中表示蒸馏和离散动作对齐的思想可跨领域借鉴。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：用行为克隆（BC）微调预训练VLM得到VLA策略已成为标准范式，但BC会逐步覆盖预训练的语义和视觉表示，损害泛化能力。现有在网页数据上联合训练的方式仍存在语言-动作不对齐，且标准评估不暴露该问题。

**方法**：提出Anchor-Align，在BC基础上增加两个目标：(1) **Vision-Language Anchoring**：冻结一个VLM副本，对每一层进行表示蒸馏，防止表示漂移；(2) **Language-Action Alignment**：将连续动作离散化为运动方向标签，在同一观测上联合训练语言输出和动作预测，实现语言-动作紧耦合。

**结果**：在xArm7真实机器人上，两种主流VLA架构成功率分别从28%提升至54%和37%提升至60%。在LIBERO-PRO、LIBERO-Plus和CALVIN三个大规模仿真环境中，对OOD扰动、感知鲁棒性和长程任务均有显著改善，表明保留预训练表示与有效动作学习并不矛盾。
