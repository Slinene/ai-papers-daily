---
title: 'BrowseFlow: Sparse Event Flow Matching for Generative User Simulation'
title_zh: BrowseFlow：用于生成式用户模拟的稀疏事件流匹配
authors:
- Yitian Pang
- Jiayi Zhang
- Zhenjia Ma
- Xiaowei Yue
- Dagui Chen
- Jian Xu
affiliations:
- Tsinghua University
- Taobao & Tmall Group of Alibaba
arxiv_id: '2610.41374'
url: https://arxiv.org/abs/2610.41374
pdf_url: https://arxiv.org/pdf/2610.41374
published: '2026-10-30'
collected: '2026-11-02'
category: RecSys
direction: 生成式用户模拟 · 离散 Flow Matching
tags:
- User Simulation
- Discrete Flow Matching
- Sparse Events
- Distributional Evaluation
- Recommender Systems
- TaobaoBrowse
one_liner: 用离散 Flow Matching 对稀疏关键事件和浏览深度建模，生成随机用户浏览轨迹，在三个数据集上取得最优分布拟合
practical_value: '- 拆解用户浏览轨迹为“浏览深度/进度 + 稀疏关键事件序列”的稀疏表示，避免逐 action 预测滚动等高频进度动作；直接生成点击/转化/收藏的计数、深度和目标，适合电商推荐模拟和
  offline RL 环境中的用户行为生成。

  - 采用离散 Flow Matching 的插入式 CTMC 生成可变长关键事件序列，天然处理事件计数和位置，不需要单独 count 预测头；训练用随机事件保留构造部分序列
  + 条件速率匹配（hazard 1/(1-s)），实现简单，可迁移到点击/加购等稀疏正反馈序列建模。

  - 评估随机用户模拟时不要只看命中或似然：用 energy score 同时度量样本对观察的保真度和样本间多样性，再加关键事件计数分布 Wasserstein
  距离，能更真实反映条件响应分布拟合；线上模拟器/A/B 评测可引入类似分布指标。

  - 对长会话，分离 browsing extent 能明显改善深浏览位置的恢复；在广告/信息流中若关心首点击深度或长浏览用户，可显式建模浏览深度分布而不是依赖逐步终止。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
用户模拟需要复现同一用户在同一推荐 feed 下可能产生的多样化浏览响应，但日志只记录其中一条轨迹；现有参考匹配评估无法判断其他合理响应是否被赋予足够概率。同时，浏览行为中点击、喜欢等关键事件稀疏（三个数据集仅 1.52%–5.96% 曝光产生正反馈），而滚动等进度动作占据绝大多数；逐步模拟器在密集动作序列中预测这些事件，导致关键事件监督不足，错误进度决策还会影响后续曝光和终止。

**方法关键点**
- 稀疏响应表示：每条浏览响应压缩为最终浏览深度 D 和有序关键事件序列 E=(d_k,μ_k)，其中 d_k 是事件深度，μ_k 是目标 mark；滚动等进度动作由 D 和事件深度决定，生成时直接聚焦稀疏事件。
- 概率化浏览深度：用 session Transformer + history Transformer 编码用户、历史和完整推荐 feed，输出到每个可达深度的 categorical 分布 π_η(D|X)，建模浏览终止的随机性。
- 条件离散 Flow Matching：给定采样深度 D，在曝光约束下用插入式 CTMC 从空序列生成关键事件序列。每个插入操作分解为 gap、depth、mark 三个归一化分布，速率 r_θ=λ_θ·π_θ；曝光约束保证事件有序且目标在深度内可见、不重复。
- 训练：条件速率匹配。随机按概率 s 保留目标事件形成部分序列，缺失事件插入 hazard 为 1/(1-s)；损失由强度项 (1-s)λ - R log λ 和插入分类项 -Σ log π_θ 组成，结合深度负对数似然。无需单独预测事件数量，事件计数由插入过程自然决定。
- 评估：采用 energy score 评估条件响应分布保真度与多样性，Count W1 评估事件计数分布；并构建 TaobaoBrowse，包含真实曝光推进轨迹、点击目标和用户/物品上下文。

**关键结果**
在 TaobaoBrowse、KuaiRand-Like、AdSERP 三个数据集上，BrowseFlow 的 Energy Score 和 Count W1 均最优。TaobaoBrowse 上 ES 0.07264、Count W1 0.0697、PPL 2.0906、SeqHit@1 0.0544，均优于基线；但 AUC 低于局部点击预测器，说明分布建模与局部判别不同。消融显示稀疏表示 + Flow Matching + 插入式生成带来最大增益，稀疏表示和插入机制对 Count W1 尤其关键；密集空间下插入反而恶化。行为分析表明首点击深度和长会话浏览深度恢复更准确。

**最值得记住的一句话**
忠实用户模拟的关键不是逐 action 复现轨迹，而是显式建模稀疏关键事件和浏览深度，捕捉同一上下文下用户可能“如何浏览”的分布。
