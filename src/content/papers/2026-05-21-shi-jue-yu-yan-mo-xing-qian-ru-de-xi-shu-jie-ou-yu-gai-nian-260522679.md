---
title: 'Conceptualizing Embeddings: Sparse Disentanglement for Vision-Language Models'
title_zh: 视觉-语言模型嵌入的稀疏解耦与概念解释
authors:
- Piotr Kubaty
- Patryk Marszałek
- Łukasz Struski
- Adam Wróbel
- Jacek Tabor
- Marek Śmieja
affiliations:
- Jagiellonian University, Kraków, Poland
- Warsaw University of Technology, Warsaw, Poland
arxiv_id: '2605.22679'
url: https://arxiv.org/abs/2605.22679
pdf_url: https://arxiv.org/pdf/2605.22679
published: '2026-05-21'
collected: '2026-05-24'
category: Multimodal
direction: 多模态嵌入的可解释性
tags:
- Sparse Disentanglement
- Vision-Language Models
- Interpretability
- Post-hoc
- CLIP
- SAE
one_liner: 提出CEDAR，通过可逆旋转+top-k稀疏瓶颈，不扩大维度实现多模态嵌入的稀疏解耦与概念对齐
practical_value: '- 主要学术贡献，针对视觉-语言模型可解释性，业务可直接迁移的工程方法较少。

  - 可借鉴旋转+top-k稀疏瓶颈的思路，对电商多模态商品向量（如CLIP嵌入）做后处理，将语义属性轴对齐，便于运营理解与人工调控，例如将某维度对应“颜色”或“风格”概念。

  - 方法保持维度不变、可逆，避免SAE的冗余与几何失真，适合线上对延迟敏感的场景，可给已部署模型附加可解释性。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：多模态模型（如CLIP、BLIP）的嵌入内部语义不透明，现有解释方法依赖稀疏自编码器（SAE）扩展维度，破坏原始几何结构并引入冗余。需要一种不增加维度的后处理方式，揭示预训练嵌入的组合语义结构。

**方法**：提出CEDAR（Conceptual Embedding Disentanglement via Adaptive Rotation），学习一个可逆的正交变换矩阵，配合top-k稀疏瓶颈，将原始嵌入旋转到新的轴对齐坐标系，使少量维度承载大部分语义信息。变换保持嵌入空间基本几何性质，且可逆，避免信息丢失。对CLIP类模型，每个轴可直接用文本概念类比；对生成式BLIP，则可解码为自然语言描述。

**关键结果**：在重建误差-稀疏性权衡上达到与SAE相当甚至更优的水平；生成的解释与人类感知对齐度更高，概念更聚焦。定性实验展示了清晰的语义轴，如“户外”“食物”等概念可被独立调控。结果表明，视觉-语言表征的“纠缠”可通过适当的基底变换解决，无需过度完备字典。
