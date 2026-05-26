---
title: 'DeGRe: Dense-supervised Generative Reranking for Recommendation'
title_zh: 密集监督的生成式重排框架 DeGRe
authors:
- Chaotian Song
- Jingyao Zhang
- Chenghao Chen
- Zisen Sang
- Dehai Zhao
- Guodong Cao
- Boxi Wu
- Deng Cai
- Jia Jia
affiliations:
- 浙江大学
- 阿里巴巴
arxiv_id: '2605.25749'
url: https://arxiv.org/abs/2605.25749
pdf_url: https://arxiv.org/pdf/2605.25749
published: '2026-05-25'
collected: '2026-05-26'
category: GenRec
direction: 生成式重排 · 密集监督 · 离线在线解耦
tags:
- Generative Reranking
- Dense Supervision
- Lookahead Planning
- Cumulative Regression
- Distillation
- Pointer Network
one_liner: 通过离线 beam search 挖掘高价值序列并转化为逐步密集监督，让轻量生成器在线仅需一次贪婪解码即逼近全局最优重排。
practical_value: '- **离线在线解耦范式**：离线用计算资源换在线效率，将排列空间探索、beam search 等重计算放在离线完成，在线仅部署轻量生成器，一次贪婪解码，适合电商实时重排的延迟约束。

  - **密集监督构造方法**：利用累积回归评估器对每个候选提供 step-wise 价值估计，构建硬标签（模仿选中的物品）和软标签（保留候选集的完整价值分布）作为训练信号。相比只用点击与否的启发式标签或
  list-wise 稀疏奖励，能更精细地指导生成器学习物品间上下文依赖。

  - **序列加权蒸馏**：对 beam search 得到的多条前瞻序列按其评估价值加权，让生成器重点学习高价值序列，避免被低质量解码路径带偏；软标签蒸馏作为辅助正则，既保留排序信息又防止过拟合。

  - **用户引导的解码启动**：用用户表征投影作为 decoder 的初始输入，替代通用的 <BOS> 令牌，增强首物品决策的个性化，可借鉴到自回归生成推荐中。

  - **候选约束的指针网络解码**：生成器每一步从输入候选集中选择物品，通过点积注意力得分选取，避免生成无效物品，适合变长候选集的电商重排场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有生成式重排方法存在两个核心问题：(1) 启发式标签偏差——常用简单规则（如将点击物品推至顶部）构造训练目标，忽略列表上下文中的因果依赖，难以探索未曝光空间的高价值排列；(2) 信用分配问题——只依赖列表级的稀疏奖励（如整体 CTR），无法为每一步生成决策提供精细指导，导致优化方向模糊。

**方法关键点**：
- **离线在线解耦架构**：离线阶段利用充足计算资源进行排列空间探索，在线阶段仅需轻量生成器做一次贪婪解码，平衡了效果与延迟。
- **前瞻评估器（DeGRe-E）**：基于累积回归的 Causal Transformer，对任意子序列估计其累积价值分布（例如点击数），输出 \(P(V \ge k)\) 并求和得到期望价值。通过 beam search 探索未曝光空间，挖掘高价值前瞻序列。
- **密集监督构造**：对每条前瞻序列，在每步生成硬标签（选中的物品）和软标签（对剩余候选物品的价值分布进行 softmax 归一化），为生成器提供 step-wise 的模仿目标与排序分布正则。同时对不同质量的序列进行加权，强调高价值序列的贡献。
- **在线生成器（DeGRe-G）**：轻量 Encoder-Decoder 结构，编码器用双向 Transformer 捕捉候选集内物品间的竞争与互补关系，解码器以用户表征投影作为初始输入，通过因果 Transformer 和指针网络进行候选约束的逐物品生成。训练时用混合蒸馏损失（交叉熵模仿 + KL 散度对齐）。

**关键实验**：在 ML-1M、Taobao Ad、Taobao Flash Shopping 三个数据集上，DeGRe-G 的 HR@1% 分别达到 89.1%、71.1%、88.7%（beam=8），远超 GoalRank 等现有方法（ML-1M 上 GoalRank 仅 59.2%）。在线 A/B 测试在淘宝闪购场景下 GMV 提升 +3.75%，CTR 提升 +2.85%，推理延时仅增加 14.8ms，并在新用户和不同客户端（支付宝）上均表现鲁棒。
