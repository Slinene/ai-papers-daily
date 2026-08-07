---
title: 'From Trajectories to Evidence: Auditable Experimental Records for Industrial
  Research Agents'
title_zh: 从轨迹到证据：工业研究智能体的可审计实验记录
authors:
- Zijie Zhuang
- Changxin Lao
- Pengbo Xu
- Hanwen Xu
- Ruochen Yang
- Yingzhi He
- Peng Zhang
- Jiangxia Cao
- Yusheng Huang
- Guohong Mu
affiliations:
- Kuaishou Technology
arxiv_id: '2608.05235'
url: https://arxiv.org/abs/2608.05235
pdf_url: https://arxiv.org/pdf/2608.05235
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: 研究智能体实验轨迹的证据化与审计
tags:
- Trajectory Evidence
- Research Agent
- Verifiable Records
- Recommendation Systems
- Industrial AI
one_liner: 提出将研究智能体实验轨迹转化为可审计、带边界的证据记录，用于可控的跨任务复用
practical_value: '- 在工业推荐 agent 实验中，将多轮实验轨迹转化为有边界、可审计的 **Repair/Guard/Withheld** 记录，不直接信任最终状态或未验证轨迹

  - 引入 **上下文隔离的“生成-验证-修复”循环**：在 proposal、code 等交接点检查 artifact 与证据一致性和下游需求缺失，用独立上下文避免盲点共享，减少无效实验消耗

  - 通过**执行有效性门控**（实现保真、执行完整、评估协议、机制保留）筛除无效轮次，并基于可归因证据对干预进行资格认定，避免混淆结果污染知识库

  - 构建**冻结的记录注册表**，下游由混合 LLM 控制器做 Apply/Defer/Reject 决策；实验显示控制器决策准确度有限（Affirmative
  precision 25%），建议将 Apply 视为待验证假设而非确认，需结合人工审核或保守策略'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机：** 研究智能体在工业推荐中执行多轮实验，产生的轨迹只记录“尝试了什么”，并未指明哪些结论有据可依。LLM 输出可能包含未支持的内容，执行可能无效或混淆，后期修改可能抹去早期收益，因此需要一种机制，将轨迹转化为可审计的、有边界的实验证据记录，以便安全复用。

**方法关键点：**
- **上下文隔离的生成–验证–修复循环**：对 proposal → code → experiment specification 等交接点，用独立上下文的证据/约束验证器和需求检查器分别找出 artifact 的违规和缺失信息，生产者可最多 K 次修复，不通过则阻断或回滚。
- **实验声明资格认定**：执行后通过实现保真、执行完整、评估协议、机制保留四个门控判断执行有效性；对有效轮次进行归因和边界检查，将候选声明分类为可操作的 Repair（可归因的有效干预）、诊断的 Guard（可归因的失败模式）或 Withheld（证据不足）。
- **冻结记录注册表与下游复用**：通过的 Repair/Guard 成为包含源上下文、干预、测量、支持证据和适用边界的记录。下游混合控制器根据目标机制、条件和观测，做出 Apply/Defer/Reject 决策；Apply 的 Repair 转换成方法契约执行，Guard 约束后续规划。

**关键实验：**
- 在 30 篇论文到工业 RankMixer 基线的适配中，26/30 的后续轮次优于首轮，但 22/30 的末轮低于中间最佳轮次，验证轨迹的非单调性。
- 上下文隔离验证使 proposal 通过率从 73.3% 升至 100%，代码完整性和可观测性大幅提升，但对齐度提升有限（50%→52%）。
- 14 个候选声明最终 8 个 Repair、1 个 Guard、5 个 Withheld；所有 Repair 和 Guard 记录均可追溯到源证据。
- 下游记忆条件适配诊断：5 个 reference-Apply 对中 3 个有益、1 中性、1 有害；强制应用的非 Apply 对多为有害。
- 控制器决策混淆矩阵：Affirmative precision 仅 25%，整体准确率 67.2%，低于 always-Reject 规则（79.7%），说明控制器倾向于过度应用。
- 两个通过完整流程产出的候选在线上 A/B 测试中分别获得直播页面时长 +0.75% 和用户增长净效用 +6.34% 的提升。

**最值得记住的一句话：** 智能体的实验轨迹只是候选证据的来源，必须通过上下文验证和跨轮次证据整合，才能形成有边界、可审计的复用记录，且复用决策应视为假设而非确认。
