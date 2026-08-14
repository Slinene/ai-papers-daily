---
title: 'STAR: Structured Tokenization and Target-Aware Interest Representation for
  PCVR Prediction'
title_zh: 面向PCVR预测的结构化分词与目标感知兴趣表征STAR
authors:
- Yimeng Xu
- Haorui Zhang
- Yingqi Song
- Ying Jiang
- Lan Ma
affiliations:
- Tsinghua University
- Peking University
arxiv_id: '2608.12986'
url: https://arxiv.org/abs/2608.12986
pdf_url: https://arxiv.org/pdf/2608.12986
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: 工业推荐排序 · 序列-特征统一建模
tags:
- PCVR
- feature tokenization
- target-aware
- InfoNCE
- HyFormer
- ranking
one_liner: STAR通过结构化特征分词、DIN式目标感知序列解码与加权InfoNCE对比目标，在PCVR排序上稳定提升AUC
practical_value: '- 高基数稀疏特征别直接丢弃：频率 remap + 共享 unknown bucket + 序列哈希分支，让长尾 ID 重新进入模型；同时保留高频
  ID 专属 embedding，可迁移到电商 user/item 长尾特征。

  - 对行为序列做 target-aware decoding 而非全局 pooling：DIN 式 query 用 candidate item 与序列 token
  的差/点积计算注意力，能更准提取与当前广告/商品相关的兴趣；公式（4-6）可落地。

  - 训练加 InfoNCE 对比辅助目标，对 user-item 表示做 in-batch 对齐，提升排序 AUC 而非 LogLoss；适合推荐排序场景，注意温度与权重衰减。

  - 稀疏特征中的零值需区分真实零与 padding/missing：加 non-zero mask、整数 ID 偏移，避免特征混淆；工程上要重建映射表保证 train/infer
  一致性。

  - 缩放容量优先加 hidden width 与 HyFormer block depth，而非 embedding 维度或稀疏参数量；embedding 扩增增益不单调且有成本。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业 PCVR 排序需联合建模异质非序列特征、多行为序列和 target-aware 兴趣，同时应对高基数稀疏、缺失值和训练推理不一致。基线 HyFormer 等统一 backbone 已经存在，但仍有高基数特征被跳过、序列对 target 条件不足、缺失零值混淆等问题。

**方法关键点**：
- 结构化特征分词：高频 ID 独立 embedding，长尾折叠到共享桶；序列哈希分支处理超高频序列；非零 mask 和 ID 偏移区分真实零与 padding；密集特征按语义 token 化，稀疏-密集对齐池化。
- 目标感知兴趣表示：DIN 式 query decoder，用 candidate item 与序列 token 的差/点积构造 q_tgt，注意力加权后残差更新 query。
- 用户-物品交互增强：对齐稀疏-密集对池化、user-item pair-product tokens、以及 fused target-aware interest token。
- 辅助目标：加权 InfoNCE 对比 user/item 表示，temperature 0.07，权重从 0.1 衰减到 0.01 并 cap 主损失比例。
- 训练推理一致性：重建特征 remap 表与结构超参数，固定 global-batch manifest，bf16 AMP、梯度累积、EMA。

**关键实验**：KDD Cup 2026 Tencent UniRec PCVR 数据集 2000 万训练样本。全优化模型相对官方 baseline：val AUC 0.844503 vs 0.829582，test AUC 0.836546 vs 0.819961，提升 0.016585。主消融中，绝对时间特征贡献最大（移除 test AUC -0.002043），其次是 padding-zero 消歧（-0.001327）、InfoNCE（-0.000336）、DIN decoder（-0.000193）、序列哈希/频率重映射（-0.000124）。模型缩放：hidden width 128→256 带来 val AUC +4.61e-4；depth 2→4 带来 test AUC +0.000199，明显优于 embedding 维度扩展。

**最值得记住**：在工业 PCVR 排序中，时间上下文、target-aware 序列解码和高基数稀疏信号恢复等针对性组件，比单纯堆容量更能稳定提升离线 AUC。
