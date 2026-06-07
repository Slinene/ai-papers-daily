---
title: 'Archi: Agentic Operations at the CMS Experiment'
title_zh: Archi：面向 CMS 实验的智能代理操作框架
authors:
- Pietro Lugato
- Luca Lavezzo
- Jason Mohoney
- Hasan Ozturk
- Muhammad Hassan Ahmed
- Juan Pablo Salas
- Viphava Ohm
- Krittin Phornsiricharoenphant
- Gabriele Benelli
- Mariarosaria D'Alfonso
affiliations:
- Massachusetts Institute of Technology
- CMS Collaboration, CERN
- University of Wisconsin-Madison
- Fermi National Accelerator Laboratory
- Brown University
arxiv_id: '2606.04755'
url: https://arxiv.org/abs/2606.04755
pdf_url: https://arxiv.org/pdf/2606.04755
published: '2026-06-03'
collected: '2026-06-07'
category: Agent
direction: Agent 系统 · 科学数据协作
tags:
- Agent
- RAG
- Open-source
- Scientific Collaboration
- On-premise LLM
one_liner: 开源端到端框架 Archi 将异构数据源与可配置私有代理结合，在 CERN CMS 实验中为技术操作提供检索分析支持，证明开源模型在私有部署下效果优秀。
practical_value: '- **异构数据源的统一 RAG 范式**：将文档、历史数据、实时监控系统等多种来源系统化摄入和组织，可迁移到电商场景，例如整合商品描述、用户行为日志、客服对话与实时库存数据，构建统一的知识问答或运维
  Agent。

  - **私有化部署开源模型的可行性**：实验证明本地部署的 open-weight 模型在专业领域问答中能与商业模型竞争，对注重数据隐私的电商企业（如用户行为分析、内部运维排障）提供了低成本、高可控的
  Agent 方案。

  - **可扩展的 Agent 架构设计**：框架支持配置和扩展不同的 agent 与数据源，可应用于电商中需要动态接入多个推荐模型、召回源或业务数据流的 Agent
  场景，实现模块化扩展。

  - **真实生产环境下的评估方法**：基于实际 operator 的问题集和人工+自动评估，为电商 Agent 系统提供了从开发到上线后持续优化的评估流程参考。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：大型科学合作（如 CERN CMS）产生海量异构、分散且过时的知识，传统检索方式耗时低效，严重阻碍实验运行和科学进展。

**方法**：提出 Archi，一个开源的端到端框架，核心包含两大模块：1）异构数据源的系统化摄入与组织层，支持文档、历史数据、实时监控数据等；2）可配置、私有化、可扩展的 Agent 层，能够对集成后的信息进行检索与推理。自 2026 年 2 月起，Archi 已部署于 CMS 计算操作团队，作为技术操作员的辅助 Agent，提供跨资料、历史记录和实时系统的综合查询与分析能力。

**结果**：在一组源于生产使用的真实问题上，经人工和自动化评估，Archi 有效解决了操作员的日常查询，展现出对操作任务的实用性。对比实验中，本地运行的 open-weight 模型（如 Llama 系列）性能与商业 API 模型相当，证明完全私有化部署下仍可保持高水准问答，避免了敏感数据外泄风险。
