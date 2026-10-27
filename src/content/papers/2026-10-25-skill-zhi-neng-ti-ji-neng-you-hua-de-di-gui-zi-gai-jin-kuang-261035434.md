---
title: 'Skill^{infty}: Recursive Self-Improvement for Agent Skill Optimization'
title_zh: Skill∞：智能体技能优化的递归自改进框架
authors:
- Wangcheng Tao
- Zhanglu Yan
- Han Wu
- Weng-Fai Wong
affiliations:
- National University of Singapore
- City University of Hong Kong
arxiv_id: '2610.35434'
url: https://arxiv.org/abs/2610.35434
pdf_url: https://arxiv.org/pdf/2610.35434
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent 递归自改进 · 技能优化
tags:
- Agent Skills
- Recursive Self-Improvement
- Skill Optimization
- Meta-Skill
- Native Skill Discovery
one_liner: 将技能优化流程编码为可自我优化的 meta-skill，实现跨任务复用的递归自改进
practical_value: '- 在电商/搜索推荐的 Agent 平台中，把策略优化器（如 query 改写、召回策略、排序规则的生成与迭代流程）封装成可被自身优化的
  skill，让优化器随业务反馈递归进化，替代人工设计 pipeline。

  - 独立 reviewer 机制值得借鉴：对候选策略用隔离上下文评审，拒绝未激活、不可用或仅靠噪声涨分的候选，可以降低离在线指标误判和 reward hacking
  风险。

  - 采用原生 skill discovery（仅凭 name/description 让 Agent 自主加载）而非 prompt 注入，更贴合部署环境；把 description
  纳入优化范围可提高激活率，这对推荐 Agent 的 skill 路由设计很实际。

  - 解耦 meta-skill 与任务 skill，先在多个优化任务上提炼通用优化器，再复用到不同类目/国家/活动场景，摊薄自改进成本，适合多业务线共用一个优化框架。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有技能优化方法（如 SkillEvolver、CoEvoSkills）使用人工设计的固定流程，优化一个技能学到的经验无法迁移到下一个；即使 MetaSkill-Evolve 引入 meta-skill，仍锁死在五角色 pipeline 中且绑定单个任务。递归自改进（RSI）要求系统不仅改进任务表现，还要改进“改进流程”本身。本文认为技能格式天然适合承载 RSI：优化流程本身可被编码为技能，从而让优化器直接、可解释地自我改进。

**方法关键点**  
- 提出 Skill∞：一个 meta agent 遵循 meta-skill 优化任务技能，并用同一套 agent-led 流程优化 meta-skill 自身，形成两个互相强化的循环。  
- 每次优化迭代包含六步：检查 archive、诊断 rollout、提出候选、评估候选、独立 reviewer 评审、选择下一父代或停止。  
- 搜索由 meta agent 的推理驱动，而非固定启发式；它根据失败模式决定候选数量、是否回溯、何时停止。  
- 独立 reviewer 隔离上下文，拒绝无实质改变、未激活或不可用的候选，防止把噪声当作进步。  
- meta-skill 与任务技能解耦：先在多个技能优化任务上提炼 m0→m*，再复用到不同领域的任务技能优化。  
- 两级技能均通过 native skill discovery 加载，Agent 只看到 name/description 自主决定是否激活；description 也在优化范围内。

**关键实验与结果**  
在 SkillsBench 83 个任务上，Skill∞ 达到 60.7% pass rate（avg@5），超过人类 curated skills 56.4%、SkillEvolver 54.5% 和无技能 45.5%；在软件工程、媒体、数学等领域领先。KernelBench 上平均正确性加权加速 1.62，高于 SkillEvolver 1.18 和无技能 1.02。消融显示去掉自改进后掉到 55.9%，说明 meta-skill 自我优化贡献显著；换成 GPT-5.6 Luna 或 OpenCode harness 仍超越人类 curated skills。预算从 1 增加到 8 时，通过率从 47.5% 增至 82.5%，显示 agent-led 分配可扩展。

**最值得记住的一句话**  
把优化器的流程本身写成可被自身优化的 skill，让“改进方式”成为一等公民，才能在部署一致、成本可控的前提下获得递归增益。
