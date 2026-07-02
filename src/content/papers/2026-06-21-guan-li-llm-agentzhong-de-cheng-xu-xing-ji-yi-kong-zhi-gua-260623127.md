---
title: 'Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation'
title_zh: 管理LLM Agent中的程序性记忆：控制、适应与评估
authors:
- Julia Belikova
- Rauf Parchiev
- Evgeny Egorov
- Grigorii Davydenko
- Gleb Gusev
- Andrey Savchenko
- Maksim Makarenko
arxiv_id: '2606.23127'
url: https://arxiv.org/abs/2606.23127
pdf_url: https://arxiv.org/pdf/2606.23127
published: '2026-06-21'
collected: '2026-07-02'
category: Agent
direction: 程序性记忆迁移与演化基准
tags:
- procedural memory
- skill transfer
- agent benchmark
- LLM agents
- skill evolution
- cross-model generalization
one_liner: 提出AFTER基准，揭示程序性技能从多样化多模型轨迹中演化可实现73.1%跨模型测试准确率
practical_value: '- 多样化经验提升泛化性：用多个不同模型的执行轨迹去演进技能，比单模型轨迹能显著提高跨模型泛化能力（+13.7%）。在电商搜索/推荐中，如果使用多个异构模型（如不同Transformer模型或不同策略）的日志来优化统一技能（如query改写、意图识别），可能提升技能在新模型上的适应性。

  - 角色特定技能退化：跨角色迁移时，同一技能（如pdf处理）可能因角色差异（如PM的摘要 vs DS的数据提取）导致性能下降。在推荐系统中，为不同业务线（如搜索推荐
  vs 广告推荐）定制的策略或prompt应区分训练，避免强制共享导致的特化退化。

  - token效率：通过前置程序性知识到prompt中，可大幅降低推理token消耗（最高-62%）。在LLM驱动的推荐agent中，将常用处理逻辑固化为技能指令，能减少运行时重复推理，降低成本和延迟。

  - 技能更新机制：单轮refinement就能提升3.7-6.7个百分点，采用COLLECT–DIAGNOSE–REVISE–PROMOTE循环，可快速迭代优化agent行为。可用于电商搜索的query生成或商品描述生成pipeline的快速迭代。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agent 在工业工作流中频繁执行重复性程序任务（如文档处理、数据库查询、基础设施配置），程序性记忆可将成功经验固化为可复用技能。但技能在不同任务、角色、模型间的迁移性未知，现有基准未区分局部优化与真正泛化，缺乏可控评估。

**方法关键点**：
- 提出 AFTER 基准：包含 382 个真实职场任务，横跨 6 个专业角色（数据工程师、数据科学家、生成式AI工程师、基础设施工程师、项目经理、软件工程师）和 22 项程序性技能，支持单/多技能工作流与跨任务、跨角色、跨模型的迁移分割。
- 引入 EVOLUTION 演化框架：技能版本化存储，遵循 COLLECT–DIAGNOSE–REVISE–PROMOTE 闭环，固定 trace 采集、验证、升级与回滚，可更换反射器考察不同更新机制。
- 评估特异性（源上下文提升）和泛化性（分布偏移下表现），使用全通准确率和部分进度准确率双指标。

**关键结果**：
- 静态技能使全通准确率平均提升 +2.8 点，对弱模型增益更明显（如 Gemma 4 E4B +4.6）。
- 单轮 LLM 引导的改进再提高 +5.2 点，累计提升 3.7–6.7 点。
- 多样化多模型轨迹演化的技能在跨模型测试上达 73.1% 准确率，比最佳单模型源高 +13.7 点。
- 跨角色迁移中，技能因角色特化而退化（如 pdf 技能从 PM 迁移至 DS 损失 4.8 点）。
- 演化技能显著降低 token 消耗（最高 -62%），节省推理成本。

核心启示：程序性记忆的关键不是存储更多经验，而是提取在训练环境外依然有效的程序结构。
