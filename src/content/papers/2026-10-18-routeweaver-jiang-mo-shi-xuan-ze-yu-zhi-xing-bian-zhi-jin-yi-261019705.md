---
title: 'RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing'
title_zh: RouteWeaver：将模式选择与执行编织进统一 LLM 路由
authors:
- Xiaohan Wang
- Haozhen Zhang
- Qingyuan Liu
- Tao Feng
- Wenya Wang
affiliations:
- Nanyang Technological University
- Huazhong University of Science and Technology
- University of Illinois Urbana-Champaign
arxiv_id: '2610.19705'
url: https://arxiv.org/abs/2610.19705
pdf_url: https://arxiv.org/pdf/2610.19705
published: '2026-10-18'
collected: '2026-10-24'
category: LLM
direction: LLM 路由 · 模式选择与执行联合优化
tags:
- LLM Routing
- GRPO
- Mode Selection
- Multi-Model Coordination
- Reinforcement Learning
one_liner: 统一 LLM 路由框架，联合学习执行模式与模型选择，COMET-GRPO 分层信用分配+渐进式探索，五领域平均准确率提升 11.03%
practical_value: '- 在构建 LLM 路由/调度层时，不要把执行模式（单次调用、多轮、Agentic）写死，可用一个策略联合选择模式与模型；在电商搜索/客服
  query 复杂度差异大时，让策略学会按需降级或升级，能平衡成本与效果。

  - COMET-GRPO 的信用分配思路可迁移：如果路由器需要同时决定“调用哪个工具/模型”和“用几步完成”，将整体奖励分解为模式级和步骤级优势信号，能缓解稀疏奖励导致策略坍缩；在
  Agent 编排中分别奖励“是否选择 Agent 模式”和“Agent 内模型选择”，可避免只选单轮或只选多轮。

  - Progressive exploration 类似课程学习：先用规则/预设模式训练执行能力，再放开让策略自主选择；在业务中可用固定策略冷启动或基于历史数据预训练路由，再逐步切换到在线强化学习，防止早期策略坍缩到某个低风险模式（如全部走单轮）。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 路由方法通常围绕单一执行范式设计，如单轮、多轮或 Agentic 路由，这固化了模型调用的组织方式，难以适应不同 query 对执行复杂度的不同需求。  
**方法**：提出 RouteWeaver，一个统一路由框架，将多种执行模式集成到单个策略中，联合学习“用哪种模式”和“在该模式下选哪些模型”。为了优化模式选择与模式内执行，开发 COMET-GRPO，将轨迹级优势分解为模式选择信号和模式内执行信号，实现分层信用分配；同时引入渐进式探索，训练早期由外部指定模式，逐步过渡到策略自主选择模式，使路由器先学会执行每种模式，再学会何时使用。  
**结果**：在数学、编码、知识、逻辑推理、事实回忆五个领域评估，RouteWeaver 平均准确率 61.4%，相对最强基线提升 11.03%，且在每个领域均优于所有对比基线。消融显示 COMET-GRPO 与渐进式探索均对自适应路由至关重要；去掉渐进式探索后，路由策略完全坍缩为单轮执行。
