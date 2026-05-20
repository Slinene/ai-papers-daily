---
title: What Do Evolutionary Coding Agents Evolve?
title_zh: 进化编码智能体究竟在进化什么？
authors:
- Nico Pelleriti
- Sree Harsha Nelaturu
- Zhanke Zhou
- Zongze Li
- Max Zimmer
- Bo Han
- Sebastian Pokutta
affiliations:
- Zuse Institute Berlin
- Technical University of Berlin
- Hong Kong Baptist University
- RIKEN Center for Advanced Intelligence Project
arxiv_id: '2605.20086'
url: https://arxiv.org/abs/2605.20086
pdf_url: https://arxiv.org/pdf/2605.20086
published: '2026-05-19'
collected: '2026-05-20'
category: Agent
direction: 进化编码 Agent 搜索行为分析
tags:
- Evolutionary Coding
- LLM
- Search Analysis
- Edit Types
- Benchmark
- Agent
one_liner: 通过 EvoTrace 数据集和 EvoReplay 回放方法，揭示进化编码搜索中分数提升多由少数编辑类型驱动，且存在高频代码回退的循环模式。
practical_value: '- 在自动化超参搜索、推荐规则生成等迭代优化场景中，不要只看最终指标，需监控搜索过程中的编辑类型分布，避免对评估器过拟合。

  - 可借鉴 EvoReplay 的回放与干预方法（例如移除代码组件、替换模型上下文）来诊断优化路径，定位真正有效的改进。

  - 编辑类型高度集中，可引导搜索策略优先尝试高频有效编辑（如常量微调），提升搜索效率。

  - 发现约 30% 代码行是先前删除行的重新引入，提示需设计机制抑制搜索回退，例如引入多样性惩罚或短期记忆。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有进化编码 Agent 仅以最终得分衡量进展，但得分可能来自算法结构创新、策略重调、已有知识重组或过拟合等多种机制，无法区分。需要深入搜索过程本身来剖析进化本质。

**方法关键点**：
- 构建 EvoTrace 数据集，涵盖 4 种进化框架、推理/非推理模型、16 个数学与算法设计任务，记录完整搜索轨迹。
- 提出 EvoReplay 方法，通过回放重建高分解的局部搜索状态，并施加控制干预（调整常量、移除代码组件、替换模型或提示上下文）分析解的结构。
- 使用 LLM-as-judge 将每个代码编辑标注为 9 种重复编辑类型，并经人工双重验证确保可靠性。

**关键结果**：
- 绝大部分得分提升源于一小部分编辑类型，而非广泛的新算法结构。
- 发现确定性的循环模式：约 30% 的新增代码行是先前已删除行的字节完全相同重新引入，几乎出现在每次运行中。
- 这表明基准收益可能来自性质不同的机制，仅有部分对应算法结构的真正创新。EvoTrace 和 EvoReplay 提供了超越最终得分的诊断性评估手段。
