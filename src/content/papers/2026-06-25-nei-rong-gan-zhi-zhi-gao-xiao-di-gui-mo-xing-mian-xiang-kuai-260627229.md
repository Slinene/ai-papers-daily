---
title: 'CARVE: Content-Aware Recurrent with Value Efficiency for Chunk-Parallel Linear
  Attention'
title_zh: 内容感知值高效递归模型：面向块并行线性注意力
authors:
- Sayak Dutta
arxiv_id: '2606.27229'
url: https://arxiv.org/abs/2606.27229
pdf_url: https://arxiv.org/pdf/2606.27229
published: '2026-06-25'
collected: '2026-06-26'
category: Training
direction: 高效递归架构 · 线性注意力
tags:
- linear-attention
- delta-rule
- content-aware-gating
- WY-form
- chunk-parallel
- memory-blind
one_liner: 通过key轴门控、输出重用与标量值门，一次性消除GDN-2内存盲、参数浪费与块并行不兼容三大缺陷。
practical_value: '- 在用户行为序列建模中，可借鉴key轴门控设计，避免值轴参数膨胀和内存盲，提升长序列训练吞吐。

  - 利用已计算的输出张量作为内容信号（输出重用），无需额外读取状态矩阵，降低显存带宽压力，适合大规模序列模型。

  - 标量值写门将每头写门投影压缩为单个标量，显著减少参数量（19%），可迁移至推荐模型的序列编码器以提升参数效率。

  - WY-form块并行求解器的恢复使递归模型训练效率可比拟Transformer，可尝试引入在线/离线排序模型的序列特征提取中，加速训练。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有delta-rule架构（GDN-2）存在三个关联缺陷：遗忘门仅基于当前token（memory-blind），无法观察已存储内容；值轴门控浪费参数且数学上破坏WY-form三角块求解器，导致递归训练无法利用块并行，吞吐量退化至串行水平。

**方法关键点**：CARVE将所有门控限制在key轴，使intra-chunk耦合矩阵与值轴解耦，恢复高效WY-form求解。在此约束下引入两项创新：1）内容感知遗忘门：复用已写入GPU内存的递归输出张量，计算chunk均值作为内容信号，通过零初始化低秩投影生成遗忘门，初始化时与GDN-2恒等，训练中激活记忆条件选择性；2）标量值写门：将每头写门投影从dv维压缩为单个标量，大幅减少参数。

**关键结果**：1.3B参数100B tokens训练，WikiText困惑度15.72（比GDN-2低0.18，4.5σ显著性）；9项常识推理基准全面领先所有递归基线；RULER检索探针全部SOTA；吞吐开销仅0.4%，峰值显存降低13%，参数减少19%。
