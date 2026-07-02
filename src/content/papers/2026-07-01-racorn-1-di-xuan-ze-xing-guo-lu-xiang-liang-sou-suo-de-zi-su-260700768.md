---
title: 'RACORN-1: Adaptive Recall-Preserving Speedup for Low-Selectivity Filtered
  Vector Search'
title_zh: RACORN-1：低选择性过滤向量搜索的自适应保召回加速方法
authors:
- Yoonseok Kim
- Gyusik Choe
affiliations:
- Naver Corporation
arxiv_id: '2607.00768'
url: https://arxiv.org/abs/2607.00768
pdf_url: https://arxiv.org/pdf/2607.00768
published: '2026-07-01'
collected: '2026-07-02'
category: Other
direction: 过滤向量搜索 · 图索引保连通
tags:
- FVS
- HNSW
- low-selectivity
- recall-collapse
- adaptive-fallback
- in-filtering
one_liner: 通过自适应搜索回退和精确回退修复ACORN-1在极低选择率下的召回崩溃，延迟降低9-26倍
practical_value: '- **可复用的自适应桥接机制**：在带过滤条件的向量召回中（如电商按类目、价格区间过滤），当过滤后节点稀疏导致图断开时，可借鉴ASF思路：将未通过过滤的节点转为“临时桥梁”，通过步长采样(strided
  sampling)增加空间多样性，既保连通又控延迟。

  - **工程实现中的召回-延迟折衷**：在推荐/搜索的HNSW索引上做低选择率过滤时，可直接应用RACORN-1的本地扩展，无需重建索引；在极低选择率（<0.1%）场景下结合AEF动态切换到线性扫描，实现召回1.0且20-75倍加速。

  - **对抗过滤-查询负相关**：电商中常见“冷门品牌+语义相似”查询会导致图索引严重断开；RACORN-1在这种负相关评测中将召回从0.08-0.41拉升至0.80-0.98，同时延迟比HNSW低5-9倍，为长尾检索提供了鲁棒方案。

  - **适用于向量库自研/选型**：业务自研向量检索引擎或评估开源方案时，可参考其分阶段跌退策略（ASF先尝试桥接，再AEF保证召回），便于在召回率和延迟间设置安全边界。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：过滤向量搜索（FVS）在RAG和推荐检索中普遍存在，但现有In-filtering方法ACORN-1在选择性低于1%时出现图连通性断裂，导致召回崩溃至0.03–0.72。亟需一种能在低选择性下保召回、低延迟的本地扩展方案。

**方法关键点**：
- **自适应搜索回退 (ASF)**：将未通过过滤的节点复用为“临时桥梁”，绕开断裂的路径；桥梁及两跳候选选取采用步长采样，增加空间多样性，避免局部过搜索。
- **自适应精确回退 (AEF)**：在选择性极低、图搜索收益小于线性扫描时，动态切换至暴力扫描，与ASF组合形成RACORN-1+，保证召回1.0。
- 完全基于ACORN-1索引本地扩展，无重新构建开销。

**关键结果**：
- 在1%–0.3%选择率甜点区，延迟较HNSW降低9–26倍；ACORN-1召回从0.45–0.72（1%）和0.03–0.10（0.3%）分别恢复至0.70–0.96和0.77–0.98。
- 在≤0.1%极端选择率下，RACORN-1+实现召回1.00，百万级数据集加速20–75倍，四千万级加速13倍。
- 负相关评测（K-means聚类）中，ACORN-1召回仅0.08–0.41，RACORN-1保持0.80–0.98，延迟仍比HNSW少5–9倍。
