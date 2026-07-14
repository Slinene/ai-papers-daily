---
title: Diversified Multinomial Logit Contextual Bandits
title_zh: 多样化多项Logit上下文Bandit算法
authors:
- Heesang Ann
- Taehyun Hwang
- Min-hwan Oh
affiliations:
- Seoul National University
arxiv_id: '2607.11684'
url: https://arxiv.org/abs/2607.11684
pdf_url: https://arxiv.org/pdf/2607.11684
published: '2026-07-13'
collected: '2026-07-14'
category: RecSys
direction: 推荐多样性 · 上下文Bandit
tags:
- Contextual Bandits
- Assortment Optimization
- Diversity
- Submodularity
- MNL
- Regret Bound
one_liner: 将多样性作为子模函数直接嵌入MNL选择概率，利用无黑箱oracle的UCB算法实现近似最优的集合推荐
practical_value: '- **多样性直接参数化选择模型**：不同于事后加权或规则注入，把多样性作为影响用户点击/购买概率的隐性参数，可借鉴到电商商品集合推荐、搜索结果的多样性建模中，用可学习的
  `λ` 自动平衡相关性与多样性，避免人工调权。

  - **项目式贪婪构造近似最优集合**：用逐项边际增益最大化方式构造推荐集合（复杂度 O(NK)），并提供理论近似比 (1 − 1/(e+1))，可替代全枚举或黑箱优化，大幅降低在线推理计算开销。

  - **在无项目级反馈下学习多样性**：模型仅收到集合整体反馈（如点击或购买），无须每个位置或项目的边际奖励信号，这与推荐列表的线上观测场景一致，可利用 UCB
  联合估计相关性和多样性参数，实现子线性后悔。

  - **子模多样性函数的选用与 strict submodularity 条件**：工程实现时可采用满足 strict submodularity 的多样性度量（如基于类目覆盖的指数衰减函数），以保证乐观奖励函数保持子模性，从而保证贪婪构造的逼近效果。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：传统的上下文 MNL Bandit 模型只基于项目相关性进行集合推荐，忽略了集合内的多样性效应。已有的子模 Bandit 虽能建模多样性，但缺少结构化的选择概率反馈机制，且常依赖黑箱优化 oracle。该工作将多样性直接嵌入 MNL 选择概率，打造一个统一模型来刻画推荐集合中“相关性-多样性”的折中，并设计高效的白色箱算法来应对优化与学习挑战。

**方法关键点**
- **DMNL 模型**：在标准 MNL 选择概率分母中引入 `exp(-λ g(S))`，其中 `g(S)` 为非负单调子模函数，量化集合多样性；选择概率随多样性升高而降低外部选项的吸引力，从而增加每个项目的选中概率。
- **参数估计**：通过定义多样性增强特征 `z_ti(S)=[x_ti, g(S)]`，将 `(θ, λ)` 联合估计转化为单一向量 `w` 的在线镜像下降，沿用 Lee & Oh (2024) 的高效近似 MLE 更新和置信域构造。
- **算法 OFU-DMNL**：基于 UCB 的乐观奖励 `eR_t(S)`，使用逐项贪婪构造（每次添加具备最大边际乐观收益的项目），避免枚举所有 K 元子集，每轮复杂度 O(NK)，且无需黑箱 oracle。
- **关键技术保证**：利用 MNL 奖励函数的特殊凹复合结构，证明贪婪能获得至少 `(1 − 1/(e+1))` 的近似比，超越一般子模函数的 `(1 − 1/e)`。在 strict submodularity 条件下，即使没有项目级反馈，乐观奖励仍保持子模性，保障贪婪的近似质量。

**关键实验结果**
- 在合成数据集（物品特征 Gaussian 分布 + 类目多样性函数）上，与 UCB-MNL、TS-MNL、OFU-MNL+ 以及部分引入多样性的 OFU-MNL-DR 对比，OFU-DMNL 在累计后悔上显著优于传统 MNL Bandit，接近基于全枚举的 OFU-DMNL-FULL，但运行时间缩减极大。
- 当 N=100, K=10 时（图 3），OFU-DMNL 凭借 O(NK) 构造比枚举快数个数量级，同时后悔保持在 OFU-DMNL-FULL 的 1.2 倍以内，展现计算与统计效率的平衡。
- 不同多样性强度 `λ*` 下（附录图 F.3），方法自动适应相关性与多样性的折中，无需手工设置权重。
