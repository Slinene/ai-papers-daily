---
title: 'UI-KOBE: Knowledge-Oriented Behavior Exploration for Lightweight Graph-Guided
  GUI Agents'
title_zh: 知识导向行为探索：轻量图引导的移动GUI代理
authors:
- Yuxiang Chai
- Han Xiao
- Xinyu Fu
- Jinpeng Chen
- Rui Liu
- Hongsheng Li
affiliations:
- CUHK MMLab
- Huawei Research
- Shenzhen Loop Area Institute
- CPII under InnoHK
arxiv_id: '2605.29534'
url: https://arxiv.org/abs/2605.29534
pdf_url: https://arxiv.org/pdf/2605.29534
published: '2026-05-27'
collected: '2026-05-29'
category: Agent
direction: 轻量级GUI Agent行为探索
tags:
- GUI Agent
- Knowledge Graph
- Lightweight Model
- Mobile Automation
- Behavior Exploration
one_liner: 通过自动构建应用知识图，为轻量GUI代理提供结构化行为指导，提升端侧任务可靠性与隐私性。
practical_value: '- 将用户操作流建模为知识图，引导Agent决策，减少对LLM的依赖，提升稳定性和响应速度，适合电商场景中的自动化操作流程。

  - 图自动构建方法可用于冷启动或快速适应新业务场景，例如新电商App的自动化测试或客户引导流程设计。

  - 轻量模型+图引导的架构适合部署在资源受限的端侧设备，对隐私敏感的推荐交互（如端侧Agent）提供参考。

  - 自环和邻居边切换策略可迁移到多Agent协作场景，将复杂任务分解为图谱上的状态转移，降低调度复杂度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：移动GUI自动化大多依赖大型视觉语言模型，推理成本高且存在隐私风险。轻量GUI代理适合端侧部署，但端到端规划能力不足，执行不可靠。

**方法**：提出UI-KOBE框架，首先自动探索目标应用，构建应用知识图谱——节点表示不同UI状态，边表示可执行操作转移。运行时，轻量GUI代理将当前截图匹配到图谱节点，然后基于节点决策：选择自环动作（如刷新）、转移到邻居节点、判定任务完成或回退到自由动作。这种结构化引导大幅减轻了端到端规划的负担。

**结果**：在多个移动GUI基准上，UI-KOBE显著提升了轻量模型的任务成功率，同时降低了推理开销，提高了可解释性，为高效隐私的端侧GUI代理提供了可行路径。
