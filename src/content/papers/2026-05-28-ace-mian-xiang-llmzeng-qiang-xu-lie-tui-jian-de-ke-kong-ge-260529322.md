---
title: 'ACE: Anisotropy-Controllable Embedding for LLM-enhanced Sequential Recommendation'
title_zh: ACE：面向LLM增强序列推荐的可控各向异性嵌入
authors:
- Dongcheol Lee
- Hye-young Kim
- Jongwuk Lee
affiliations:
- Sungkyunkwan University
arxiv_id: '2605.29322'
url: https://arxiv.org/abs/2605.29322
pdf_url: https://arxiv.org/pdf/2605.29322
published: '2026-05-28'
collected: '2026-05-30'
category: RecSys
direction: 序列推荐 · LLM嵌入初始化 · 各向异性控制
tags:
- Embedding Anisotropy
- Sequential Recommendation
- LLM-as-Extractor
- Linear Autoencoder
- Whitening
- Spectral Shrinkage
one_liner: 用线性自编码器连续控制LLM嵌入的各向异性程度，缓解几何不平衡并保留语义层次，提升序列推荐效果。
practical_value: '- **LLM物品嵌⼊预处理的标准化步骤**：在电商/推荐业务中，如果使用大模型（如text-embedding-3-large）生成商品编码，可直接套用ACE进行后处理：对嵌入矩阵做SVD，用收缩函数
  $g_\lambda(\sigma)=\sqrt{\sigma^2/(\sigma^2+\lambda)}$ 调整奇异值，再降维至目标维度。该操作是闭式解，计算开销小，可无缝集成到现有训练流程中。

  - **平衡语义保留与各向同性**：完全的白化（Whitening）会破坏语义主次，导致效果不稳定。ACE通过调节 $\lambda$ 提供连续控制，让从业者能在语义保真度和几何均匀性之间折中，避免因过度白化而损失重要语义方向。

  - **架构无关的嵌入初始化**：ACE对不同SR骨架（SASRec、GRU4Rec、BERT4Rec）均有效，说明该方法可作为通用初始化策略，应用到召回/排序模型的特征层，尤其在冷启动或语义稀疏场景下表现突出。

  - **超参 $\lambda$ 的选择经验**：实验表明中等 $\lambda$ （如10²量级）普遍最佳，可根据验证集Recall@K快速搜索；同时配合缩放因子
  $\gamma$ 控制嵌入范数，避免过小或过大影响模型收敛。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM增强的序列推荐通常将预训练语言模型生成的物品嵌入直接初始化SR模型，但这些嵌入存在严重的各向异性（anisotropy），即向量集中在少数主导方向，导致表征多样性和可分离性下降，阻碍下游微调时协作信号的适应。现有方案如PCA或白化（whitening）要么控制力弱，要么强制各向同性而抹平语义层次，破坏原有语义结构。本文旨在找到一种既能削弱各向异性又能保留语义主次顺序的初始化方式。

**方法关键点**  
- 提出Anisotropy-Controllable Embedding (ACE)，核心是一个线性自编码器（LAE），其目标函数包含重构损失（保留语义方向）和L2正则项（控制光谱平整度）。  
- 利用SVD分解将LAE闭式解转化为对嵌入矩阵奇异值的非线性收缩：$g_{\lambda}(S) = \sqrt{S^2 / (S^2 + \lambda I)}$，衰减过大奇异值，平滑特征分布。  
- 调整后的嵌入通过保留top-k奇异向量并乘以缩放因子$\gamma$，最终得到几何均衡的低维初始化矩阵，可直接送入SASRec等SR骨架。  
- 超参$\lambda$实现从完全各向同性（$\lambda=0$）到原始各向异性（$\lambda\to\infty$）的连续控制，无需重新训练LLM。

**关键实验结果**  
- 数据集：Amazon Beauty/Toys、Yelp、ML-20M；LLM编码器默认使用text-embedding-3-large。  
- 对比基线：LLM2X（PCA）、WhitenRec+、LLMEmb、AlphaRec、AlphaFuse。  
- 性能：在SASRec上，ACE在Beauty的Recall@20达12.88%，相对次优提升2.0%；在GRU4Rec和BERT4Rec上，Recall@20最高提升12.4%，NDCG@20最高提升11.8%。  
- 鲁棒性：在F2LLM-4B、Qwen3-8B、KaLM-12B三种编码器下均保持最优。  
- 超参分析：$\lambda$过小（约0）等同于各向同性白化，性能下降；过大不改变各向异性；中等值（如500）能最佳平衡，验证了连续控制的有效性。

**值得记住的一句话**  
“ACE通过线性自编码器的光谱收缩，将完全白化推广为一种可微调的、语义层次保持的各向异性控制手段。”
