---
title: 'misi: a Metric Inverted Sample Index'
title_zh: misi：基于随机样本的度量空间倒排索引
authors:
- Edgar Chavez
affiliations:
- CICESE
arxiv_id: '2608.27422'
url: https://arxiv.org/abs/2608.27422
pdf_url: https://arxiv.org/pdf/2608.27422
published: '2026-08-27'
collected: '2026-08-29'
category: Other
direction: 度量空间近似最近邻索引
tags:
- Approximate Nearest Neighbor
- Inverted Index
- Metric Space
- Memory-constrained serving
- Index Construction
one_liner: 用数据库随机样本作为词汇表构建近似最近邻倒排索引，构建快且省内存，查询吞吐弱于图索引
practical_value: '- 商品/内容 embedding 召回索引需要频繁更新（新品上架、活动换向量）时，misi 的构建可并行、确定性、比匹配召回
  graph 构建快 3.7x，适合每日/小时级全量重建，避免在线增量索引不一致。

  - 倒排样本思路可迁移为“粗召回-精排”两阶段：先用小样本词汇表构建轻量倒排，idf 加权投票快速取候选，再用高精度模型验证，适合在严格内存预算（如 8GB）下服务大规模候选库。

  - 使用黑盒度量/多模态 embedding（如 CLIP 或用户-商品联合空间）时，无需修改距离定义即可索引；RAG 知识库频繁更新、设备端内存受限场景可复用。

  - 注意查询吞吐是代价，线上高 QPS 场景应将其作为冷启动/离线批处理组件，或与 graph 索引组合，用其快速重建能力定期刷新主索引。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**  
已有近似最近邻（ANN）索引在构建成本、内存占用与查询吞吐之间存在权衡：图索引查询快但构建慢、内存高，很多场景（频繁重建、批处理、内存受限、黑盒度量）需要构建代价低、确定性强的通用索引。  

**方法**  
misi 用数据库自身的随机样本作为词汇表，样本大小正比于 n。每个对象用其 k_b 个最近样本点表示，通过可插拔内部索引在样本上检索；查询时用 idf 加权共享邻居投票，再精确验证 C 个候选。构造把 NAPP 从常数枢轴推广到线性词汇表，使倒排列表期望长度保持常数 ρ = k_b/α，将任意高召回 αn 点索引组合成 n 点索引。概率模型给出召回保证：k_b 对数于 n 即可跨越 overlap gap，验证预算由索引自身估计的 confusable count 提供；局限是投票无法分辨低于 1/√k_b 的 overlap 差异。  

**结果**  
构建 10^8 向量、64 核仅 5250 s，比匹配召回图构建快 3.7 倍，可在 3 GiB 内存 cap 下流式构建；从 NVMe 服务 10^8 向量仅需 8 GB 预算，低于 SSD-graph 基线工作下限。查询代价是吞吐：RAM 中饱和图基线快 6–16 倍，0.99 召回验证预算增长 n^{0.30}。适合构建成本、确定性、内存或黑盒度量优先的场景，而非峰值查询吞吐。
