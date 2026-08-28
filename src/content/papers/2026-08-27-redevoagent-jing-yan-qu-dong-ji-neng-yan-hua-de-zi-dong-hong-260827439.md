---
title: 'RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution'
title_zh: RedEvoAgent：经验驱动技能演化的自动红队智能体
authors:
- Junjie Zhang
- Hui Liu
- Kecheng Chen
- Xianbo Mo
- Changsheng Chen
- Haoliang Li
affiliations:
- City University of Hong Kong
- Shenzhen MSU-BIT University
arxiv_id: '2608.27439'
url: https://arxiv.org/abs/2608.27439
pdf_url: https://arxiv.org/pdf/2608.27439
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: LLM Agent 技能进化与安全红队
tags:
- Red-teaming
- Skill Evolution
- Validation Ratchet
- Tool Selection
- LLM Agent
- Jailbreak
one_liner: 将攻击轨迹蒸馏为可读技能，并用验证棘轮做候选更新，提升黑盒 Agent 攻击效果与工具效率
practical_value: '- 对商品推荐/搜索 Agent 的策略迭代：把召回-排序-重排或 query 改写策略写成可读 skill 文档，候选版本只有验证集或小流量指标严格优于当前策略才上线；失败候选进入
  rejection context，减少反复生成无效配置。

  - 在多工具 Agent 链路中做“决定性工具归因”：不按工具出现频率记功，而把成功案例归因到直接带来正向反馈的工具/动作，可避免策略坍缩到高频但低效的工具。

  - 工具/策略先做隔离评分画像：对候选工具在固定数据上单独评估，再让 LLM 结合轨迹总结优先级；比检索全量历史轨迹上下文成本更低、可读性更好。

  - 可零样本复用与安全测试：在一个模型/执行环境上进化出的 skill 可迁移到其他模型/harness，适合多租户电商 Agent 的对抗测试、鲁棒性评估；工具调用次数也可作为效率指标纳入评估。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
产品级 LLM Agent 接入 Claude Code / Codex 等执行环境后，一旦被 jailbreak，会触发危险工具调用和持久化状态修改，风险高于纯文本不安全输出。固定攻击方法覆盖空间有限；基于相似轨迹检索的 agentic 红队又容易复用误导性经验，且全轨迹上下文开销大、可解释性差。

**方法关键点**
- 用 Markdown 攻击技能替代轨迹检索：从训练 split 的攻击轨迹中蒸馏出工具优先级与攻击策略，减少上下文并便于审计。
- 经验构造由两部分组成：隔离评估每个攻击工具得到 tool-effectiveness profile；再收集成功/失败轨迹，并用 Deciding-Tool Attribution 把成功轨迹归因到首次成功 QUERYTARGET 前的那个工具，避免“共现频率”带来的自强化偏差。
- validation ratchet：每轮蒸馏器基于当前技能、工具画像、轨迹和 rejection context 生成候选技能；候选只有在独立验证集上严格提升才算接受，否则保留旧技能并记录失败候选。

**关键结果**
ASB 和 AgentHarm 上跨 3 个 target model、2 个 execution harness：RedEvoAgent 在多数设置超过最强单工具和 RedCodeAgent/MAJIC。例如 ASB MiniMax-M2.5 + Claude Code 为 93.2 ASR，FlipAttack 为 91.8，RedCodeAgent 为 76.4；AgentHarm DeepSeek-V4-Flash + Claude Code 为 74.3 HarmScore，而 FlipAttack 67.9、RedCodeAgent 37.5。同时平均工具调用更少。消融显示去掉 tool-effectiveness profile 下降最严重（93.2→76.9，-16.3）；去掉 trajectory collection 和 Deciding-Tool Attribution 分别降至 85.0/87.5。技能可零样本迁移到不同 attacker model（+5.6/+7.3 ASR）和 harness（+9.7 ASR）。

**一句话**
候选技能只有在独立验证集上严格超过 incumbent 才被接受，既是方法核心，也是可迁移到业务 Agent 的策略更新原则。
