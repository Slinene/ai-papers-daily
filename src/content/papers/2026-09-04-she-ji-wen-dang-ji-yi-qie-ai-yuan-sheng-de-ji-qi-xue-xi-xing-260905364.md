---
title: 'Design Docs Are All You Need: An AI-native Machine-Learning Performance Tool'
title_zh: 设计文档即一切：AI 原生的机器学习性能建模工具
authors:
- Samuel Kushnir
- Kimia Noorbakhsh
- Kavya Sreedhar
- Liqun Cheng
- Ming Liu
- Parthasarathy Ranganathan
- Mohammad Alizadeh
- Fred Kjolstad
- Suvinay Subramanian
affiliations:
- Google DeepMind
- MIT
- Stanford
- Google
arxiv_id: '2609.05364'
url: https://arxiv.org/abs/2609.05364
pdf_url: https://arxiv.org/pdf/2609.05364
published: '2026-09-04'
collected: '2026-09-08'
category: Agent
direction: Agent 驱动代码生成 · 设计文档化
tags:
- Design Docs
- AI Coding Agents
- Performance Modeling
- Symbolic IR
- SymPy
- Code Generation
one_liner: 用设计文档作为唯一持久化工件，让 AI 编码代理按需重新生成性能建模库代码
practical_value: '- 借鉴“文档即代码”的范式：将推荐/搜索系统中最易变的模块（如召回粗排、性能预算模型）用结构化自然语言设计文档描述，并让 AI
  编码代理根据文档自动生成实现，减少因架构频繁变动带来的维护成本。

  - 使用逐步工作示例（worked examples）作为设计文档的一部分，充当生成代理的 in-context demonstrations，提高代码生成准确率；在业务中编写复杂策略文档时可附带典型输入输出样例。

  - 构建符号化成本表达式（如 SymPy）对推荐系统推理链路进行性能建模，支持快速解析化扫描不同候选集大小、模型结构、硬件配置，辅助容量规划和架构选型。

  - 定义最小递归算子 IR 来表达计算图，将粗粒度汇总与细粒度调度分离，可用于优化在线推理的资源分配与调度策略。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：ML 性能建模框架同时受模型架构和底层硬件快速演进冲击，既有抽象快速过时，导致持续重构。AI 编码代理的成熟让“整体重新生成”比“增量修补技术债”更便宜。

**方法**：SMART 仓库主分支几乎不含代码，而是由自包含的自然语言设计文档组成 DAG。编码子代理仅根据这些文档在新版本更新时重新生成实现；人类修改就是直接编辑文档，天然自文档化。两个关键设计：（1）文档风格围绕逐步工作示例展开，充当生成代理的 in-context demonstrations；（2）定义最小递归算子 IR，结合符号化（SymPy）成本表达式，提供快速解析汇总模式和慢速模调度模式。

**关键结果**：重新生成的实现复现了手工审计的参考模型——包括在 TPU pod 切片上服务 DeepSeek-V3——达到舍入精度，证明设计文档可以成为 ML 系统协同设计工具的持久化工件。
