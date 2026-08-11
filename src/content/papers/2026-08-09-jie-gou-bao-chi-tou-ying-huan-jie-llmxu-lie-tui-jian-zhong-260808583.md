---
title: Structure-Preserving Projection for Mitigating Modality Bias in LLM-Based Sequential
  Recommendation
title_zh: 结构保持投影缓解LLM序列推荐中的模态偏差
authors:
- Tzu-Wei Chiu
- Song-Duo Ma
- Hsin-Yu Lin
- Pu-Jen Cheng
affiliations:
- National Taiwan University
arxiv_id: '2608.08583'
url: https://arxiv.org/abs/2608.08583
pdf_url: https://arxiv.org/pdf/2608.08583
published: '2026-08-09'
collected: '2026-08-11'
category: RecSys
direction: LLM推荐 · 模态偏差缓解
tags:
- Sequential Recommendation
- LLM
- Modality Bias
- Contrastive Learning
- Structure Preservation
- Collaborative Embedding
one_liner: 通过余弦相似度保持与序列感知对比损失，迫使投影后的协同嵌入保留原始结构，抵消LLM对文本的过度依赖
practical_value: '- **Embedding Shuffle诊断法**：冻结标题、随机打乱协同嵌入，观察性能下降幅度可直接衡量LLM对协同信号的依赖程度，适合用于评估自身融合模块的有效性。

  - **结构保持损失可作为即插即用的约束**：在MLP投影器后添加成对余弦相似度保持损失（MSE），或序列感知对比损失（正负样本区分），无需改动LLM结构，实现简单。

  - **两段训练策略**：先用纯结构保持损失预训练投影器，再联合LLM微调，可避免协同结构在语言模型训练初期就被破坏，适合在已有推荐pipeline中快速植入。

  - **课程式组合损失**：先用余弦相似度保持建立稳定拓扑，再渐进切换至对比损失，最大化几何保真与任务判别力的平衡，对需要同时保持物品泛化语义和序列偏好的场景（如电商多兴趣建模）有参考价值。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
在LLM驱动的序列推荐中，主流做法是将传统协同模型（如SASRec）产生的物品嵌入投影至LLM空间，与标题等文本信号共同输入。然而，论文发现这种直接投影会引入**模态偏差**：LLM过分依赖文本信号，几乎忽视协同嵌入中蕴含的行为模式。通过embedding shuffle诊断实验——对调物品的协同嵌入而保持标题不变，模型HR@1几乎无变化——证明投影嵌入退化为通用软提示，失去了真实的协同意义。该问题在视觉-语言模型中也被称为“模态偏置”，严重限制LLM推荐对物品关系的利用。

**方法**
论文提出**结构保持投影**，在训练投影器时显式保留原始协同空间的关系结构。
- 架构：冻结的SASRec提供协同嵌入e，一个MLP将其映射为z，与标题embedding拼接后输入LLaMA2-7B，整体用LoRA微调。
- 两个结构保持损失：
  1. **余弦相似度保持损失**：强制投影空间中物品对的余弦相似度与原始空间一致（MSE），保留全局几何结构。
  2. **序列感知对比损失**：对每个序列，让序列投影表示与正例（下一实物）相似，与随机负例远离，保留序列判别性。
- 训练分两阶段：先只用结构损失预训练MLP，再联合LLM用语言建模损失+结构损失微调。最后还尝试课程式组合：早期侧重余弦保持，后期渐变为对比保持。

**关键结果**
- 在LastFM（HR@1）与MovieLens上，Contrastive-LM对比最强基线LLaRA分别提升约8.4%和5.3%（SASRec骨架）。
- Embedding shuffle实验证明，与基线不同，结构保持方法在协同嵌入被乱序后出现大幅性能下降，表明模型真正依赖了协作信息。
- 几何保持分析显示，Cosine-LM的Kendall’s Tau高达0.78，但Contrastive-LM的推荐精度更高，说明过分强调全局几何可能牺牲任务判别力。
- 组合损失（余弦→对比）进一步在两个数据集上超越单一损失，证明两种结构保持具有互补性。
