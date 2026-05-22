---
title: 'Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning'
title_zh: Search-E1：自蒸馏驱动搜索增强推理的自进化
authors:
- Zihan Liang
- Yufei Ma
- Ben Chen
- Zhipeng Qian
- Xuxin Zhang
- Huangyu Dai
- Lingtao Mao
arxiv_id: '2605.22511'
url: https://arxiv.org/abs/2605.22511
pdf_url: https://arxiv.org/pdf/2605.22511
published: '2026-05-21'
collected: '2026-05-22'
category: Agent
direction: 搜索增强推理 Agent 自进化训练
tags:
- Self-Distillation
- GRPO
- Search-Augmented Reasoning
- OFSD
- Process Supervision
- Multi-Hop QA
one_liner: 通过交替 GRPO 与离线自蒸馏，从同一问题的正负轨迹对中提取 token 级监督，无需外部教师或奖励模型
practical_value: '- **从轨迹对中生成 token 级细粒度信号**：在搜索、对话等多步 Agent 训练中，正例轨迹的某一步往往比负例轨迹的对应步更优。可以用离线自蒸馏从正负轨迹对中学习
  step-wise 差异，无需额外训练过程奖励模型，降低工程成本。

  - **GRPO 与自蒸馏交替训练，避免干扰在线探索**：Search-E1 的离线自蒸馏轮次完全独立于 GRPO 的 rollout 采样，不改变 RL 的训练动态，可以作为现有
  GRPO 训练流程的插件式增强，适用于电商搜索、推荐等场景中逐步提升 agent 的决策粒度。

  - **利用同一模型的 privileged context 进行知识蒸馏**：将更优轨迹作为 prompt 前缀送入同一模型，让学生分布逼近教师分布，不需额外存储或调用外部模型，适合线上模型迭代。

  - **多轮自进化循环，适合持续优化**：随着训练的进行，可以从日益稳定的 rollout 池中挖掘新的 pair 持续进行自蒸馏，适合推荐系统或搜索 Agent
  在用户反馈闭环中在线持续学习。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
当前的搜索增强推理 Agent（如 Search-R1）通常用 GRPO 进行端到端强化学习，但仅基于最终答案的 outcome reward 会忽略中间搜索步骤的质量差异。许多工作通过外部强模型、过程奖励模型或手工奖励设计来提供步骤级监督，但引入了大量额外训练开销和资源依赖。本文观察到，在同一问题的多个 rollout 中，正例轨迹与负例轨迹在搜索步上存在天然对比，可以从中提取步骤级信号，无需外部监督即可驱动自进化。

**方法关键点**  
- **Search-E1 自进化管线**：交替执行标准 GRPO 轮次和离线自蒸馏（OFSD）轮次。  
- **OFSD 机制**：从刚结束的 GRPO 轮次产出的 rollout 池中，为每个问题选择一对 (reference, student) 轨迹。reference 是正确且搜索次数最少的轨迹，student 是错误或与 reference 差异最大的轨迹。  
- **非对称条件化**：让学生仅以问题和指令为输入，教师则额外获得 reference 轨迹作为前缀（privileged context），两者共享模型参数，并在 student 生成的 token 序列上计算前向 KL 散度损失（带逐项截断）。  
- **实现**：OFSD 使用 LoRA adapter 在冻住的 GRPO checkpoint 上进行，student 为 LoRA 活跃模式，teacher 为禁用 LoRA 的基模型，蒸馏后合并权重。  
- **离线设计**：OFSD 完全在 GRPO 轮次结束后离线进行，不影响 RL 采样效率，且能反复迭代。

**关键实验**  
- 使用 Qwen2.5-3B-Instruct 作为基座，在 7 个单跳/多跳 QA 基准上评估。  
- 与 outcome-reward RL（Search-R1, ReSearch, AutoRefine）、过程监督方法（StepSearch, GiGPO）等对比。  
- Search-E1 达到平均 EM 0.440，超越所有开源基线，尤其多跳任务提升显著（2Wiki +4.3, MuSiQue +3.6, Bamboogle +12.0 vs. AutoRefine）。  
- 在与依赖 GPT-4o 标注的 StepSearch 和基于状态分组优势的 GiGPO 比较中，Search-E1 在大部分基准上领先，证明了从自身 rollout 提取的信号比手工或外部监督更有效。

**最值得记住的一句话**：同一模型在给定更优兄弟轨迹作为上下文时能产生更准确的下一步分布，这个差异就是 free 的步骤级训练信号。
