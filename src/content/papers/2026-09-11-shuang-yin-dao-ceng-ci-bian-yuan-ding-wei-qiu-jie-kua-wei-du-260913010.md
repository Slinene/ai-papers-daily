---
title: Dual-guided Hierarchical Edge Localization for Large-scale Optimal Transport
  Across Dimensions
title_zh: 双引导层次边缘定位求解跨维度大规模最优传输
authors:
- Wenzhou Xia
- Qiaoqiao Ding
- Jingwei Liang
- Xiaoqun Zhang
arxiv_id: '2609.13010'
url: https://arxiv.org/abs/2609.13010
pdf_url: https://arxiv.org/pdf/2609.13010
published: '2026-09-11'
collected: '2026-09-14'
category: Other
direction: 大规模最优传输优化算法
tags:
- Optimal Transport
- Hierarchical Solver
- GPU Acceleration
- Large-scale Optimization
- KKT
- Edge Localization
one_liner: 提出 HELLO 层次求解器，以对偶势引导边缘定位，实现大规模离散 OT 的线性内存和数量级加速，并证明有限终止到全局最优。
practical_value: '- 在电商/推荐中，跨域用户/物品 embedding 对齐、域适应、分布校准等常需大规模 OT，HELLO 提供可扩展到百万样本、高维特征的求解器，可直接替换
  Sinkhorn 等正则化方法，获得更精确的非正则 OT 解，适合对精度要求高的场景。

  - 层次粗到细 + 对偶引导边定位的思想可迁移到大规模稀疏匹配问题（如用户-商品候选匹配、跨平台实体对齐），不必显式计算全对全代价矩阵，仅维护候选边集合，从而把内存降到线性，适合在线或近线系统。

  - 细化阶段按行/列插入最大对偶违反者、用 KKT 残差作为停止准则和 budgeted pruning，为工程实现提供可控精度与内存的模板，可用于对偶上升、列生成等算法的优化。

  - 作为 balanced-OT oracle，可直接支持 Flow Matching 生成模型（如电商素材生成、用户序列生成）和 Gromov-Wasserstein
  对齐，降低底层 OT 瓶颈；业务中若已有 OT 组件，可考虑集成 HELLO 提升规模。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：无正则离散 OT 需要求解线性规划，变量数为 m*n，在百万样本和高维特征下计算和内存均不可行，现有正则化近似（如 Sinkhorn）引入熵偏置，求解精度受限。
方法：HELLO 把离散 OT 重新表述为边缘定位问题，利用对偶势引导两个层次：初始化阶段在递归子采样层次间传播粗粒度对偶势以分配候选边；细化阶段在每行/列插入最大的对偶违反者，直到相对 KKT 残差满足预设容差，同时采用预算修剪实现线性内存。精确算术下，符号字典序规则保证有限步终止于全局最优。
结果：在百万点规模上，HELLO 相比强基线获得更低的传输目标，运行时间有数量级改进；在单张 H100 上可处理每个边际 128 万样本、8192 维问题，峰值 GPU 内存 41.6 GiB，且满足相对 KKT 残差低于 1e-6。框架支持一般 pairwise cost，并可作为 balanced-OT oracle 扩展到半离散 OT、Gromov-Wasserstein、非平衡 OT 和基于 OT 的 Flow Matching。
