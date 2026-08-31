---
title: Information-Guided Selective Modality-Interest Alignment for Multimodal Recommendation
title_zh: 信息引导的选择性模态-兴趣对齐多模态推荐框架
authors:
- Wenze Ma
- Chenyu Sun
- Yanmin Zhu
- Qiwen Gu
- Xuhao Zhao
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2608.27950'
url: https://arxiv.org/abs/2608.27950
pdf_url: https://arxiv.org/pdf/2608.27950
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 多模态推荐 · 兴趣对齐与去噪
tags:
- Multimodal Recommendation
- Modality-Interest Alignment
- Information Theory
- Graph Refinement
- User Interest Modeling
one_liner: 提出信息论引导的 AMUR 框架，选择性对齐与用户兴趣相关的多模态语义并抑制噪声模态
practical_value: '- 多模态推荐里不要默认全量融合所有模态：业务上可以先利用用户行为信号筛选与兴趣更相关的模态子集，降低视觉/文本噪声对点击率、转化率建模的干扰。

  - 借鉴信息论显式约束：用互信息或熵正则替代隐式 attention 加权，让模态-兴趣对齐有明确优化目标；在电商多模态商品塔中可加入兴趣相关性损失，提升冷启动和长尾商品表征。

  - 图结构先 refinement 再融合：先用用户行为调整物品多模态图，剪掉弱相关边，再跨模态对齐；对应到商品关系图，能减少无关商品连接带来的 embedding
  噪声。

  - 保留模态特定互补信息：对齐共享语义时不要完全抹掉模态独有信号，电商场景中文本标题、主图、视频信息有互补性，可设计共享/私有特征分离结构。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：多模态推荐中直接注入全部模态信息未必提升偏好建模，因为用户兴趣通常只与部分模态信号相关，其他信号可能弱对齐甚至引入噪声。现有方法通过不变学习、注意力、图精化或对比学习改善模态利用，但对齐过程多为隐式或启发式，缺乏选择与用户兴趣匹配模态的明确目标。

方法关键点：提出 AMUR，一个信息引导的选择性模态-兴趣对齐框架。从信息论视角出发，AMUR 增强与用户兴趣更相关的模态信息，同时降低弱对齐信号影响。具体包括两步：先基于用户行为精化模态图结构，使图邻接关系更贴近用户偏好；再选择性对齐跨模态中与兴趣相关的共享语义，同时保留有用的模态特定互补信息。

关键结果：在三个真实世界数据集上的大量实验表明，AMUR 相对多个竞争基线取得更优推荐效果，代码已公开。
