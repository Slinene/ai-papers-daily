---
title: The Lattice of Transition Laws
title_zh: 转移法则格：扩散与自回归解码调度的统一框架
authors:
- T. Y. Tsui
- Jiatao Gu
- Lingjie Liu
affiliations:
- University of Pennsylvania
arxiv_id: '2610.11216'
url: https://arxiv.org/abs/2610.11216
pdf_url: https://arxiv.org/pdf/2610.11216
published: '2026-10-07'
collected: '2026-10-10'
category: Other
direction: 生成模型统一解码调度与成本预测
tags:
- diffusion
- autoregression
- decoding schedule
- treedepth
- corruption lattice
- generative models
one_liner: 将扩散、自回归及混合模型统一为 corruption lattice 上的路径，用依赖成本预测不同解码调度性能
practical_value: '- 在生成式推荐或文本生成中，不必固定 AR 顺序或全并行扩散，可根据数据依赖图/树深设计中间解码调度，平衡推理延迟与生成质量。

  - 利用预训练模型权重估计成对依赖成本，可低成本预测不同解码策略的排序，用于离线筛选最优推理策略，减少在线实验成本。

  - 对于商品序列或图结构数据（如购物车序列、类目树），treedepth 给出最少零成本并行步数，可用于并行生成商品描述、推荐理由等任务时估计加速上限。

  - 在支持混合解码的推理框架中，可先用依赖成本排序候选 schedule，再小规模验证，替代全量解码调参，提升工程效率。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：扩散与自回归长期被视为两类生成模型，分别擅长连续场和离散 token，近期混合模型往往固定解码调度，缺少统一理论来预测不同调度的性能。

方法关键点：将 diffusion、AR 及中间模型描述为 corruption lattice 上的路径；定义调度的 cost 为其并行步骤丢弃的依赖。分析表明，零成本调度的最少步数由数据几何决定，且对 token 与连续场一致：若数据在图上满足马尔可夫性且沿路径依赖，则最少步数等于图的 treedepth。序列的 treedepth 关于长度呈对数增长，网格关于边长呈线性增长。当步数少于 treedepth 时，每种调度都产生正 cost，其排序可用从预训练权重估计的成对依赖核预测，无需实际解码。

关键结果：在文本生成、图像生成和视频生成任务上，验证了不同调度在不同指标与基准下的排名预测，大部分预测成立。该工作为未来 AR、扩散及混合模型的解码提供了通用设计原则。
