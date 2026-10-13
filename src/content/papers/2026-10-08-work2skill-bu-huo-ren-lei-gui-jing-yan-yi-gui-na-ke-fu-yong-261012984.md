---
title: 'Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction'
title_zh: Work2Skill：捕获人类 GUI 经验以归纳可复用智能体技能
authors:
- Yuqi Huang
- Hui Li
- Yifei Cao
- Zikun Cai
- Tianci Xie
- Yangfan Gao
- Pinxue Guo
- Chaoyun Zhang
- Bingxuan Li
- Rui Zheng
affiliations:
- Shanghai Jiao Tong University
- Fudan University
- Nanyang Technological University
- Zhejiang University
- Shanghai Qiji Zhifeng Co., Ltd
arxiv_id: '2610.12984'
url: https://arxiv.org/abs/2610.12984
pdf_url: https://arxiv.org/pdf/2610.12984
published: '2026-10-08'
collected: '2026-10-13'
category: Agent
direction: Agent 技能归纳与复用
tags:
- GUI Agent
- Skill Induction
- Human Demonstration
- Multimodal Dataset
- Agentic Learning
one_liner: 提出 Work2Skill 框架，从人类 GUI 演示中自动归纳可复用技能，显著提升多个执行模型的任务成功率
practical_value: '- **构建领域操作技能库**：把电商运营、广告投放、客服工单等复杂后台操作的人类专家录屏与键鼠事件、UI 树对齐，自动抽取可复用的
  workflow rules 和 completion checks，将流程规则与任务特定参数分离，供 Agent 在新任务中直接调用。

  - **采用按需证据检查的归纳方法**：不一次性解析长轨迹，而是让 LLM Agent 根据问题动态检索关键片段，避免长上下文噪声，适合从海量操作日志或工单记录中提取高质量
  SOP。

  - **搭建高质量演示采集管道**：参考 WorkRecorder 的多模态对齐与完整性/成功筛选，企业内部可持续积累经过验证的专家示范，形成训练与评估数据闭环。

  - **技能与执行模型解耦**：验证技能注入对四种执行模型均有提升，说明可将技能作为独立模块叠加在 LLM/VLM Agent 上，便于迭代和迁移到不同业务场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Computer-use agents 可处理复杂 GUI 任务，但面对陌生软件和工作流仍缺乏领域知识。人类演示蕴含操作流程，但直接复用需分离 workflow rules 与 task-specific 细节。

**方法关键点**：
- WorkRecorder 采集基础设施：对齐屏幕录像、鼠标键盘事件和 accessibility-tree，形成同步多模态演示数据。
- WorkDemo-350 数据集：350 个经完整性和成功筛选的人类桌面 GUI 演示，用于技能归纳与下游评估。
- Agentic Skill Induction：通过按需检查证据（evidence on demand）生成可复用技能，捕获 workflow rules、步骤依赖和完成检查。

**关键结果**：在相同的执行设置下，将四种执行模型分别装入 Work2Skill 归纳的技能，与无技能基线相比，MyPCBench Bounded Action 平均得分提升 4.67–10.54 分，OSWorld-Verified 的 286 任务子集提升 3.11–7.50 分，成功率同步提升。
