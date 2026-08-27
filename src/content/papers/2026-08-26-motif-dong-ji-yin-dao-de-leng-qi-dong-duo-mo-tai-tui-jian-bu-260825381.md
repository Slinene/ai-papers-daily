---
title: 'MOTIF: Motivation-guided Topology Inference for Cold-start Multimodal Recommendation'
title_zh: MOTIF：动机引导的冷启动多模态推荐拓扑推断
authors:
- Yurui Shi
- Yuchen Miao
- Ximing Hu
- Zijun Wang
- Chang Han
affiliations:
- Taiyuan University of Technology
- Sydney Smart Technology College, Northeastern University, China
arxiv_id: '2608.25381'
url: https://arxiv.org/abs/2608.25381
pdf_url: https://arxiv.org/pdf/2608.25381
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 冷启动多模态推荐 · LLM 语义拓扑重建
tags:
- Cold-start Recommendation
- Multimodal Recommendation
- LLM Reasoning
- Graph Contrastive Learning
- Topology Reconstruction
- Semantic Alignment
one_liner: 用离线 LLM 推理用户与商品动机，重建 item-item 图并做加权对比学习，显著提升冷启动多模态推荐
practical_value: '- **LLM 语义只做图重建，不做在线预测输入**：业务中可以把 LLM 对商品/内容的功能、场景、人群、替换/互补关系推理离线缓存，转成
  item-item 图边权或关系特征，避免 LLM embedding 与协同过滤 embedding 空间不一致带来的噪声，同时不增加在线推理延迟。

  - **冷启动用户动机从训练可见历史生成**：电商推荐中可用用户短期点击/购买商品的标题、图片、属性离线总结用户动机（如户外训练、礼品购买、家庭活动），作为召回或排序的辅助特征，不泄露测试集。

  - **只扰动最后一层表示 + SE 门控的图对比学习**：对于不确定性较高的重建边，相比全图扰动更高效、更鲁棒；可迁移到 GNN 召回、商品关系图学习，用 feature-wise
  gate 自动抑制噪声维度。

  - **语义-结构对齐作为辅助损失而非直接拼接**：将 LLM 语义向量投影到与图嵌入共享空间做对比对齐，最终主任务只用图嵌入，可解决多模态/文本特征与协同信号不对齐的问题，适合电商冷启动
  or 新内容分发。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
冷启动多模态推荐面临三个耦合难题：稀疏交互掩盖用户真实意图、冷物品在图传播中处于孤立状态、基于外观相似度构建的 item-item 图容易导致语义漂移。现有方法常把语义建模、图重建、表示鲁棒性分开处理，并且直接把 LLM 生成的文本或 embedding 注入预测，会引入语义噪声。

## 方法关键点
MOTIF 采用语义-拓扑协同重建框架：
- **Semantic Motivation Reasoning**：离线使用 LLM 对商品生成功能角色、使用场景、目标人群、互补/替代关系等动机文本，并编码为语义向量；用户侧仅用训练可见历史及其对应商品内容生成用户动机向量，避免信息泄漏。
- **Knowledge-enhanced Graph Reconstruction**：融合原始多模态相似度与动机语义相似度，再加上 LLM 估计的关系先验，计算边权并保留 top-Kg 邻居，重建可迁移的 item-item 图，与 user-item 交互图合并。
- **Weighted Graph Contrastive Learning**：只对最后一层图表示加扰动得到两个视图，通过池化统计和 SE 激励门重新校准每个节点的表示，再做对比学习，增强对不确定重建边的鲁棒性。
- **Semantic-Structural Alignment**：将 LLM 语义向量与图嵌入投影到共享空间做对比对齐，作为辅助监督；最终预测只使用图嵌入，不直接融合语义 embedding。

## 关键实验
在 Amazon-Baby、Amazon-Sports、MicroLens-50K 三个多模态数据集上，与 LightGCN、SimGCL、FREEDOM、LLMRec、LMMRec、RecGOAT 等基线相比，MOTIF 整体 Recall@20/NDCG@20 相对最强 baseline 提升约 5-6%；在 extreme-cold users 和 cold items 场景下提升约 20-27%。消融显示去掉 LLM 动机推理、图重建或改用相似度图都会明显掉点，直接融合 LLM embedding 也低于对齐辅助监督方案。

## 最值得记住的一句话
把 LLM 推导出的动机语义转化为 item-item 图拓扑和表示对齐监督，而不是直接注入预测，是冷启动多模态推荐的有效模式。
