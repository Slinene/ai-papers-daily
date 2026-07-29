---
title: 'TopoGR: Revealing and Preserving Latent Structure of Semantic ID in Generative
  Recommendation'
title_zh: TopoGR：保留语义ID拓扑结构的生成式推荐框架
authors:
- Ziyu Zheng
- Zhengshun Du
- Yaming Yang
- Bin Tong
- Guan Wang
- Meng Yan
- Ziyu Guan
- Wei Zhao
affiliations:
- Xidian University
- Alibaba
- University of Science and Technology of China
arxiv_id: '2607.25216'
url: https://arxiv.org/abs/2607.25216
pdf_url: https://arxiv.org/pdf/2607.25216
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · Binary Semantic ID 拓扑保持
tags:
- Semantic ID
- Generative Recommendation
- Hamming Topology
- Bit-decomposable Quantization
- Structural Mismatch
one_liner: 提出Bit-decomposable Semantic ID暴露汉明拓扑，在输入、监督、推理三阶段利用该结构，解决生成式推荐中tokenizer与generator的结构性不匹配
practical_value: '- **二进制分解 Semantic ID**：将物品内容（标题、描述等）经预训练模型得到向量，采用位分解量化（LFQ+可学习位基重建）生成二进制编码作为物品的生成式ID，保留汉明距离表示的语义邻近度，使不同但相近的物品可通过比特重叠关联，优于纯整数ID匹配。

  - **训练时用汉明软目标代替 one-hot**：根据码字间的汉明距离构造 soft target，让模型对近邻码的惩罚更小，有效提升冷启动物品的推荐质量，可迁移至电商新品冷启动场景。

  - **推理时汉明一致性重排**：利用预测分布构建软二进制原型，计算候选物品二进制 SID 与原型的一致性分数，修正并行生成得分，只需在小候选池操作，无额外解码延迟，适合在线推理。

  - **工程实现注意点**：保持 item 级序列输入（不展平 token 序列）以控制 self-attention 复杂度；平衡比特数 r 与 SID 长度
  M，确保无码本崩溃；可结合并行预测进一步加速，TopoGR 的整体设计可平滑嵌入现有生成式推荐管线。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机

生成式推荐通常将物品量化为离散语义ID（SID）序列，并由生成模型自回归预测下一物品的SID。现有方法在tokenization阶段能学到具备拓扑结构的码本（相近语义分散到相邻码字），但在generation阶段，SID被视作独立的类别嵌入，导致语义相近但ID不同的物品被完全割裂，无法利用码本中潜藏的结构信息。这种结构化不匹配限制了稀疏物品和冷启动物品的推荐效果。

### 方法关键点

- **Bit-decomposable Quantizer（BDQ）**：将物品语义表示映射为 \(M \times r\) 的潜在矩阵，对每行做LFQ量化得到 \(r\)-bit 二进制码（Binary SID），并通过一组可学习基向量进行位组合重建，迫使汉明距离与表示相似性对齐。二进制码可无损转换为标准整数SID。
- **二进制特征输入**：将历史物品的 Binary SID 展平后直接作为序列模型输入，取代传统的SID嵌入查表，使模型在输入层即可感知物品间的汉明距离。
- **并行SID预测**：采用多token并行预测头，同时预测下一物品所有 \(M\) 个SID位置，避免自回归解码的串行开销。
- **汉明软目标**：基于码字间的汉明距离构建soft target分布，用KL散度监督，使模型对汉明近邻码施加更小的惩罚，保留拓扑信息。
- **汉明一致性重排**：推理时根据预测分布计算期望二进制向量（软原型），与候选物品的Binary SID的点积作为一致性得分，修正原始对数概率，实现轻量重排。

### 关键结果

在Amazon四数据集（Beauty、Sports、Toys、CDs）上，TopoGR全面超越TIGER、RPG、MHL、DiffGRM等强基线。典型提升：Toys数据集NDCG@5达0.0497，相对RPG提升约24%；Sports数据集NDCG@5提升约19%。冷启动物品分组分析显示增益更明显。控制实验表明，在相同整数SID重叠下，汉明近距离组的NDCG@10比远距离组高出2～6倍，直接验证二进制拓捕获了超越精确ID匹配的物品关系。

> **核心结论**：把语义ID从独立类别符号升级为具备汉明几何的二进制编码，并将该拓扑显式注入生成过程的输入、监督和推理三阶段，是提升生成式推荐泛化能力的有效路径。
