---
title: 'From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization
  for Self-Evolving LLM Agents'
title_zh: 从原子动作到标准操作流程：LLM Agent 的迭代工具自进化
authors:
- Haipeng Ding
- Yuexiang Xie
- Zhewei Wei
- Yaliang Li
- Bolin Ding
affiliations:
- Renmin University of China
- Alibaba Group
arxiv_id: '2607.07321'
url: https://arxiv.org/abs/2607.07321
pdf_url: https://arxiv.org/pdf/2607.07321
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 工具自进化与工具集迭代优化
tags:
- Tool Synthesis
- SOP
- Iterative Optimization
- LLM Agents
- Self-Evolving
- Non-Parametric
one_liner: 迭代地从执行轨迹中提取可复用 SOP，并持续合并、评估、剪枝，实现工具集的自进化与精简。
practical_value: '- 在电商/搜索推荐场景中，可借鉴 EVOSOP 的**轨迹驱动的工具抽象**：从 Agent 多次调用原子 API（查订单、发消息、改状态）的轨迹中，自动提取高频共现的动作序列并封装成
  SOP，减少重复推理和 token 开销。

  - **工具生命周期管理**是工程落地的关键：必须配套合并与剪枝机制，否则工具集会快速膨胀导致决策质量下降。可设计类似 REVIEWER 的轻量级评判器，基于执行成功率、是否引发故障等信号自动淘汰低质工具。

  - **非参数化自进化**思路值得注意：无需微调 LLM，仅通过优化工具集就能持续提升 Agent 表现，适合模型已封装或不易训调的场景。同时，采用 checkpoint
  与“按训练成功轮次选最优工具集”的策略，规避了 LLM 随机性的坑。

  - 方法论上的“符号反向传播”类比（从行为轨迹中提取逻辑块固化回工具集）可迁移到复杂多步查询、多 Agent 协作的 SOP 自动发现，比如将跨服务调用的子流程封装成高级工具函数。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
现有 LLM Agent 主要使用静态的原子工具集，每个任务都要从头编排细粒度动作，导致长任务中推理开销大、易出错。尽管已有方法支持动态生成工具，但往往是一次性行为，缺乏持续的管理，造成工具集膨胀、冗余工具干扰决策。论文提出 Agent 应能像人类一样，将原子动作提炼为可复用标准操作流程（SOP），并通过迭代优化实现工具集的自进化。  

**方法关键点**  
- 提出 EVOSOP 框架，包含四个协同模块：**CONSTRUCTOR** 从执行轨迹中识别频繁共现的动作序列，生成带条件检查的可执行 SOP；**MERGER** 合并功能重叠的 SOP，维持工具集精简；**EVALUATOR** 在新工具集上重跑训练任务，收集真实表现；**REVIEWER** 分析每次 SOP 调用的结果，按“完美执行/部分可用/无作用/负面干扰/实现缺陷”分类，剪除低质、冗余或故障工具。  
- 整个过程形成闭环的**非参数化训练**：数据获取（交互轨迹）→ 前向传播（任务执行）→ 反向传播（从轨迹中提取 SOP 并固化），合并与剪枝充当正则化，防止工具过拟合于特定任务。  
- 使用 mini-batch 迭代，前几个 epoch 生成新 SOP，后续 epoch 仅进行合并、评估、剪枝，并通过 checkpoint 选择训练成功率最高的工具集版本。  

**实验结果**  
在 ACEBench 和 Tau2Bench（Telecom）上，EVOSOP 相比 ReAct、DFSDT 及一次式工具生成方法 ASI、工具描述优化方法 DRAFT，任务成功率显著提升（ACEBench Multi-Step 上 GPT-4o 代理提升至 84.2%～85.0%，对比 ReAct 78.3%），同时平均推理轮数大幅压缩。消融实验中，去除 REVIEWER 或 MERGER 均导致性能明显下滑，验证了持续评价与合并对保持工具集质量的关键作用。案例分析显示，EVOSOP 能有效区分并保留高频、稳定的核心 SOP，淘汰缺陷或冗余工具。  

**核心结论一句话**  
Agent 自进化的核心不仅在于创建新工具，更在于建立包含合并、评估、剪枝的完整工具生命周期管理，通过非参数化的迭代优化实现可靠且高效的推理压缩。
