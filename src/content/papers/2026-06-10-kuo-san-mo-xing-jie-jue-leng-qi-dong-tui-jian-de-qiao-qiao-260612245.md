---
title: 'DiffCold: A Diffusion-based Generative Model for Cold-Start Item Recommendation'
title_zh: 扩散模型解决冷启动推荐的跷跷板困境
authors:
- Kangning Zhang
- Yingjie Qin
- Weinan Zhang
- Yong Yu
- Jianghao Lin
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
arxiv_id: '2606.12245'
url: https://arxiv.org/abs/2606.12245
pdf_url: https://arxiv.org/pdf/2606.12245
published: '2026-06-10'
collected: '2026-06-11'
category: RecSys
direction: 冷启动物品推荐 · 扩散模型生成表示
tags:
- Cold-Start
- Diffusion Models
- Recommendation
- Representation Alignment
- Retrieval-enhanced Aggregator
- Seesaw Dilemma
one_liner: 提出DiffCold扩散框架，用检索增强聚合与模拟对齐统一温冷表示，同时提升冷热物品性能
practical_value: '- 扩散模型用于物品嵌入生成：用内容特征作为条件引导逆扩散过程，在温物品上训练，对冷物品生成与温物品分布一致的嵌入，电商可直接移植到新品冷启动，避免跷跷板困境。

  - 检索增强的起点初始化：对冷物品，基于内容相似度检索top-k温物品，聚合其嵌入作为扩散起点，远优于纯噪声，保留个性化信息，工程实现简单，适合大规模线上推理。

  - 模拟表示对齐训练技巧：训练时用温物品的内容和聚合起点模拟冷生成过程，并通过对比学习对齐到真实温表示，这种“模拟冷启动”的对齐策略可推广到其他生成式表示学习场景。

  - 轻量级扩散设计：步数T=20、线性调度即可达最优，时间开销与普通模型持平，证明扩散模型在推荐系统中能够兼顾效果与效率，可低成本部署。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
冷启动物品推荐长期面临“跷跷板困境”：提升冷物品效果必然以牺牲温物品性能为代价，反之亦然。本文指出根源在于温冷物品的表示分布存在本质差异——温物品由交互信号学习，形成复杂“行为流形”；冷物品仅依赖内容特征，构成“语义流形”。现有方法（Dropout、生成式、对齐式）强制映射不同分布，导致模型在二者间失衡。

## 方法关键点
- **扩散重建框架**：在温物品嵌入上执行正向加噪与逆向去噪，以内容特征为条件，学习从噪声中恢复行为嵌入，建立语义空间到行为空间的柔性桥接。推理时对冷物品由条件扩散生成嵌入。
- **检索增强聚合器**：对冷物品依据内容相似度检索top-K温物品，聚合其嵌入作为扩散推理的起点，替代纯高斯噪声，避免丢失个性化信息。
- **模拟表示对齐**：训练期间用温物品的内容与聚合起点模拟冷生成过程，将模拟表示与真实温表示经InfoNCE对比对齐，强制分布一致性。
- **多任务训练**：联合优化扩散重构损失、BPR冷推荐损失、模拟对齐损失以及温物品增强损失（BPR温+对比），防止温表示退化。

## 关键结果
在Movielens、Citeulike、Xing三数据集、MF/LightGCN/SimGCL三个骨架上，DiffCold全面超越DropoutNet、Heater、GAR、ALDI等基线。以MF为例，Movielens上整体Recall@20提升15.2%，冷物品Recall@20提升9.65%，温物品提升8.68%，首次实现冷热同步增长。分布度量（类内余弦相似度、Wasserstein距离、MMD）显示DiffCold生成的嵌入与温物品分布最一致，可视化也证实冷温表示充分混合。

**最值得记住的一句话**：扩散模型通过学习温物品的流形结构并用内容条件重建，能自然解耦温物品保真度与冷物品生成，为冷启动推荐开辟了新的范式。
