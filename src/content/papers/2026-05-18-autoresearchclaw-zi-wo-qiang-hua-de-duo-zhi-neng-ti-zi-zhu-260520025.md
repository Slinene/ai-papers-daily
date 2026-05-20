---
title: 'AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration'
title_zh: AutoResearchClaw：自我强化的多智能体自主研究与人机协作
authors:
- Jiaqi Liu
- Shi Qiu
- Mairui Li
- Bingzhou Li
- Haonian Ji
- Siwei Han
- Xinyu Ye
- Peng Xia
- Zihan Dong
- Congyu Zhang
affiliations:
- UNC-Chapel Hill
- UC Santa Cruz
- Carnegie Mellon University
- NUS
- UC Berkeley
arxiv_id: '2605.20025'
url: https://arxiv.org/abs/2605.20025
pdf_url: https://arxiv.org/pdf/2605.20025
published: '2026-05-18'
collected: '2026-05-20'
category: MultiAgent
direction: 多智能体自主科研管线与人机协作
tags:
- Multi-Agent Systems
- Autonomous Research
- Human-AI Collaboration
- Self-Healing
- Benchmark
one_liner: 多智能体自主研究管线，通过辩论、自修复、交叉运行演化等机制，在ARC-Bench上超越AI Scientist v2 54.7%
practical_value: '- **多智能体辩论机制**：用于电商推荐系统中的创意评估或策略生成，多个专业Agent从不同角度（如合规、新颖性、业务指标）辩论和打分，提升输出可靠性。

  - **自修复执行循环**：在Agent工作流（如商品知识图谱更新、营销文案生成）中引入 Pivot/Refine 决策，将执行失败（如API错误、数据缺失）转化为结构化信息，自动尝试修复或优雅降级。

  - **人机协作干预模式**：7种干预模式（从全自动到逐步监督）的消融实验表明，在关键决策点（高杠杆点）进行精准人工干预能取得比全自动或过度监督更好的效果，可用于设计电商Agent的控制面板，让运营在关键环节介入。

  - **跨运行演化记忆**：将历史错误转化为未来防护规则（类似让推荐Agent记住哪些商品搭配曾导致差评，避免再次推荐），可作为长期运行的生成式推荐Agent的经验积累机制。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有自主科研系统多为线性流程，单一智能体推理，遭遇失败即停止，且无法跨实验积累经验。真实科研是迭代、多视角质疑、从失败中学习的循环过程。

**方法关键点**：
- 五个核心机制：① 结构化多智能体辩论生成假设并分析结果；② 自修复执行器，含 Pivot/Refine 决策循环，将失败转化为信息；③ 可验证的结果报告，防止编造数据和虚假引用；④ 七种人机交互干预模式（从全自动到逐步监督），允许在关键节点介入；⑤ 跨运行演化，将历史错误转化为未来防护规则。
- 构建 ARC-Bench 基准，含 25 个实验级研究主题，评估自主研究全流程。

**关键结果**：
- 在 ARC-Bench 上比 AI Scientist v2 性能提升 54.7%。
- 人机消融实验表明，精准、有目标地在高杠杆决策点协作，持续优于全自主或 exhaustive 逐步监督。
