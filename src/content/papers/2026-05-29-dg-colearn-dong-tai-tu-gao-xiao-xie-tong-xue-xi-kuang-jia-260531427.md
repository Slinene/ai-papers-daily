---
title: 'DG-CoLearn: An Efficient Collaborative Learning Framework for Dynamic Graphs'
title_zh: DG-CoLearn：动态图高效协同学习框架
authors:
- Ashley Hoi-Ting Au
- Zikun Zhang
- Ligang He
- Qiang Ni
affiliations:
- Department of Computer Science, The University of Warwick
- School of Computing and Communications, Lancaster University
arxiv_id: '2605.31427'
url: https://arxiv.org/abs/2605.31427
pdf_url: https://arxiv.org/pdf/2605.31427
published: '2026-05-29'
collected: '2026-06-01'
category: RecSys
direction: 动态图协同学习 · 增量图处理
tags:
- Dynamic Graph
- Incremental Update
- Collaborative Learning
- Privacy-Preserving
- Graph Neural Networks
- Federated Learning
one_liner: 增量图快照处理与服务器中介嵌入交换，实现动态图协同训练加速33.8倍且保护客户端间结构隐私
practical_value: '- 在电商用户-商品交互图的动态推荐场景中，全图重训成本高，可借鉴其增量更新策略：只对时间戳变化的局部子图（新交互、新节点）触发消息传递与嵌入更新，保留历史记忆，大幅降低训练计算量。

  - 多主体协同训练（如多个电商部门或跨组织联邦学习）涉及图结构隐私，采用服务器中介的嵌入交换，代替直接共享邻接表，既完成多跳邻居聚合又避免暴露连接关系，可直接复用到联邦图推荐系统。

  - 增量管道设计覆盖节点更新检测、采样邻居、聚合与预测全流程，工程实现上可按“变更节点驱动”的思路重构现有静态图训练循环，替换为版本快照管理，使系统具备在线学习能力。

  - 实验结果表明加速与隐私保护的同时，节点分类和链接预测性能均有提升，说明增量方法不会牺牲模型质量，适合对时延敏感且要求可解释性的 Agent 协同推理任务。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：动态图学习在社交网络、金融等应用中至关重要，但现有中心化方法面临全图快照重训的巨大计算开销，且将数据分区协同处理时，跨客户端边的原始结构共享可能违反隐私约束。

方法：提出 DG-CoLearn，一种面向客户透明的协同动态图学习框架。核心是增量图快照处理——仅对受时间更新影响的局部图区域进行消息传递和嵌入更新，同时通过时间建模保留历史信息。该增量设计贯穿整个图处理流程：使用服务器中介的嵌入交换机制，客户端上传受影响节点的嵌入而非原始图结构，服务器聚合分发，从而在不暴露跨客户端邻接关系的前提下实现精确的多跳邻居聚合。

效果：在节点分类和链接预测任务上，DG-CoLearn 相比全图重训方法训练时间最高加速 33.8 倍，通信开销减少 27.4 倍；预测性能同时提升，F1 值最高提升 13.36%，MAP 最高提升 8.27%。框架有效平衡了效率、可扩展性与客户端间图结构隐私。
