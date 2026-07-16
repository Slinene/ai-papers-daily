---
title: 'TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce
  Search'
title_zh: TMallGS：面向生成式电商搜索的统一特征与序列建模扩展
authors:
- Zhentao Song
- Yufeng Gao
- Xing Fang
- Jing Wang
- Guangxin Song
- Bokang Wang
- Yipin Dai
- He Guo
affiliations:
- Southeast University
- Taobao & Tmall Group of Alibaba
- Peking University
arxiv_id: '2607.13398'
url: https://arxiv.org/abs/2607.13398
pdf_url: https://arxiv.org/pdf/2607.13398
published: '2026-07-15'
collected: '2026-07-16'
category: RecSys
direction: 搜索排序 · 计算密集型架构扩展
tags:
- Feature Heterogeneity
- Signal Dilution
- Scaling Laws
- Decoupled Architecture
- Search Ranking
- CTR Prediction
one_liner: 通过解耦语义交互与信号保留的Transformer架构，首次在搜索排序中实现Scaling Law并带来显著GMV提升
practical_value: '- **分层tokenization平衡异构特征**：利用Field-wise Saliency Reweighting（FSR）做全局裁剪，再用Distribution-Calibrated
  Projection（DCP）以校准Swish替代SwiGLU，在降低33% FLOPs的同时保持精度，适合电商搜索中大量稀疏ID与稠密统计特征的混合输入。

  - **解耦晚期融合保留强匹配信号**：将Q2I匹配分等显式交叉特征通过FiLM作为调制信号，而非直接输入注意力流，避免深层Transformer过度平滑，可直接迁移至需精准相关性匹配的排序场景（如广告、搜索重排）。

  - **Error-Aware Progressive Training**：用浅层预测误差为深层样本动态加权，实现自适应课程学习，改善稀疏反馈下深层网络的梯度消失；可将该策略应用于任何深层排序模型的训练，提升收敛速度和排序指标。

  - **Context-Aware Bias Net正交化解耦偏差**：用全局上下文锚点的深层编码学习位置/页面等偏差，与主语义logit加法融合，在pairwise
  loss中自动抵消，确保GAUC优化不被全局点击先验干扰，适用于所有需在请求内做相对排序的工业系统。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业排序模型正从内存密集的DLRM范式转向可扩展的Transformer骨干，以突破算力墙并利用Scaling Laws。但直接将LLM的全Token化架构搬到高精度搜索排序，会引入三个核心问题：1）搜索中Query、用户行为、商品属性等特征高度异构，统一注意力导致梯度冲突；2）深层自注意力对显式交叉特征（如Query-Item匹配分）过度平滑，稀释关键匹配信号；3）稀疏点击反馈下深层网络梯度消失严重。针对这些问题，本文提出TmallGS，核心思想是“语义分治、交互解耦”。

## 方法关键点
- **分层分布校准Tokenization**：先通过Field-wise Saliency Reweighting（FSR）进行场级别重要性重标定，再用Distribution-Calibrated Projection（DCP）以自门控的Calibrated Swish代替SwiGLU投影，相比标准FFN降低33%计算量，同时适配异构特征分布。
- **Field-Adaptive Gated Transformer**：采用Per-Field QKV投影，为每个特征域学习专属变换矩阵；引入噪声自适应门控机制，在注意力输出后乘以基于Pre-Norm的Gate，动态抑制噪声行为序列中的干扰。
- **解耦FiLM晚期融合**：将Heavy Cross-Attributes（如文本匹配、统计命中率）通过FiLM产生仿射参数，以缩放和平移方式调制最终语义表示，避免深层低通滤波效应，保留高频匹配信号。
- **Context-Aware Bias Net**：利用序列首位的Context Anchor token的深层编码预测页面级偏差，与主语义logit加法融合，在pairwise loss中自动抵消，实现偏差解耦，直接优化GAUC。
- **Error-Aware Progressive Training**：用每层辅助预测误差动态计算下一层样本权重，迫使深层专注难分样本，并结合pairwise ranking loss，缓解稀疏反馈下的优化困难。

## 关键实验
在涵盖13M用户、74M商品、平均序列长度1500的Tmall搜索31天日志数据（500M样本）上，TmallGS相比生产基线DIN+RankMixer，GAUC提升1.26%，AUC提升1.12%；在线A/B测试30天，UCTCVR提升1.38%，GMV提升1.52%，延迟仅增加6ms。消融实验证实FiLM融合、门控注意力、Tokenization管线及pairwise loss对搜索排序至关重要。进一步展示沿宽度、深度、序列长度三个维度均遵循Scaling Law，证明了计算密集型架构的可行性。
