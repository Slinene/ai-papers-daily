---
title: 'WorkFactory: Turning Professional Intents into Executable Work for Scalable
  Agent Training'
title_zh: WorkFactory：将职业意图转化为可执行工作以规模化训练智能体
authors:
- Ziyang Zeng
- Tingyang Chen
- Jia Deng
- Qiyao Wang
- Shuo Tang
- Yike Yang
- Tao Ren
- Wayne Xin Zhao
- Feng Chang
- Jujie He
affiliations:
- IQuest Research
- Zhejiang University
- Renmin University of China
- Shenzhen Institutes of Advanced Technology
- Shanghai Jiao Tong University
arxiv_id: '2610.37161'
url: https://arxiv.org/abs/2610.37161
pdf_url: https://arxiv.org/pdf/2610.37161
published: '2026-10-26'
collected: '2026-10-30'
category: Agent
direction: Agent 职业任务构建与 SFT 训练
tags:
- Agent Training
- Task Construction
- Information Planning
- Repair Loop
- WorkPilot
- SFT
one_liner: 提出 WorkFactory 框架，通过信息级规划与探针执行修复构建可执行职业任务，训练 WorkPilot 系列显著提升专业工作基准
practical_value: '- 构建电商/广告 Agent 微调数据时，用「业务意图 → 信息支持图」方式定义任务依赖（如商品信息、用户画像、预算约束），自动实例化并校验信息完备性，减少专家演示失败。

  - 在数据管线中引入「探针执行 + 修复」闭环：先让弱模型/环境跑任务，诊断缺失或不一致信息，再修复任务定义但保持原意图，可显著提升 SFT 数据质量与下游收益，尤其适合多步营销
  Agent。

  - 多尺寸训练结论：不要盲目扩展数据/模型，监控执行轨迹长度等行为指标；其先增后降与收益递减提示 agent 训练存在效率拐点，可帮助企业选择合适规模。

  - 环境缺陷修复可迁移到电商 Agent 平台：给任务模板维护信息依赖清单，执行前校验工具/上下文完备性，减少无效动作与专家演示噪声。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
训练工作 agent 需要海量专业任务和可靠专家演示，但任务信息缺失或不一致会阻碍 teacher 执行、削弱监督质量。

**方法关键点**  
WorkFactory 从职业意图出发，信息级规划构建信息支持图，显式刻画输出所需信息的依赖关系和位置，指导任务实例化；随后探针执行识别支持失败并引导修复，同时保持原意不变。据此构建 112,686 个任务、覆盖 612 个职业，采集 teacher 轨迹微调 Qwen 4B/27B/35B-A3B 模型，得到 WorkPilot 系列。

**关键结果**  
三个模型在四个专业工作基准上均超过各自基座；WorkPilot-35B-A3B 在 GDPval-AA v2.1 上 Elo 从 879 提升到 1565。扩展分析显示模型相关收益递减，执行长度先升后降；组件分析证明规划与修复减少探针诊断出的任务环境缺陷并提升下游表现。数据和模型已开源。
