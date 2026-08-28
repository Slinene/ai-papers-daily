---
title: Conversational Recommendation over Live E-Commerce Catalogues with Self-Refreshing
  Retrieval
title_zh: 自刷新检索驱动的实时电商目录对话推荐
authors:
- Ante Kapetanovic
- Tomislav Duricic
- Dionizije Fa
- Andro Mercep
- Emanuel Lacic
affiliations:
- Infobip
arxiv_id: '2608.27006'
url: https://arxiv.org/abs/2608.27006
pdf_url: https://arxiv.org/pdf/2608.27006
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 实时电商目录增量检索对话推荐
tags:
- Conversational Recommendation
- Incremental Indexing
- Retrieval-Augmented
- E-commerce
- Vector Index
- LLM Controller
one_liner: 提出自刷新检索器，用stable ID与双哈希只重嵌入新增/语义变化商品，将实时目录增量同步到向量索引，支撑低成本WhatsApp对话购物助手
practical_value: '- **增量索引可直接落地电商搜索/推荐**：用 stable product ID + full hash + semantic
  hash 对商品变化分类，只重嵌入新增/语义变化商品，价格库存等 metadata-only 只更新过滤字段。这样可以在高频变动的促销/库存场景中保持向量索引实时性，避免全量重建的成本。

  - **LLM 使用做减法**：对话侧只让 LLM 做意图分类和偏好引导，检索/重排/多样性走专用函数。生成路径 free 让成本、延迟可预测，适合大规模线上
  QPS；换成小模型或规则也不会影响核心推荐效果。

  - **同步安全机制值得抄**：拒绝空/不完整快照防止误删；先准备 embedding 再写，先 upsert/metadata update 再 deletion；非事务写需加
  staging/rollback 和异常 delta 监控。这些是生产上目录刷新容易踩的坑。

  - **架构解耦便于多商户/多渠道扩展**：VectorStore interface + 单一 model proxy，使商品 feed 接入、embedding
  模型、前端渠道可替换；语言检测后英文检索本地语言回复可降低多语言 embedding 成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM-based CRS 通常在静态 benchmark 上评测，但真实电商目录持续变化：商品新增、下架、改价、改描述。全量 re-index 浪费计算，索引漂移又会推荐缺货/下架商品。作者把目录新鲜度作为生产化对话推荐的工程核心，而不是模型质量。

## 方法关键点
- **自刷新检索器**：从 merchant product feed（XML）抓取、流式解析、缓存；对每个商品计算三类标识：stable product ID 用于精确定位和删除；full hash 检测任意字段变化；semantic hash（name/description/brand/category）判断是否需要重新 embedding。
- **五类增量变化**：new / semantically changed 需要 enrich + embed + upsert；metadata-only（价格/库存）只更新记录和过滤条件，保留向量；deleted 删除；unchanged 跳过。这样计算量与变化子集成正比。
- **对话 pipeline**：orchestrator-as-controller，LLM 只做 8 类意图分类和 elicitor 子代理的 1–3 个澄清提问；推荐路径为 content-based semantic retrieval + 可选 non-generative rerank + greedy brand/category diversity，生成路径 free，成本可预测。
- **工程解耦**：单一 model proxy 统一 embedding/生成/rerank 调用；VectorStore interface 可替换；语言检测后英文检索、用户语言回复。

## 关键结果数字
在 500 条匿名目录上的同步实验（median）：full rebuild 2.914s。增量同步中，no change 0.053s（占全量 1.8%），add product 0.321s（11.0%），price/stock 更新 0.072s（2.5%），description/category 变化 0.357s（12.3%），delete 0.062s（2.1%）。所有 ID/hash/embedding 调用检查均通过，证明变化分类和操作计数符合预期。注意评估只覆盖同步，不涉及 ranking quality。

## 最值得记的一句话
生产化 LLM 对话推荐的核心瓶颈不是生成质量，而是目录新鲜度：用 stable ID + 双哈希做增量同步，让索引更新成本与变化量成正比，同时把 LLM 仅用于意图与偏好抽取，推荐路径保持可预测、低成本。
