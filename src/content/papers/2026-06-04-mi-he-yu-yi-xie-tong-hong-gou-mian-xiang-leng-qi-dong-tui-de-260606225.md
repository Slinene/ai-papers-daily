---
title: 'Bridging the Semantic-Collaborative Gap: An Asymmetric Graph Architecture
  for Cold-Start Item Recommendation'
title_zh: 弥合语义-协同鸿沟：面向冷启动推荐的非对称图架构
authors:
- Anh Truong
- John Trenkle
- Yuanbo Chen
- Honghong Zhao
- Abdullah Alchihabi
- Effy Fang
- Michael Tamir
affiliations:
- Tubi
- Kumo AI
arxiv_id: '2606.06225'
url: https://arxiv.org/abs/2606.06225
pdf_url: https://arxiv.org/pdf/2606.06225
published: '2026-06-04'
collected: '2026-06-06'
category: RecSys
direction: 图推荐系统 · 冷启动物品嵌入生成
tags:
- Cold-Start
- Graph Neural Networks
- Asymmetric Architecture
- Link Prediction
- Content Embedding
- Collaborative Filtering
one_liner: 提出Shallow-RHS非对称链路预测架构，使内容塔仅从固有特征生成协同感知嵌入，实现冷启动物品检索的图补全
practical_value: '- 将冷启动物品推荐视为图补全：训练内容编码器将元数据等固有特征映射到协同过滤对齐的嵌入空间，新物品上线即可获得嵌入，通过 ANN
  检索相似暖物品作为隐式邻居，无需重新训练或索索引重建。

  - 工程实现上采用非对称设计：内容塔刻意不引入交互衍生特征或图上邻居聚合，避免冷启动阶段交互缺失导致的梯度断裂，同时降低在线推理延迟；设备塔则正常利用时序图捕获协同信号，二者解耦部署。

  - 设备冷启动可复用同样思路：利用人口统计等属性构建群组级嵌入，在没有历史行为时提供兜底表示，协助新设备获得合理推荐。

  - 这种做法对电商冷启动物品召回有直接参考价值：新商品可用标题、类目、属性等特征实时生成向量，直接接入已有向量检索通路，靠代理物品的协同信号撬动流量，冷启动周期缩短且可量化评估。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：协同过滤和图推荐依赖用户交互，新内容无历史行为导致冷启动困境。Tubi 生产检索系统要求新内容立即获得独立嵌入，且设备嵌入需用于近似最近邻检索，这对冷启动提出严格约束。

**方法**：将冷启动建模为时序二分设备-内容图上的归纳式图补全。提出 **Shallow-RHS** 非对称链路预测架构：左侧设备塔（LHS）通过时间感知的观看历史消息传递捕获协同信号；右侧内容塔（RHS）刻意设计为浅层，仅编码内容的固有特征（如元数据），不使用 ID 嵌入、内容侧子图、邻居聚合或交互衍生表示。这强制内容编码器将语义特征映射到协同过滤感知的嵌入空间。训练后，该编码器可为任意内容（暖或新）生成嵌入，通过检索暖物品作为代理邻居实现隐式图补全。设备冷启动则扩展为基于人口统计特征的群组嵌入构建。

**结果**：大规模在线实验表明，在内容冷启动参与度、推广速度、印象获取及设备冷启动参与度上均取得持续相对提升（具体数字未披露），验证了非对称表示补全的有效性。
