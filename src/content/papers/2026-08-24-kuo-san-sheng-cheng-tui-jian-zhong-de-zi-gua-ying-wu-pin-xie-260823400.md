---
title: Adaptive Item-based Collaborative Structures via Noise Rescheduling in Diffusion
  for Generative Recommendation
title_zh: 扩散生成推荐中的自适应物品协作结构与噪声重调度
authors:
- Jiaqi Wang
- Tianying Liu
- Heng Chang
- Jihong Guan
- Wengen Li
- Shuigeng Zhou
affiliations:
- Tongji University
- Huawei Technologies Co., Ltd.
- Fudan University
arxiv_id: '2608.23400'
url: https://arxiv.org/abs/2608.23400
pdf_url: https://arxiv.org/pdf/2608.23400
published: '2026-08-24'
collected: '2026-08-25'
category: GenRec
direction: 生成式推荐 · 离散扩散 · 噪声重调度
tags:
- Generative Recommendation
- Discrete Diffusion
- Semantic ID
- Noise Rescheduling
- Collaborative Filtering
- RQ-KMeans
one_liner: 在离散扩散生成式推荐中注入物品共现先验与自适应噪声重调度，显著提升协作结构建模与召回精度
practical_value: '- 生成式推荐的 Semantic ID 构建不要只用文本语义；用 item co-occurrence 矩阵 + SVD 提取
  64 维协作特征，与文本 embedding 拼接后再 RQ-KMeans 量化。实验表明一阶共现信号足够，LightGCN 无额外提升，工程上简单且省成本。

  - 训练 BERT4Rec / 扩散式推荐等 masked 模型时，可以把 uniform mask loss 换成本文的自适应重加权：按 inter-item
  距离衰减、intra-item 位置衰减和 item 级 attention 动态给每个 masked token 的 loss 赋权，并 detach 权重防止模型偷懒，能明显提升协作信号学习。

  - 推理端加入 SID-validity constrained decoding：每一步根据已 unmask token 维护真实 item 候选集，只在合法
  token 子集上重归一化，可避免生成无效 item；可直接迁移到生成式召回、搜索词 token 生成等场景。

  - 在扩散式生成推荐与 AR 生成之间选型时，本文显示双向离散扩散在长序列和中频 item 上更稳，配合噪声重调度可超过强 AR baseline；但需评估 beam
  search + 约束过滤的推理延迟。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
离散扩散模型（DDM）用于生成式推荐具备非自回归、双向建模 Semantic ID 的优势，但现有方法在 item 表示和训练目标上都忽视 item-based 协同过滤信号：SID 多只由文本语义构造，缺少共现先验；扩散训练采用 uniform noise schedule，不区分被掩码 token 的上下文难易，难以学习 item 间结构依赖。

**方法关键点**  
- **共现指导的 SID 生成**：构建 item co-occurrence 矩阵，用截断 SVD 得到 64 维协作嵌入，与 Sentence-T5 文本语义特征拼接后，经 RQ-KMeans 生成多级离散 SID；相比 RQ-VAE 更稳定。  
- **两阶段扩散训练**：同时进行用户历史级掩码重建 L1 和下一 item 级掩码预测 L2，总损失 L=λL1+L2。  
- **自适应噪声重调度**：对 L1 中每个 masked token 的损失，动态赋权 W = W_struct + αA_ij；W_struct 使用 inter-item 与 intra-item 的几何衰减核建模局部可恢复性，A_ij 使用 item 级 attention 建模行为依赖，并 detach 权重防止退化。  
- **约束推理**：beam search + SID-validity filtering，保证生成 token 序列对应真实 item。

**关键结果**  
在 Amazon Scientific/Instrument/Video Game、MovieLens、Steam 五个数据集上，ANR-DiffRec 在 Recall@k 与 NDCG@k 上均超过 16 个 baseline。Scientific 上 Recall@1 从 LLaDA-Rec 的 0.0098 提升到 0.0122（相对 +24.5%）；MovieLens Recall@10 为 0.2977 vs 0.2820；Steam Recall@10 为 0.0991 vs 0.0914。消融显示去掉 noise rescheduling 后 Scientific NDCG@1 下降超过 15%，去掉共现信息也有一致下降；SVD 与 LightGCN 构造协作信号效果接近，Node2Vec 较差。

**最值得记住的一句话**：在生成式推荐的离散扩散训练中，给不同 masked token 赋予基于 item 协作结构的自适应 denoising weight，比 uniform noise schedule 更有效地学习协同过滤信号。
