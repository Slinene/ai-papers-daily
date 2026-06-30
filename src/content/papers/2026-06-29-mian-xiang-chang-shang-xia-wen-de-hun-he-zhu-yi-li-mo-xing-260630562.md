---
title: Morphing into Hybrid Attention Models
title_zh: 面向长上下文的混合注意力模型层选择优化
authors:
- Disen Lan
- Jianbin Zheng
- Yuxi Ren
- Xin Xia
- Xuanda Wang
- Xuefeng Xiao
- Xipeng Qiu
- Yu Cheng
affiliations:
- Fudan University
- ByteDance Seed
- The Chinese University of Hong Kong
arxiv_id: '2606.30562'
url: https://arxiv.org/abs/2606.30562
pdf_url: https://arxiv.org/pdf/2606.30562
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: 混合注意力模型自动化层选择
tags:
- hybrid attention
- layer selection
- linear attention
- long-context
- gating optimization
one_liner: 提出FlashMorph，通过联合优化层门控自动选择全注意力层，构建高效长上下文混合模型
practical_value: '- 在搜索推荐场景中处理用户长行为序列、多轮对话等长上下文时，可借鉴 FlashMorph 将全注意力模型转换为部分线性注意力的混合架构，在保留关键层全注意力的同时大幅降低推理成本。

  - 层选择不再依赖手工规则，而是通过可学习门控在合成数据上端到端优化，能自动发现更优的混合配置，适合业务中快速适配不同长上下文任务。

  - 线性化正则项显式鼓励模型信任线性注意力，防止门控退化成全注意力，可在部署时平衡效率与效果。

  - 整个流程冻结原模型权重，仅优化门控和后续微调，实现成本低，便于在已有业务模型上低成本实验和上线。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机** 混合注意力模型（部分层全注意力 + 部分层线性注意力）能缓解长上下文推理的平方复杂度瓶颈，然而哪些层保留全注意力对效果至关重要。现有选择方法（固定模式、逐层打分）独立看待层重要性，忽略层间在全局混合配置下的相互影响。

**方法** 将层选择形式化为预算约束的子集优化问题，提出 FlashMorph。首先构建可变形模型：为每个全注意力层增加一个线性注意力分支；然后冻结模型权重，在合成的长上下文检索数据上联合优化所有层的二值门控，并加入**线性化正则项**鼓励模型优先使用线性注意力以获得效率；优化后根据预设的全注意力预算离散化门控，得到混合架构；最后通过标准的 logits 蒸馏和长上下文微调恢复性能。

**关键结果** 在多个长上下文基准上，FlashMorph 发现的混合配置在保持相近召回率的同时，显著超越启发式层选择的基线；层选择过程高效，对比现有逐层评估方法大幅降低算力开销；且在通用 benchmark 上性能无明显下降，证明了方法的有效性、高效性和可扩展性。
