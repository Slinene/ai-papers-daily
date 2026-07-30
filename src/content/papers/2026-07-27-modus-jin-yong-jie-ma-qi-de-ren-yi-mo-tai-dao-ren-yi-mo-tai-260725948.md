---
title: 'MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities'
title_zh: MODUS：仅用解码器的任意模态到任意模态统一建模
authors:
- Mingqiao Ye
- Zhaochong An
- Zhitong Gao
- Xian Liu
- François Fleuret
- Chuan Li
- Amir Zadeh
- Serge Belongie
- Afshin Dehghan
- Jesse Allardice
affiliations:
- EPFL
- Apple
- University of Copenhagen
- CUHK
- University of Geneva
arxiv_id: '2607.25948'
url: https://arxiv.org/abs/2607.25948
pdf_url: https://arxiv.org/pdf/2607.25948
published: '2026-07-27'
collected: '2026-07-30'
category: Multimodal
direction: 解码器仅有 · 任意到任意多模态建模
tags:
- any-to-any
- decoder-only
- multimodal
- autoregressive
- self-verification
- vision-language
one_liner: 提出解码器仅有的任意模态到任意模态统一框架，无需特定头或损失，支持链式生成与自我验证
practical_value: '- **多模态搜推统一表示**：将商品标题、描述、图片、属性等异构模态统一 token 化，用单一解码器模型完成多模态理解与生成，可简化特征工程与模型部署。

  - **跨模态增强与验证**：利用模型生成深度、法线等中间模态，增强商品图像理解；或在生成描述后，用另一模态（如图像）对文本输出进行自我验证，提升生成质量与可信度。

  - **链式生成与多步推理**：通过中间模态链式生成（如文本→草图→商品图），实现复杂创意内容生产，适用于动态广告物料生成、个性化推荐理由可视化等场景。

  - **工程实现轻量化**：取消模态专用头与多任务管道，所有模态共享同一个 Transformer 解码器，降低多模态业务维护成本，便于快速扩展新模态。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 any-to-any 多模态模型普遍采用编码器-解码器或扩散架构，需从零训练且无法利用成熟预训练解码器先验，限制性能与应用灵活性。

**方法**：提出 Modus，纯解码器架构，将任意模态（RGB、深度、法线、边缘、文本、DINOv2 特征等）统一为自回归 token 序列，通过单个 Transformer 解码器实现输入与输出的对称处理。无需模态特定 head、损失函数或任务管线，所有模态平等地作为输入或输出。训练后，模型天然支持链式生成（跨多步模态转换）与自我验证（用生成的另一模态对原输出进行评分）。

**结果**：在多种视觉、视觉-语言基准上，单一 Modus 模型取得与专家模型、多任务基线可比的结果，展示了强大的开箱即用能力。
