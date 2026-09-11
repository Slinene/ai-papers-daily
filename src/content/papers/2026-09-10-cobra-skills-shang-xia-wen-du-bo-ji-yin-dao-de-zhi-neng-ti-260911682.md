---
title: 'COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization'
title_zh: COBRA-Skills：上下文赌博机引导的智能体技能优化
authors:
- Pingchen Lu
- Xiangyi Wang
- Xiang Li
- Jie Mao
- Zikun Qu
- Junfeng Luo
- Yao Shu
- Bryan Kian Hsiang Low
- Zhongxiang Dai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Tianjin University
- The Hong Kong University of Science and Technology (Guangzhou)
- National University of Singapore
arxiv_id: '2609.11682'
url: https://arxiv.org/abs/2609.11682
pdf_url: https://arxiv.org/pdf/2609.11682
published: '2026-09-10'
collected: '2026-09-11'
category: Agent
direction: Agent 技能优化 · Contextual Bandit
tags:
- Contextual Bandit
- Agent Skill Optimization
- LLM Agents
- Evolution
- LinearUCB
- Skill Search
one_liner: 用语义 embedding + 神经预测器 + LinearUCB 选择性评估候选技能，结合证据驱动的进化算子，在六个基准上平均提升 13–27
  个点且成本降 55%+
practical_value: '- 在 prompt / skill / workflow 优化场景中，用语义 embedding + 轻量神经预测器 + LinearUCB
  对候选策略打分，每轮只执行最高 UCB 分数的候选，可大幅降低真实评估成本；适合线上 A/B 或仿真评估昂贵的场景。

  - 进化算子可迁移到业务策略迭代：regeneration 从无策略轨迹产生多样性新解，rollout mutation 用当前策略的成败轨迹做局部修订，crossover
  用强策略做 backbone、弱策略做负例重组；可用于 query 生成策略、Agent 工具调用策略、广告文案生成的自动优化。

  - 定期（对数间隔）更新候选 population 而非每轮更新，且只保留高 UCB 候选、淘汰低优先级候选，能显著减少 LLM 调用次数；仅用 50 个优化样本即可达到强效果，说明小样本
  + 有效探索可替代大规模优化池，适合业务中少量标注或仿真轨迹的快速迭代。

  - 技能跨模型迁移性强（34/36 正向），说明优化出的技能捕获任务级策略而非绑定特定模型；业务中可为多个模型复用同一套优化好的技能或 prompt 库。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机

LLM agent 可以从历史任务经验中蒸馏可复用的技能，但现有技能优化方法依赖昂贵的执行反馈和大优化集，导致大量预算浪费在评估低质量候选上，且反复用 LLM 分析轨迹、诊断失败、生成修订的 token 成本很高。核心挑战是在有限计算和任务经验下，选择性分配候选评估并高效重用执行证据。

## 方法关键点

- 将技能优化形式化为预算约束、动态候选空间上的序列优化；每个候选技能视为 contextual bandit 的 arm，用 semantic embedding 表示。
- 每轮用两层 MLP 神经奖励预测器对技能 embedding 预测 reward，并加 LinearUCB 不确定性 bonus 计算 priority score，选择最高分候选执行评估。
- 定期（对数调度）进行 population evolution：regeneration 从 no-skill 轨迹生成新技能；rollout mutation 用当前技能的成败轨迹局部修订；crossover 用强技能作 backbone、强技能提供正证据、弱技能作负证据重组；低优先级技能被剪枝，新技能重新加入 bandit 评估循环。
- 新生成技能不继承历史 reward，必须通过目标 agent 真实评估重新获得分数。

## 关键结果

在 SearchQA、SpreadsheetBench、DocVQA、LiveMath、SocialMaze、ALFWorld 六个基准、三个目标模型上，COBRA-Skills 平均成绩最高；相对 no-skill baseline 分别提升 13.1、26.9、22.5 个百分点。与 SkillOpt 相比，总优化成本降低 55–58%，cost per point improvement 降低 60–69%，且只用 50 个优化样本。消融显示 bandit 和 evolution 各自贡献约 2 个点；自教学下性能几乎不降且成本减半；跨模型迁移 34/36 正向。

最值得记住的一句话：把昂贵的技能评估交给 contextual bandit 做选择性优先，把候选空间更新交给证据驱动的进化算子，就能用极少样本和成本获得高质量可迁移的 agent 技能。
