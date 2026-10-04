---
title: 'MoLE: Mixture of Latent Experts for Complementary Visual Reasoning'
title_zh: MoLE：互补视觉推理的潜在专家混合
authors:
- Yingcheng Liu
- Tianyi Jiang
- Yujuan Ding
- jiangbo Ai
- Xun Jiang
- Guoqing Wang
- Wei Ye
- Yi Bin
affiliations:
- Tongji University, China
- Hong Kong Polytechnic University, Hong Kong
- Alibaba Group, China
- University of Electronic Science and Technology of China, China
arxiv_id: '2610.01917'
url: https://arxiv.org/abs/2610.01917
pdf_url: https://arxiv.org/pdf/2610.01917
published: '2026-10-01'
collected: '2026-10-04'
category: Reasoning
direction: 视觉推理 · 潜在专家混合
tags:
- Mixture of Experts
- Latent Reasoning
- Vision-Language Model
- Complementary Visual Reasoning
- Multimodal
one_liner: 用潜在专家混合让不同 latent token 提取互补视觉证据，在相同 latent 预算下显著提升视觉推理
practical_value: '- 在多模态商品理解/搜索中，若用 latent token 做视觉推理，避免让多个 token 共享 value projection；可给每个
  latent expert 独立 routing/value，迫使它们提取互补视觉证据，减少冗余。

  - 两阶段训练可直接复用：先强制视觉证据走 latent pathway 学习专业化表示，再恢复 direct visual access，无需预定义专家角色或中间视觉标签，适合业务多模态
  VLM 微调。

  - latent summary experts 聚合互补表征，能在固定 latent budget 下提升推理性能，适合多图/多区域商品理解等需要控制计算成本的场景。

  - 用 latent-state similarity 和 attention diversity 作为诊断指标，评估多专家或多模态融合是否真正学到互补信息，有助于排查模型冗余。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 latent visual reasoning 方法中多个 latent token 通过共享 value projection 访问相同视觉证据，缺乏互补信息提取机制，单纯增加 latent budget 会带来冗余。

**方法关键点**：将不同 latent token 视为专门化视觉专家，提出 MoLE。它控制每个 latent visual expert 观察哪些视觉证据以及如何转换证据；在证据提取阶段隔离各专家，避免共享 value 带来的同质化；引入 latent summary experts 聚合互补表征；采用两阶段训练，先强制视觉证据走 latent pathway，再恢复直接视觉访问，无需预定义专家角色或中间视觉目标。

**关键结果**：在五个视觉推理 benchmark 上平均 78.6，比 data-matched SFT 高 4.9，比同 latent budget 下最强 latent baseline 高 3.6；表征分析显示 latent state 相似度更低、视觉 attention 更多样；mask latent pathway 后平均性能下降 9.2，说明专门化 latent 计算比单纯加 latent token 更有效。
