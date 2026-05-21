---
title: Spectral bandits for smooth graph functions with applications in recommender
  systems
title_zh: 基于图光滑函数的谱Bandit算法及其在推荐系统中的应用
authors:
- Tomáš Kocák
- Michal Valko
- Rémi Munos
- Branislav Kveton
- Shipra Agrawal
affiliations:
- Inria Lille
- Microsoft Research
- Technicolor Research Center
arxiv_id: '2605.20552'
url: https://arxiv.org/abs/2605.20552
pdf_url: https://arxiv.org/pdf/2605.20552
published: '2026-05-19'
collected: '2026-05-21'
category: RecSys
direction: 图光滑Bandit · 有效维度 · 推荐冷启动
tags:
- spectral bandits
- graph smoothness
- effective dimension
- Thompson sampling
- UCB
- recommender systems
one_liner: 将图光滑性引入Bandit学习，通过有效维度使regret与节点数解耦，适用于探索阶段（T<N）的推荐场景
practical_value: '- **物品冷启动探索**：利用物品相似图（如内容/协同过滤构建的k-NN图）的拉普拉斯谱基，在用户反馈稀少时（T≪N），可以用少量试探发现高偏好物品，Regret远低于标准线性bandit。

  - **有效维度作为复杂度指示**：真实推荐场景中，物品图的有效维度d通常远小于总数N，可提前估算d来决定是否值得使用谱Bandit，若d接近T则普通LinUCB足够。

  - **SpectralTS实现高效探索**：Thompson采样版本无需对每个物品计算置信区间，每次更新仅需O(N²)（V秩一更新+采样），比SpectralUCB的O(N³)更易于部署在大图上；适合需要毫秒级决策的在线推荐系统。

  - **图光滑先验的注入方式**：将图拉普拉斯作为正则项（谱惩罚）等价于假设物品奖励函数光滑，可复用到其他线性bandit或贝叶斯模型（如LinUCB/LinearTS）中，只需在协方差矩阵初始化时加入Λ=Λ_L+λI即可。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
在线推荐中物品数量N巨大，用户历史反馈有限（T<N），传统线性bandit的regret随N增长，无法高效探索。现实中物品相似性构成图，用户对相邻物品评分相近（图光滑性），可利用该先验将推荐问题转化为在图上学习光滑函数的Bandit问题。

**方法关键点**  
- 将奖励函数表示为图拉普拉斯特征向量的线性组合：\(f_\alpha(v) = \langle x_v, \alpha \rangle\)，其中\(x_v\)是节点v对应的特征基坐标。
- 引入**有效维度d**：基于特征值衰减速率自适应确定，当特征值快速增长时d≪N，regret界与N解耦。
- 提出**SpectralUCB**：在LinUCB中利用谱惩罚（协方差初始化为Λ=Λ_L+λI），置信宽度基于d计算，regret为\(O(d\sqrt{T\log T})\)。
- 提出**SpectralTS**：Thompson采样版本，采样分布协方差为\(v^2 V_t^{-1}\)，同样初始化为Λ，regret为\(O(d\sqrt{T\log N})\)，且无需逐臂计算置信区间，计算更高效。

**关键实验**  
- 合成数据：Barabási-Albert随机图，N=250，T<200，basis size=3，d=1；与LinUCB、LinearTS对比，SpectralTS和SpectralUCB累积regret降低约50%。
- 真实数据：MovieLens 1M，构建10-NN相似图，N=2019，T=200，d≈5；两种谱算法regret显著低于线性对照，且SpectralTS单步耗时远小于SpectralUCB（约1/10）。

**核心洞察**  
通过图光滑先验，将bandit探索的复杂度从物品总数N转移到有效维度d，实现在T≪N时的低regret推荐，为冷启动和稀疏反馈场景提供了一种理论优雅、工程可复用的方案。
