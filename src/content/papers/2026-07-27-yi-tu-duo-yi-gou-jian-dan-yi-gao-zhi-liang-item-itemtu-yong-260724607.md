---
title: 'One Graph, Multiple Gains: Single High-Quality Item-Item Graph for Multimodal
  Recommendation'
title_zh: 一图多益：构建单一高质量item-item图用于多模态推荐
authors:
- Jinfeng Xu
- Zheyu Chen
- Ziyue Peng
- Shuo Yang
- Jinze Li
- Zewei Liu
- Shujie Li
- Yipeng Du
- Edith C. H. Ngai
affiliations:
- The University of Hong Kong
- The Hong Kong Polytechnic University
- The Hong Kong University of Science and Technology
arxiv_id: '2607.24607'
url: https://arxiv.org/abs/2607.24607
pdf_url: https://arxiv.org/pdf/2607.24607
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 多模态推荐 · item-item图复用
tags:
- Multimodal Recommendation
- Item-Item Graph
- Graph Neural Networks
- Triadic Closure
- BPR Augmentation
- Cold-start
one_liner: 预处理构建高质量item-item图，在表征增强、交互图增强和优化增强三阶段复用以全面提升推荐性能
practical_value: '- **图构建方法可迁移**：融合语义和共现信号，并通过三元闭合的NCER重加权边，能显著降噪。直接用于电商商品相似图构建，提升GNN召回或排序特征的质量，尤其适合多模态商品库。

  - **残差门控机制RIG**：自适应控制每个物品从近邻吸收多少信息，避免噪声平滑。可嵌入任何Graph SAE或注意力层，作为表征增强的插件，缓解过度平滑。

  - **交互图增强解决冷启动**：通过高置信度语义邻居创建虚拟user-item边，间接扩展交互图，对冷启动物品和长尾商品有明显增益。实现轻量，只需在线查表，适合大规模推荐系统。

  - **优化增强INA**：将正样本的top邻居作为折扣软正样本加入BPR，类似难例挖掘但更稳定。可直接应用于排序训练的目标函数，提升模型对相似商品的区分度，降低假阳性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：现有多模态推荐虽用item-item图，但图构建噪声多且仅用于单一的信息传播，未充分挖掘其潜力。

方法：提出IIMRec，在预处理阶段构建**单一高质量item-item图**，融合语义相似与共现信号，并通过**Neighborhood Consistency Edge Reweighting (NCER)** 基于三元闭合原理强化结构可靠边、抑制虚假边。该图在三个环节系统复用：
- **表征增强**：Item-item传播加入**残差II门(RIG)**，自适应控制各物品对语义邻域信息的吸收程度，防止噪声引入。
- **交互图增强**：**内容引导的UI图扩展**，利用高置信度语义邻居为冷启动物品创建虚拟user-item边，丰富交互信号。
- **优化增强**：**II邻居BPR增强(INA)**，把正样本物品的top邻居作为折扣软正样本，改进排序损失。

理论分析：NCER降低谱噪信比，RIG收敛到非退化门控态，INA得到更紧泛化界。实验在四个数据集上一致超越SOTA，速度更快、GPU占用更少，在冷启动和稀疏交互场景下优势尤为突出。
