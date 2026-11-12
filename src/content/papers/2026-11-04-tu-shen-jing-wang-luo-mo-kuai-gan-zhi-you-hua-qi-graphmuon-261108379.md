---
title: Module-Aware Optimization for Graph Neural Networks
title_zh: 图神经网络模块感知优化器 GraphMuon
authors:
- Guy Hadad
- Haggai Roitman
- Moshe Eliasof
- Bracha Shapira
affiliations:
- Ben-Gurion University of the Negev
arxiv_id: '2611.08379'
url: https://arxiv.org/abs/2611.08379
pdf_url: https://arxiv.org/pdf/2611.08379
published: '2026-11-04'
collected: '2026-11-12'
category: Training
direction: GNN 优化器 · 矩阵几何
tags:
- Graph Neural Networks
- Optimizer
- Muon
- Training Speedup
- OGB
one_liner: 提出 GraphMuon，在图传播特征的度量下正交化 Muon 更新，缓解图诱导放大，OGB 上获 1.32–2.42× 加速。
practical_value: '- 若业务中使用 GNN（如用户-商品二部图、社交关系图）做召回/排序，可尝试将 AdamW 替换为 GraphMuon，OGB
  大规模基准显示时间到目标加速 1.32–2.42 倍，直接缩短模型迭代周期；需评估协方差估计的额外内存与计算开销。

  - 借鉴「输入统计→权重更新度量」的思想：对输入分布不平坦的层，用输入协方差对更新做度量调整与步长归一化，比只约束权重矩阵本身更稳定；可迁移到推荐模型 Embedding
  层或 cross-attention 层，尤其是输入呈长尾/幂律分布的场景。

  - 关注 GraphMuon 开源的 PyTorch 实现，作为基础设施层优化集成到训练框架；在分布式训练中需注意正交化过程的通信与数值稳定性。

  - 主要收益在训练加速而非最终推荐指标提升，适合作为工程效率工具引入，而非业务策略创新。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
不同优化器对参数更新施加不同几何：Adam 按坐标缩放，Muon 利用权重矩阵结构做正交化。但 GNN 中权重矩阵的有效几何不仅由自身的通道混合权重决定，还受其作用的图传播表示影响。即使矩阵更新本身规范化，施加到图传播特征上仍可能被放大，导致训练不稳定或收敛慢。

## 方法关键点
GraphMuon 是面向 GNN 的建模感知优化器，核心有两处：一是在图传播层输入的协方差度量中执行正交化；二是根据更新对层表示产生的实际效应归一化步长。理论上证明 vanilla Muon 存在图诱导更新放大，而 GraphMuon 通过图度量下的正交化与归一化缓解该问题，等价于 Muon 极分解更新在图度量下的推广。

## 关键结果
在三个大规模 OGB 基准上，GraphMuon 相对 AdamW 的验证损失 time-to-target 加速达 1.32–2.42 倍；在 15 个覆盖节点分类、归纳图分类、图回归的数据集-架构组合中，13 个配置 time-to-target 更低，且预测性能保持有竞争力或更优。代码已开源。
