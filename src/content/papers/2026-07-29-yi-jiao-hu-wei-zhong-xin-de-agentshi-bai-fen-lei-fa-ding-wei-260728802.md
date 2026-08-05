---
title: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures
title_zh: 以交互为中心的Agent失败分类法：定位故障源与修复责任
authors:
- Harsh Raj
- Vipul Gupta
- Anas Mahmoud
- Razvan-Gabriel Dumitru
- Darvin Yi
- Aakash Sabharwal
- Yunzhong He
affiliations:
- Scale AI
arxiv_id: '2607.28802'
url: https://arxiv.org/abs/2607.28802
pdf_url: https://arxiv.org/pdf/2607.28802
published: '2026-07-29'
collected: '2026-08-05'
category: Agent
direction: 交互为中心的Agent失败诊断
tags:
- Agent
- FailureTaxonomy
- InteractionModel
- FaultLocalization
- Evaluation
- Reproducibility
one_liner: 提出基于组件交互边的Agent失败分类法，41种模式指定故障方，使评估直接指向可修复组件
practical_value: '- 在构建电商搜索/推荐多智能体系统时，可借鉴交互图建模，将失败归因到具体组件交互边（如LLM↔工具、LLM↔记忆），避免笼统的“模型不好”结论，精准指导是微调模型还是修复脚手架。

  - 使用分类法指导Agent评估框架设计，标注失败时区分模型侧、工具侧、环境侧，确保改进资源投向正确组件。

  - 可自研类似的离线失败分析流程：对Agent日志轨迹按交互边分类失败模式，生成故障热力图，辅助迭代优化。

  - 利用LLM作为评判器自动分类失败，实现监控告警的细粒度归因，降低人工分析成本（论文验证强法官κ=0.76，可复现性高）。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Agent评估常只输出系统级成败，无法定位失败源于模型、脚手架、环境还是评估设计，导致改进盲目。  
方法：提出以组件间交互为分析单元的失败分类法。定义一个Agent系统由模型（Model）、脚手架（Harness）、用户、工具、记忆、环境等组件构成，将41种失败模式分配到特定组件交互边上，并指明故障方（如模型侧需后训练，脚手架侧需修复工具集成）。分类法跨架构适用，包括编码助手、长期个人助理和多智能体系统。采用公共基准、系统卡、发布报告和日志轨迹进行示例验证，并让四个前沿LLM作为独立评判器复现人工标签。  
结果：最强评判器Cohen's κ达0.76，表明分类捕捉共享结构而非偏好。分类法可操作性强，能将失败直接映射到修复动作。
