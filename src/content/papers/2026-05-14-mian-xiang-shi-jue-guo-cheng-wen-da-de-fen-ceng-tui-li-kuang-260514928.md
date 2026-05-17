---
title: 'Chain-of-Procedure: Hierarchical Visual-Language Reasoning for Procedural
  QA'
title_zh: 面向视觉过程问答的分层推理框架与基准
authors:
- Guanhua Chen
- Yutong Yao
- Shenghe Sun
- Ci-Jun Gao
- Shudong Liu
- Lidia S. Chao
- Feng Wan
- Derek F. Wong
arxiv_id: '2605.14928'
url: https://arxiv.org/abs/2605.14928
pdf_url: https://arxiv.org/pdf/2605.14928
published: '2026-05-14'
collected: '2026-05-17'
category: Multimodal
direction: 视觉过程问答 · 多模态分层推理
tags:
- VLM
- ProcedureQA
- Benchmark
- Hierarchical Reasoning
- Multimodal
- Chain-of-Thought
one_liner: 提出ProcedureVQA基准和CoP层次推理框架，通过先检索后细化的方式增强VLM的过程推理能力
practical_value: '- **Agent 多步决策借鉴**：CoP 的“先粗粒度检索 → 细粒度步骤分解”架构可直接用于电商场景的过程式 Agent，如根据订单状态图片自动检索售后退款流程并定位下一步操作。

  - **多模态 RAG 实现**：利用视觉线索检索结构化过程知识库的方法，能迁移到商品手册、安装教程的智能问答系统，通过图像匹配相关文档段落再生成答案。

  - **数据构建思路**：ProcedureVQA 的构建方式可用于内部评测 Agent 的多模态过程推理能力，暴露模型在细粒度跨模态对齐上的短板。

  - **流程优化 trick**：CoP 的语义分解模块对于长文本步骤的细化，可用于将用户粗糙的意图（如“退货”）分解为可执行的子步骤，提升推荐或客服 Agent
  的指令可操作性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：视觉语言模型（VLM）在标准图像-文本任务上进展显著，但在视觉过程问答（VP-QA）中仍面临挑战：用户上传过程中间状态图片询问下一步动作，现有模型难以跨模态检索结构化过程指令，且图像序列粒度与文本步骤分解不匹配。为系统评估此能力，需构建专用基准并设计针对性推理方法。

**方法**：提出 **ProcedureVQA** 基准，精心构造覆盖多种过程领域的问答对。同时提出 **Chain-of-Procedure (CoP)** 分层推理框架：（1）基于视觉线索检索最相关的文本指令；（2）通过语义分解将粗粒度步骤细化为子步骤；（3）结合上下文生成准确的下一步动作。该框架以 VLM 为基础，显式注入过程结构知识。

**结果**：在六个代表性 VLM 上评估，CoP 在 ProcedureVQA 上均带来显著提升，最高绝对改进达 13%。消融实验验证了检索模块与分解模块的必要性，表明分层设计有效缓解了单步推理中的跨模态对齐误差。工作揭示了当前 VLM 在过程性推理上的短板，并提供了数据和算法支撑。
