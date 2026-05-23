---
title: 'LatentOmni: Rethinking Omni-Modal Understanding via Unified Audio-Visual Latent
  Reasoning'
title_zh: LatentOmni：统一音视频潜在推理的全模态理解框架
authors:
- Yifan Dai
- Zhenhua Wu
- Bohan Zeng
- Daili Hua
- Jialing Liu
- Bozhou Li
- Yuran Wang
- Chengzhuo Tong
- Hao Liang
- Xiaochen Ma
affiliations:
- Shanghai Jiao Tong University
- Kuaishou Technology
- Peking University
- HKUST
- CASIA
arxiv_id: '2605.22012'
url: https://arxiv.org/abs/2605.22012
pdf_url: https://arxiv.org/pdf/2605.22012
published: '2026-05-20'
collected: '2026-05-23'
category: Multimodal
direction: 统一潜在空间的音视频联合推理
tags:
- Latent Space Reasoning
- Audio-Visual Understanding
- Omni-Modal
- Chain-of-Thought
- Temporal Alignment
- Feature Supervision
one_liner: 提出在潜在空间进行音视频联合推理，保留连续感知信息，通过特征级对齐与时序同步，超越显式文本思维链。
practical_value: '- **潜在空间推理可用于多模态内容理解**：电商直播、视频评论等场景中，可直接在连续潜在空间融合音视频信息进行推理，避免先转文本带来的信息压缩和时序错位，可用于商品属性校对、演示合规检测等。

  - **特征级监督对齐任务相关信号**：在训练多模态推荐或Agent模型时，可借鉴其feature-level supervision让潜在表示直接与目标任务（如动作定位、事件检测）所需的细粒度特征对齐，提升下游任务精度。

  - **Omni-Sync Position Embedding（OSPE）保持时序一致性**：该位置编码方法可应用于处理同步的音视频流，如直播切帧与语音的精确对齐、跨模态时序
  grounding，适用于视频理解、虚拟主播驱动等。

  - **构建交织推理轨迹数据**：LatentOmni-Instruct-35K的构造思路可用于生成电商场景的多模态思维链数据，监督模型学习在潜在空间中混合文本和感知状态进行逐步推理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前多模态大模型在需要细粒度音视频联合推理的任务上表现不佳，核心原因是显式文本思维链将连续的视听信号压缩为离散token，导致时序信息弱化、推理偏向语言先验。论文认为统一的潜在空间更适合跨模态推理，能保留密集的感知信息并兼容自回归生成。

**方法**：提出LatentOmni框架，将文本推理与音频-视觉潜在状态交织在一起。引入特征级监督，使潜在推理状态与任务相关的感官特征对齐；设计Omni-Sync Position Embedding（OSPE）保持潜在音视觉状态间的时序一致性。此外，构建了包含35K条音视交织推理轨迹的数据集LatentOmni-Instruct-35K用于监督训练。

**结果**：在多个音视频推理基准上，LatentOmni在所有开源模型中取得最佳性能，且一致优于显式文本CoT基线，验证了潜在空间联合推理是提升全模态理解的有效路径。
