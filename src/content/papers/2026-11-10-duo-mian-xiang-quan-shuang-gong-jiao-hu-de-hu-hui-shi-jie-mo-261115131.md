---
title: 'Duo: A Reciprocal World Model for Full-Duplex Interaction'
title_zh: Duo：面向全双工交互的互惠世界模型
authors:
- Hengyuan Cao
- Biao Gong
- Guoshan Lu
- Qiyuan Zhang
- Lin Liu
- Yiding Tian
- Yilei Jiang
- Yuxin Ma
- Chengzhang Wu
- Kun Chen
affiliations:
- inclusionAI
arxiv_id: '2611.15131'
url: https://arxiv.org/abs/2611.15131
pdf_url: https://arxiv.org/pdf/2611.15131
published: '2026-11-10'
collected: '2026-11-14'
category: Multimodal
direction: 全双工多模态世界模型
tags:
- World Model
- Full-Duplex Interaction
- Autoregressive
- Audiovisual
- Real-time
one_liner: 提出互惠世界模型，Duo v1 以意图与实现双模块实现全双工音视频实时交互
practical_value: '- 借鉴 Intent + Realization 双模块解耦：将决策推理（Intent）与内容生成（Realization）分开建模，适合对话式推荐或导购
  Agent，便于分别优化和调试。

  - 采用 chunk 级条件与统一时间线同步 tokens，配合因果 attention mask 防止未来信息泄漏，可迁移到实时流式交互系统，如直播推荐、实时客服、语音导购等场景。

  - 双 rollout 蒸馏策略：在自回归生成的 tokens 上训练而非仅依赖 ground-truth，可缓解分布偏移，可借鉴到生成式推荐或对话系统中的自训练与蒸馏。

  - 全双工感知与响应（支持打断、自发对话）对构建语音/视频导购、虚拟主播等业务有参考意义，但工程复杂度较高，需要权衡实时性与模型规模。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有世界模型主要模拟物理现实，将推理和决策作为外部控制，而非世界本身的一部分。论文提出互惠世界模型（RWM），认为智能与物理现实同等基础，并将世界交互拆分为两个同等核心的能力：Intent（意图，负责认知与决策）和 Realization（实现，负责生成连贯的音视频行为）。

**方法关键点**：Duo v1 实现了 RWM，包含三项技术设计：
1. 自回归建模用于持续交互推理和参与决策，而非仅作为扩散模型的指令理解；
2. 构建 chunk 特定的条件，在统一时间线上同步 Intent 与 Realization 的 tokens，并通过模块特定的 attention mask 强制 chunk 内和跨 chunk 的因果依赖，防止未来输入泄漏；
3. 通过双重 rollout 蒸馏缓解分布偏移，训练基于自回归生成的 Intent tokens 和 Realization 合成的视听历史。

**结果**：Duo v1 能够实时感知音视频和文本，支持全双工交互，包括自发对话和打断。用户可分享实物、重塑虚拟场景、引导助手或玩音视频游戏，无需键鼠。模型已开源，发布代码与权重。
