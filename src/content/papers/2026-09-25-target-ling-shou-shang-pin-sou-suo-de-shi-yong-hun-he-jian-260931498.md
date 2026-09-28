---
title: 'Retail Product Search: A Practical Approach at Target'
title_zh: Target 零售商品搜索的实用混合检索方案
authors:
- Darshan Sonagara
- Qujiaheng Zhang
- Ankit Singh
- Alex Li
affiliations:
- Target Corporation
arxiv_id: '2609.31498'
url: https://arxiv.org/abs/2609.31498
pdf_url: https://arxiv.org/pdf/2609.31498
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 电商搜索 · 混合检索与结果融合
tags:
- Hybrid Search
- Dense Retrieval
- Rank Fusion
- E-commerce Search
- Vector Search
- Latency Optimization
one_liner: Target 混合词法-向量检索，加权交错融合，线上 CTR/转化提升并零结果减半
practical_value: '- 电商搜索/推荐候选生成不要用向量完全替代词法或协同信号：保留双通道，向量通道承接自然语言和长尾查询，词法/ID 通道保证精准意图与品牌/SKU
  命中；同时把 zero-result 作为上线必须观测指标。

  - 多路融合优先实验 weighted interleaving：相比简单分数归一化或串行合并，它能更稳地控制各通道曝光与排序多样性，本案例线上 CTR、订单转化和每访客需求均获得提升。

  - 将精度控制作为最终结果集独立环节：对向量召回噪声做词法命中、规则或分类器过滤，再交给精排，尤其适合电商 SKU/品牌/规格等硬约束场景。

  - 生产部署把 embedding 计算、ANN 索引、缓存和融合放关键路径优化，并对向量通道做降级与超时控制，保证低延迟；可复用到实时搜索和推荐召回。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
电商搜索既要相关又要可购买，用户意图覆盖从精确匹配到开放发现，还需平衡相关性、营收、利润与低延迟。纯关键词方法难以处理自然语言或语义查询；纯向量搜索又会丢失关键意图信号或低精度结果。

**方法关键点**  
Target 上线混合检索：词法检索与向量检索双通道召回；针对数据清洗与 embedding 训练单独设计；在最终结果集做 precision control；比较多种融合策略后采用 weighted interleaving；并对生产链路做性能优化以维持低延迟。

**关键结果**  
离线评估指标提升；线上 A/B 相比纯词法搜索：CTR +0.97%，订单转化率 +0.98%，Demand per Visitor +1.10%，零结果搜索约减少一半。系统已全量部署，每日服务数百万用户。
