---
title: 'CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements'
title_zh: CUA-Master：开放世界递归改进驱动的计算机使用智能体扩展
authors:
- Xinlei Yu
- Gen Li
- Ji Zhao
- Zhangquan Chen
- Congcong Wang
- Shuai Dong
- Zelin Peng
- Yuqi Xu
- Hongrui Wu
- Kaiwen Tuo
affiliations:
- MMLab, CUHK
- THU
- HKUST(GZ)
- Explore Academy
- JD
arxiv_id: '2611.03126'
url: https://arxiv.org/abs/2611.03126
pdf_url: https://arxiv.org/pdf/2611.03126
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: CUA 数据飞轮与递归训练
tags:
- CUA
- Data Flywheel
- GUI Agents
- Trajectory Reconstruction
- Self-Improvement
- Training
one_liner: 提出嵌套双循环递归改进框架 CUA-Master，结合开放世界数据与自催化传播，显著提升 GUI 智能体性能。
practical_value: '- 构建双循环数据飞轮：外层利用开放世界语料和模型弱点指导数据迭代，内层从教学视频提取真实工作流作为种子任务，通过视觉-语义双路径重建轨迹，可迁移到电商
  RPA/后台自动化数据生产。

  - 自催化传播：将种子任务提炼为可重用原语（primitives），可控合成多样、复杂、可验证任务，适合生成大规模 GUI 操作训练集，降低人工采集成本。

  - 快照回滚重试机制：在真实环境中通过反馈引导快照与回滚，提升轨迹收集的成功率和可靠性，可用于线上 Agent 执行时的容错与数据回收。

  - 结果证明递归迭代可带来持续增益，CUA-Master-27B 在 OSWorld 等 benchmark 达到 80.2，说明中等规模模型配合高质量数据合成可逼近大模型，适合资源有限的业务团队。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 CUA 受交互数据多样性、可控性和可靠性限制，传统优化缺乏迭代反馈，自生成经验方法收益递减。

方法：提出嵌套双循环框架。系统层外循环用开放世界语料和模型弱点驱动后续数据构建与优化；数据层内循环结合开放世界种子与自催化传播：先从教学视频挖掘真实工作流作为种子任务，用视觉-语义双路径轨迹重建；再将种子转化为可复用原语，可控合成多样、复杂、可验证任务。为高效可靠收集轨迹，引入反馈引导快照-回滚重试机制。

结果：CUA-Master-27B 在 GUI-only 和 GUI-CLI 混合 benchmark 上具竞争力，OSWorld Verified 80.2，OSWorld 2.0 36.9，WeaveBench 43.9，Agents' Last Exam 25.0；数据合成质量与效率显著提升，递归迭代持续增益。
