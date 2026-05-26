---
title: 'GCIB: Graph Contrastive Information Bottleneck for Multi-Behavior Recommendation'
title_zh: GCIB：图对比信息瓶颈用于多行为推荐
authors:
- Likang Wu
- Zihao Chen
- Jianxin Zhang
- Sangqi Zhu
- Yuanyuan Ge
- Haipeng Yang
- Lei Zhang
affiliations:
- Tianjin University
- Anhui University
arxiv_id: '2605.25690'
url: https://arxiv.org/abs/2605.25690
pdf_url: https://arxiv.org/pdf/2605.25690
published: '2026-05-25'
collected: '2026-05-26'
category: RecSys
direction: 多行为推荐 · 图信息瓶颈去噪 · 对比学习语义对齐
tags:
- Multi-Behavior Recommendation
- Graph Information Bottleneck
- Graph Contrastive Learning
- Denoising
- Graph Neural Networks
one_liner: 通过图信息瓶颈去噪辅助行为图结构，并结合跨行为对比学习实现语义对齐，提升稀疏目标行为的推荐精度
practical_value: '- **结构级噪声过滤**：在辅助行为图上直接做边级去噪，而非仅压缩表征。使用目标行为偏好引导的边保留概率（MLP融合user/item
  embedding），通过Gumbel-Softmax实现可微的边丢弃，可借鉴到电商多行为数据清洗，仅保留与购买/加购等目标行为相关的辅助交互。

  - **HSIC正则替代互信息最小化**：由于图结构互信息难以直接优化，采用HSIC衡量去噪前后图节点表征的独立性作为压缩项，计算高效且可微。在推荐系统的特征选择或图去噪场景中，可作为轻量级冗余抑制手段。

  - **跨行为对比对齐**：将去噪后的辅助行为表征与目标行为表征作为正例构建对比损失（InfoNCE），用户侧和物品侧分别计算。这能缓解目标行为稀疏时的监督信号不足，尤其适合交易型电商场景中购买行为少、点击/浏览行为多的情况。

  - **分层编码设计**：先通过全局异质多行为图LightGCN编码获得共享初始化，再分别在目标图和去噪辅助图上做浅层传播（2-3层），最终简单平均融合。这种轻量级设计易于工程实现和增量更新，对行为频繁变化的电商场景友好。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
多行为推荐利用点击、收藏、加购等辅助行为缓解购买（目标行为）数据稀疏，但辅助行为图常含有大量与目标无关的噪声交互，直接融合会误导偏好学习。现有方法或在表征层面压缩，或未在结构传播前显式去噪，导致噪声污染用户/物品嵌入。实验表明仅用辅助行为性能最差，仅用目标行为受限于稀疏，混合使用提升有限，说明有效去噪和利用辅助行为仍是关键挑战。

**方法关键点**  
- **双层级去噪**：结构层对辅助行为图进行边级剪枝，保留与目标任务最相关的子结构；特征层通过跨行为对比学习对齐去噪辅助与目标表征。
- **图信息瓶颈目标**：最大化去噪图与目标信号互信息（以BPR损失实现），同时最小化去噪图与原始图互信息（用HSIC近似），实现最小充分子图保留。
- **目标偏好引导的边选择**：用目标行为域学习到的用户/物品表征计算每条辅助边的保留概率（MLP + sigmoid），以Gumbel-Softmax重参数化使过程可微。
- **跨行为对比对齐**：将去噪辅助表征与目标表征作为正样本对，构建用户侧和物品侧InfoNCE损失，补充目标行为监督。
- **全局共享初始化**：先用LightGCN在异质多行为图上获取全局编码，再送入目标图和去噪辅助图，结合分层传播。

**关键结果**  
在Tmall、Taobao、Yelp、ML-10M四个数据集上，GCIB一致超越所有基线（LightGCN、MBGCN、CRGCN、BCIPM、NSED等）。尤其Yelp数据集上HR@10提升40.5%，NDCG@10提升37.2%。消融实验证实全局编码、IB去噪、对比对齐均至关重要，去除任一组件性能明显下降。噪声注入实验显示，添加20%合成噪声后GCIB仅相对下降3.6%，而对比模型（MBLFE、HGIB）下降超过10%，验证了结构级边过滤的鲁棒性。
