---
title: 'DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search
  and Rubric-Grounded Reasoning'
title_zh: DuMate-DeepResearch：可审计的多智能体深度研究框架
authors:
- Lingyong Yan
- Can Xu
- Yukun Zhao
- Wenxuan Li
- Qingyang Chen
- Jiulong Wu
- Wenli Song
- Xiangnan Li
- Weixian Shi
- Yiqun Chen
affiliations:
- Baidu AI Cloud
arxiv_id: '2606.07299'
url: https://arxiv.org/abs/2606.07299
pdf_url: https://arxiv.org/pdf/2606.07299
published: '2026-06-05'
collected: '2026-06-08'
category: MultiAgent
direction: 多智能体深度研究架构与动态规划
tags:
- Multi-Agent System
- Deep Research
- Graph-Based Planning
- Rubric-Guided Reasoning
- Recursive Execution
one_liner: 通过图动态规划、递归两级执行和量规引导推理，实现可审计且 SOTA 的深度研究报告生成。
practical_value: '- **可审计的多智能体架构**：将核心推理与工具生态解耦，使每一步规划和工具调用都可追踪。在电商推荐流程中，可将召回、排序、解释生成等环节分解为独立可审计的
  Agent，便于调试与合规。

  - **图动态规划与反思**：用有向无环图管理长程子任务，支持粗到细扩展、回溯和剪枝。生成式推荐中的候选集生成、过滤、排序等步骤可建模为 DAG，遇到低质量结果时自动重规划，提高整体鲁棒性。

  - **递归两级执行**：外层规划代理将复杂搜索子任务委托给内层搜索代理，隔离噪声和局部失败。推荐系统中，可将高代价的实时检索或内容生成封装为子 Agent，防止单个子任务拖慢全局。

  - **量规引导的推理与生成**：动态生成任务特定的质量准则，注入搜索、规划和报告合成阶段，作为实时推理约束。生成推荐理由或商品描述时，可设计类似量规来强制证据链接、多源校验，降低幻觉。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
现有 Deep Research 系统面临长程规划难、任务分解调度易出错、长文合成幻觉高、过程不透明四大痛点。单调 ReAct 风格 agent 缺乏全局视野，一旦单步工具失败容易导致整条轨迹崩溃。为此，本文提出了一种可审计的多智能体框架，将研究流程形式化为可追踪的状态转移过程。

**方法关键点**  
- **解耦架构**：基于千帆 Agent Foundry，将认知核心（Router、Planner、Writer）与工具生态分离，使全部中间决策和工具调用可审计。
- **图动态规划**：研究计划表示为一个有向无环图，节点按深度排序执行，支持粗到细的边界探索；每个节点完成后由 Planner 评估证据，进行剪枝、重连或扩展，保持全局视野。
- **递归两级执行**：外层 Research Agent 负责全局规划，每遇复杂搜索子任务即派发一个完整的 Search Agent（内部自行规划-执行），将检索噪声隔离在子任务内，避免全局连锁失败。
- **量规引导测试时优化**：动态生成持久性与临时性量规，作为 Planner、Search Agent 和 Writer 的实时推理脚手架。持久量规锚定主题质量维度，临时量规追踪当前证据缺口，并作为自适应停止条件。

**关键实验**  
在 DeepResearch Bench（100 任务）和 DeepResearch Bench II（132 任务）上评估。DuMate-DeepResearch 在两个基准上均取得最佳总体得分：58.03%（DR Bench，超第二名 0.76%）和 61.95%（DR Bench II，超第二名 2.04%），且在信息召回和分析维度上领先明显。消融实验显示，去除量规主要损伤报告阶段的全面性和洞察力；替换报告模型则造成更大质量下降，表明合成模型是整体性能最敏感的组件。

**最值得记住的一句话**  
量规不应只是事后评价标准，而应作为实时推理约束注入 agent 的规划与生成过程，动态校准证据采集与报告合成。
