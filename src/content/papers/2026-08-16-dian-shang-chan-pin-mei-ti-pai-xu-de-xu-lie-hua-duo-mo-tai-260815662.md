---
title: Sequential Multimodal Evidence Optimization for Product Media Ranking in E-Commerce
title_zh: 电商产品媒体排序的序列化多模态证据优化
authors:
- Prasenjit Dey
- Frank McIntyre
- Arnab Sinha
affiliations:
- Amazon.com Inc.
arxiv_id: '2608.15662'
url: https://arxiv.org/abs/2608.15662
pdf_url: https://arxiv.org/pdf/2608.15662
published: '2026-08-16'
collected: '2026-08-18'
category: RecSys
direction: 多模态媒体排序 · 离线策略优化
tags:
- Multimodal Ranking
- Off-policy RL
- Survival Weighting
- Pointer Network
- Conversion Optimization
- E-commerce
one_liner: 两阶段效用引导框架学习前缀转化效用并训练生存加权自回归策略，将决策关键媒体前置
practical_value: '- 两阶段解耦：先学习并冻结轨迹效用模型作为 reward，再训练 Pointer Network 排序策略，避免直接对稀疏终端转化做
  REINFORCE；适合 item/媒体 slate 排序，稳定且易于调参。

  - 生存加权 reward-to-go：用用户到达位置的概率乘以边际效用作为逐步奖励，显式将高价值媒体前置，降低滑动深度；比终端回报和点击代理更贴合转化目标。

  - PAL 双塔去位置偏差：训练时位置塔吸收 slot 偏差，推理/策略优化时丢弃，防止位置效应污染内容表示；离线评估中移除 PAL 会同时损伤 CVR 和 MSC。

  - 交互特征 masking：训练期按概率将 dwell/click/zoom 替换为 mask token，推理全 mask，弥合 train-serve 分布差异；在实时交互特征不可用的排序场景可复用。

  - 冻结效用模型支持 leave-one-out counterfactual 归因，无需媒体级标签即可评估每个媒体贡献，用于内容审计、低价值替换和类目级媒体策略。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：电商移动端详情页以 carousel 呈现图片、视频、3D 等多模态媒体，用户必须滑动才能看到后续内容，常提前放弃。现有排序多优化点击/停留等短视代理，或把媒体视为独立竞争 item，未考虑它们作为协同证据对最终转化的顺序性影响，也面临媒体级归因缺失、stop depth 内生截断与位置偏差。

方法关键点：SMEO 分两阶段。首先构建多模态 token：用冻结的 ViT/VideoMAE/Uni3D 提取视觉，拼接模态 embedding、历史先验和训练期交互特征（30% mask，推理全 mask 以对齐 train-serve）。轨迹效用模型为 4 层因果 Transformer，仅用观测到的 consumed prefix 监督终端转化；PAL 双塔把位置偏差隔离到 position-only 塔，训练后丢弃，输出内容效用。生存深度加权对深层样本 upweight，并截断控制方差。冻结效用后，用 Pointer Network 自回归生成媒体排列；每个位置的边际效用 Δ_t 乘以到达概率 ρ_t 和折扣，作为生存加权 reward-to-go；用 REINFORCE+SCST baseline 优化，熵正则防止策略坍塌。最后冻结模型可做 leave-one-out counterfactual 归因。

实验与结果：在约 1.5 亿移动会话、数百万商品、跨电子/服装/家居/美妆类目数据上与 heuristic、CTR、CLTR-CVR、Listwise-MM、Seq2Slate-Adapt 对比，SNIPS-CVR +6.1%、DR-CVR +5.4%、MSC 减少 15.3%。消融显示生存加权贡献最大，移除后 MSC 恶化最明显；PAL 和交互 masking 也带来稳健提升。定性上，SMEO 前置高信息媒体；冗余视觉边际效用显著为负（partial Spearman -0.61），并学到类目特异的媒体价值：3D 在家居、视频在电器/运动、规格图在电子/消耗品贡献更高。

一句话：把产品媒体视为顺序累积证据，用到达概率加权边际转化效用来训练自回归策略，比点击代理和终端回报更有效。
