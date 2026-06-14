---
title: Efficient and Robust Online Learning to Rank in Decentralized Systems
title_zh: 去中心化在线排序学习的鲁棒高效框架
authors:
- Marcel Gregoriadis
- Martijn de Vos
- Sayan Biswas
- Anne-Marie Kermarrec
- Johan Pouwelse
affiliations:
- TU Delft
- EPFL
arxiv_id: '2606.12246'
url: https://arxiv.org/abs/2606.12246
pdf_url: https://arxiv.org/pdf/2606.12246
published: '2026-06-10'
collected: '2026-06-14'
category: RecSys
direction: 去中心化在线排序学习 · 拜占庭鲁棒性
tags:
- Decentralized Learning
- Online Learning to Rank
- Byzantine Robustness
- Poisoning Attack
- Click Model
- Gossip Learning
one_liner: RankGuard 利用用户私有点击历史验证外来模型更新，有效抵御拜占庭攻击，并首次给出收敛证明
practical_value: '- **模型验证即防御**：在聚合其他节点的模型前，用本地私有交互数据（如用户点击序列）做似然检测，仅当外来模型对历史行为的解释优于本地模型时才接受。这可以低成本过滤恶意更新或噪声模型，适用于联邦推荐或分布式排序场景。

  - **位置偏置校正的无偏评估**：利用位置偏置点击模型（如 PBM）校准似然计算，确保评估的是真正的相关性提升而非位置引起的伪反馈。电商搜索排序中可借鉴此思想，用去偏后的点击信号做线上模型更新验证。

  - **轻量高效的安全聚合**：相比基于安全多方计算的聚合方法，RankGuard 只需简单的对数似然比较，计算开销极低（实验中达 62 倍加速）。在资源受限的边缘设备或需实时响应的推荐系统中，这种"先验后聚合"的策略有直接工程价值。

  - **理论保障下的去中心化实践**：首次为去中心化 OLTR 提供收敛性证明，表明即便在存在恶意节点的 Gossip 学习环境中仍可收敛到接近无攻击时的性能。这为电商去中心化推荐（如用户端训练个性化模型后共享）提供了可行性证据。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有在线排序学习依赖中心服务器收集用户交互，存在偏见和单点风险；去中心化学习让用户点对点交换模型，但易受拜占庭节点投毒攻击，现有防御算法计算量大且收敛性未知。

**方法**：提出 RankGuard，每个节点本地维护一个排序模型（广义线性模型）。收到邻居模型时，用自己私有点击历史（经位置偏置校正）计算新模型对历史点击的对数似然，只有当似然高于当前本地模型时，才通过指数滑动平均聚合该模型。聚合阈值天然阻止了恶意更新——攻击者只有提供真正提升用户点击似然的模型才能通过验证。论文给出了该算法在异步 Gossip 传播下的收敛上界，首次实现去中心化 OLTR 的理论收敛保证。

**结果**：在 MQ2007、MQ2008、MSLR-WEB10K、Istella-S 四个标准排序数据集，以及 perfect/informational/navigational 三种点击模型下，对抗随机噪声、梯度符号反转、自适应攻击等四种攻击。无攻击时 RankGuard 与普通去中心化 OLTR 性能持平；存在攻击时，RankGuard 在 11/12 种设定下排名质量（NDCG）显著优于七个基线（包括中心化 OLTR 的安全聚合、Krum、Multi-Krum 等），且计算效率最高提升 62 倍，仅需少量节点交换即可收敛。
