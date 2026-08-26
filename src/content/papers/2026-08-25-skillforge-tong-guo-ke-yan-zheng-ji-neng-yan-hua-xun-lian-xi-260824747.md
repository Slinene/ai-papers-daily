---
title: 'SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents'
title_zh: SkillForge：通过可验证技能演化训练强化学习智能体
authors:
- Shidong Yang
- Ziyu Ma
- Tongwen Huang
- Xucong Wang
- Renda Li
- Yiming Hu
- Yong Wang
- Xiangxiang Chu
affiliations:
- AMAP, Alibaba Group
arxiv_id: '2608.24747'
url: https://arxiv.org/abs/2608.24747
pdf_url: https://arxiv.org/pdf/2608.24747
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 技能演化与 RL 训练优化
tags:
- LLM Agent
- Skill Learning
- GRPO
- Verifiable Skills
- Memory
- RL
one_liner: 让 LLM Agent 通过显式技能调用和基于证据的验证，在 RL 训练中持续积累并修正可复用技能
practical_value: '- 在电商导购/客服 Agent 中，可将经验从原始日志蒸馏成结构化技能（title/intent/principle/when
  to apply），检索时只注入 title+intent 的紧凑目录，调用后展开完整内容，能控制 prompt 长度与 KV cache，适合技能库/策略库持续膨胀的场景。

  - 借鉴 evidence-based verification：对每条技能/策略模板维护 EMA 成功率与调用次数，计算 underperformance score，优先让
  LLM 反思和改写高失败率策略；可用于推荐 Agent 的 prompt 模板、工具选择策略、query 改写规则库的持续治理。

  - 显式技能调用标签把技能使用变成可归因事件，RL 或线上日志可直接统计哪些策略真正影响转化/点击，避免“注入一堆 prompt 但不知道有没有用”；可迁移到生成式推荐的
  Semantic ID 策略库或多 Agent 工作流节点的版本管理。

  - 多路径技能归纳：从成功会话抽取、失败会话提炼修正、成功/失败对比分析差异生成新策略，且弱模型演化出的技能可迁移到强模型，能降低高质量策略库的生成成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

动机：LLM agent 用 RL 训练仍以 episode 为单位，跨 episode 难以积累可复用知识。SKILLRL 等把经验蒸馏成技能，但技能库只增不减，技能使用不可观测，无法验证有效性与归因，错误或过时技能会污染知识库。

方法关键点：
- 技能结构：每个技能含 title/intent/principle/applicability/category/status；检索时只注入 title+intent 的紧凑 catalog，调用后才返回完整内容。
- 显式技能调用：agent 在轨迹中输出 <skill_call> 标签，视为离散动作；GRPO 同时优化环境动作与技能调用，使技能使用可观测、可归因。
- 证据化技能验证：按技能维护 EMA 成功率和调用次数，计算 underperformance score conf(s)=(1-p̂)*(1-0.5 n/h)，高失败率高使用技能优先由 LLM reflexion 修订或废弃。
- 多路径技能归纳：每 I=5 步，基于成功轨迹抽取、失败轨迹提炼修正、成功/失败对比分析三条路径生成新技能，经 lexical+semantic 去重后入库。
- RL-only，无需 SFT 初始化；teacher 用 Qwen3-Max。

关键实验：ALFWorld/WebShop/AppWorld。Qwen2.5-7B 下 ALFWorld 93.6 vs SKILLRL 89.9，WebShop success 83.0 vs 72.7，AppWorld TGC/SGC 23.8/14.3 vs 19.0/5.36，整体平均提升约 6.3%；Qwen3-4B 达到 87.9/84.0，Qwen3-30B-A3B 达 94.3/59.5 TGC。消融显示：去掉显式调用 ALFWorld 掉到 77.9，去掉 effectiveness tracking 掉到 83.6，multi-pathway 最关键。

最值得记住的一句话：把技能调用变成离散可追踪动作，并用成功率+使用次数做持续验证和修订，是技能库质量不衰减的关键。
