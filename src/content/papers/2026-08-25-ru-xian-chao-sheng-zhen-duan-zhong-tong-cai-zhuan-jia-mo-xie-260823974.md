---
title: Boot-and-Feedback Framework for Generalist-Expert Model Collaboration in Breast
  Ultrasound Diagnosis
title_zh: 乳腺超声诊断中通才-专家模型协作的引导与反馈框架
authors:
- Ming Cheng
- Hongyu Sun
- Zhaolin Chen
- Jun Liu
- Hossein Rahmani
- Qiuhong Ke
affiliations:
- Department of Data Science & AI, Monash University, Australia
- Department of Computer Science, Renmin University of China, China
- School of Computing and Communications, Lancaster University, UK
arxiv_id: '2608.23974'
url: https://arxiv.org/abs/2608.23974
pdf_url: https://arxiv.org/pdf/2608.23974
published: '2026-08-25'
collected: '2026-08-30'
category: Multimodal
direction: MLLM 与视觉专家协作优化
tags:
- Multimodal LLM
- Expert Collaboration
- BI-RADS
- Breast Ultrasound
- Attention Fusion
- Hallucination Reduction
one_liner: 提出 BooF 框架，通过 BI-RADS 引导 MLLM 生成可靠描述并反馈给视觉专家，提升诊断准确性与可解释性
practical_value: '- 借鉴领域知识约束：用结构化 schema（如商品属性、广告合规词表）引导 LLM 生成内容，减少幻觉。

  - 两阶段协作：先由轻量专家模型给出初步信号，再让通用 LLM 基于该信号生成解释或描述，反馈给专家模型融合，可提升多模态推荐/审核模型性能。

  - Attention-Gated 跨模态融合模块：轻量、可自适应过滤噪声，适合工程上在现有多模态模型中插入，无需大改架构。

  - Bootstrapping 思想：通用模型与专家模型循环增强，可用于 Agent 系统中不同角色协作，比如生成式商品描述与检索模型互反馈。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：乳腺超声诊断依赖操作者经验，深度学习方法缺乏可解释性，而 MLLM 因领域知识不足常产生幻觉描述，误导下游专家模型。

**方法关键点**：提出 BooF 框架，包含两个阶段。Boot 阶段：利用 BI-RADS 词典和视觉专家模型的初步良恶性预测来引导 MLLM，使其生成符合临床规范的描述，减少幻觉。Feedback 阶段：设计轻量级 Attention-Gated Cross-Modality Fusion Module，将 MLLM 生成的文本描述与视觉特征融合，让专家模型利用文本反馈，同时自适应过滤噪声。该框架实现了通才 MLLM 与专家模型的协同，提升诊断准确性和可解释性。

**关键结果**：在多个乳腺超声数据集上，BooF 显著优于现有 SOTA 方法，在诊断准确性和可解释性方面均有大幅提升（具体数值见原文）。
