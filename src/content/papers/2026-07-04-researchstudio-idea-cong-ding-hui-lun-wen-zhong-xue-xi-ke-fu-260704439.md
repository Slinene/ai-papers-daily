---
title: 'ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from
  ML Conference Outcomes'
title_zh: ResearchStudio-Idea：从顶会论文中学习可复用研究构思模式的技能套件
authors:
- Qihao Zhao
- Yangyu Huang
- Yalun Dai
- Lingao Xiao
- Jianjun Gao
- Xin Zhang
- Wenshan Wu
- Scarlett Li
- Yang He
- Yan Lu
affiliations:
- Nanyang Technological University
- Microsoft Research
- National University of Singapore
- CF AR, A*STAR
arxiv_id: '2607.04439'
url: https://arxiv.org/abs/2607.04439
pdf_url: https://arxiv.org/pdf/2607.04439
published: '2026-07-04'
collected: '2026-07-07'
category: Other
direction: 自动化研究构思 · 证据驱动生成
tags:
- Research Ideation
- LLM Agent
- Pattern Mining
- Novelty Check
- Evidence Grounding
one_liner: 从机器学习顶会论文中提取15种可复用构思模式，构建证据驱动的端到端创意生成工作流
practical_value: '- **模式提取可复用到策略创意生成**：类似地从历史高转化广告文案、高效召回策略中挖掘重复出现的“成功模式”（如特定痛点切入、差异化角度），形成结构化卡片，引导
  Agent 批量生成新的营销方向或推荐策略。

  - **证据准备度检查模板**：在接收业务需求（如提升冷启动推荐效果）时，先让系统核查输入信息的充分性（类似 IdeaSpark 的 evidence readiness），避免基于不完整上下文生成低质量方案。

  - **碰撞检测机制用于创意排重**：在批量生成推荐理由或 push 文案时，可引入类似 Scoop-Check 的冲突检索，确保新颖性，防止重复已有内容或竞品方案。

  - **审查与追溯卡片提升交付物可信度**：对生成的推荐策略附上“提案卡片”，包含依赖的前人工作、可能失败模式，便于工程团队评估风险、追溯决策依据，尤其适合 Agent
  辅助的离线策略推荐场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 虽能生成研究方向，但研究者仍需扎实文献基础、识别瓶颈、差异化创新并评估风险，现有工具缺乏端到端支持。

**方法**：
- 从 ICLR、ICML、NeurIPS 2021-2025 年 1947 篇论文（含 Oral、高引用、被拒稿）中提炼出 31 个子模式，合并为 15 个可复用构思模式，每个模式封装为结构化卡片，包含研究背景、瓶颈类型、差异化策略、支持先例和常见失败模式。
- 构建技能套件 **ResearchStudio-Idea**：
  - **Paper-Search**：多源文献搜索；
  - **Scoop-Check**：新颖性碰撞检测；
  - **IdeaSpark**：端到端工作流——评估证据准备度、重建研究上下文、识别未解决瓶颈、匹配相关模式、实例化一个候选方向、检索潜在冲突先验工作、基于会议成果进行审查，最终生成可追溯的提案卡片。

**关键结果**：
- 盲审自动评测中，IdeaSpark 生成的提案在整体质量上显著优于无技能和通用技能基线，且新奇性保持竞争水平；表明大规模会议结果中包含可复用的构思信号，并可转化为实用技能。
