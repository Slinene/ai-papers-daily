---
title: 'Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with
  AtlasNav'
title_zh: 直接语料交互中的证据盲区与 AtlasNav 持久化导航
authors:
- Hongyu Guo
- Zhiyu Zheng
- Zhao Cao
arxiv_id: '2608.24764'
url: https://arxiv.org/abs/2608.24764
pdf_url: https://arxiv.org/pdf/2608.24764
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 有限预算语料导航 · 持久化多视图 Atlas
tags:
- Agentic Search
- Evidence Blindness
- Corpus Navigation
- Multi-view Atlas
- DCI
one_liner: 提出 Evidence Blindness 四阶段诊断，并用持久化多视图语料图谱 AtlasNav 把有限预算的 agentic search
  从反复探索转为可复用导航
practical_value: '- 离线为商品/内容/企业知识语料构建持久化多视图结构：Topic、Identity、Episode、Relation，再与 BM25
  做加权 RRF 融合，供 Agent 查询时自适应路由；避免每个 query 动态重建 workspace，能显著降低在线 token/cost。

  - 用 Evidence Blindness 漏斗（Construction→Surface→Open→Locate）做过程诊断：不只追踪最终答案，还追踪相关商品/属性/证据片段是否被
  surface、open、locate 到模型上下文，可定位静默失败。

  - 保留原语料直接读取与全文检索，不做 query 条件剪枝，而是通过共享层级 + region anchors + cross-region bridges
  导航；适合电商/广告中长尾商品、合规要求高、多跳关系推理等场景。

  - Query-adaptive router 可用语料自监督任务训练：单文档/pair/triple 构造，parent-disjoint split，无需人工业务标注；轻量线性
  router 学一组语义+词法通道权重，可直接迁移到搜索/推荐入口的混合召回。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM agent 正从传统 RAG 走向 Direct Corpus Interaction（DCI），直接搜索、阅读、验证语料。但可达证据未必在有限交互预算内变得可用：证据可能不出现、支撑文档不被打开、打开后关键片段未被定位，而且往往没有显式失败信号。作者把这种渐进式静默损失称为 Evidence Blindness，并形式化为 Construction→Surface→Open→Locate 四阶段漏斗。仅靠最终答案会掩盖这一过程性失败。

### 方法关键点
- **持久化多视图 Corpus Atlas**：离线对每个文档构造 Topic、Identity、Episode、Relation 四个语义视图，分别编码；通过 multiplex Leiden 社区检测生成共享层级（77 个 parent regions / 443 个 leaves），保留区域内 anchors 和跨区 bridges，但不剪枝语料，原文档仍可直接读写。
- **Query-adaptive navigation**：轻量 router 输出四个语义通道 + BM25 的权重，用加权 Reciprocal Rank Fusion（RRF）融合全 corpus 排名；每个查询只决定导航优先级，不重建搜索空间。
- **过程诊断指标**：定义 EB_Any / EB_Mean / EB_All，以及 empirical reference gap `G_I(B) = A_ref - A_I(B)`，以同模型拿到 evidence-supplied reference 的表现为效率目标。

### 关键结果
- BrowseComp-Plus 上，AtlasNav 严格准确率 92.05%，比 DR-DCI（84.58%）高 7.47 个百分点，同时在线推理成本降低 30.21%；DeepSeek 骨干下 EB^S_All 从 14.10% 降到 4.94%，EB^L_All 从 24.46% 降到 11.45%。
- PhantomWiki 10K→1M 扩展中，1M 规模下 AtlasNav 的 Surface EB 为 49.5%，优于 DCI 59.0% 和 DR-DCI 87.0%，准确率 61.0% 最高。
- EnterpriseRAG-Bench 上 Overall 73.72，Invalid Extra Documents 仅 0.66，说明覆盖面提升不是靠无差别扩大证据集。

### 最值得记住的一句话
语料表示应被当作 agent 接口的一等公民：可复用结构能把有限交互从反复探索变成有效导航。
