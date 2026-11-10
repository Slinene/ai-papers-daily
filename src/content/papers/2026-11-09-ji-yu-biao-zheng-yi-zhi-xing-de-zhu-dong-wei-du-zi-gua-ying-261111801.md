---
title: Proactive Dimension-Adaptive Denoising for Graph Collaborative Filtering via
  Representation Coherence
title_zh: 基于表征一致性的主动维度自适应图协同过滤去噪
authors:
- Wenjun Li
- Dong Zhao
- Jiaying Shi
- Juan Zhang
- Zhaoming Pan
- Zhimin Zhang
affiliations:
- Netease Media Group
arxiv_id: '2611.11801'
url: https://arxiv.org/abs/2611.11801
pdf_url: https://arxiv.org/pdf/2611.11801
published: '2026-11-09'
collected: '2026-11-10'
category: RecSys
direction: 图协同过滤去噪 · 表征一致性
tags:
- Graph Collaborative Filtering
- Denoising
- Representation Coherence
- Dimension-Adaptive Mask
- LightGCN
one_liner: 提出表征一致性检测作为主动噪声信号，融合 loss 驱动交互级维度自适应掩码，显著提升图协同过滤去噪效果
practical_value: '- **噪声检测信号可迁移**：在电商隐式反馈（点击、加购、成交）中，用交互 embedding 与用户历史偏好中心的距离（表征一致性）作为主动噪声信号，比单纯依赖训练
  loss 更早、更稳定地识别误点击/冲动行为。尤其对活跃用户，一致性信号更可靠；冷启动用户可融合 loss 信号兜底，这种 activity-aware 加权策略可直接借鉴到用户行为序列清洗。

  - **维度自适应掩码有落地价值**：对低质量交互限制其有效表示维度（等效于降权/降容），而不是完全丢弃样本，保留信息的同时抑制噪声传播。该方法只在训练阶段生效，线上推理零额外延迟和参数，适合
  LightGCN 类生产管线，可低成本嵌入现有召回模型。

  - **对比正则化稳定几何**：轻量对比正则化提升 embedding 均匀性，增强噪声判别边界的稳定性。这一 trick 可以移植到其他需要基于嵌入距离做可靠性判断的场景，例如用户历史行为去噪、多兴趣召回中的兴趣簇纯度优化。

  - **对生成式推荐的借鉴**：若用 LLM 生成 semantic ID 或用户兴趣表示，输入序列中的噪声交互会污染生成质量。可先训练阶段用 RCD 思路对用户行为序列做去噪加权，再输入生成模型，可能提升推荐准确度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：隐式反馈中的噪声交互（误点击、冲动购买）会沿用户-物品图传播，污染表示学习。现有显式去噪方法统一依赖训练 loss 估计交互可靠性，但 loss 是被动信号——噪声已经造成预测误差后才被检测到，且受训练阶段、负采样、困难正样本混淆。

**方法关键点**：提出 Noise-aware Dimension Learning (NDL)。核心组件 Representation Coherence Detection (RCD) 计算交互表示与用户历史偏好中心在嵌入空间的 coherence，作为独立于 loss 的主动噪声信号。RCD 与 loss 信号通过 activity-aware 加权融合：活跃用户更依赖 coherence，冷启动用户自动退化为 loss。融合后的估计驱动 interaction-level 维度自适应掩码，限制不可靠交互的有效表示容量。轻量对比正则化进一步改善 embedding 均匀性，稳定 RCD 判别几何。NDL 仅在训练循环内，推理时无额外延迟或参数。

**关键结果**：在三个公开基准上，NDL 一致超越最强基线 DAR：Amazon-book Recall@5 +17.95%，Yelp +12.33%，MovieLens-1M +5.63%。去除对比正则化的核心变体在稀疏数据集上仍超过 DAR，表明表征一致性是主要增益来源。
