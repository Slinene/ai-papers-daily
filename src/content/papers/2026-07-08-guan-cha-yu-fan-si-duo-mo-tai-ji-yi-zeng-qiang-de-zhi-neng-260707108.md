---
title: 'Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for
  Recommendation'
title_zh: 观察与反思：多模态记忆增强的智能体协同推荐
authors:
- Hao Cong
- Huizu Lin
- Zihan Wang
- Chengkai Huang
- Quan Z. Sheng
- Lina Yao
affiliations:
- Tsinghua University
- University of Science and Technology of China
- Peking University
- The University of New South Wales
- Macquarie University
arxiv_id: '2607.07108'
url: https://arxiv.org/abs/2607.07108
pdf_url: https://arxiv.org/pdf/2607.07108
published: '2026-07-08'
collected: '2026-07-09'
category: RecSys
direction: 多模态记忆增强的智能体协同推荐
tags:
- Multimodal Recommendation
- LLM Agent
- Memory Evolution
- Reciprocal Rank Fusion
- Attribute-Guided Reflection
- Collaborative Agents
one_liner: 提出双轨多模态记忆增强智能体协同框架，融合推理与稠密匹配，在视觉密集型推荐上大幅领先
practical_value: '- **双轨解耦推荐**：将 LLM agent 的推理排序与多模态稠密匹配分为两个独立 track，通过加权 RRF 融合。电商推荐系统中，可借鉴将基于
  agent 的可解释推理结果与基于视觉/文本的稠密检索结果进行加权融合，兼顾可解释性与精度。

  - **属性引导的记忆演化**：预定义语义属性空间，利用 LLM 抽取关键属性来指导记忆的强化或反思，有效减少噪声和偏好漂移。在用户画像管理模块，可以设计类似机制，用结构化属性来控制画像更新，避免自由反思带来的冗余。

  - **多模态记忆初始化**：从商品图片生成视觉描述并与标题融合，构建多模态 item memory。可直接用于视觉敏感场景（时尚、电子产品）的 item 表征，或为多模态检索增强生成提供素材。

  - **推理与匹配的记忆分离**：推理 track 保留压缩后的结构化记忆，匹配 track 保留原始交互叙述和图片用于稠密检索，既保持 agent 推理效率，又不丢失细粒度多模态信号。可迁移到需要实时更新用户向量的召回-排序联合设计。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有 LLM 驱动的 agent 推荐系统大多仅基于文本线索，忽略商品图片等视觉证据；记忆更新粗粒度，容易引入噪声和偏好漂移。尤其在服饰、电子产品等视觉敏感领域，文本描述无法完整捕捉样式、外观等关键属性。由此提出了双轨多模态记忆增强的智能体协同框架（MMEACR），整合视觉证据与结构化反思，提升推荐精准度与可解释性。

**方法关键点**：
- **双轨设计**：推理轨利用 User / Item Memory Agents，通过 LLM 比较候选项并生成推理，基于预定义属性空间提取结构化的偏好信号，根据预测正确与否执行属性引导的强化或反思，更新记忆；匹配轨使用多模态嵌入模型（GME）编码原始交互叙述和商品图片，保留细粒度跨模态信号，通过余弦相似度排序。
- **属性引导记忆演化**：从语义属性集合中抽取关键属性，约束记忆更新方向，减少自由反思带来的噪声，抑制偏好漂移。
- **加权 RRF 融合**：将推理轨和匹配轨的排序结果通过加权 Reciprocal Rank Fusion 结合，平衡可解释推理与稠密跨模态相似性。
- **推理加速**：推理仅需单次 LLM 调用，比 AgentCF 快 6-16%，适合实际部署。

**关键实验**：在 Amazon 的 CD、手机、服饰三个域上评估，对比 Pop、BM25、SASRec、LLMRank、AgentCF、CoTAgent 等强基线。**最显著结果**：服饰域上，N@1 提升 45.45%，MRR 提升 27.14%；手机域上 N@5 提升 21.26%。消融实验表明，移除属性引导和反思机制会导致性能明显下降。**核心洞察**：属性引导的反思机制让记忆更稳定，双轨融合让推理与感知互补。
