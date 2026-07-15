---
title: Stream-aware Side Adaptation for Large Pre-trained Multimodal Embedding Models
  in Sequential Recommendation
title_zh: 序列推荐中大型多模态嵌入模型的流感知侧适配
authors:
- Junchen Fu
- Kaiwen Zheng
- Ioannis Arapakis
- Wenhao Deng
- Xin Xin
- Joemon M. Jose
- Xuri Ge
affiliations:
- University of Glasgow
- Telefónica Scientific Research, Telefónica Innovación Digital
- Shandong University
arxiv_id: '2607.10909'
url: https://arxiv.org/abs/2607.10909
pdf_url: https://arxiv.org/pdf/2607.10909
published: '2026-07-12'
collected: '2026-07-15'
category: RecSys
direction: 序列推荐 · 多模态大模型侧适配
tags:
- Sequential Recommendation
- Multimodal Embedding
- Side Adaptation
- Stream-aware Fusion
- Residual Adapter
- Large Pre-trained Models
one_liner: 提出流感知侧适配框架Stresa，用SHAF保留历史记忆和ReSA选择性残差更新，根治深层侧适配退化
practical_value: '- 使用预训练多模态大模型（如商品图文）得到通用语义嵌入，再用侧适配器调整到推荐域，可避免全量微调，大幅降低训练成本，适合电商快速迭代。

  - SHAF 和 ReSA 可插拔于任何冻结的 Transformer 骨干，深层适配不再退化，能有效利用中间层隐藏状态提升序列建模。

  - 流感知融合保留历史侧信息，适合商品交互序列中长短期偏好捕捉，可迁移到点击率预估等任务。

  - 侧适配器计算量极小，易于线上部署，且支持热插拔更换下游任务，适合多场景复用同一多模态基座。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：直接使用 Qwen3-VL Embedding 等大型多模态嵌入模型做序列推荐会因域不匹配而次优；侧适配是高效解决路径，但现有方法普遍存在深层适配退化（层数越深效果越差），丢弃深层隐藏状态浪费了有用信息。根本原因有二：(1) 残差加法时缺乏融合选择建模；(2) 逐步 sigmoid 融合丢失早期表示。

**方法**：提出流感知侧适配框架 Stresa，包含两个核心模块：
- **SHAF (Stream-aware Hidden-Adapter Fusion)**：在融合层输出与侧适配器输出时，引入历史侧记忆流，保留之前层的适配信息，缓解逐步融合中的信息丢失。
- **ReSA (Residual Stream Adapter)**：在每层产生选择性的残差更新，而非固定残差加法，让模型学习哪些隐藏状态需要调整，哪些保留骨干原输出，有效利用深层表示。

**结果**：在多个公开序列推荐数据集上，基于不同骨干嵌入模型，Stresa 一致优于标准侧适配器与现有 SOTA；消融实验验证了两个模块的必要性。该方案使得冻结的通用大模型经过轻量侧适配即可达到甚至超过专门训练的推荐模型性能。
