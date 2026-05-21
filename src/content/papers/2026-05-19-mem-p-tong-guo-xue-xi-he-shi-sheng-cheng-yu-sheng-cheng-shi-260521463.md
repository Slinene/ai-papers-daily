---
title: 'Mem-π: Adaptive Memory through Learning When and What to Generate'
title_zh: Mem-π：通过学习何时生成与生成什么实现自适应记忆
authors:
- Xiaoqiang Wang
- Chao Wang
- Hadi Nekoei
- Christopher Pal
- Alexandre Lacoste
- Spandana Gella
- Bang Liu
- Perouz Taslakian
affiliations:
- ServiceNow AI Research
- Mila – Quebec AI Institute
- Université de Montréal
- Polytechnique Montréal
- McGill University
arxiv_id: '2605.21463'
url: https://arxiv.org/abs/2605.21463
pdf_url: https://arxiv.org/pdf/2605.21463
published: '2026-05-19'
collected: '2026-05-21'
category: Agent
direction: Agent记忆系统 · 生成式记忆
tags:
- Generative Memory
- LLM Agents
- Reinforcement Learning
- Abstention
- Decision-Content Decoupling
- Experience Distillation
one_liner: 提出生成式记忆框架Mem-π，让记忆模型自主决定何时生成指导与生成什么内容，在多种Agent基准上平均相对提升超20%
practical_value: '- **记忆模块与下游Agent解耦**：使用一个独立的小模型（如7B）作为可训练的生成式记忆策略，专注产生任务相关的文本提示，可与任何更强的下游Agent配合，方便工程集成和迭代。

  - **离线蒸馏 + 在线自适应两阶段训练**：先用历史交互数据做SFT初始化，再利用环境reward做RL微调（GRPO），适合积累了大量交互轨迹的电商推荐或Agent场景，能够将粗经验转化为精确的策略。

  - **结构化rollout与决策-内容解耦**：强制每组采样包含abstain和generate分支，将优势信号分解为决策优势和内容优势，分别驱动''是否生成''和''生成什么''的学习，避免内容梯度淹没决策信号，可迁移到需要模型主动决定是否执行某个动作的场景。

  - **自适应abstention提升效率与鲁棒性**：模型在任务简单时主动[ABSTAIN]，避免注入冗余或误导信息；在困难任务上才生成指导，既减少token消耗（实验显示token用量降低31%），又防止检索记忆固有的“复制偏差”，对实时推理的成本敏感型电商Agent很有参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有LLM Agent的记忆系统多依赖检索（RAG、工作流记忆或RL优化检索），返回静态经验条目，常与当前上下文错位或包含过时信息。生成式记忆虽然能动态合成提示，但如果不加控制，可能产生有害或无用的指导。核心挑战在于：记忆模块应同时决定**何时需要生成**（避免在不必要时干扰Agent）以及**生成什么内容**（提供上下文相关、简洁的提示）。

**方法关键点**  
- **两阶段训练**：1) **经验蒸馏**：用离线经验库中的(context, hint)对做SFT，将显式经验内化为模型参数，初始化π_mem；2) **适应蒸馏**：在π_mem输出空间中引入[GENERATE]/[ABSTAIN]决策，用下游Agent的任务成功奖励进行RL（GRPO），并加入长度正则奖励鼓励简洁。  
- **决策-内容解耦优化**：每组采样强制包含1个abstain分支和G-1个generate分支，计算跨分支的决策优势（abstain vs generate）和generate分支内的内容优势；决策token仅接收决策优势，内容token仅在generate优于abstain时接收内容优势（Δ-gating），避免梯度混淆。  
- **记忆模型独立**：π_mem与下游Agent参数分离，可使用不同规模的backbone，支持跨Agent泛化。

**关键实验**  
在WebArena、WorkArena、ALFWorld、LifelongAgentBench四个Agent基准上，以GPT-5.4-mini为下游Agent，**Mem-π相对基础Agent平均提升20%以上**，在WebArena上提升+16pp（27.1→43.1%）。与检索式记忆（RAG、Mem0）和RL优化检索（Memory-R1、MemRL）对比均显著领先。消融显示：去掉S1初始化导致WebArena下降5.2pp；去掉结构化rollout下降4.8pp；自适应abstention在容易任务上abstain率约71%，在困难任务上降至13%，生成记忆的收益在困难任务上最大（+9.7pp）。跨Agent迁移实验表明，用较弱Agent训练的π_mem仍能为更强的GPT-5.4-mini带来显著增益。  

**一句话记住**：将Agent的记忆从检索范式转向可学习的生成策略，关键是解耦“是否生成”与“生成什么”的强化学习信号，使记忆模块能够自适应地提供真正有帮助的上下文指导。
