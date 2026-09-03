---
title: Index-Free Dynamic Edge Retrieval with Energy-Tail-Aware Partial Scans
title_zh: 无索引动态边缘检索：能量尾部感知的部分扫描
authors:
- Mohammad Arif Rasyidi
- Omar Alhussein
affiliations:
- Khalifa University
arxiv_id: '2609.01820'
url: https://arxiv.org/abs/2609.01820
pdf_url: https://arxiv.org/pdf/2609.01820
published: '2026-09-01'
collected: '2026-09-03'
category: RecSys
direction: 边缘向量检索加速 · 动态 MIPS
tags:
- Dynamic MIPS
- Edge Retrieval
- Index-Free
- Partial Scan
- Quantization
one_liner: 提出 ETAR，通过保留查询高能量坐标与低精度表示加速动态 MIPS，兼顾高召回与简单更新
practical_value: '- 在推荐系统召回阶段，若使用内积打分（如双塔 embedding），可借鉴 ETAR 的查询能量裁剪思路：对 query 向量按平方值从大到小累加，直到覆盖总能量的
  90%-95%，仅在这些维度上做部分内积，跳过尾部长尾，大幅减少每次请求的计算量。

  - 对于需要频繁更新（新商品上架、用户行为流式更新）的在线召回，ETAR 的无索引设计避免了索引重建成本，天然适配流式数据；可在边缘/移动端部署个性化召回，如手机端本地推荐，利用
  ARM 设备上实测最高 6.9 倍加速。

  - 低精度表示与全精度 rerank 的组合值得落地：先用低精度（如 int8/float16）估算相似度筛选候选，再对固定数量候选用全精度向量精确重排，实测召回
  99.2% 的同时延迟显著下降，适合精度敏感但延迟有限的生产环境。

  - 该方法也可用于 Agent 的本地检索记忆或工具调用时的向量匹配，在资源受限环境中实现快速相似度搜索，减少对服务端依赖。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：边缘设备上的动态最大内积搜索（MIPS）面临查询延迟与更新成本的两难：全向量扫描更新简单但查询慢，索引方法查询快但更新需维护额外结构。论文针对边缘检索场景，提出索引免费的方法 ETAR，在保持更新简单的同时降低查询计算量。

**方法关键点**：ETAR 利用查询向量坐标的能量分布：按平方值从大到小保留坐标，直到保留部分覆盖查询总平方幅值的绝大部分，剩余视为低幅值尾部。查询时只对保留坐标进行内积计算，并用紧凑的低精度表示（如量化）加速；对跳过坐标进行校正估计相似度；最后取固定数量的候选用全精度向量重新排序，保证精度。由于不构建任何索引，插入、替换、删除等更新操作与简单扫描一样直接修改向量列表。

**关键结果数字**：在 9 个静态数据集上五次运行平均 Recall@10 达 99.2%，同时在代表性设置下比精确扫描快 4 倍以上；在 ARM 移动设备上，四种合成分布下最高快 6.9 倍；在五个流式工作负载中，所有测量点均保持 100% Recall@10，无需重建索引。代码已开源。
