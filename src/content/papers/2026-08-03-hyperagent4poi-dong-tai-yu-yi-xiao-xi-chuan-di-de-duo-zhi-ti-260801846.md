---
title: 'HyperAgent4POI: Dynamic Semantic Message Passing on Multi-Agent Hypergraphs
  for Missing-Modality Recommendation'
title_zh: HyperAgent4POI：动态语义消息传递的多智能体超图缺失模态推荐
authors:
- Jinze Wang
- Yuze Liu
- Tiehua Zhang
- Jiong Jin
- Zhu Sun
affiliations:
- Swinburne University of Technology
- Tongji University
- Singapore University of Technology and Design
arxiv_id: '2608.01846'
url: https://arxiv.org/abs/2608.01846
pdf_url: https://arxiv.org/pdf/2608.01846
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 缺失模态补全 · 超图消息传递 · LLM增强推荐
tags:
- Multimodal Recommendation
- Missing Modality
- Hypergraph
- LLM
- LoRA
- Point-of-Interest
one_liner: 在超图层内用冻结Llama+LoRA联合完成模态补全与软关联细化，有效应对POI多模态缺失
practical_value: '- **缺失模态补全与消息传递层内耦合**：电商商品描述、图片常缺失，可借鉴DSMP在每层GNN/超图传递时利用LLM根据当前邻域上下文动态补全，使用冻结主干+LoRA适配器，既避免重训大模型又比一次补全更准确。

  - **软关联学习控制拓扑漂移**：推荐图中交互边常有噪声，DSMP通过有界候选池（固定K_ret）、软关联分数和保守KL正则，允许层内拓扑可微调整。可迁移到物品共现或查询-文档超图，用阈值筛选控制图规模，提升高阶关系挖掘的鲁棒性。

  - **离线LLM语义增强，在线无LLM延迟**：角色提示词和LoRA操作仅在训练/离线刷新时运行，最终节点表示缓存用于点积排序，线上不调用LLM。在搜索推荐系统中，可离线用LLM丰富商品或用户表征，在线直接检索缓存向量，兼顾效果与性能。

  - **可插拔角色适配器与消息接口**：聚合、拓扑、补全等语义操作使用同一冻干主干但各自独立的LoRA，模式高度复用。在商品属性补全、用户兴趣演化等任务，可定义不同提示模板和LoRA适配器，保持主干参数冻结，大幅减少训练参数量，适合多任务和轻量化部署。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：真实LBSN中POI的文本和图片模态经常缺失，这不仅削弱POI表示，还会在超图消息传递中逐层放大偏差（差异传播）。现有方法要么在传播前一次性补全特征，要么独立细化超边关联，未将二者在层内上下文联合优化。HyperAgent4POI提出动态语义消息传递（DSMP），将模态补全与超图拓扑精细化耦合在同一层中。

**方法关键点**：
- 每个节点维护持久代理状态，所有代理共享冻结的Llama-3主干，并通过角色特定的LoRA适配器（聚合、进化、推断）执行四种语义操作。
- **Local Expert** 根据节点当前状态和超边上下文生成节点到超边消息；**Semantic Aggregator** 将消息汇总为语义超边主题；**Topology Evolution** 利用LLM的兼容性判断输出有界软关联分数；**Modality Deduction** 从层内汇聚的超边上下文补全缺失模态，更新节点状态进入下一层。
- 超边候选池通过检索扩展原始成员，但严格控制大小，避免递归膨胀。软关联学习受保守先验KL正则，平衡拓扑探索与初始图结构。
- 训练优化结合BPR排序损失、模态补全InfoNCE和拓扑正则项，LLM仅离线参与，最终节点表示缓存供线上点积排序。

**关键结果**：在Yelp-2018、FSQ-NYC、FSQ-TKY三个LBSN数据集上，当60%模态随机缺失时，HyperAgent4POI的NDCG@20平均超出最强基线HIRE 8.2%。随着缺失率从0.2升至0.8，其NDCG@20降幅仅17-18%，远低于HIRE的25%以上，且补全余弦相似度和表示鲁棒性显著更优。消融实验表明，移除拓扑演化、语义聚合或模态推断分别导致NDCG@20下降16.2%、13.6%和10.5%，用参数量匹配的MLP替代LLM/LoRA操作后性能明显下降。

**核心结论**：层内动态上下文驱动的模态补全结合LLM的语义理解，能有效缓解缺失模态下的跨层偏差传播，且冻结LLM加角色适配器可作为高效的消息传递算子。
