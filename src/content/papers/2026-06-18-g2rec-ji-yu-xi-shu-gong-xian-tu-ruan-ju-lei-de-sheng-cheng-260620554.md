---
title: Structuring and Tokenizing Distributed User Interest Context for Generative
  Recommendation
title_zh: G2Rec：基于稀疏共现图软聚类的生成式推荐结构化分词
authors:
- Ruizhong Qiu
- Yinglong Xia
- Dongqi Fu
- Hanqing Zeng
- Ren Chen
- Xiangjun Fan
- Hong Li
- Hong Yan
- Hanghang Tong
affiliations:
- University of Illinois Urbana-Champaign
- Meta MRS
arxiv_id: '2606.20554'
url: https://arxiv.org/abs/2606.20554
pdf_url: https://arxiv.org/pdf/2606.20554
published: '2026-06-18'
collected: '2026-06-19'
category: GenRec
direction: 生成式推荐 · 软聚类共现图 tokenization
tags:
- Generative Recommendation
- Graph Clustering
- Tokenization
- Co-engagement Graph
- Soft Modularity
- Scalable
one_liner: 通过稀疏共现图软聚类提取物品多兴趣原型并转化为连续 token，结合生成式推荐实现工业级全局行为建模
practical_value: '- **共现图稀疏化**：用 O(M log M) 采样子图替代全量共现图，借助图拉普拉斯近似理论保证结构信息，可直接迁移到电商/广告场景的用户行为图构建，减小工程开销。

  - **软聚类与多兴趣原型**：采用可微 soft modularity，在 GPU 上优化，得到每个物品的多兴趣分布，而非硬聚类；适合电商商品多用途属性（如一件商品同时属于“性价比”、“送礼”等）。

  - **交替 token 化序列**：将兴趣 profile 连续 token 与物品 token 交替输入生成式序列模型，并同时用交叉熵预测下一物品和兴趣软标签，可复现到推荐
  Agent 的上下文表示中。

  - **离线计算在线使用**：兴趣原型和物品兴趣 token 离线周期性更新，推理时仅需查表拼接，额外耗时可忽略，适合工业低延迟推荐服务。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有生成式推荐在融合用户行为图结构和物品语义 token 时面临两大难题：图方法（如序列化、GNN）不可扩展或仅利用局部信息；语义 tokenization 通常缺乏监督信号，易产生次优表示。为此，需要一种既能捕获全局共现模式，又能以可扩展语义 token 注入推荐模型的方法。

**方法关键点**：
- **稀疏共现图**：从全量用户行为构建物品-物品共现图，采样 O(M log M) 条边，理论上近似保留图拉普拉斯（Theorem 2），避免 O(M²) 复杂度。
- **可扩展软聚类**：设计可微的 soft modularity 目标（Closed form），在 GPU 上以 O(ρ M log M) 复杂度优化，得到每个物品的软成员分布（兴趣画像），形成多个兴趣原型（簇）。
- **兴趣 profile 分词**：由软分布计算兴趣原型嵌入和物品兴趣 token（加权均值），将原始交互序列重构为「〈BOS〉，物品向量，兴趣 token，…」的交替序列，同时用下一物品预测损失和兴趣分布交叉熵损失联合训练生成式模型。
- **无监督语义增强**：无需真实用户兴趣标签，利用图结构作为软监督信号，使模型学习兴趣转移模式。

**关键结果**：
- 公开数据集（Beauty、Sports、Toys、Yelp）上，G2Rec 在所有指标上均优于经典（POP/MF）、序列（GRU4Rec/SASRec/BERT4Rec/Caser/EAGER）和图方法（LightGCN/HeLLM），平均排名 1.04，Sports 上 NDCG@5 提升 14.9%。
- 在线 A/B 实验：在 Meta 产品表面，session 层面提升 >0.03%，总时长、点赞、分享等指标提升 0.06%-0.19%。
- 消融实验：软聚类 modularity 比 Leiden 硬聚类高 8%（Sports），兴趣 profile loss 有效提升 MRR；训练/推理额外耗时仅 0.043s/0.0027s 每批。
