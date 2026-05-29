---
title: 'GRASP: Plan-Guided Graph Retrieval with Adaptive Fusion and Reranking on Semi-Structured
  Knowledge Bases'
title_zh: 面向半结构化知识库的计划引导图检索与自适应融合重排序框架
authors:
- Yicheng Tao
- Yiqun Wang
- Xiangchen Song
- Xin Luo
- Kai Liu
- Jie Liu
affiliations:
- University of Michigan
arxiv_id: '2605.30237'
url: https://arxiv.org/abs/2605.30237
pdf_url: https://arxiv.org/pdf/2605.30237
published: '2026-05-28'
collected: '2026-05-29'
category: RecSys
direction: 半结构化知识库检索 · 图与文本融合
tags:
- Semi-structured KB
- Graph Retrieval
- Dense Retriever
- Reranker
- Plan-guided
- Hybrid Retrieval
one_liner: 提出三阶段GRASP框架，通过计划引导图检索、条件融合稠密检索和重排序，大幅提升半结构化知识库检索性能。
practical_value: '- **电商搜索场景可直接复用**：Amazon 产品搜索属于典型的半结构化知识库，查询常同时包含自由文本与结构化约束（如品牌、类别），GRASP
  将查询解析为图遍历计划 + 文本条件，再融合稠密检索与重排序，可直接迁移到电商搜索系统，提升带约束查询的 Hit@1。

  - **图计划生成模块的低成本实现**：GRASP 使用 LLM 将自然语言查询转换为逻辑图计划，但不依赖 LLM 在线推理，而是将计划离线生成后作为融合的先验，这在工程上可以预先计算常见查询模式，减少线上延迟与成本。

  - **自适应融合与重排序的架构设计**：利用计划条件加权融合图分支与文本分支的候选集，再通过微调重排序模型做最终排位，该模块化设计可独立应用于现有文本-图混合检索系统，只需注入计划向量即可控制融合权重，无需端到端重训。

  - **重排序器微调的数据构造技巧**：GRASP 用推理时暴露的候选分布合成困难负样本，以微调重排序模型，这种基于检索结果的负采样策略对提升排序准确性很有效，可直接借鉴到推荐/广告的排序模型训练中。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：半结构化知识库（SKB）将文本文档嵌入实体与关系的类型图中，支撑产品搜索、学术论文查找等应用。现有混合检索方法要么仅将图用于查询扩展，要么全局加权混合文本与图分支，或依赖微调图遍历生成器，往往未能充分解耦查询的结构约束与文本意图。  
**方法**：GRASP 提出三阶段框架：（1）**计划引导的图检索**：利用 LLM 将自然语言查询解析为逻辑形式的图遍历计划，在图上执行计划以获取符合结构约束的候选实体集合；（2）**计划条件融合**：将生成的计划向量与稠密检索文本分支的嵌入进行条件加权融合，实现自适应平衡图与文本信号；（3）**重排序**：采集融合后的候选集，基于难负采样微调重排序模型，进一步精排。  
**结果**：在 STaRK 的三个基准（Amazon、MAG、Prime）上全面超越 SOTA，平均 Hit@1 从 62.0 提升至 73.9，消融实验验证各模块的必要性，对计划生成误差也表现出鲁棒性。
