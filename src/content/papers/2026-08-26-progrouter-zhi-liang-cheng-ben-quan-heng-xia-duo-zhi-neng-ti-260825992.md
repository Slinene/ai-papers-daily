---
title: 'ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows
  under Quality-Cost Tradeoffs'
title_zh: ProgRouter：质量-成本权衡下多智能体 LLM 工作流的在线进度引导编排
authors:
- Somgyuan Li
- Ahmed M. Abdelmoniem
- Shiqiang Wang
affiliations:
- Aston University
- Queen Mary University of London
- University of Exeter
arxiv_id: '2608.25992'
url: https://arxiv.org/abs/2608.25992
pdf_url: https://arxiv.org/pdf/2608.25992
published: '2026-08-26'
collected: '2026-08-27'
category: MultiAgent
direction: 多 Agent LLM 工作流在线路由编排
tags:
- Multi-Agent
- LLM Routing
- Online Orchestration
- Quality-Cost Tradeoff
- Progress Prediction
one_liner: 面向多智能体 LLM 工作流，提出在线进度引导路由，逐步选择大小模型以在预算内保持任务质量
practical_value: '- 多智能体工作流不要一次性 query 级路由，而应在每一步根据当前状态重估进度增益，用小模型处理常规步骤、大模型只处理关键卡点；电商客服/商品调研/推荐解释等
  agent pipeline 可直接套用这种 step-wise routing。

  - 用 multi-view progress scorer 把中间 workflow state 转化为 coarse regime + 子任务完成度/趋势/状态质量，能作为轻量
  domain adapter。推荐/搜索场景可定义类似 milestone 信号（如召回完成率、排序置信度、引用覆盖）指导 LLM 调用。

  - 虚拟队列 + 指数预算惩罚很实用：通过 Lyapunov virtual queue 跟踪长期平均成本，并用 exp(已消耗预算) 惩罚后续高成本调用，避免前期耗尽大模型配额；可直接迁移到广告竞价
  / Agent 调用成本治理。

  - 结构化特征与语义 embedding 双路径预测 + meta-gating + 在线 epsilon-greedy 探索更新，冷启动无需离线标注数据，适合业务中缺乏路由标注的
  Agent 系统快速上线并逐渐稳定。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
多智能体 LLM 工作流能协作解决复杂任务，但反复调用 LLM、长上下文累积带来巨大 token、能耗和延迟成本。现有 cascade/query 级路由方法只做一次性决策，无法适应多步工作流中逐步演化的状态：每一步该用哪个 LLM，取决于已完成进度、剩余难度和剩余成本预算。单模型策略在实验中全部违反长期成本约束——小模型因反复失败重试而总耗能过高，大模型因单次成本过高而超支。因此需要在线、逐步、进度感知的 LLM agent 路由。

**方法关键点**
- 将多 agent 工作流建模为在线约束优化：在每一步为已派发的 worker role 选择具体 LLM，最大化任务成功率，同时满足单任务时间/能耗预算和长期平均能耗约束。
- 设计 multi-view task progress scorer，将中间 workflow state 编码为归一化进度得分 g(st)∈[0,1]：coarse outcome regime 作为基础锚点，加上子任务完成度、近期进度趋势、状态质量三个细粒度子分数做 hierarchical aggregation。该 scorer 充当轻量 domain adapter，跨领域迁移只需重定义可观测 milestone。
- 提出 dual-path task progress predictor：结构化路径用表格特征（当前进度、子任务完成状态、趋势、调度历史、候选 LLM）训练树模型；语义路径用 coordinator 生成的自然语言摘要经 MiniLM 编码后训练树模型；meta-gated learner 根据 workflow state 自适应融合两条路径，预测每个候选 LLM 的步骤级进度增益 y_hat。
- 在线路由决策：路由得分 = V·(1−g(st))·y_hat(mt) − Q_w·(E(mt)−eE) − c_Γ·Γ(mt) − c_E·E(mt)。第一项是 progress-gap-aware 价值，剩余进度越小越抑制大模型；虚拟队列 Q 跟踪长期成本违规；指数系数 c_Γ、c_E 对接近单任务预算的高成本调用施加惩罚。用 epsilon-greedy 在线探索收集样本更新 predictor，epsilon 逐渐衰减。

**关键实验与结果**
在 HumanEval Plus（164 任务）、MBPP（200）、MATH-500（200）、ASQA（100）上评估，模型 zoo 包含 Qwen 2.5-Coder/Owen 3.5/Granite 4.1/Gemma 4/Owen 3.6 等大小模型。对比 MasRouter、CASCADIA、Educated Guessing 和单模型基线。ProgRouter 在满足长期能耗约束的方法中表现最佳：HumanEval Plus pass@1 93.0%（预算 4800J），优于 MasRouter 90.9%、CASCADIA 84.8%；MBPP 79.4% pass、3376J 最低能耗、10.3s 最短时间；MATH-500 84.3% pass、6112J 最低能耗；ASQA citation precision 92.1%，优于两个 routing baseline 的 89.8%。路由分布显示 80%+ 调用落在小模型，只有任务仍有显著进步空间时才升级到大模型。

**最值得记住的一句话**
在每一步用虚拟成本队列约束长期平均预算，并用 (1−g(st))·y_hat(mt) 衡量“剩余进度稀缺性”，让大模型只在真正能换来大幅进度提升时被调用。
