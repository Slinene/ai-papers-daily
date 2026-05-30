---
title: No More K-means:Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval
title_zh: 告别K-means：单阶段稀疏编码实现高效多向量检索
authors:
- Lixuan Guo
- Yifei Wang
- Tiansheng Wen
- Aosong Feng
- Stefanie Jegelka
- Chenyu You
affiliations:
- Stony Brook University
- Xidian University
- Amazon AGI SF Lab
- Georgia Tech
- Yale University
arxiv_id: '2605.30120'
url: https://arxiv.org/abs/2605.30120
pdf_url: https://arxiv.org/pdf/2605.30120
published: '2026-05-28'
collected: '2026-05-30'
category: RecSys
direction: 多向量稀疏检索 · 倒排索引加速
tags:
- Sparse Retrieval
- Multi-Vector Retrieval
- Inverted Index
- Sparse Autoencoder
- Late Interaction
one_liner: 提出SSR框架，用Sparse Autoencoder将token嵌入稀疏化，直接构建倒排索引，实现精度、速度和索引速度三赢。
practical_value: '- 电商搜索/推荐召回中，可用稀疏编码替代K-means聚类构建索引，大幅降低离线索引时间（15倍加速），适合实时更新频繁的语料。

  - 训练时联合重构损失与对比损失的混合目标，可保证稀疏特征既保留语义又具备判别力，可借鉴到query-doc/query-item匹配的稀疏表示学习。

  - 倒排索引上利用块级上限跳过与粗到精剪枝（SSR++），在保证精度无损前提下将延迟减半，对高流量在线检索场景有直接工程价值。

  - 该方法可扩展到LLM backbone，结合现代大模型生成式推荐或Agent的记忆检索，用稀疏token交互实现高效知识召回。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机：** 多向量检索（如ColBERT）通过保留token级交互大幅提升精度，但面临存储和计算瓶颈：现有系统依赖K-means聚类和量化进行压缩，导致索引构建耗时百小时以上，且压缩造成语义信息损失。亟需一种既保留细粒度交互又消除聚类负担的范式。

**方法：** 提出Single-stage Sparse Retrieval (SSR)，核心是用Sparse Autoencoder (SAE) 将每个token嵌入投影到高维（如h=16384）但极度稀疏（仅K=32个激活神经元）的空间，从而直接利用倒排索引进行检索，无需聚类。关键设计包括：
- 稀疏交互评分：MaxSim仅计算重叠激活神经元的内积，可通过倒排列表高效实现；
- 混合训练：结合无监督TopK稀疏重构损失（含Multi-TopK、辅助损失和稀疏对比损失）与监督对比损失，使稀疏特征同时保持重构性和判别力；
- 索引构建：为每个神经元维度建立倒排列表，存储文档内该维度的最大激活值，并分块以便块级剪枝；
- 加速策略（SSR++）：粗阶段仅用Kcoarse=4个主要神经元和块跳过生成候选集，精阶段再用全部K个神经元精确打分。

**实验：** 在MS MARCO和BEIR 13个数据集上，SSR-CLS平均nDCG@10达53.4，超过Splade-v3（51.2）和PLAID（49.3）；SSR-tok检索延迟仅17.5ms，ColBERTv2为37.1ms；索引时间从ColBERTv2的122.9小时降至7.5小时（>15×加速），峰值内存从274GB降至34.6GB。扩展至Llama-Embed-8B时，SSR-CLS平均nDCG@10达67.1，优于Qwen3-Embedding-8B。消融表明K=32为最佳效率-效果平衡。
