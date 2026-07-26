---
title: Expanding Flow Maps
title_zh: 扩展流映射：支持可变维度与变长序列的生成模型
authors:
- Sophia Tang
- Pranam Chatterjee
affiliations:
- University of Pennsylvania
arxiv_id: '2607.21585'
url: https://arxiv.org/abs/2607.21585
pdf_url: https://arxiv.org/pdf/2607.21585
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 生成式流模型 · 可变维度生成
tags:
- flow models
- variable-length generation
- generative models
- discrete flows
- sequence generation
- few-step generation
one_liner: 提出扩展流映射(EFM)，将生成模型从固定维度/长度解放，支持可变大小图和序列的少步生成
practical_value: '- 电商推荐中常需生成可变长度的商品序列（如个性化feed流长度不固定），EFM的expand operator可直接建模输出长度本身，将序列长度作为可控自由度，避免预设最大长度带来的浪费或截断。

  - 广告创意生成或搜索query推荐中，需要生成可变长度的文本，EFM在离散simplex上的扩展支持变长token序列生成，可端到端学习生成过程的长度分布，替代现有固定长度或启发式终止的方案。

  - 通过蒸馏为少步生成，EFM可在在线推理中实现低延迟；对于推荐系统的实时生成场景，可将训练好的变长生成流蒸馏为仅需几层计算的网络，兼顾效果与效率。

  - 图生成在推荐中可用于建模物品关系图或用户行为图，EFM的可变大小图生成能力可用来直接生成适应不同规模的结构化数据，省去预先定义图尺寸的麻烦。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：现有基于流的生成模型（flow-based）受限于固定的状态维度或序列长度，无法处理输出大小本身为自由度的任务，如图生成、变长序列生成等。

方法：首先定义**扩展生成流（EFlow）**，设计一种扩展插值路径，通过向当前状态添加条件噪声的方式逐步增加维度。基于此提出**扩展流映射（EFM）**，将任意两个时刻间的映射分解为两个可学习算子：
1. **扩展算子**：根据当前状态生成新的坐标或token，扩充状态空间；
2. **传输映射**：将扩展后的状态沿插值路径推进。
两个算子复合即实现联合扩展与去噪，一步完成可变维度的生成。现有固定画布的流与流映射是该框架在扩展算子为恒等映射时的特例。进一步将框架扩展到离散单形体，直接建模类别分布，实现可变大小图与变长序列生成。

结果：在连续与离散模态上验证，EFlow与EFM展示了统一的变长生成框架，输出尺寸可作为可控自由度学习。EFM可通过蒸馏获得高效的少步生成模型，保证了推理速度。
