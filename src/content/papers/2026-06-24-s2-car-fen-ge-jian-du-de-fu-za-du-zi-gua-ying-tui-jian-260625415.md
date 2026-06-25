---
title: 'S2-CAR: Segmentation-Supervised Complexity-Adaptive Recommendation'
title_zh: S2-CAR：分割监督的复杂度自适应推荐
authors:
- Linjiang Guo
- Nitin Bisht
- Shiqing Wu
- Xianzhi Wang
- Guandong Xu
affiliations:
- University of Technology Sydney
- City University of Macau
- The Education University of Hong Kong
arxiv_id: '2606.25415'
url: https://arxiv.org/abs/2606.25415
pdf_url: https://arxiv.org/pdf/2606.25415
published: '2026-06-24'
collected: '2026-06-25'
category: RecSys
direction: 顺序推荐 · 意图分割与多兴趣建模
tags:
- Sequential Recommendation
- Intent Segmentation
- Soft-TPP
- Multi-Interest
- Contrastive Learning
one_liner: 通过连续能量衰减建模意图动态实现无监督分段，结合自适应多兴趣提取与对比辅助训练，提升长序列中间信号利用
practical_value: '- **无监督意图分割插件**：利用 Soft-TPP 基于行为动态划分 session，可在电商推荐系统中替代固定时间窗规则，避免硬切分导致的意图错位，尤其适合处理用户长期后重回同一品类时的意图连续性问题。

  - **分段自适应的兴趣压缩**：根据分段数量动态调整兴趣槽位，引入压缩比 ρ 抑制周期重复兴趣的浪费，能生成更紧凑的用户多兴趣向量，在召回或排序阶段降低计算和存储开销。

  - **层次对比辅助训练**：训练时加入基于分段的全局兴趣编码器作为教师信号，通过对比损失正则化因果序列编码器，推理时丢弃，零额外延迟提升长序列建模能力，可直接迁移到现有的
  Transformer 推荐模型。

  - **边界类型嵌入**：将分段边界标志作为可学习嵌入加入物品表示，仅增加微小参数量，便能让模型显式感知意图变迁，该 trick 可方便集成到自注意力架构中。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
长序列推荐中，用户意图随时间异步转换，固定时间窗分割常将同一意图割裂或将不同意图混入同一片段，导致模型过度依赖近期信号、忽略中段有效信息。需要一种随行为动态变化的意图分割方法，并以此为基础紧凑表达多兴趣。

**方法**  
- **Soft-TPP 无监督分割**：将意图建模为连续能量向量，上下文自适应的衰减率（融合类别转移与用户历史分布），当能量保留率低于阈值时产生边界，实现无标签的意图分段。
- **顺序推理编码器 (SIE)**：因果 Transformer + 多尺度旋转位置编码 (MS-RoPE) + 边界类型嵌入，从最后位置提取用户嵌入用于推荐。
- **层次兴趣编码器 (HIE)**：基于分段聚合得到等权片段表示，再用跨注意力与压缩比 ρ 自适应提取多兴趣（ρ 抑制周期重复），引入多样性正则防坍缩。
- **训练策略**：Soft-TPP 预训练后冻结；主训练联合交叉熵、对比损失（对齐 SIE 与 HIE 表示）和多样性损失；推理时仅保留 SIE。

**实验**  
在 ML-1M、Amazon、Steam 三个数据集上与 13 个基线对比，S2-CAR 在所有指标上最优。ML-1M 上 R@10 达 28.74（第二高 24.75），MRR@10 为 13.07（第二高 9.94），相对提升显著；消融与插件实验验证了 Soft-TPP 分割的通用增益及各模块的必要性。

**核心洞见**  
以能量衰减驱动的 Soft-TPP 替代固定窗口分割，能让序列推荐模型在无监督信号下感知意图边界，有效激活长序列中段的语义信息。
