---
title: Closing the Indexing-Decoding Gap in Multimodal Generative Retrieval via Prefix
  Retention Optimization
title_zh: 通过前缀保留优化弥合多模态生成检索的索引-解码鸿沟
authors:
- Yufei Chen
- Zihan Wang
- Yubao Tang
- Yukun Zhao
- Maarten de Rijke
- Zhaochun Ren
affiliations:
- Shandong University
- CISPA Helmholtz Center for Information Security
- University of Amsterdam
- Leiden University
arxiv_id: '2606.09241'
url: https://arxiv.org/abs/2606.09241
pdf_url: https://arxiv.org/pdf/2606.09241
published: '2026-06-08'
collected: '2026-06-09'
category: GenRec
direction: 多模态生成式检索 · 前缀保留优化
tags:
- Generative Retrieval
- Prefix Retention
- Multimodal Retrieval
- Residual Quantization
- Beam Search
one_liner: 提出前缀保留优化框架，从排序蒸馏、词汇调度和几何融合三方面提升残差码本在束搜索中的前缀存活率
practical_value: '- **前缀排序蒸馏**：在RQ标识符学习时，引入listwise蒸馏损失，使量化后前缀概率分布与冻结编码器的原始分布对齐，减少索引-解码排名分歧。该方法可直接用于生成式推荐中的Semantic
  ID训练，提升束搜索解码时的目标保留。

  - **词汇表调度**：将残差量化各级codebook大小设计为递增（浅层小、深层大），降低束搜索早期大量非目标前缀的竞争，增大教师边际，提高目标前缀浅层存活率。在电商推荐粗粒度类目上可借鉴，减少不必要的早期剪枝。

  - **几何分数融合**：解码时，用查询与候选codeword的几何相似性（残差距离减少量）增强解码得分，无需重新训练即可改善解码器与量化分布的对齐。适用于线上实时推理，可直接集成到现有生成式检索/推荐系统中。

  - **理论生存界限**：将前缀存活分解为排名散度、教师边际和解码器不匹配三个可控量，提供了一种诊断工具，可迁移到其他RQ-based生成式系统，识别并优化瓶颈。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多模态生成式检索（MGR）将跨模态搜索建模为离散标识符的序列生成，避免了外部向量索引。主流方法使用残差量化（RQ）构建标识符，并通过trie约束的束搜索解码。但发现存在“索引-解码鸿沟”：标识符学习的目标（重构损失、对比损失）未显式保证前缀在解码时的区分性，导致目标前缀在束搜索早期即被剪枝，即使最终重构质量良好。理论证明，两个具有相同优化目标值的不同量化器，一个可以让目标前缀存活，另一个却会被剪枝，说明现有目标无法决定前缀生存。

**方法**
基于生存界限推导，提出了PRO框架，包含三个组件：
1. **前缀排序蒸馏**：在RQ训练时，对每一层前缀用冻结编码器产生的分布作为教师，通过listwise KL散度损失让量化后前缀分布对齐教师，减少排名散度Kₗ。
2. **词汇表调度**：改变传统均匀codebook大小，采用递增调度（先小后大），浅层小词汇降低竞争，增大教师边际mₗ。
3. **几何分数融合**：在束搜索解码时，计算候选codeword加入后重建向量与查询的距离减少量，作为加性偏置项加到解码器log概率中，缓解解码器不匹配εₗ。

**实验**
在9个多模态检索任务（M-BEIR/Flickr30k，覆盖文搜图、图搜文、组合检索）上，PRO一致优于现有MGR基线（GENIUS等），Recall@1平均提升6-9个百分点，将生成式检索与稠密检索的差距缩小40-60%。消融实验证实三者互补，诊断实验验证生存界限中三量级与存活率的单调关系。此外，在Amazon推荐数据集上，将PRO集成到TIGER模型中也带来一致提升，显示泛化性。

**值得记住的一句话**
“即使RQ完全重构质量高，也无法保证束搜索中目标前缀存活；而通过直接调控排名散度、教师边际和解码器不匹配，可以系统性地解决这个索引-解码鸿沟。”
