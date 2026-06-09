---
title: 'DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction'
title_zh: DeRes：解耦残差稳定性与自适应性的高效 CTR 预估
authors:
- Wenzhuo Cheng
- Shipeng Nie
- Qixin Guo
- Xuefeng Sun
- Jianguo Lou
- Zhengwei Zheng
arxiv_id: '2606.07980'
url: https://arxiv.org/abs/2606.07980
pdf_url: https://arxiv.org/pdf/2606.07980
published: '2026-06-06'
collected: '2026-06-09'
category: RecSys
direction: CTR 预估 · 残差连接 · 双路径架构
tags:
- CTR Prediction
- Residual Connection
- Dual-Path Network
- Attention Residuals
- Scaling Law
one_liner: 双路径残差解耦稳定性与自适应，点式 SiLU 注意力支持多兴趣并行，得到更优 AUC 和更陡缩放律
practical_value: '- 双路径残差设计：保留恒等跳跃连接保证梯度流和低阶特征复用，同时增加块注意力路径提取跨层高阶信号；电商推荐中特征异构性强，可照搬此解耦方式，避免深层
  Transformer 的信号稀释。

  - 点式注意力（Pointwise AttnRes）用 SiLU 替代 Softmax：打破跨层注意力的零和竞争，支持多兴趣同时激活并提供负权遗忘；适用于多兴趣用户建模（如
  DIN 升级），可推广到序列推荐中的跨层特征聚合。

  - 向量级门控融合：每个隐藏维度独立决定两路径权重，比标量门控更精细；可借鉴到多路特征融合场景，实现维度级别的自适应路由。

  - 缩放律优化：在同等 FLOPs 下获得更高 AUC，8 层模型即达到 16 层 OneTrans 性能，计算节省约 2 倍；工业部署时可用更浅的网络达到同等效果，直接降低推理成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
CTR 预估的 Transformer 化面临着残差连接的瓶颈：Pre-Norm 导致早期兴趣信号随深度稀释，恒等跳跃无法遗忘漂移兴趣，每层仅能看到前一层输出而丢失跨层依赖。语言模型中的 AttnRes、DenseFormer 等方法改进了层间连接，但丢弃了保护性的恒等跳跃，且未针对 CTR 的异构特征、浅层深度和多兴趣并行做适配。因此，需要一种既保持梯度稳定性又能动态利用跨层信息的连接机制。

**方法**  
DeRes 采用双路径架构：
- 恒等残差路径：保留标准恒等跳跃，保证一阶特征复用和梯度流动；
- 块注意力残差路径：将各层输出压缩为块，通过跨层注意力动态聚合历史信号；使用 **Pointwise AttnRes**（SiLU 激活替代 Softmax）支持多块同时激活和负权遗忘；
- 向量门控融合：每个隐藏维度独立学习两路径的混合权重，实现细粒度信息路由。
理论分析表明双路径严格增大函数容量，恒等残差避免了可学习矩阵随深度的指数衰减，且更高的交互阶数带来更优缩放律。

**结果**  
在 331M 交互的工业数据集、Criteo 和 Avazu 上，DeRes 超越 12 个基线（包括 OneTrans、TokenMixer-Large、UniMixer、AttnRes 等）。工业集上 AUC +0.32%，GAUC +0.53%，RelaImpr 达 2.27%；额外 FLOPs 小于 5%。缩放律指数 γ=0.118 vs. OneTrans 0.071，8 层 DeRes 达到 16 层 OneTrans 的性能，约 2 倍计算节省。消融确认：双路径优于单路径，恒等残差优于可学习矩阵，SiLU 优于 Softmax，门控融合优于加性融合，尾部物品提升最显著（+0.74% AUC）。
