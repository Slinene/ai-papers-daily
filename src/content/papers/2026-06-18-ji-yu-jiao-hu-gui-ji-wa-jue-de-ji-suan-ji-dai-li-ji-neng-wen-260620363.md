---
title: Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory
  Mining
title_zh: 基于交互轨迹挖掘的计算机代理技能文档自动生成
authors:
- Yuexing Hao
- Xiaomin Li
affiliations:
- Massachusetts Institute of Technology
- Harvard University
arxiv_id: '2606.20363'
url: https://arxiv.org/abs/2606.20363
pdf_url: https://arxiv.org/pdf/2606.20363
published: '2026-06-18'
collected: '2026-06-22'
category: Agent
direction: Agent 交互轨迹挖掘与技能自动化
tags:
- Skill Mining
- Interaction Trajectory
- GUI Agent
- Policy Learning
- GRPO
- Diagnostic Study
one_liner: 轨迹聚类可得到高可读性的技能库，但对策略迁移几乎无帮助，暴露当前方法缺陷
practical_value: '- 在构建电商/广告投放的 Agent 时，若从操作日志中挖掘可复用子任务，需警惕：无监督聚类的高纯度并不保证下游策略收益，必须进行任务导向评估。

  - 当前的边界检测和无序片段表示是主要瓶颈，实际系统中应优先采用能保留顺序信息的轨迹编码（如序列模型），避免丢失操作依赖。

  - 离线奖励模型（如本文中使用的 GRPO 奖励）可能与真实任务成功指标存在偏差，在线评估或使用任务完成信号作为奖励会更可靠。

  - 频率先验（高频子序列直接作为技能）是强基线，在资源有限时可作为快速冷启动方案验证概念，再迭代至学习模型。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：计算机使用代理（CUA）常需将重复操作封装为可读技能（SKILL.md），但人工编写成本高且易过时。交互轨迹中蕴含自然子任务结构，本文探索能否从中自动挖掘出有效的技能库，并验证其对下游策略的改善。

**方法**：提出三阶段流水线：① 用边界检测器分割 GUI 轨迹为片段；② 将片段聚类为候选技能（无监督）；③ 以聚类标签作为监督信号，训练技能感知的策略模型（GRPO）。实验在 InteraSkill Workflows 和 BrowseComp+ 上评估。

**关键结果**：聚类阶段取得高可读性——8 个集群中 5 个纯度≥0.95；但策略迁移几乎失效：GRPO 仅将 IW 技能步准确率从 18.5% 提升至 20.5%，BrowseComp+ 无变化，且在源领域指标上显著弱于频率先验。结论为诊断性研究：当前边界检测、无序表示和离线奖励模型不足以支撑可靠的跨域策略提升。
