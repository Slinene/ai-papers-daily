---
title: 'URecJPQ: Memory-efficient Multimodal Recommendation Models through RecJPQ
  in Large-Scale Scenarios'
title_zh: 大规模多模态推荐的URecJPQ：联合乘积量化实现内存高效模型
authors:
- Giuseppe Spillo
- Zixuan Yi
- Aleksandr Petrov
- Cataldo Musto
- Craig Macdonald
- Iadh Ounis
affiliations:
- University of Bari Aldo Moro
- University of Glasgow
- Spotify
arxiv_id: '2606.23291'
url: https://arxiv.org/abs/2606.23291
pdf_url: https://arxiv.org/pdf/2606.23291
published: '2026-06-22'
collected: '2026-06-23'
category: RecSys
direction: 多模态推荐模型压缩 · 联合乘积量化
tags:
- Multimodal Recommendation
- Product Quantization
- Memory Efficiency
- Large-scale RecSys
- Embedding Compression
one_liner: 用联合乘积量化将用户/物品ID与多模态特征压缩为共享子嵌入拼接，在参数量减少98%+的同时保持推荐精度
practical_value: '- 在电商/广告等大规模多模态推荐场景，可直接采用 **联合乘积量化（JPQ）** 替换全量 ID 嵌入表：为每个 user/item
  分配多组码本中的码字索引，拼接得到嵌入向量，将参数量压缩 98%–99%，大幅降低 GPU 显存占用和检查点大小。

  - 多模态侧，可将预训练的模态特征（文本、图像等）也纳入量化框架，例如对模态编码器输出做分桶或学习离散码本，避免存储每个 item 的完整 dense 向量，特别适合物品库频繁更新的广告系统。

  - 实验发现，在婴童产品等某些品类上，量化后模型 **Recall 反而提升 85%**，暗示嵌入压缩带来的正则化效应能缓解稀疏数据下的过拟合，可尝试在 cold-start
  或长尾 item 上刻意使用更高压缩比。

  - 工程落地几乎零成本：URecJPQ 仅修改嵌入查找层，不改变模型主干架构，可以直接嫁接到现有双塔、DIN 等模型上，快速上线测试。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：工业级多模态推荐系统中，用户和物品的 ID 嵌入表以及多模态特征存储消耗大量显存，限制了大模型训练和部署。现有压缩方法往往忽略多模态特征的存储瓶颈，导致整体内存压力依然巨大。

**方法**：提出 URecJPQ，将 Joint Product Quantization 扩展到多模态推荐。核心做法是：不再为每个 user/item 学习独立的 dense embedding，而是构建多个共享的 **子嵌入码本**（sub-embedding codebooks）；每个 user/item 的最终表示为从各个码本中选取对应行的向量拼接。对于多模态特征，同样可量化或采用同结构压缩。训练时只学习这些共享码本，参数量与 user/item 数量解耦。

**结果**：在 MovieLens（电影）、Amazon Baby（婴童）、Amazon Sports（体育）三个数据集上评估。大规模设置下，检查点大小缩减 86%–98%，可训练参数量缩减 98%–99%；平均召回下降仅 8.5%，NDCG 下降 16%；在婴童品类上，Recall 甚至提升 85%，说明量化正则化对稀疏场景有益。
