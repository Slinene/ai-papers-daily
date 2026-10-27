---
title: 'DynaFlow: Learning Free-Form Multi-Agent Orchestration'
title_zh: DynaFlow：学习自由形式多智能体工作流编排
authors:
- Ruhao Liu
- Qi Li
- Shizun Wang
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2610.34467'
url: https://arxiv.org/abs/2610.34467
pdf_url: https://arxiv.org/pdf/2610.34467
published: '2026-10-24'
collected: '2026-10-27'
category: MultiAgent
direction: 自由形式多智能体工作流学习
tags:
- MultiAgent
- Workflow Synthesis
- LLM Orchestration
- Supervised Fine-tuning
- Cross-stage Information Flow
one_liner: 将自由形式工作流合成融入主智能体动作空间，动态编排子智能体，仅训练主智能体，多任务准确率提升 10.9 个百分点
practical_value: '- 在电商推荐/搜索 Agent 系统中，避免固定多智能体管线：可借鉴 DynaFlow 设计一个 orchestrator LLM，根据
  query 或任务动态生成工作流（先并行召回/排序/生成，再验证与融合），而不是为每个场景硬编码子 agent 调用顺序，减少维护成本并适应长尾需求。

  - 只训练 orchestrator、冻结执行子智能体：业务中已有大量稳定的子服务（搜索、推荐、广告文案、风控等），可构造专家轨迹对主控模型做 SFT，并用过滤出的“信息流缺陷/有偏验证”样本做拒绝采样或再训练，实现低成本升级且不破坏下游服务。

  - 强调跨阶段信息流：在推荐系统多阶段推理中，显式对上游结果进行 use/verify/refine，而不是让每个 agent 一次成稿；例如让验证 agent
  检查推荐理由是否支持用户意图，再回退修正，可提升输出可靠性和可解释性。

  - 工程上可复用三类工作流原语：顺序执行、并行执行、结构化信息交换与验证，作为工作流 DSL 或工具调用规范，让 orchestrator 生成 JSON/Python
  工作流，执行器统一解析，便于与现有 RAG / 工具调用框架集成。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有多智能体系统通常依赖预定义协作结构，难以适应不同任务需求。

**方法关键点**：DynaFlow 把自由形式可执行工作流合成加入主智能体动作空间：主智能体判断何时需要协作，并生成任务专用程序，通过顺序或并行执行、结构化信息交换与验证来协调子智能体。执行结果与轨迹作为上下文影响后续动作，支持随推理过程动态调整协作模式。训练上只对主智能体做 SFT，先蒸馏轨迹，再对三类缺陷样本（unsupported premises、biased verification、information-flow defects）进行 refinement；子智能体全部固定，将编排学习与执行能力提升解耦。

**关键结果**：在数学推理、科学问答、多跳检索等六个基准上，DynaFlow 在 Forced 模式取得 88.08% 总体准确率，比同一 Qwen3.5-27B backbone 下最强基线高 10.90 个百分点；Dynamic 模式也达到 87.9% 且平均每个问题使用 3.44 个 agent 角色。工作流分析显示训练后模型更频繁显式使用、验证和细化上游输出，表明跨阶段信息流是多智能体编排的关键维度。
