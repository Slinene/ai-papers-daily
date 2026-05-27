---
title: 'SIA: Self Improving AI with Harness & Weight Updates'
title_zh: SIA：通过支架与权重联合更新的自改进AI
authors:
- Prannay Hebbar
- Yogendra Manawat
- Samuel Verboomen
- Alesia Ivanova
- Selvam Palanimalai
- Kunal Bhatia
- Vignesh Baskaran
affiliations:
- Hexo Labs
- University of Oxford
arxiv_id: '2605.27276'
url: https://arxiv.org/abs/2605.27276
pdf_url: https://arxiv.org/pdf/2605.27276
published: '2026-05-26'
collected: '2026-05-27'
category: Agent
direction: Agent 自改进与测试时训练
tags:
- Self-Improving Agents
- Test-Time Training
- Scaffold Optimization
- LoRA
- RL
- Agentic Systems
one_liner: 提出反馈智能体同时更新任务智能体的支架（提示、工具）和模型权重（LoRA）的联合自改进循环，在三个领域全面超越纯支架迭代
practical_value: '1. 在Agent开发中可引入「反馈智能体」动态选择改进动作：当纯提示/工具优化（支架更新）收益停滞时，自动触发模型权重微调（RL训练），实现支架与模型权重的协同进化。

  2. 对商品分类、法律条款匹配等细粒度分类场景，可直接套用「支架迭代到权重更新」的模式：先用支架优化解析、重排逻辑，再用GRPO按组优势进行LoRA微调，可显著提升准确率（如从50%到70%）。

  3. 针对GPU算子优化、超参调优等探索性任务，可借鉴「支架探索+权重内化」思路：支架负责搜索空间构建和编译/运行反馈解析，权重通过强化学习内化领域设计模式，获得超越人工调参的性能。

  4. 工程上，反馈智能体根据奖励密度自动选择训练算法（PPO/GRPO/entropic weighting/DPO等）的设计，可直接复用为动态训练策略选择器，降低RL训练调参成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
当前AI系统的改进严重依赖人类工程师分别优化模型权重和任务支架（提示、工具、解析逻辑等）。两大研究路线“支架自改进”和“测试时训练”各自孤立，前者固定模型只改支架，后者固定支架只调权重，未能发挥二者联动的潜力。本文旨在打破孤岛，构建一个统一的自改进循环：给定任务规范和验证器，系统自动迭代同时优化支架和模型权重。

**方法关键点**
- **双杠杆循环**：反馈智能体（Feedback-Agent）观察执行轨迹和奖励，在每一步动态选择执行支架更新（重写系统提示、工具调度、答案抽取）或权重更新（通过RL更新LoRA参数）。
- **多算法自主选择**：反馈智能体根据奖励稠密度、rollout成本等自动挑选训练算法：PPO（稠密奖励，高稳定性）、GRPO（稀疏结局奖励，并行高效）、Entropic Advantage Weighting（极稀疏高信号）、REINFORCE+KL（防回归）、Best-of-N行为克隆（冷启动）、DPO（仅序数信号）。
- **支架与权重的互补**：支架更新改善软件工程层面的解析、重试和工具流，权重更新则内化领域直觉（如法律条文区分、GPU共享内存块选择、生物数据后处理不变性）。

**关键实验与结果**
在三个差异显著的领域上验证：
- **LawBench（191类中文刑事指控分类）**：纯支架迭代将Top-1准确率从13.5%提升至50.0%，联合GRPO权重更新后达到70.1%（提升20.1个百分点），超越此前最佳模型45.0%。
- **AlphaEvolve TriMul（H100 CUDA核优化）**：纯支架仅1.14倍加速，联合Entropic Advantage Weighting训练后实现14.02倍加速，相比纯支架最佳运行时间再减少91.9%，达到1,017μs。
- **MAGIC scRNA-seq去噪**：纯支架优化mse_norm至0.241，联合GRPO后提升至0.289（+20%），权重更新甚至自发引入了支架从未生成的后处理步骤（np.clip+np.rint）。
所有任务上，支架+权重联合方案均显著优于仅支架更新，证实双杠杆协同的有效性。

**值得记住的一句话**
支架决定智能体“如何搜索”，而权重更新改变模型“知道什么”，二者的联合进化能解锁单一路径永远无法触及的性能天花板。
