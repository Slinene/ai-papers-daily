---
title: 'SAERec: Constructing Fine-grained Interpretable Intents Priors via Sparse
  Autoencoders for Recommendation'
title_zh: 'SAERec: 利用稀疏自编码器构建细粒度可解释意图先验的推荐'
authors:
- Jiangnan Xia
- Xuansheng Wu
- Yu Yang
- Xin Wang
- Ninghao Liu
affiliations:
- University of Georgia
- Shanghai AI Laboratory
- The Education University of Hong Kong
- Jilin University
- The Hong Kong Polytechnic University
arxiv_id: '2606.18897'
url: https://arxiv.org/abs/2606.18897
pdf_url: https://arxiv.org/pdf/2606.18897
published: '2026-06-17'
collected: '2026-06-18'
category: RecSys
direction: 意图感知推荐 · 稀疏自编码器解耦
tags:
- Sparse Autoencoder
- Intent-based Recommendation
- Interpretability
- Sequential Recommendation
- LLM
- Textual Data
one_liner: 利用稀疏自编码器从评论文本中解耦出可解释意图先验，并融合个性化与公共意图提升序列推荐
practical_value: '- **意图先验的自动构建**：利用稀疏自编码器（SAE）将LLM文本嵌入解耦为高维稀疏特征，通过关键词对齐和LLM过滤自动生成细粒度意图集，无需预设意图数量，适合电商场景中意图多样且快速变化的情况。意图构建离线完成，直接复用现有文本语料（评论/描述）。

  - **双级意图检索平衡个性化与泛化**：从意图集中为每个用户检索个人意图（与序列特征余弦相似度）和公共意图（EMA加权全局高频意图），简单有效，可嵌入到各种序列模型（如SASRec）中，增强冷启和噪声场景下的稳定性。

  - **多分支注意力与自适应融合**：独立建模个人意图、公共意图和时序依赖，再通过自适应权重融合，为意图注入提供通用范式，可直接迁移至电商推荐的精排或召回模块。

  - **工程可实现性**：SAE训练仅需少量GPU（<3GB），意图集一次构建可复用；检索和注意力计算轻量，训练时间随数据量线性增长，适合大规模落地。意图操纵可导向推荐分布，便于业务干预。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有意图推荐方法依赖交互序列聚类或固定数量的原型学习，意图数量难确定且缺乏语义可解释性，稀疏行为下不可靠。评论文本富含意图信号，但LLM嵌入高度纠缠，难以直接抽取细粒度意图。本文希望从文本语料中自动构建全面、可解释的意图先验，并有效注入序列推荐。

**方法**  
- **意图构建**：用推荐微调的P5编码评论，训练Top-K稀疏自编码器（SAE）将稠密嵌入解耦为高维稀疏特征，每个特征方向对应一个潜在语义。通过互信息为每个方向选取最具代表性的10个词，再让LLM（Mistral-7B）总结语义并判定是否为推荐相关意图，过滤后形成固定意图集。该过程无监督且无需预设意图数。
- **双级意图检索**：对每个用户，基于序列编码与意图向量的余弦相似度取Top-S作为个人意图；同时用EMA累积所有用户意图激活频率，取全局Top-S作为公共意图，兼顾个性化和泛化。
- **意图注入序列建模**：设计三支注意力（个人意图-序列、公共意图-序列、序列自注意力），得到三种序列表示后，通过自适应融合层加权求和，输出最终用户表示用于下一个物品预测。

**关键结果**  
在Amazon Beauty、Toys、Sports和Yelp四个数据集上，SAERec在所有指标一致最优。以Beauty为例，HR@10提升10.70%，NDCG@10提升11.63%；在Sports上HR@20提升7.80%。消融实验证实意图过滤、双级检索、自适应融合均带来显著增益。相比聚类式意图构建，SAE方式在Beauty HR@20 0.1427 vs. 0.1349。模型对评论缺失鲁棒（30%缺失性能几乎无下降），训练时间随数据量线性增长，SAE训练峰值显存低于3GB。所学意图语义清晰、可解释，且通过权重干预能定向改变推荐分布（如增强护肤类意图后护肤品推荐量上升）。

**核心认知**：将LLM文本空间的隐语义通过稀疏解耦转化为可检索、可解释的意图先验，再以多分支注意力注入序列模型，是平衡可解释性、个性化与泛化的一条高效路径。
