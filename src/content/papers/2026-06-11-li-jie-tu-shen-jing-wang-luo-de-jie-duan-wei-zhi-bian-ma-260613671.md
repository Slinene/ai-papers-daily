---
title: Understanding Truncated Positional Encodings for Graph Neural Networks
title_zh: 理解图神经网络的截断位置编码
authors:
- James Flora
- Mitchell Black
- Weng-Keen Wong
- Amir Nayyeri
affiliations:
- Oregon State University
- University of California San Diego
arxiv_id: '2606.13671'
url: https://arxiv.org/abs/2606.13671
pdf_url: https://arxiv.org/pdf/2606.13671
published: '2026-06-11'
collected: '2026-06-14'
category: Other
direction: 图神经网络位置编码理论分析
tags:
- graph neural networks
- positional encodings
- truncation
- expressive power
- WL test
one_liner: 揭示截断位置编码的表达能力差异，指出混合使用优于单一类型
practical_value: '- 推荐系统构图若采用截断谱位置编码（如前k个拉普拉斯特征向量），需注意其表达能力不超过1-WL，建议同时引入walk-based位置编码（如邻接矩阵幂）以增强节点区分能力。

  - 混合不同类型的截断位置编码在实验中表现更好，类似多模态特征融合，可在异构图或用户-物品交互图中组合多种廉价PE（如随机游走特征+低阶谱特征）来补偿各自的表达力损失。

  - k-harmonic distances 作为新型谱PE，提供了不同于传统特征向量的全局信息，可尝试在商品相似图或会话图中添加该特征，捕捉局部与全局结构的平衡。

  - 资源受限场景下必须截断时，避免仅单一截断类型；可设计轻量级混合PE模块，通过可学习权重或门控机制自适应融合，在不显著增加复杂度的前提下提升图模型性能。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：图神经网络中的位置编码（PE）能提升表达力，理论上完整的谱PE（如拉普拉斯特征空间）与基于游走的PE（如邻接矩阵多项式）在表达力上等价，均介于1-WL和3-WL测试之间。然而完整PE计算和存储需O(n³)复杂度，实际中普遍使用截断版本（如前k个特征或k次幂），但截断后的理论性质未知。

**方法**：作者首次系统研究了截断PE的表达能力。理论上证明了截断后不同PE族的表达力存在根本差异：截断的谱PE不再强于1-WL测试，而基于游走的PE依然保持一定优势。还引入一种新的谱PE族——k-harmonic距离，用以揭示即使密切相关的截断PE之间也存在表达力差异。

**结果**：在真实数据集上的实验表明，混合多种截断PE总是优于使用任何单一PE族，单一截断PE可能无法充分捕获图结构信息。这为实践中如何选择和组合PE提供了理论依据。
