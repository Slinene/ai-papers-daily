---
title: Improving General Role-Playing Agents via Psychology-Grounded Reasoning and
  Role-Aware Policy Optimization
title_zh: 基于心理学推理与角色感知策略优化的通用角色扮演智能体
authors:
- Zhenhua Xu
- Dongsheng Chen
- Jian Li
- Yitong Lin
- Zhebo Wang
- Jiafu Wu
- Yizhang Jin
- Chengjie Wang
- Meng Han
- Yabiao Wang
affiliations:
- Zhejiang University
- Tencent Youtu Lab
arxiv_id: '2606.27025'
url: https://arxiv.org/abs/2606.27025
pdf_url: https://arxiv.org/pdf/2606.27025
published: '2026-06-25'
collected: '2026-06-26'
category: Agent
direction: 心理学引导推理与角色感知强化学习
tags:
- role-playing agents
- chain-of-thought
- reinforcement learning
- mutual information
- policy optimization
- reward hacking
one_liner: 提出心理学引导的CoT与基于互信息的策略优化，抑制奖励黑客，提升角色保真度。
practical_value: '- **对话推理结构可复用**：Psy-CoT 将回复前思考分解为交互感知、心理共情与逻辑构建三步，电商虚拟导购、客服机器人可借鉴该链式推理，生成更贴近用户心理、更具说服力的对话。

  - **互信息梯度加权抑制奖励黑客**：RAPO 用 profile–token 互信息不对称缩放梯度，放大角色相关 token 的正优势、衰减负优势，该技巧可迁移到任意
  LLM 对齐任务（如推荐解释生成、广告文案优化），防止模型学得空洞通用回复而冲高奖励。

  - **训练不稳定时的干预思路**：当发现 LLM 奖励模型给出相同梯度信号导致性能退化，可引入类似 RAPO 的 token 级重要性加权，无需改变奖励模型，仅调整策略梯度，工程成本低。

  - **多尺度模型验证**：实验在多种模型规模上均超越 GRPO，证明该策略优化方法对基座能力不敏感，适合在推荐/对话系统实际部署中逐步升级基座模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：通用角色扮演代理（RPA）依靠自然语言角色设定扮演任意人物，现有监督微调方法仅模仿表面行为而非深层思考，导致分布外泛化差；同时强化学习对齐时，LLM 奖励模型无法区分真正角色特定短语与通用奖励黑客短语，两者获得相同梯度信号，训练中误导模型。

**方法**：提出 Psy-CoT，一种心理学引导的链式思考框架，将回复前推理分解为三个角色特定步骤——交互感知（理解上下文意图）、心理共情（推断角色心理状态）和逻辑构建（组织符合角色设定的回应），使模型动态思考而非机械模仿。进一步提出 Role-Aware Policy Optimization (RAPO)，利用角色设定与 token 之间的互信息构建不对称梯度权重：当优势为正时放大角色相关 token 的梯度，优势为负时衰减，从而在策略优化中强化角色特征、抑制通用短语。

**结果**：在 CoSER、CharacterBench 和 CharacterEval 三个基准上，Psy-CoT 超越现有角色扮演 CoT 方法，RAPO 在不同模型规模下一致优于 GRPO 等基线，角色保真度和对话质量显著提升。
