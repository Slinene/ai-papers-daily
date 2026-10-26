---
title: 'A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy,
  Evolution, and Future Directions'
title_zh: 面向任务的长文档视觉问答综述：分类、演进与未来方向
authors:
- Yufei Tong
- Guanjie Cheng
- Tianle Wu
- Leilei Zhang
- Hang Zheng
- Peihan Wu
- Jianwei Yin
- Shuiguang Deng
affiliations:
- College of Computer Science and Technology, Zhejiang University
- School of Software Technology, Zhejiang University
- Polytechnic Institute, Zhejiang University
- BWTON Technology Co., Ltd.
arxiv_id: '2610.31385'
url: https://arxiv.org/abs/2610.31385
pdf_url: https://arxiv.org/pdf/2610.31385
published: '2026-10-22'
collected: '2026-10-26'
category: RAG
direction: 多模态检索增强生成 · 长文档 VQA 综述
tags:
- Long-Document VQA
- Multimodal RAG
- Document Understanding
- Agentic Reasoning
- Information Retrieval
- Survey
one_liner: 以任务瓶颈为主线，系统梳理长文档 VQA 的解析、证据检索、生成与评测，突出预算约束下的证据充分性
practical_value: '- 电商售后、产品手册、合规条款等长文档问答场景，可参考其「证据组织与检索」组件化设计：把版面元素（表格、图表、段落空间关系）作为显式检索证据，而不仅是文本
  chunk。

  - 广告审核、商家资质审核需要从长合同/报告中找到依据，可借鉴「预算感知协调」与可验证理解的思想，在 token/延迟约束下动态选择直接阅读或检索。

  - 面向客服 Agent 的架构：论文梳理的 Agentic Reasoning 与显式检索结合，可用于设计能持续管理证据、支持可纠正问答的长文档助手，降低幻觉风险。

  - 评测维度中的证据充分性、可验证性，可直接迁移到内部长文档 VQA 评测集构建，重点考察答案是否有高保真证据支撑。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：现有长文档 VQA 综述多按架构或技术路线组织，忽视任务瓶颈如何影响技术选择与优先级。本文以任务为中心，将长文档视觉问答拆解为四个组件：文档解析、证据组织与检索、生成器组织与学习、评测，并建立细粒度分类体系。

方法关键点：围绕显式检索，同时覆盖直接阅读路径；对每个组件追踪动机、技术响应与跨组件连接。时间演化分析显示研究重心从多模态内容理解，扩展到证据获取的充分性与高保真，再到证据的持续管理。

关键结果：论文统计显示 2020–2023 年 12 篇，2024 年 24 篇，2025 年 42 篇，2026 年 80 篇，呈加速增长。未来方向包括证据充分性、可验证与可纠正理解、预算感知协调及持续文档理解。
