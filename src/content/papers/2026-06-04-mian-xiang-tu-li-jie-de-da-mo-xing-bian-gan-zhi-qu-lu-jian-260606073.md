---
title: Edge-Aware Curvature Modeling for Graph Understanding in Large Language Models
title_zh: 面向图理解的大模型边感知曲率建模
authors:
- Zhenghong Lin
- Zhibin Shi
- Hongyang Dong
- Xinjie Ye
- Yuhong Chen
- Shiping Wang
affiliations:
- Nanyang Technological University
- Fuzhou University
- University of Wisconsin-Madison
- Newland Digital Technology Co., Ltd.
- Xiamen University
arxiv_id: '2606.06073'
url: https://arxiv.org/abs/2606.06073
pdf_url: https://arxiv.org/pdf/2606.06073
published: '2026-06-04'
collected: '2026-06-07'
category: LLM
direction: 图感知LLM · 边曲率信息注入
tags:
- Graph LLM
- Edge Curvature
- Over-squashing
- Node Alignment
- Curvature-aware Prompt
one_liner: 首次理论分析节点对齐的不足，提出曲率增强的边感知提示与正曲率消息传递，解决图文本对齐的过压缩问题
practical_value: '- 构建商品知识图谱增强的LLM问答或推荐解释时，可借鉴边感知提示设计：将结构化边信息（如“用户-购买-商品”）直接注入提示词，无需额外训练，低成本提升图结构感知。

  - 在用户-商品交互图上进行消息传递时，可利用离散Ricci曲率识别负曲率边（如噪声交互或长尾连接），仅沿正曲率边传播信息，缓解过压缩，提升表示质量。

  - 针对多模态对齐（如商品图文与用户行为图），分析论证了单纯节点对齐的次优性，提示我们需显式建模边特征（如交互强弱、关系类型）以避免信息瓶颈。

  - 曲率引导的消息传递可作为一个轻量级模块嵌入现有Gnns，在召回或排序的图模型中尝试，可能改善稀疏交互下的用户/物品表示。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有图感知大语言模型（LLM）通过图编码器与冻结LLM的节点级对齐联合建模图与文本，但忽略了边结构，导致信息传播次优。本文首次从理论上证明：（1）忽略边信息会导致对齐目标陷入次优解；（2）负曲率边引发瓶颈信息流，造成图-文本视图间的过压缩现象。

**方法**：提出CureLLM框架，注入边信息信号。（1）训练无关的边感知文本提示机制：将图的边信息（如邻接关系、边类型）转化为提示词，直接让LLM基于此生成输出，无需额外参数学习。（2）曲率感知图表示学习：利用离散Ricci曲率计算边的几何特性，消息传递仅沿正曲率边进行，避免负曲率边导致的过压缩；同时设计曲率感知的对齐损失，强化正曲率边上的跨模态一致性。

**结果**：在11个不同领域的真实数据集上，与20种方法对比，CureLLM在图理解任务（如节点分类、链接预测）上取得显著提升，验证了边感知曲率建模的有效性。
