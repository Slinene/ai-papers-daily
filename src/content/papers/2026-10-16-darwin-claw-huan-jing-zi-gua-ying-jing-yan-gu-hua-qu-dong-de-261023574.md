---
title: 'Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively
  Self-Evolving Agents'
title_zh: Darwin-Claw：环境自适应经验固化驱动的递归自进化智能体
authors:
- Mingze Yin
- Xiaohan Wang
- Dian Li
- Longfei Luo
- Jiahong Yan
- Yiheng Zhu
- Chang-Yu Hsieh
affiliations:
- Zhejiang University
- Tencent
- Zhongguancun Academy
arxiv_id: '2610.23574'
url: https://arxiv.org/abs/2610.23574
pdf_url: https://arxiv.org/pdf/2610.23574
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 自进化经验固化与技能管理
tags:
- Self-Evolving Agent
- Experience Consolidation
- Skill Management
- Causal Validation
- Memory Externalization
one_liner: 提出 Darwin-Claw，将交互失败归因为结构化经验单元并外置到技能槽位，驱动递归自进化，在 WildClawBench 上平均得分提升
  24.1%
practical_value: '- 把用户/环境特定经验固化为结构化 Experience Unit（trigger conditions、keywords、handling
  strategies），并注入 SKILL.md 作为 inline patch；可直接用于电商导购 Agent、客服 Agent，将高频失败 case 沉淀为情境级补救策略，而不是每次从原始轨迹重放。

  - 通过槽位限制与生命周期状态机（Nursery probation → Active → evict/archive）管理外部技能，防止 prompt 信息过载；搜索/推荐
  Agent 可以用同样机制管理候选策略、query 模板或召回规则，保持上下文复杂度可控。

  - 采用两阶段 LLM 做 causal attribution 加多维评分（coverage/effect/efficiency，S=w1e+w2c+w3η），避免把偶然成功固化进策略；在广告文案、push
  选词等自动优化场景中，可用来评估一次改写的真实增量贡献。

  - 经验外置化而不是微调模型参数，兼容 OpenClaw、Claude Code、Codex 等主流 harness，并支持多用户技能生态集体进化；适合在推荐对话系统上做轻量、可回滚的持续优化，不触碰底座模型。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
LLM Agent 大多在孤立会话中运行，无法从历史交互中持续学习或适应用户特定环境。现有自进化范式直接把原始交互轨迹注入 memory/skill，导致行为模式被噪声掩盖、更新不可控。随着基础模型推理能力增强，瓶颈已从积累通用知识转向有效管理情境经验。Darwin-Claw 提出将交互失败归因、结构化为可验证的情境经验，并外置到技能与记忆中，实现可控的递归自进化。

**方法关键点**  
- Hierarchical Experience Consolidation System：增量解析新会话轨迹，提取 Skill Invocations；用 LLM triage 筛选有学习信号的 trace，生成结构化 Experience Unit（EU），包含 trigger conditions、keywords、handling strategies，分 exploit/explore 两类。
- Causal Validation & Multi-Dimensional Scoring：两阶段 LLM pipeline 做相关性与因果归因，判断性能变化是否真正来自 EU；按 coverage、effect、efficiency 加权评分，effect 为主目标。
- Externalized Memory Management：验证后的 EU 直接写入 SKILL.md 的 inline block；每个技能限制 6 个 active slots（3 exploit + 3 explore），EU 经 Nursery probation → Active → evict/archive 状态机，带 TTL，支持用户 pin/evict；通过竞争选择保留最有效策略，不修改模型参数。

**关键结果**  
在 WildClawBench 的 60 个长程多模态任务上，GPT-5.5 OpenClaw 平均得分提升 +24.1%，其中 tool-use +31.6%、web +27.3%，难度越大提升越明显（hard +29.4%，extreme +33.2%）。在 RSIBench-Data 自动优化场景中，skill-based 进化在 19/24 任务上优于 base，平均性能从 28.42% 提升到 31.91%，且始终优于 context-passing 方案，避免 GPQA Diamond 退化；SWE-P 相对增益 +68.8%，Terminal-Bench 2.0 相对增益 +34.1%。

**最值得记住的一句话**  
在 LLM 推理能力快速提升的背景下，自进化 Agent 的核心竞争力不再是堆通用知识，而是把交互失败归因、固化为可验证的情境经验，并通过受控的槽位与生命周期管理外置到技能与记忆中。
