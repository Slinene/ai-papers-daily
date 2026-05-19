---
title: 'Echoes in Filter Bubble: Diagnosing and Curing Popularity Bias in Generative
  Recommenders'
title_zh: 滤泡回声：生成式推荐流行度偏差的诊断与治愈
authors:
- Jun Yin
- Bangguo Zhu
- Peng Huo
- Ruochen Liu
- Hao Chen
- Senzhang Wang
- Shirui Pan
- Chengqi Zhang
affiliations:
- Hong Kong Polytechnic University
- Central South University
- National Super Computing Center Tianjin
- City University of Macau
- Griffith University
arxiv_id: '2605.16825'
url: https://arxiv.org/abs/2605.16825
pdf_url: https://arxiv.org/pdf/2605.16825
published: '2026-05-16'
collected: '2026-05-19'
category: GenRec
direction: 生成式推荐·流行度偏差诊断与纠偏
tags:
- Generative Recommender
- Popularity Bias
- Semantic ID
- Gradient Starvation
- Skeleton-Founded Tokenization
- Asymmetric Unlikelihood Optimization
one_liner: 诊断出梯度饥饿与无差别令牌化导致生成式推荐严重流行偏差，并通过骨架令牌化和非对称不似然优化进行纠偏。
practical_value: '- 生成式推荐长尾物品曝光优化：借鉴 SKT，为尾部物品分配额外专用 SID 令牌，继承头部物品前缀但增加区分性，可抑制头部令牌在生成过程中的几何级压制，提升长尾覆盖率。

  - 训练技巧迁移：引入 AUO 构建“不期望集合”——基于文本语义相似但 SID 前缀差异大的头部物品，并对生成这些令牌的概率进行额外惩罚，可校正尾部令牌的梯度饥饿，无需重新采样数据。

  - 快速诊断方法：通过分析梯度更新符号和 SID 分支点数量，可以快速定位生成式推荐中哪些物品令牌遭遇梯度饥饿，辅助业务系统发现偏差根源。

  - 公平性与整体性能的帕累托平衡：在 AUO 权重 α 和不期望集合大小上做精细调参，可在不显著损害整体指标（如 HR 仅降 ~7%）的前提下，大幅提升尾部性能与公平性，这为电商平台实现多目标优化提供了可落地的调节手段。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
当前最先进的生成式推荐（GRs）虽端到端生成语义 ID，却严重偏向流行物品，形成过滤气泡：头部物品垄断推荐列表（占 97% 以上），尾部物品推荐准确率与头部相差数十倍。现有去偏方法效果有限，且未触及 GRs 内在机制。本文从 GRs 两个核心特性——MLE 优化与语义 ID 令牌化——深入诊断，揭示流行偏差的根本原因。  

**方法关键点**  
- 诊断发现：MLE 目标下尾部令牌因训练分布长尾而持续接收负梯度，陷入“梯度饥饿”，其嵌入被推离用户偏好；无差别的令牌化引入不可预测的分支点，使尾部物品在生成过程中每一步都面临头部令牌的优势竞争，偏差呈几何级放大。  
- 骨架驱动令牌化（SKT）：先为头部物品分配 SID 作为骨架，尾部物品根据语义相似度继承前缀，再附加专有令牌，将分支点统一至一个固定位置，阻断偏差放大链。  
- 非对称不似然优化（AUO）：对每个尾部物品，检索语义最相似但 SID 差异大的头部物品组成“不期望集合”，训练时主动惩罚这些令牌的生成概率，为尾部令牌提供正向救援梯度。  
- 整体目标：L_All = L_NLL + α * L_AUO，仅对尾部物品应用 AUO，实现不对称优化。  

**关键实验结果**  
在三个 Amazon 数据集（Musical Instruments、Arts、Video Games）上对比 LETTER、LC-Rec、ED2 及去偏基线 IFairLRS。Ghost 使尾部 HR@10 和 NDCG@10 平均提升 63.91% 和 70.66%，MGU 平均降低 55.76%，整体 HR 仅微降（~7.46%）。在 0.6B 至 8B 不同骨干上一致有效，CNS 综合得分提升最高 22.06%。消融证实 SKT 与 AUO 缺一不可。  

**核心洞察**  
生成式推荐的流行偏差根植于令牌级梯度饥饿与无差别分支点竞争，通过骨架化前缀继承和针对性不似然惩罚即可低成本地逼近帕累托最优。
