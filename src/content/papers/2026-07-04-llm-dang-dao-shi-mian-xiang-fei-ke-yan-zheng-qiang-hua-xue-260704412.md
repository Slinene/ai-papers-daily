---
title: 'LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL'
title_zh: LLM 当导师：面向非可验证强化学习的策略感知提示自适应
authors:
- Yujin Kim
- Namgyu Ho
- Sangmin Hwang
- Joonkee Kim
- Yongjin Yang
- Sangmin Bae
- Seungone Kim
- Jaehun Jung
- Se-Young Yun
- Hwanjun Song
affiliations:
- KAIST
- Upstage
- University of Toronto
- Carnegie Mellon University
- NVIDIA
arxiv_id: '2607.04412'
url: https://arxiv.org/abs/2607.04412
pdf_url: https://arxiv.org/pdf/2607.04412
published: '2026-07-04'
collected: '2026-07-09'
category: Training
direction: LLM 训练 · 奖励信号自适应
tags:
- RLHF
- Reward Modeling
- Prompt Adaptation
- LLM Judge
- Instruction Following
one_liner: 让 LLM 同时充当考官和生成器，通过追加原子约束实现提示难度自适应，恢复奖励区分度。
practical_value: '- 在搜索推荐中使用 LLM 评委评估生成质量时，可借鉴 append-only 约束生成方法，随策略能力提升动态增加评估提示的难度，避免奖励信号失效。

  - Agent 训练中，固定任务指令易导致简单样本无区分度，可引入自适应难度机制：比较 agent 产出质量，对简单任务自动追加新约束，维持训练信号有效性。

  - 工程实现上，复用单一 LLM 完成比较判别与约束生成，原子化约束的追加方式保证难度单调递增，无需外部调度模块，降低系统复杂度。

  - 在广告文案或推荐理由生成中，可动态调整评估维度（如“增加情感诉求”、“限制字数”）来持续激发模型能力提升。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：非可验证指令遵循的强化学习中，常用 LLM 裁判根据提示明细评分作为奖励。现有工作自适应评分细则，但训练提示本身固定不变，导致提示难度与策略能力失配——当提示无法引发生成样本的质量差异时，裁判无法给出有区分度的信号，训练陷入停滞。

**方法关键点**：提出 LLM-as-a-Tutor，将单模型同时用作考官和生成器：
- **检测**：通过成对比较策略的两个输出，识别当前提示是否过于简单（即两个输出质量无显著差异）。
- **自适应**：对检测出的非挑战性提示，以原子约束的形式追加新要求（append-only），单调提升难度，直到能区分策略输出质量。
- 整个过程无需外部难度调度，奖励信号随训练自校准。

**关键结果**：在三个复杂指令遵循基准上，该方法一致超越策略无关基线及先前的策略自适应方法（仅自适应评分细则或重写提示），证实提示自适应是策略感知 RL 中缺失的关键维度。
