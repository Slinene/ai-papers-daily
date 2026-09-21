---
title: Grounded Skill Synthesis from Code at Scale for Agentic Intelligence
title_zh: 从代码大规模合成有依据的智能体技能
authors:
- Yongqi Tong
- Pan Wang
- Hang Wang
- Jianshe Li
- Xin Zhang
- Jiang-Ming Yang
- Wei Wu
affiliations:
- Ant International
arxiv_id: '2609.05571'
url: https://arxiv.org/abs/2609.05571
pdf_url: https://arxiv.org/pdf/2609.05571
published: '2026-09-03'
collected: '2026-09-21'
category: Agent
direction: 代码挖掘 · 技能合成 · Agent 流程增强
tags:
- Skill Synthesis
- Code Mining
- Agentic Intelligence
- Procedural Knowledge
- Retrieval
- SWE-bench
one_liner: Code2Skill 从 GitHub 代码挖掘并验证 100 万+可复用技能，检索增强后智能体平均提升 11.7%
practical_value: '- 构建可复用的业务 skill bank：不只依赖 agent 轨迹，可把推荐/广告/搜索系统中的特征工程、策略规则、pipeline
  代码片段蒸馏为带 when-to-use、invariants、anti-goals 的技能卡，供 LLM Agent 检索增强。

  - 用 source-body-blind reconstruction 做 grounding 质检：只给技能描述让 LLM 重构实现，再用 source-aware
  judge 对比源实现过滤不支持或过度概括的记录，能有效抑制技能库幻觉，可迁移到知识库/规则库审核。

  - 技能注入位置比数量更重要：planning-time 与 post-generation critique 比 generation-time prompting
  更稳；RL 中作为 reviewer 提升最大。业务上优先把检索到的技能/知识放到规划、评审或 verifier 侧，而不是直接拼进生成 prompt。

  - 用 compact summary 替代完整记录可减少约 89% context 且性能不降，适合降低 LLM 调用成本与 KV cache 压力；对候选技能做摘要化而非全量拼接。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有技能合成主要有两条路线：trajectory-based 技能与具体环境/模型强耦合，质量受 agent 自身经验限制；document-sourced 技能虽可规模化，但缺乏可执行证据与验证。代码天然支持执行、版本化与验证，因此从大规模 GitHub 代码库中提炼可复用程序知识，能在 agent 积累轨迹前提供可靠的技能来源。

## 方法关键点
- 提出 Code2Skill，四阶段流水线：从 19,769 个高星活跃 GitHub 仓库中解析函数、方法、CLI 入口等候选单元；LLM 打标签选取有复用意图和操作结构的单元。
- 技能记录分三种粒度：atomic（单一操作）、composite（有序工作流）、recurring-pattern（跨实现对级模式），每条记录包含 when-to-use、workflow、invariants、failure handling、anti-goals、source evidence 等。
- 关键验证机制：source-body-blind reconstruction——只给技能记录让 LLM 重建实现，再用 source-aware judge 对照原始代码，过滤不支持或过度概括的记录。
- 构建 CodeSkillBank：1,006,822 条接受记录，保留 provenance 和证据，支持检索、审计与更新。

## 关键实验
在 9 个模型配置、8 个 benchmark 上，检索 CodeSkillBank 技能后平均分从 42.90 提升到 47.90，相对 +11.7%，57/72 个 protocol-matched 对比获胜；SWE-bench Verified 全部 9 组提升。与 trajectory-derived 技能库对比，Code2Skill 在 7 个共享 benchmark 上平均 49.5，显著高于 Trace2Skill 31.0、ExpeL 27.9、SkillRL-Bank 32.8。技能注入位置研究显示 planning-time 和 post-generation critique 最稳，compact summary 降低 88.9% context 仍保持效用；coding RL 中 post-generation review 比无技能提升 14 个百分点。AI 生成代码提取的技能 pass rate 93.50% 与人类代码 93.00% 接近，说明可自我扩展。

## 最值得记住的一句话
代码是天然可执行、可验证、可扩展的技能来源，用重构验证 grounding 后，repository-derived skills 可以在 agent 积累自身轨迹之前就提供有效的程序性知识。
