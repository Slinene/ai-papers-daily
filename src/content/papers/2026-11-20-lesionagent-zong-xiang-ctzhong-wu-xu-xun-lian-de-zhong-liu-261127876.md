---
title: 'LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment
  in Longitudinal CT'
title_zh: LesionAgent：纵向CT中无需训练的肿瘤追踪与疗效评估Agent
authors:
- Maximilian Rokuss
- Jeya Maria Jose Valanarasu
- Alejandro Lozano
- Benjamin Hamm
- Yannick Kirchhoff
- Fabian Isensee
- Klaus Maier-Hein
affiliations:
- German Cancer Research Center (DKFZ)
- Heidelberg University
- Microsoft Research
- Stanford University
- National Center for Tumor Diseases (NCT) Heidelberg
arxiv_id: '2611.27876'
url: https://arxiv.org/abs/2611.27876
pdf_url: https://arxiv.org/pdf/2611.27876
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: LLM Agent 多工具编排与决策
tags:
- LLM Agent
- Tool Orchestration
- Medical Imaging
- Longitudinal Tracking
- Rule Engine
- Verification
one_liner: LLM Agent 编排冻结3D模型与确定性规则引擎，在纵向CT肿瘤追踪与疗效评估中超越专用基线
practical_value: '- 将领域规则和数值计算外置为确定性引擎（如RECIST engine），LLM只负责感知、匹配和决策建议，避免幻觉与计算错误；电商推荐中可将价格、库存、优惠计算和业务规则交给确定性服务，LLM只做意图理解与商品匹配。

  - 为LLM构建结构化harness：维护跨会话状态注册表（如用户历史、商品列表），提供坐标标注视图或切片，逐步验证中间结果；论文中同一LLM在harness内开源模型从6%提升至73%，说明工程封装比模型本身更关键。

  - 多工具编排模式：冻结现有专用模型（召回、排序、CTR预估）作为工具，LLM进行动态调用和结果整合，无需微调即可扩展到新业务场景，同时保留可审计的决策链条。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：癌症治疗中，每几个月CT决定是否继续治疗。放射科医生需判断病灶、跨时间匹配、是否进展，并依据RECIST等临床指南。现有3D基础模型能检测、分割、配准、追踪，但无法像医生一样综合决策，固定规则流水线易误报进展。

**方法**：LesionAgent是一个训练无关的LLM Agent。它将冻结的3D基础模型作为工具，在坐标标记的2D视图上观察，维护跨访问的病灶注册表，验证每个模型输出，并将所有数值计算和指南判定交给确定性的RECIST引擎。LLM负责看片、检查和决策，但不需要微调。

**结果**：在四个公开纵向CT数据集上，LesionAgent追踪病灶更多、测量更准；固定规则基线在56个随访中假阳性进展33次，LesionAgent仅2次。临床随访CT上，与放射科响应一致性达20/23（包括所有响应变化）。在DeepLesion上，未训练却检索出89.0%病灶（此前最佳跟踪器为87.4%）。消融显示，harness是关键：同一LLM和3D模型，Claude Code检测F1仅41%，LesionAgent达78%；开源LLM从6%升至73%。
