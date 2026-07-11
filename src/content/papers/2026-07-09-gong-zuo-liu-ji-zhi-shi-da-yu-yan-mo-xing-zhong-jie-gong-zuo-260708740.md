---
title: 'Workflow as Knowledge: Semantic Persistence for LLM-Mediated Workflows'
title_zh: 工作流即知识：大语言模型中介工作流的语义持久性
authors:
- Emanuele Quinto
- Carlo Andrea Rozzi
- Francesco Zanitti
affiliations:
- UNHCR
- CNR—Istituto Nanoscienze
- ZeLe & F ApS
arxiv_id: '2607.08740'
url: https://arxiv.org/abs/2607.08740
pdf_url: https://arxiv.org/pdf/2607.08740
published: '2026-07-09'
collected: '2026-07-11'
category: Agent
direction: LLM 工作流语义持久化
tags:
- workflow
- semantic persistence
- LLM agents
- knowledge objects
- derive vs infer
- conceptual model
one_liner: 将工作流定义、实例、推理记录等作为可持久化的知识对象，支持工作流的可检查、可恢复和可审查
practical_value: '- 在复杂推荐或广告策略工作流中，可借鉴“derive vs infer”语义区分：将确定性计算步骤（如特征工程、规则过滤）归为
  derive，将需要 LLM 判断的步骤（如创意生成、用户意图理解）归为 infer，以控制成本与可预测性。

  - 将工作流状态持久化为结构化知识对象（如上下文快照、依赖关系）形成知识图谱，可用于事后审计、错误排查和增量构建，提升推荐管线透明度。

  - 利用“语义持久性”实现工作流的中断恢复与人工审批门：当推荐任务被中断（如突发流量）或需要人工干预（如敏感内容审核）时，可基于持久化知识恢复执行，避免状态丢失。

  - 该概念模型可用于设计可复用的子工作流模板，将已验证的推荐流程（如召回→粗排→精排→重排）作为知识对象复用，加速新业务接入。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有 LLM 工作流系统虽已显式定义控制流，但缺乏统一的表示模型，导致工作流定义、执行实例、中间推理状态等难以作为可持久化的知识被管理、检查与恢复。

**方法**：提出一种语言无关的概念模型，将工作流定义、工作流实例、推理记录、上下文快照和依赖关系统一表示为**持久化知识对象**，存放在共享知识层。核心贡献是引入两个关键语义区分：**derive**（确定性计算，基于当前状态给出确定结果）与 **infer**（LLM 调解下的判断，在声明的上下文和执行者控制的能力策略下进行）。

**结果**：形成“语义持久性”的初步概念——工作流不仅是产生知识和留下痕迹的过程，其自身可被表示为可检查、可恢复、可审查的知识对象。模型借鉴了 Lisp 的符号形式、对象同一性和活映像思维，但未绑定具体实现，形式化转换语义留待将来工作。
