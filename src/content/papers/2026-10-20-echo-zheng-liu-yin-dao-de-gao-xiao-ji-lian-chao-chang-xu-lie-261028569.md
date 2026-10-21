---
title: 'ECHO: Efficient Cascade with Homogeneous Operators for Distillation-Guided
  100K-Sequence Modeling'
title_zh: ECHO：蒸馏引导的高效级联超长序列建模
authors:
- Wenhao Li
- Qinglin Jia
- Chenghou Jin
- Zihong Xian
- Jiezhou Ji
- Yanzhi Liu
- Zezheng Wang
- Ruiming Tang
- Chaoyi Ma
- Zhaojie Liu
affiliations:
- Kuaishou Technology
arxiv_id: '2610.28569'
url: https://arxiv.org/abs/2610.28569
pdf_url: https://arxiv.org/pdf/2610.28569
published: '2026-10-20'
collected: '2026-10-21'
category: RecSys
direction: 长序列用户行为建模 · 蒸馏级联检索
tags:
- long-sequence modeling
- distillation
- two-stage retrieval
- CTR prediction
- user behavior sequence
- industrial recommendation
one_liner: 蒸馏引导的用户级选择+目标感知检索，将100K长序列压缩至10K原始记录，在线计算量降160倍且GAUC提升
practical_value: '- **用户级选择器离线写、在线只读固定K条记录**：将100K原始历史压缩为10K原始事件记录，在线排序只对K条做目标感知检索，完全解耦在线计算与原始序列长度。适合电商/广告场景下用户长期行为超长、多候选排序的工程落地。

  - **蒸馏监督替代简单的最近截断**：用全历史教师的目标感知打分做软分布蒸馏，再加边界排序辅助损失，让选择器在用户级就保留目标相关的历史。可直接借鉴到召回/精排的长期行为筛选，尤其对长尾兴趣和稀疏反馈更友好。

  - **教师、检索器、目标注意力共享Q/K参数**：保证粗选和精排的相关性度量一致，避免两阶段不一致导致的召回损失。工程实现上可用 key-side projection
  absorption 省去历史向量投影缓存。

  - **紧凑记录编码降低存储成本**：按字段宽度打包而不是统一int64，100亿用户规模下可节省数百TB存储。对大规模推荐系统的用户行为存储设计有直接参考价值。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

工业推荐中用户行为序列可达10万级，直接做目标感知的历史建模计算量随候选数和序列长度线性增长，在线不可行。检索式方法（如TWIN）虽然保留原始记录、可细粒度匹配，但每次候选请求都要扫描全历史；压缩式方法（如SequenceO1）固定计算量，但丢失item级可寻址性，长尾目标难以利用分散的历史证据。

## 方法关键点

ECHO采用两级预算的级联架构：
- **Distilled Selector（DS）**：用户级选择器，只用用户特征，对每用户历史打分并保留 Top-K=10000 条原始事件记录（含item ID、时间戳、side features）。该选择器通过一个全历史候选感知的teacher进行蒸馏监督：teacher为每个target计算历史相关打分，用软分布蒸馏损失 + 边界排序辅助损失训练DS，使DS在用户级就能保留目标相关的历史。
- **Target-aware Fine-grained Retriever（TFR）**：在线对每个候选从保留的K条记录中检索M=100条，再做目标注意力聚合。教师、TFR和聚合共享relevance Q/K参数，保证相关性度量一致。
- **部署优化**：common user inputs 按用户分组共享长历史，compact record encoding 按字段宽度打包节省存储，key-side projection absorption 避免在线投影历史向量。

在线复杂度与原始长度L无关，仅为 O(CK+CM)，在100K序列下相比端到端STCA减少约160倍序列分支FLOPs。

## 关键结果

在KuaiRand-1K和快手工业数据集上，8个任务GAUC全部最优，相对最强基线提升0.113%–1.520%。其中Comment任务在KuaiRand-1K上提升1.520%，工业数据Like提升0.345%。消融显示蒸馏监督对Comment任务带来2.371%的GAUC提升。选择器保留教师Top-100行为的recall达99.976%，保留attention mass 98.5%。在线A/B测试中，总App使用时长提升0.613%。

**最值得记住的一点**：用户级选择器通过目标感知蒸馏，在不依赖候选的情况下保留原始行为记录，把在线计算与序列长度解耦，同时维持细粒度匹配能力。
