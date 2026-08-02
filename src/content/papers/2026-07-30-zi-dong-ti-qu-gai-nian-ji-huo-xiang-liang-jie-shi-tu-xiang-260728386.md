---
title: Explaining Image Similarity with Automatically Extracted Concept Activation
  Vectors
title_zh: 自动提取概念激活向量解释图像相似性
authors:
- Isaac Roberts
- Petra Bevandic
- Alexander Schulz
- Barbara Hammer
affiliations:
- Bielefeld University - Faculty of Technology
- University of Zagreb - Faculty of Electrical Engineering and Computing
arxiv_id: '2607.28386'
url: https://arxiv.org/abs/2607.28386
pdf_url: https://arxiv.org/pdf/2607.28386
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 可解释AI · 概念向量
tags:
- Concept Activation Vectors
- Sparse Autoencoders
- Explainable AI
- Image Similarity
- Example-based Explanation
one_liner: 用稀疏自编码器自动发现概念方向，通过嵌入扰动解释图像相似度的全局因素
practical_value: '- **商品图像相似性解释**：在电商图像搜索或推荐中，可利用本方法自动发现颜色、纹理、形状等概念，解释为何两个商品图像被判定相似，增强用户信任。

  - **多模态对齐的全局解释**：该方法模型无关、度量无关，可直接嵌入现有视觉-文本对齐流程，为召回的图文对提供概念重要性排序与归因热力图。

  - **范例检索复用**：借鉴“Exemplar Retrieval”的思路，从商品库中挖掘与当前 pair 具有相似解释概念的案例，辅助人工审核或生成自然语言解释。

  - **数据分布保真扰动**：潜空间概念扰动比像素空间篡改更符合真实数据分布，可用于推荐系统的反事实解释生成，避免产生不自然的反事实样例。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：图像相似性在图像检索、人脸识别、时尚兼容等应用中至关重要，但现有方法仅提供局部梯度归因，缺乏对相似性判断的全局语义解释，如不清楚“纹理 vs. 形状”哪个主导了相似度。

**方法关键点**：提出模型和度量无关的框架，首先用稀疏自编码器（SAE）在预训练模型的嵌入空间中自动提取概念激活向量（CAVs）；对图像对，沿发现的概念方向扰动嵌入，测量余弦相似度等函数的变化，得到概念重要性分数，并生成概念归因图定位关键区域。进一步扩展到簇级相似性解释（多个图像的共同相似驱动因素）和范例检索（查找具有相似解释概念的图像）。

**关键结果**：在多个数据集和模型上，潜空间概念扰动比像素空间方法更忠实于数据分布（保真度显著更高）；概念重要性能够线性近似真实相似度分数；定性的归因图和检索结果验证了方法的解释有效性。
