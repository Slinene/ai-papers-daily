---
title: When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities
title_zh: 结构化稀疏自编码器实现跨模态概念一致学习
authors:
- Weiduo Liao
- Yunqiao Yang
- Ying Wei
affiliations:
- Zhejiang University
- Nanyang Technological University
arxiv_id: '2607.08605'
url: https://arxiv.org/abs/2607.08605
pdf_url: https://arxiv.org/pdf/2607.08605
published: '2026-07-09'
collected: '2026-07-11'
category: Multimodal
direction: 多模态可解释性 · 结构化稀疏自编码
tags:
- sparse autoencoders
- multimodal interpretability
- concept consistency
- structured sparsity
- vision-language models
one_liner: 在视觉语言模型中，通过图像块分组与结构化稀疏正则化，解决稀疏自编码器概念碎片化问题，提升跨模态概念一致性与单义性
practical_value: '- 对电商/推荐多模态模型（如商品图文理解）的依赖时，S2AE 可作为特征解释工具，分析不同模态下概念表示的一致性，辅助定位模型偏差或碎片化表达。

  - 结构化稀疏正则化思路可迁移至其他需要分组特征选择的场景，例如用户行为序列按场景分组后，强制组内一致性与组间解耦，提升表示紧凑性。

  - 跨模态概念一致性评估方法（mIoU、monosemanticity）可直接用于评估推荐系统中文本描述与图像特征共嵌入空间的对齐质量。

  - 工程上，基于注意力相似度和空间邻近的图像块分组策略可启发商品图像多尺度特征的组织方式，提升视觉概念的可解释性与可控性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：在视觉语言模型（VLM）中，普通稀疏自编码器（SAE）学习的视觉概念常呈现碎片化覆盖（例如同一概念在图像中表现为不连续区域），导致跨模态概念不一致，阻碍对模型内部机理的可靠解释。

**方法关键点**：
- 提出 **结构化稀疏自编码器（S²AE）**，首先基于 Transformer 注意力相似度和空间邻近对图像块进行分组，使同一语义对象的像素聚合成组。
- 训练时施加结构化稀疏正则化：**排他性稀疏（exclusive sparsity）** 强制不同组激活不同的神经元，实现概念解耦；**组稀疏（group sparsity）** 促使同一组内的块激活相同神经元集合，强化概念一致性。
- 这种视觉结构先验将碎片化的激活引导至语义连贯的概念区域，无需额外标注。

**关键结果**：
- 在 Qwen2.5-VL-7B-Instruct 上，S²AE 语义对齐指标（mIoU）平均提升 **6.06%**，表示效率（L0 范数）降低 **60.81**（更稀疏），重建保真度（Explained Variance）仍 > 99%。
- 跨模态一致性：多模态特征的平均语义一致性提升 **3.08%**，单体语义性（monosemanticity）评分提升 **2.37%**，学到的概念更连贯、解耦。
