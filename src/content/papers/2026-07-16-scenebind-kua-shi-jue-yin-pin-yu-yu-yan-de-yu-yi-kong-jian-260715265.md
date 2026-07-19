---
title: 'SceneBind: Binding What and Where Across Vision, Audio and Language'
title_zh: SceneBind：跨视觉、音频与语言的语义-空间绑定表征
authors:
- Mingfei Chen
- Zijun Cui
- Ruoke Zhang
- Hyeonggon Ryu
- Eli Shlizerman
affiliations:
- University of Washington
- University of Texas at Dallas
- Hankuk University of Foreign Studies
arxiv_id: '2607.15265'
url: https://arxiv.org/abs/2607.15265
pdf_url: https://arxiv.org/pdf/2607.15265
published: '2026-07-16'
collected: '2026-07-19'
category: Multimodal
direction: 多模态语义-空间场景表征
tags:
- omni-modal
- scene representation
- cross-modal retrieval
- spatial grounding
- semantic-spatial binding
one_liner: 提出一种全模态场景表征，联合语义与3D空间理解，实现跨模态检索与目标定位
practical_value: '- 电商多模态商品理解可参考：将商品图片构建为对象级语义-空间槽位（如衣服的款式+空间位置），提升跨模态检索的细粒度匹配。

  - 轻量级空间建模（仅增加少量 token）的设计，适合对已有预训练语义编码器（如 CLIP）做低成本空间扩展，可直接迁移到商品 3D 展示或 AR 试穿中对象位置的理解。

  - 语义-空间匹配（全局相似度+对象对齐）的思路可用于推荐系统的多模态融合，例如在视频推荐中同时对齐标题语义与画面中物体的空间关系。

  - Agent 在真实环境中的空间感知：将环境抽象为对象槽位，可提升 Agent 对“什么地方有什么”的理解，适合电商客服 Agent 在对话中引用商品图片位置信息。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有全模态编码器（如 ImageBind）虽能理解场景中“有什么”（语义），但缺乏对“在哪里”（3D 空间结构）的显式建模，限制了空间感知与推理。

**方法**：提出 SceneBind，将场景表示为全局语义嵌入与多个对象中心化的语义-空间槽位（slot）。每个槽包含对象语义、3D 空间属性（距离、方位、高度）及不确定性估计。模型兼容现有预训练语义编码器（如 CLIP、ImageBind），仅增加少量可学习 token 实现轻量级空间建模。训练时使用对比学习对齐不同模态（视觉、音频、语言）的语义与空间信号，并设计了 SceneBind Matching 机制，联合全局相似度和对象级对齐进行跨模态检索与对象定位。同时贡献了一个含双耳音频和结构化语义-空间标注的真实场景数据集。

**结果**：在场景检索和空间检索任务上达到 SOTA，相较基线显著提升；无需微调即可零样本迁移至音视频定位等下游任务，展现出很强的泛化能力。
