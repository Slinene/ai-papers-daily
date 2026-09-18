---
title: 'Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents'
title_zh: 反思、修订、复用：GUI Agent 的无训练技能演化
authors:
- Bofan Chen
- Boxuan Zhang
- Fei Tang
- Zhengxi Lu
- Yong Du
- Tongbo Chen
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
affiliations:
- Zhejiang University
- UESTC
arxiv_id: '2609.17653'
url: https://arxiv.org/abs/2609.17653
pdf_url: https://arxiv.org/pdf/2609.17653
published: '2026-09-14'
collected: '2026-09-18'
category: Agent
direction: GUI Agent 技能演化 · 训练自由反思修订
tags:
- GUI Agent
- Skill Evolution
- Training-Free
- Failure Recovery
- Procedural Knowledge
one_liner: 提出训练自由的 EvoSkill-GUI，将技能作为多文件包通过反思-修订-复用循环持续从执行反馈中改进，在三大 GUI 基准上最多提升 16.2%
practical_value: '- 技能包多文件结构化：将 retrieval metadata、plans、backup localization、failure-recovery
  rules、failure cases 分文件管理，业务 Agent（如客服自动化、营销流程）可借鉴把关键过程知识模块化，方便局部更新，避免整体重写。

  - 反思-修订-复用闭环：部署后从失败轨迹自动修订技能，不需重新训练模型；推荐/广告 Agent 可利用线上失败样本持续改进执行策略，提升动态环境鲁棒性。

  - 即时 in-rollout 修订 + 隔离 critic：执行时遇到弹窗/页面变化可立刻根据备用定位和恢复规则调整；critic 在信息隔离下诊断避免被错误轨迹污染，对构建可靠自动化流程有参考。

  - 训练自由，低成本迭代：无需 GPU 训练，仅依赖 LLM 推理与文件编辑，适合需要快速适应界面改版或流程变化的电商运营自动化场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：GUI agents 在动态界面中执行长任务，弹窗、延迟、控件移位等使固定计划失效。现有技能框架把技能视为部署前静态产物，缺乏针对执行动态的修订机制。

方法关键点：EvoSkill-GUI 将每个技能设计为结构化多文件包，包含检索元数据、可执行计划、备用定位、失败恢复规则、可访问性工具和失败案例。运行过程是 reflect-revise-reuse 循环：执行器在 rollout 中即时修订；隔离的 critic 在严格信息隔离下诊断失败轨迹；执行器通过受限工具接口编辑特定技能文件。训练自由，无需额外训练。

结果：在 MobileWorld、AndroidWorld、OSWorld 三个跨移动和桌面的主流 GUI 基准上，EvoSkill-GUI 在多种基础模型上带来一致提升，最大增益分别为 +16.2%、+6.0%、+10.5%，且演化后的技能库能继续惠及相关任务，无需从零重建。
