---
title: 'Not Only NTP: Extending Training Signal Coverage for Generative Recommendation'
title_zh: 不仅限于NTP：扩展生成式推荐的训练信号覆盖
authors:
- Changhao Li
- Shuli Wang
- Junwei Yin
- Senjie Kou
- Yinqiu Huang
- Chi Wang
- Yinhua Zhu
- Haitao Wang
- Xingxing Wang
arxiv_id: '2607.12277'
url: https://arxiv.org/abs/2607.12277
pdf_url: https://arxiv.org/pdf/2607.12277
published: '2026-07-14'
collected: '2026-07-15'
category: GenRec
direction: 生成式推荐 · 训练信号优化
tags:
- 生成式推荐
- NTP
- 对比学习
- 跨域学习
- 训练信号
- 序列推荐
one_liner: 提出NONTP框架，通过时序对比学习和跨域学习增强NTP训练信号，提升生成式推荐效果
practical_value: '- **训练信号增强可即插即用**：TCL和TDL作为辅助任务，只增加训练开销，推理零成本，可直接嵌入现有基于NTP的生成式推荐模型，无需改动推理架构。

  - **时序对比学习TCL**：采用BYOL风格EMA教师和InfoNCE损失，将隐藏状态与未来K步轨迹对齐，能捕捉长程行为结构，适合电商用户长期兴趣建模，可尝试替代或补充传统序列建模。

  - **跨域学习TDL**：通过跨域隐藏状态池化后经共享预测头，无额外参数开启第二条梯度通路，有效融合多域行为，适合电商多场景联合训练（如搜索、推荐、广告序列混合）。

  - **梯度冲突分析**：论文发现辅助任务间可能存在梯度冲突，实际部署时需监控梯度余弦相似度，考虑动态调整任务权重或应用PCGrad等策略。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有生成式推荐普遍采用Next-Token Prediction（NTP）训练，但NTP存在两个结构性问题：时间局部性（只监督单步预测，忽略长程行为依赖）和空间局部性（多域序列中，每个目标item仅从前一个隐藏状态接收梯度，缺乏跨域上下文显式梯度通路）。

**方法**：提出NONTP框架，包含两个辅助训练目标：
- **时序对比学习（TCL）**：使用BYOL风格的EMA教师网络，通过InfoNCE损失将当前隐藏状态与未来K步轨迹表示对齐，迫使模型学习更长远的行为结构。
- **跨域学习（TDL）**：对跨域隐藏状态进行均值池化，通过共享预测头预测目标item，为每个token引入第二条梯度路径，无额外参数。
两者在推理时被丢弃，不增加开销。

**结果**：在美团四域工业数据集上，NONTP相比NTP的HR@10提升34.3%，相比MBGR提升18.3%；在公开Amazon Movie-Book-CDs数据集上，HR@10提升2.8%，NDCG@10提升3.7%；线上A/B测试CTR提升1.8%，GMV提升2.1%（p<0.01）。消融实验验证各组件独立贡献，并初步探讨了梯度冲突问题。
