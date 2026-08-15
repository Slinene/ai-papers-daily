---
title: Training AI Scientists to Replicate Research
title_zh: 训练 AI 科学家复现研究
authors:
- Damon Falck
- Samer Sabri
- Anja Surina
- Thom Foster
- Anya Sims
- Sam Devlin
- Dylan Rogers
- Tantum Collins
- Kaloyan Aleksiev
- Louis Kirsch
affiliations:
- Inherent
arxiv_id: '2608.13331'
url: https://arxiv.org/abs/2608.13331
pdf_url: https://arxiv.org/pdf/2608.13331
published: '2026-08-13'
collected: '2026-08-15'
category: Agent
direction: AI Scientist 智能体训练
tags:
- AI Scientist
- Paper Replication
- Post-training
- Rubric Judge
- Coding Agents
one_liner: 构建论文复现任务集 Replica 与低噪声自动打分 judge，后训练 27B Faraday 智能体在复现任务上超越 Claude Opus
  4.8 和 GPT-5.5
practical_value: '- **自动生成评分 rubric 的思路可迁移到电商 Agent 评估**：用可自动构建的细粒度 rubric 替代人类打分，能降低标注成本、减少评分噪声，适合评估推荐解释、query
  改写质量或 Agent 执行轨迹。

  - **用编码 Agent 作为工具是轻量级垂直 Agent 的有效构造方式**：不必事事靠大模型规划，把可验证的子任务交给代码执行器，能在复现/批处理/数据管道等场景里提升稳定性和可复现性。

  - **后训练 27B 小模型在垂直任务上超过 GPT-5.5 和 Claude Opus 4.8**：说明在定义清晰、有自动 reward 的任务中，用中等规模模型+领域数据微调是性价比很高的选择，适合电商内部
  Agent 落地。

  - **低噪声 judge 可以作为强化学习 reward 信号**：如果你的业务 Agent 需要 RL 优化（如广告文案生成、搜索 query 推荐），可借鉴这种
  rubric-based 自动 judge 设计，减少 reward hacking。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：论文复现是科学可靠性的基础，但复现任务本身定义模糊、信息不完备，现有 LLM Agent 更擅长封闭式任务，难以应对这种开放式、假设驱动的探索。

**方法关键点**：
- 提出 Replica，一个可扩展的论文复现任务集，将复现过程标准化为可评估的 Agent 任务。
- 引入自动生成的 rubric-based judge，基于细粒度评分标准评估复现质量，噪声低且与人类判断一致，可作为训练和评估的 reward 信号。
- 后训练一个 27B 参数的 Faraday “AI Scientist” Agent，让它在执行复现时调用编码 Agent 作为工具，处理代码编写、实验运行等子任务。

**关键结果**：
- Faraday 在 held-out 复现任务上超越 Claude Opus 4.8 和 GPT-5.5。
- 单条 rollout 定性分析显示 Faraday 采用更符合科学方法的工作方式，如先形成假设、再设计实验验证。
- 整个方案不需要复杂 harness，为长时程科学创新 Agent 提供了基础。
