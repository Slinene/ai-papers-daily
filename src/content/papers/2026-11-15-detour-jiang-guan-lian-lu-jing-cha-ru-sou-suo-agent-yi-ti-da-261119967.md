---
title: 'DetouR: Plugging Association Routes into Search Agents for Multi-hop Question
  Answering'
title_zh: DetouR：将关联路径插入搜索 Agent 以提升多跳问答
authors:
- Tingwei Chen
- Yunxiao Shi
- Zhendong Chu
- Zhiying Deng
- Min Xu
- Qingsong Wen
arxiv_id: '2611.19967'
url: https://arxiv.org/abs/2611.19967
pdf_url: https://arxiv.org/pdf/2611.19967
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: 搜索 Agent 关联证据链路增强
tags:
- Search Agents
- Multi-hop QA
- Link Rerouting
- Personalized PageRank
- RAG
- Context Selection
one_liner: 用页面超链接重路由近重复查询，并用个性化 PageRank 保留证据链，零额外搜索/LLM 调用提升多跳问答 EM
practical_value: '- 在电商/推荐的 RAG/Agent 流程中，商品详情页、品牌、品类、相关推荐等已有关联关系可充当 association graph；当后续
  query 与历史 query 近重复且不新增有效证据时，不要继续搜原 query，改为从已召回 item 的关联 item 发起查询，用 LightGBM 预估「新增有效证据/商品」即可，不必上
  LLM。

  - 多 query 结果融合不要只依赖 RRF：它会偏向反复出现的头部结果，丢掉仅由单个 query 召回的关联证据。可改为 Round-robin 去重 +
  以 query 命中 item 为 seed 的 personalized PageRank，在 item-item 图上传播，保留多条证据链/推荐理由。

  - 链路选择与上下文保留用 CPU 级 LightGBM/PageRank 即可，无需 7B/8B reranker；该方案零额外 search/LLM 调用，且作为插件对现有
  agent 无侵入，适合高 QPS 业务，不需要重训 agent。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
搜索 Agent 通常走语义路由：从问题推缺失信息并写成 query，只能检索到模型能命名的内容。但多跳证据往往就在已检索页面的超链接一步之外。同时，常见 RRF 融合会偏向反复出现的结果，丢弃仅由单次检索命中的第二跳证据。论文量化显示，HotpotQA 上关联路由可触达 85.8% 的 gold pages，高于语义路由的 76.7%；近重复 query 约占 1/4 且几乎不新增 gold，还会导致 context completeness 随搜索次数下降。

**方法关键点**
- **Link Rerouting**：对后续 query 与历史 query 的 content-word Jaccard ≥ 0.8 判为近重复；从已检索 top pages 的链接中构造候选关联路由，用 LightGBM LambdaRank 预估每条路由的新增 gold 数量，选择最佳路由替换原 query；不增加 search 或 LLM 调用。
- **Chain-aware Context Selection**：先用 Round-robin 对多列表去重合并形成先验，再以问题中命名的实体为 seeds，在检索到的 passage 链接图上做 personalized PageRank，最终按 `s(d)=p(d)+μ/(π(d)+1)` 选 top-n，保留仅由单次检索命中的证据链。

**关键实验与结果**
在 HotpotQA 和 2Wiki 上接入 4 个 agent（IRCoT、ReAct、Search-R1、Plan），同样检索 budget 下，平均 EM 分别提升 1.4 和 4.0；live 与 replay 结果一致。消融显示，仅做 Link Rerouting 提升 +0.3/+0.8，仅做 Chain-aware Context Selection 提升 +0.8/+2.5，两者组合后超过单独之和。Chain-aware Context Selection 不用模型调用，在 2Wiki 上完整上下文率 64.5%，高于 8B reranker 和 LLM judge；LightGBM 路由选择与 0.6B cross-encoder reranker 效果相当。

**最值得记住的一句话**：用已有超链接/关联结构做非语义证据补充，关键是「把近重复查询改走关联路径，并用图传播保住单次检索命中的证据」，轻量 CPU 方案即可，不必上 LLM。
