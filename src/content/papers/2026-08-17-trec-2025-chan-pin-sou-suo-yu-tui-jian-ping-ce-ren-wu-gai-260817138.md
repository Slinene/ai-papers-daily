---
title: Overview of the TREC 2025 Product Search and Recommendation Track
title_zh: TREC 2025 产品搜索与推荐评测任务概览
authors:
- Dean E. Alvarez
- Surya Kallumadi
- Daniel Campos
- ChengXiang Zhai
- Alessandro Magnani
- Rikiya Takehi
- Michael D. Ekstrand
affiliations:
- University of Illinois Urbana-Champaign
- Coursera
- Snowflake
- Coupang
- Waseda University
arxiv_id: '2608.17138'
url: https://arxiv.org/abs/2608.17138
pdf_url: https://arxiv.org/pdf/2608.17138
published: '2026-08-17'
collected: '2026-08-19'
category: Eval
direction: 电商搜索与推荐评测 · 产品关系数据集
tags:
- TREC
- Product Search
- Recommendation
- Evaluation
- Query Expansion
- Complementary Products
one_liner: 提供 TREC 2025 产品搜索与推荐评测框架，新增区分互补/相关关系的产品推荐标注数据集
practical_value: '- 产品关系建模：借鉴其区分 complementary（互补，如配件）与 related（相关，如替代品）的思路，在电商推荐中构建更细粒度关系标签，用于训练排序模型或构建知识图谱，提升推荐可解释性和多样性。

  - Query 扩展任务：在搜索/推荐中，query expansion 可用于生成式推荐（LLM4Rec）的 prompt 设计或 query 特征增强；可参照其评估框架设计离线和在线指标，验证扩展
  query 对检索效果的影响。

  - 对话式产品发现：数据标注为 complementary/related 为对话式购物代理（Agent）提供候选商品关系基础，可用于约束 LLM 生成的候选
  item 集合，减少幻觉，提升上下文相关性。

  - 开箱即用评测：若公司需快速验证检索/推荐模型，可复用该 benchmark 作为外部评测集，节省自建标注成本；同时其任务设计启示内部评测集应区分“互补”和“相关”，避免混淆。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：电商产品目录规模激增，产品搜索与推荐成为核心能力，但缺乏高质量端到端检索质量评测数据集。2025 年 TREC 产品搜索与推荐 track 在 2023/2024 基础上继续，聚焦两个关键任务。

**方法关键点**：
- 搜索任务为 query expansion：给定用户查询，生成扩展查询以提升产品检索效果。
- 推荐任务为 related-product recommendation：核心创新是提供标注数据集，明确区分 complementary（互补，如手机壳与手机）和 related（相关，如相似或替代产品）两类关系；可作为对话式产品发现体验的构建块。
- 提供统一评测框架与标注数据，支持研究社区开发端到端检索与推荐系统。

**关键结果数字**：作为 track overview 论文，未报告具体参与者得分或对比结果；主要贡献在于任务设计、数据标注与评测基准。
