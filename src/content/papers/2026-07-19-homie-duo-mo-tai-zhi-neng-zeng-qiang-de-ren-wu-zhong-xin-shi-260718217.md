---
title: 'HOMIE: Human-object Centric Video Personalization via Multimodal Intelligent
  Enchancement'
title_zh: HOMIE：多模态智能增强的人-物中心视频个性化
authors:
- Yiyang Cai
- Nan Chen
- Rongchang Xie
- Junwen Pan
- Chunyang Jiang
- Cheng Chen
- Wen Zhou
- Zhenbang Sun
- Wei Xue
- Wenhan Luo
affiliations:
- Hong Kong University of Science and Technology
arxiv_id: '2607.18217'
url: https://arxiv.org/abs/2607.18217
pdf_url: https://arxiv.org/pdf/2607.18217
published: '2026-07-19'
collected: '2026-07-21'
category: Multimodal
direction: 人-物交互视频个性化生成
tags:
- Video Generation
- Personalization
- Multimodal
- MLLM
- Subject-driven
- Attention Alignment
one_liner: 统一处理 inter/intra-subject 的视频个性化框架，通过 MLLM 全局引导注意力提升人-物交互保真度
practical_value: '- 视频个性化在电商中可用于虚拟试穿或商品展示，该工作对**人-物交互**的可控生成有直接价值，尤其保持主体身份的同时实现合理交互。

  - **MLLM 融入自注意力**的全局多模态引导方式可借鉴：在推荐系统中融合多模态特征时，可尝试在注意力层注入预训练多模态大模型的高层语义特征，增强物品与用户行为的对齐。

  - **模态引用嵌入**区分不同来源特征（如图像、文本、MLLM 特征），可迁移至多模态用户建模，显式编码不同类型行为序列的模态差异，提升特征融合质量。

  - 对**抽象概念**（如品牌 logo）的自动关联方法，可用于商品属性与视觉风格的隐式绑定，增强生成式推荐中 semantic ID 的视觉化表达。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有主体驱动视频生成在人与物体交互场景下难以同时保证**主体保真度**与**交互模式准确性**，尤其当物体为抽象概念（如 logo）时；此外，缺乏对**intra-subject 参考**（如 OCR 图、多视图）的潜在对应关系的理解。  
**方法**：提出 **HOMIE**，统一处理 inter-subject（多主体交互）和 intra-subject（同主体多参考）两种设定。核心创新在于**更优的 MLLM 集成策略**：在自注意力层引入**全局多模态引导**，将 MLLM 提取的跨模态语义特征与 VAE 视觉 token 进行对齐，避免破坏文本编码器的可控性或引入昂贵的重对齐；同时设计**模态引用嵌入**，显式区分 MLLM 特征 token 与 VAE token，并关联 intra-subject 的多张参考图像，增强特征对应。  
**关键结果**：在多种人-物中心视频个性化任务上达到 **SOTA**，显著改善了交互模式合理性与主体细节保真度，并成功扩展到 OCR 地图增强、多视图一致等场景。
