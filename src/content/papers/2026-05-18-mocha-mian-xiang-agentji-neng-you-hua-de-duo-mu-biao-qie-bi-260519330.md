---
title: 'MOCHA: Multi-Objective Chebyshev Annealing for Agent Skill Optimization'
title_zh: MOCHA：面向Agent技能优化的多目标切比雪夫退火方法
authors:
- Md Mehrab Tanjim
- Jayakumar Subramanian
- Xiang Chen
- Branislav Kveton
- Subhojyoti Mukherjee
- Anlan Zhang
- Sungchul Kim
- Somdeb Sarkhel
- Sunav Choudhury
affiliations:
- Adobe Research
arxiv_id: '2605.19330'
url: https://arxiv.org/abs/2605.19330
pdf_url: https://arxiv.org/pdf/2605.19330
published: '2026-05-18'
collected: '2026-05-22'
category: Agent
direction: Agent技能多目标帕累托前沿探索
tags:
- Multi-Objective Optimization
- Skill Optimization
- Chebyshev Scalarization
- Agent
- Pareto Front
- Prompt Engineering
one_liner: 通过切比雪夫标量化与退火探索，打破单目标优化僵局，实现Agent技能帕累托前沿全覆盖。
practical_value: '- 在电商Agent场景中，商品推荐、客服等技能的描述与指令体常受平台字数硬限制，可借鉴MOCHA的多目标优化生成不同长度-性能折中的技能版本，供运营按场景择优上线，避免单目标优化器因无法突破约束而停滞。

  - 探索–利用退火策略（HVC门控阈值指数衰减）可迁移到推荐系统的prompt优化：前期用超体积贡献（HVC）广搜多样性候选，后期切换至切比雪夫接受精确提升核心指标，能有效避免陷入局部最优。

  - 切比雪夫标量化能探索非凸帕累托前沿，当业务指标（如点击率、多样性、合规分）存在非凸冲突时，它比线性加权更能发现传统方法遗漏的折中解，适合多目标A/B测试中的候选生成。

  - 结构化突变机制（如带合规反馈的字段感知改写）可应用于生成式推荐的item描述生成，在保证字数、排版合规的前提下逐步丰富推理结构，兼顾描述吸引力与展示约束。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现代LLM Agent通过技能（SKILL.md）组织行为，每个技能包含描述字段（用于路由和检索）和指令体（控制推理与回答），它们受平台硬约束（描述≤1024字符、指令体≤5000字符）。技能优化本质上是一个多目标问题：需同时最大化任务正确性与平台合规性。现有提示优化器（如TextGrad、ProTeGi）均将技能视为单目标文本优化，或在多目标间线性加权，导致在非凸帕累托前沿区域完全无法改进。实验显示，在6个任务中，4个任务上所有基线经1000次采样后毫无进步。

**方法关键点**
1. **切比雪夫父技能选择**：每轮随机生成权重向量，选择最小化最大加权偏差的技能作为变异父本，保证能访问所有帕累托最优解（包括非凸区域）。
2. **双阶段接受策略**：
   - **探索阶段**：以超体积贡献（HVC）作为接受准则，只要新候选提升帕累托前沿任意方向即被接受，快速扩张前沿。
   - **利用阶段**：退火至切比雪夫接受，仅当候选在与父本选取方向一致的标量值上更优时才接受，精准推挤最弱目标。
3. **退火调度**：阈值τ(b)随预算消耗指数衰减，约在预算中点切换模式，平衡多样性与收敛性。
4. **结构化变异**：LLM变异器接收当前技能及各字段合规状态（如指令体超限提示），生成带约束意识的新技能，所有基线共享此变异机制以隔离选择策略的影响。

**关键实验**
- **数据集与模型**：6个技能（GPQA、TheoremQA、HoVer、HotpotQA、FEVER、DebugBench），Claude Haiku 4.5执行技能，Claude Opus 4.6负责反思与变异。
- **基线**：TextGrad（贪婪选择）、ProTeGi（UCB束搜索）、GEPA（验证点帕累托过滤），统一1000次采样预算。
- **核心结果**：
  - 基线在4/6任务中完全卡在种子技能，正确率零提升。
  - MOCHA在所有任务均实现改善，平均正确率相对最强基线ProTeGi提升7.5%（0.628→0.675），在FEVER上提升14.9%（0.632→0.726），TheoremQA提升10.4%（0.690→0.762）。
  - MOCHA发现的帕累托最优技能数量是基线的2倍（3.6 vs 1.6），3D超体积高出3.1%。
- **消融实验**：移除HVC门控导致多样性下降但正确率最高（0.687），移除退火导致多样性上升但正确率略降，全模型在二者之间取得平衡。

**核心洞察**
单目标选择策略无法利用多目标反馈，即使变异阶段已暴露提升可能性；而切比雪夫标量化与超体积驱动的退火探索是突破多目标冲突僵局的有效组合。
