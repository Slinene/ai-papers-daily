---
title: 'TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge'
title_zh: TaskBridge：面向 2026 SIGIR 电商挑战赛的任务型查询改写技术报告
authors:
- Zhiheng Fu
- Yupeng Hu
- Zixu Li
- Zhiwei Chen
- Qinlei Huang
- Shaokun Wang
- Han Liu
- Fan Liu
- Weili Guan
- Liqiang Nie
affiliations:
- Shandong University
- Harbin Institute of Technology (Shenzhen)
- City University of Hong Kong
- Southeast University
arxiv_id: '2610.37231'
url: https://arxiv.org/abs/2610.37231
pdf_url: https://arxiv.org/pdf/2610.37231
published: '2026-10-27'
collected: '2026-10-28'
category: QueryRec
direction: 任务型电商 Query 改写 · Catalog 锚定选词
tags:
- Query Reformulation
- Catalog Anchoring
- BM25
- LLM
- Pareto Selection
- E-commerce Search
one_liner: 以目录语义锚定、五候选改写和协议感知选择实现任务型电商查询的 BM25 检索增强，获挑战赛第一
practical_value: '- 构建 catalog 短语词典与 semantic anchors：从商品标题/描述中抽取 n-gram 短语，用 LLM
  纯化为 product category/object/accessory 三类可购买实体，过滤品牌、场景噪声，再用 embedding 在线检索语义锚点。这套离线资源可直接用于电商搜索
  query 改写、query 推荐、召回阶段的 query 扩展，缓解用户活动型表达与商品标题的词汇鸿沟。

  - 多候选改写 + 协议感知选择：生成 raw/feedback/vote/need/prod 五类候选，覆盖保守到激进、意图保护到产品导向的不同改写假设；再以
  BM25 top10 的 reranker 分数加 log 折扣作为质量代理，Automatic 选最高分，Interactive 用 weighted Jaccard
  overlap 做 Pareto 多样性选择。这个选择框架可迁移到多 query 改写、生成式重写、多策略召回合并，控制多样性与质量平衡。

  - 无训练 LLM 改写 + 传统 BM25 的轻量架构：整个方案不训练模型，依赖 Qwen3.5-9B 生成改写、embedding/reranker 做选择，最终仍走
  BM25 检索。适合需要快速落地、资源有限的业务场景，可先用 LLM 辅以字典约束生成多个候选，再用 reranker 代理选优，降低上线成本。

  - 多轮反馈里的 Keep/Add/Drop/Replace 编辑和 margin 接受条件：对 Agent 式 query 优化有直接参考价值，能避免 LLM
  在迭代中过度改写造成意图漂移。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
任务型电商查询如 “make lasagna” 隐含产品需求（烤盘、食材、厨具），与商品标题词汇差异大，直接用 BM25 检索效果差；改写需在保留任务意图的同时映射到目录可匹配表达，避免过改写或欠改写。

**方法关键点**  
TaskBridge 由三个模块组成。Catalog Semantic Anchoring 从商品语料构建两级短语词典：标题级 2-5 gram 用于纯化为 product category/object/accessory 的 semantic anchors，语料级 1-3 gram 用于受限改写候选；在线用 Qwen3-VL-Embedding-8B 检索 top50 相关锚点。Unified Five-Candidate Rewriting 生成五个候选：原始 query 保护；基于 BM25 反馈的多轮编辑（Keep/Add/Drop/Replace，接受需质量代理提升超过 margin）；三角色投票（conservative/taxonomy/intent）共识选择锚点；保守 need-aware 从词典选短语；紧凑 product-oriented 选短短语。Protocol-Aware Selection 用 BM25 top100，Qwen3-VL-Reranker-8B 对 top10 打分，取 top5 对数折扣得到质量代理；Automatic 选最高分，Interactive 在四候选组合上以平均质量最大、最大 weighted Jaccard overlap 最小做 Pareto 选择。

**关键结果**  
Open Phase 相对原始 query BM25 基线，Automatic NDCG@10 0.42→0.49，Recall 0.30→0.29，MAP 0.19→0.20；Interactive NDCG@10 0.42→0.58，Recall 0.30→0.33，MAP 0.19→0.23。Closed Phase TaskBridge Automatic 0.27/0.16/0.11，Interactive 0.31/0.18/0.12，多改写带来额外增益。最终获 SIGIR 2026 eCommerce Challenge 第一。

**最值得记住的一句话**  
任务型查询改写的核心不是简单扩展词，而是用 catalog 语义锚点可控地把 activity-level intent 翻译成可检索的产品表达，并用多候选质量-多样性选择适配单/多 query 预算。
