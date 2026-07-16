---
title: 'Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking
  for Zero-Shot Composed Image Retrieval'
title_zh: 面向视觉无关的组合图像检索：属性增强评分与LLM重排序
authors:
- Ryotaro Shimada
- Yu-Chieh Lin
- Yuji Nozawa
- Youyang Ng
- Osamu Torii
- Yusuke Matsui
affiliations:
- The University of Tokyo
- Kioxia Corporation
arxiv_id: '2607.12621'
url: https://arxiv.org/abs/2607.12621
pdf_url: https://arxiv.org/pdf/2607.12621
published: '2026-07-14'
collected: '2026-07-16'
category: Multimodal
direction: 视觉无关组合图像检索·属性增强与LLM重排
tags:
- Composed Image Retrieval
- Vision-Free
- Zero-Shot
- LLM Reranking
- Attribute Augmentation
one_liner: 通过属性增强混合评分和LLM重排序，实现视觉无关的零样本组合图像检索，CIRR R@1 44.04%（+8.79%）
practical_value: '- **视觉无关检索范式**：将数据库图像离线预生成文本描述（如商品标题/属性），用文本检索替代视觉编码器，大幅降低计算和存储成本，适合电商海量商品库的粗召回。

  - **属性增强评分**：显式提取并匹配查询与候选图像的属性（颜色、类别、材质等），弥补纯文本描述的视觉细节丢失，可嵌入商品搜索排序的relevance score计算中。

  - **LLM重排序**：对粗排Top-K结果，利用LLM验证“修改文本”是否被满足（如“改成黑色”），提升语义一致性；可迁移至电商对话式搜索、多模态交互中的精排阶段。

  - **零样本能力**：整个流程不依赖CIR标注数据，开箱即用，适合冷启动或快速迭代场景；可快速验证“参考图+修改文本”这种查询形式在导购、搭配推荐中的效果。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：组合图像检索（CIR）要求根据参考图像和修改文本检索目标图像，传统方法依赖视觉编码器，成本高、跨域难。视觉无关范式（将图像作文本表示）在标准检索上有效，但在CIR中因文本描述丢失视觉细节而挑战大。

**方法关键点**：
1. **属性增强混合评分**：自动从参考图和候选图的文本描述中提取结构化属性（如颜色、对象类别），计算属性匹配分数，并与基于嵌入的文本相似度分数加权融合，补偿视觉细节损失。
2. **LLM重排序**：对初始检索的Top-K候选，将参考图描述、修改文本和候选描述拼接成提示，让LLM判断修改是否被满足，以此重排结果，强化语义一致性。

**关键结果**：
- 在CIRR数据集上，零样本R@1达44.04%，显著超过先前最佳方法（+8.79%）。
- 在FashionIQ上，观察到语义推理与细粒度视觉匹配的权衡：属性增强有利于细粒度匹配，LLM重排有利于语义推理。
- 消融实验证实两个模块均稳定带来增益。
