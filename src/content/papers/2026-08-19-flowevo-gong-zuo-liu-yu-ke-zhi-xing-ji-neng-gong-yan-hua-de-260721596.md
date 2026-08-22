---
title: 'FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable
  Skills'
title_zh: FlowEvo：工作流与可执行技能共演化的自进化智能体
authors:
- Zeyu Ren
- Ling Yue
- Ran Li
- Yishu Wang
- Shengxiang Xu
- Hanmo Liu
- Shaowu Pan
- Shimin Di
affiliations:
- Southeast University
- Rensselaer Polytechnic Institute
- The Hong Kong University of Science and Technology
arxiv_id: '2607.21596'
url: https://arxiv.org/abs/2607.21596
pdf_url: https://arxiv.org/pdf/2607.21596
published: '2026-08-19'
collected: '2026-08-22'
category: Agent
direction: Agent 自进化 · 工作流与技能共演化
tags:
- Agent
- Workflow
- Skill Library
- Self-Evolution
- Training-Free
- Token Efficiency
one_liner: 训练免更新框架，将成功工作流编译为可执行技能，并在推理时通过直接复用或技能条件生成持续提升智能体能力
practical_value: '- 在导购/客服/搜索推荐 Agent 中，把验证通过的会话或工具调用轨迹编译为带接口与测试的技能条目，而不是仅存 prompt
  文本；可显著降低重复探索的 token 成本，适合高并发商品推荐、Query 改写等场景。

  - 采用「动态生成 / 直接执行 / 技能条件化生成」三级路由，并设直接执行失败自动回退；可嵌入商品属性抽取、推荐解释、营销文案生成等 workflow，结构化任务优先走缓存式执行。

  - 用对比式效用追踪（compare skill applied vs withheld）做负迁移治理：对 prompt 版本、策略技能、推荐模板做持续 AB
  式统计，低于阈值自动降权/停用，防止线上记忆库被低质量经验污染。

  - 该框架在可验证信号（结构化 action、code、math）下更稳，对无明确 reward 的开放对话需谨慎；其「小模型受益大」结论可用于低资源场景，用记忆库补偿模型能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：LLM agent 在推理时构建 workflow，但成功经验通常随 episode 丢弃；已有 skill library 常离线构建、无法从 agent 自身工作流中增长。这导致重复探索、高 token 成本和高方差。FlowEvo 旨在不更新参数的情况下，让工作流与可执行技能在推理时共同演化。

方法关键点：
- 将成功 workflow 编译为可执行 skill record：s=(f, σ, T, m, ℓ)，包含可调用体、接口、重放测试、元数据和生命周期状态；仅从通过 verifier 的 trace 编译。
- 三层路由：无技能动态生成 / 直接执行检索技能 / 技能条件化生成；直接执行校验失败自动回退。
- 准入与治理：interface compliance、functional correctness、safety compliance；用 contrastive utility 跟踪下游收益，持续负迁移则抑制/降权/修复。
- 训练免更新，仅维护持久化 skill bank 与记忆状态。

关键实验：
- 共享 GPT-4o-mini，5 个标准 full split：ALFWorld、HumanEval、MBPP、GSM8K、MATH-500；对比 8 个 baseline。
- ALFWorld 85.6%，比最强 baseline AFlow 高 26.4 点，token 约 1/3；HumanEval 95.1%、MBPP 79.6%、GSM8K 97.1%、MATH-500 75.9%，均最高。
- 10 个 backbone（7B–671B）中 49/50 优于 ExpeL，模型越小增益越大；ALFWorld 小模型 +53.2。
- 消融：编译 +5.2、技能反馈 +41.8、治理 +5.0；治理能自动抑制有害技能。

最值得记住的一句话：把成功 workflow 沉淀为「可调用 + 可校验 + 可治理」的技能银行，而不是文本记忆，才能同时获得直接执行的效率和结构化上下文的泛化。
