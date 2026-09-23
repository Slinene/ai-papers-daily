---
title: 'Ovis-Embedding: Pushing the Frontiers of Universal Omni-Modal Embeddings'
title_zh: Ovis-Embedding：全模态统一嵌入模型
authors:
- Embedding Team
affiliations:
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2609.25165'
url: https://arxiv.org/abs/2609.25165
pdf_url: https://arxiv.org/pdf/2609.25165
published: '2026-09-20'
collected: '2026-09-23'
category: Multimodal
direction: 多模态统一 Embedding 训练
tags:
- Omni-modal Embedding
- Contrastive Learning
- Focal Loss
- Embedding Distillation
- Low-rank Decomposition
- Multimodal Retrieval
one_liner: 基于Qwen-omni的原生多模态统一embedding，在多个检索基准上达到SOTA
practical_value: '- **复用大规模多模态LLM作为embedding backbone**：直接对Qwen-omni做对比学习微调，而不是从零搭多塔，能以较低成本获得高质量统一表示。电商场景可类似地用商品图文视频数据微调多模态LLM，得到商品统一embedding用于跨模态召回。

  - **同源采样构造任务一致batch**：按数据来源/模态分组采样，让in-batch negatives更相关、更有信息量。在推荐/搜索的多行为、多内容源训练中，可以按用户行为类型或item类目分组，提升对比学习效率。

  - **focal loss强调难样本**：对困难负例加大权重，适合处理点击/转化数据中的长尾和难区分样本，尤其适用于召回模型中难负例挖掘。

  - **低秩特征分解灵活控制维度**：一套模型可输出不同维度embedding，低维用于快速召回、高维用于精排，减少存储和计算成本，类似推荐系统里的多级向量索引设计。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有embedding模型多为各模态单独tower，跨模态检索碎片化，难以统一表示文本、图像、视频、音频。

**方法关键点**：
1. **原生全模态初始化**：采用预训练Qwen-omni作为共享backbone，通过低秩初始化进行对比学习适配，而不是拼接独立模态塔。
2. **数据为中心的训练**：构建覆盖文本、图像、视频、音频及交错多模态数据的高质量语料；提出同源采样（homogeneous-source sampling）形成任务一致的batch，增强in-batch negatives的信息量。
3. **训练与推理优化**：使用focal loss强调困难样本；采用相似度Embedding Distillation从互补专家模型迁移细粒度相似结构；推理时用低秩特征分解获得紧凑、维度灵活的embedding，性能损失极小。

**关键结果**：Ovis-Embedding家族在MMEB-v3、MMEB-v2、MVEB、MAEB、RTEB五个基准上达到SOTA。例如Ovis-Embedding-Omni-3B在MMEB-v3 Omni-modal Retrieval上达到77.5，Ovis-Embedding-VL-9B在MMEB-v2 Vision-Language Retrieval上达到84.0，显著超越同规模模型，证明统一全模态训练能突破模态割裂。
