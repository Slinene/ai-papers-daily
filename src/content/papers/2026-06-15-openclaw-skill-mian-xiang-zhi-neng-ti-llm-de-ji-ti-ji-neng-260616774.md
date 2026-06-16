---
title: 'OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models'
title_zh: OpenClaw-Skill：面向智能体 LLM 的集体技能树搜索框架
authors:
- Tianyi Lin
- Chuanyu Sun
- Jingyi Zhang
- Changxu Wei
- Huanjin Yao
- Shunyu Liu
- Xikun Zhang
- Liu Liu
- Jiaxing Huang
affiliations:
- The Hong Kong Polytechnic University
- Nanyang Technological University
- Tsinghua University
- Royal Melbourne Institute of Technology
- Beijing University of Aeronautics and Astronautics
arxiv_id: '2606.16774'
url: https://arxiv.org/abs/2606.16774
pdf_url: https://arxiv.org/pdf/2606.16774
published: '2026-06-15'
collected: '2026-06-16'
category: Agent
direction: 集体技能树搜索与强化学习框架
tags:
- Skill Tree
- Collective Intelligence
- LLM Agents
- Reinforcement Learning
- Tool Use
- Multi-Model
one_liner: 利用多模型集体智能构建结构化、多样且可迁移的技能树，并配合跨技能对比的强化学习，显著提升 LLM 智能体在长程工具使用任务上的表现
practical_value: '- **复杂推荐流程的工序化拆解**：将多步骤推荐任务（如 Query 理解→候选召回→重排序→解释生成）显式分解为子任务，对每个子任务构建技能节点，形成可组合的推荐技能树，避免长流程的碎片化推理。

  - **多模型轨迹蒸馏生成多样技能**：在电商/搜索场景中，利用多个不同偏好或规模的 LLM 对同一子任务生成执行轨迹，再蒸馏为候选技能，能显著提升技能覆盖度，防止技能集过度拟合单一模型的推理风格。

  - **技能迁移性评估确保跨模型复用**：采用「技能合成模型≠验证模型」的迁移性评分，可筛选出真正通用的推荐技能。这在推荐 Agent 需要部署在不同 backbone
  LLM 上时尤其有价值，避免反复定制。

  - **技能条件下的跨分支对比 RL 训练**：在推荐策略优化中，不局限于单个技能，而是对多个备选技能分别 rollout，并基于跨技能归一化优势进行 GRPO
  更新，迫使策略学会在不同场景下自适应选择最优技能，避免陷入单一策略的局部最优。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前 LLM 智能体技能构建主要存在三个痛点：(1) 技能碎片化，仅捕获局部子任务的孤立过程，缺乏跨步骤的组合与依赖管理；(2) 技能多样性不足，通常由单一模型的轨迹提炼，带有明显偏好偏差；(3) 技能迁移性差，切换到不同 backbone LLM 时性能下降明显。这些问题限制了技能在长程交互环境（如 OpenClaw）中的复用与扩展。

### 方法
提出 **Collective Skill Tree Search (CSTS)**，核心是利用多模型集体智能迭代搜索并构建结构化、多样且可迁移的技能树。
- **任务分解**：将复杂任务拆分为有序子任务序列，确定技能树的层数。
- **集体技能节点生成 (CSN-Gen)**：多个异构模型对同一子任务各自执行并产生轨迹，经统一的技能合成器提炼为候选技能节点，覆盖更广的规划、诊断与恢复模式。
- **集体技能节点评估 (CSN-Assess)**：通过两个分数筛选节点——① 集体质量评分：多个裁判模型独立评价技能的清晰性、可执行性、完整性和相关性，取均值；② 集体迁移性评分：技能由模型 A 生成后，在其余模型上执行同一子任务并统计成功率，衡量技能跨模型的泛化能力。两者相加选出最优技能节点，形成子任务间的有序技能路径。
- **训练数据构建**：用选出的最佳技能路径和对应轨迹构造 SFT 数据，进行监督微调。
- **集体技能强化学习 (CSRL)**：对每个子任务，从技能集中采样多条技能条件 rollout，在集体 rollout 组内计算跨技能归一化优势，采用 GRPO 目标优化策略，使模型主动偏好更高效、可迁移的技能策略。

### 关键实验
在 QwenClawBench 和 PinchBench（23/123 任务版本）上评估，覆盖文件操作、代码执行、网页交互、多步决策等。
- QwenClawBench：OpenClaw-Skill 将 Qwen3.5-9B 总分从 34.5 提升至 44.9（+10.4），Qwen3.5-4B 从 31.5 提升至 41.2（+9.7），尤其在 SVM（30.2→78.4）和 CS（33.2→70.9）等长程工具使用类别上提升巨大。
- PinchBench 123 任务版：9B 模型 best score 从 61.1→68.2，平均从 47.1→53.6；4B 模型平均从 45.9→47.6。
- 消融证实 CSN-Gen 单步提升 5.3 分，加 CSN-Assess 再涨 3.0 分，最后 CSRL 带来额外 2.1 分，各组件均有效。

### 核心洞察
通过多模型集体搜索构建的树状技能结构和跨技能对比的强化学习，将长程任务的成功率瓶颈从「产生一个技能」转移到「从多样技能中自适应选择最优组合」，是对智能体可复用知识库设计的直接升级。
