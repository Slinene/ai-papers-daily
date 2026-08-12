---
title: Multi Interests for Joint Search-Recommendation Modeling
title_zh: 从结构和语义解耦混合序列的多兴趣搜索-推荐联合建模
authors:
- Xiangchen Pan
- Wei Wei
- Huakang Niu
- Zhicong Cheng
affiliations:
- 华中科技大学
arxiv_id: '2608.10535'
url: https://arxiv.org/abs/2608.10535
pdf_url: https://arxiv.org/pdf/2608.10535
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 联合搜索-推荐 · 多兴趣建模
tags:
- Multi-Interest
- Joint Search-Recommendation
- Query Semantics
- Contrastive Learning
- Multi-Task Learning
- PLE
one_liner: 提出从行为类型和查询语义两个视角提取多兴趣，解决搜索推荐混合序列中的兴趣耦合问题
practical_value: '- **结构化兴趣分解可作为电商混合行为建模的通用插件**：将用户行为按搜索、推荐及跨域转换拆分，分别用独立 self-attention
  + target attention 建模，再与候选商品交互，可解耦短期意图与长期偏好。实际落地时，搜索行为用 query+点击 item 均值，推荐行为用 item
  embedding，通过掩码注意力捕获跨域转换，成本可控。

  - **查询语义聚类实现低成本语义多兴趣分割**：对全量 query 做 K-Means，将混合序列按最大相似度分配到语义簇，再在每个簇内用 target attention
  聚合。电商场景中 query 文本易得，该方法无需额外标签，且正交损失使簇更分散，可直接迁移至搜索/推荐双渠道行为序列的粗粒度兴趣划分。

  - **对比学习对齐 query 与 item 表示可提升行为融合质量**：以点击 item 为正例，采样负例做 InfoNCE 损失，让搜推两种行为的表示空间一致。在商品搜索推荐联合模型中，此对齐步骤十分关键，尤其对描述文本稀疏或
  ID 语义弱的场景，可用类似 span 的方式减少模态鸿沟。

  - **PLE 多任务架构对搜推联合预测的平衡有效**：引入共享专家与任务专属专家，通过门控网络加权，可缓解搜推任务间的负迁移。在电商多目标优化中，如果搜索和推荐共享底层用户表示，PLE
  结构可直接替换 MLP 预测头，提升整体指标。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：当前联合搜索与推荐建模通常将用户主动搜索和被动推荐行为按时间混合成统一序列，但忽视混合序列中不同场景下的多兴趣表达，导致短期意图被长期偏好淹没。此外，现有方法对搜索查询的利用仅限于词均值池化，没有充分利用查询的语义信息来划分兴趣边界。为解决兴趣耦合问题并更细粒度地刻画用户偏好，本文提出从**行为结构**和**查询语义**两个视角进行多兴趣挖掘，并自适应融合用于多任务预测。

**方法关键点**：
- **跨域行为融合**：搜索行为表示为查询embedding加点击item均值池化，推荐行为用item embedding。通过query与点击item的对比学习（InfoNCE损失）对齐两者分布，统一表示空间。
- **结构化多兴趣**：按行为类型拆分为搜索子序列和推荐子序列，分别用self-attention + target attention提取搜索兴趣和推荐兴趣；对混合序列施加类型掩码（仅跨域 attention），提取搜索与推荐的交叉兴趣。
- **语义多兴趣**：对所有query做K-Means聚类，通过序列级对比学习训练一个投影网络，将item特征映射到query语义空间；再将混合序列按聚类中心分配语义标签，划分成语义子序列，每个子序列内用target attention得到语义兴趣，最后加权融合。引入正交损失使语义簇更独立。
- **多任务预测**：自适应融合四种兴趣（搜索、推荐、交叉、语义），拼接用户/物品特征和序列表示，输入PLE网络（含搜索专家、推荐专家、共享专家）分别预测搜索和推荐点击分。

**实验**：在KuaiSAR（真实视频平台）和Amazon Kindle（半合成）两个公开数据集上，与15个基线对比，包括序列推荐（DIN/SASRec等）、个性化搜索（HEM/TEM等）和联合建模（USER/UniSAR等）。结果：搜索任务上，KuaiSAR的HR@5达78.11%（较UniSAR提升4.48%），NDCG@5提升3.40%；推荐任务上，Amazon的NDCG@5提升4.85%。消融表明去掉任一多兴趣组件或PLE均导致性能下降。最优语义簇数𝑘=10，对比损失权重1e-3，正交损失权重1e-4，搜索任务权重0.5时综合最佳。

**核心一句话**：“从结构（搜索、推荐、交叉）和语义（查询聚类）两个角度解耦混合序列的多兴趣，能同时提升搜索和推荐精度，且各组件对真实场景行为建模均有显式增益。”
