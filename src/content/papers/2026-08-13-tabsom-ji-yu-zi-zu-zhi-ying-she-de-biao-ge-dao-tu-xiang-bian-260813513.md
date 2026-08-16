---
title: 'TabSOM: A tabular-to-image encoding method based on self-organizing maps'
title_zh: TabSOM：基于自组织映射的表格到图像编码方法
authors:
- David Chushig-Muzo
- María Ángeles Rodríguez de Cara
- Eva Milara
- Francisco J. Lara-Abelenda
- Luis Zhinin-Vera
- Diego H. Peluffo-Ordóñez
arxiv_id: '2608.13513'
url: https://arxiv.org/abs/2608.13513
pdf_url: https://arxiv.org/pdf/2608.13513
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 表格数据图像化编码与可解释性
tags:
- Tabular-to-image
- Self-Organizing Maps
- CNN
- Interpretability
- Feature Encoding
- Deep Learning
one_liner: 用SOM组件平面布局特征并建模特征间关系，将表格数据编码为图像以提升CNN/ViT的分类性能与可解释性
practical_value: '- 在电商/推荐特征工程中，当需要把混合类型表格特征喂给 CNN/ViT 做多模态或排序时，可借鉴 TabSOM 的 SOM 布局思路：用
  SOM 分量平面做特征定位，稳定且保留相似特征空间关系，避免 t-SNE/UMAP 随机性和仅编码边际值的问题。

  - 显式建模特征交互：TabSOM 第二通道把 pair 关系画成空间连接，可启发我们用图像/图混合输入增强深度学习排序模型对交叉特征的表达能力，尤其在特征数量不多但交互重要的场景（如用户×商品属性）。

  - 可解释性工具：class-separation importance score 以 SOM 原型为基础，能给出全局重要性和原型级别的局部解释，可作为 SHAP
  的补充，用于推荐模型特征归因和排查线上 bad case。

  - 工程实现注意：Hungarian assignment 保证特征在画布位置无冲突且固定，利于增量训练/缓存特征图像；多尺度节点通道让模型同时看到精细和粗粒度模式，值得在构建图像化特征时复用。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有 tabular-to-image 方法（t-SNE、UMAP、PCA 布局）只把每个特征映射到固定像素，只编码特征边际值，丢失特征间关系。TabSOM 用 Self-Organizing Map (SOM) 生成特征空间布局和关系图，试图在图像表示中保留特征交互。

**方法关键点**：
- 用 SOM 组件平面为每个特征确定固定画布位置，通过无冲突的 Hungarian assignment 分配。
- 从组件平面提取 pairwise 特征关系图，将特征值和特征交互分别编码为两个多尺度节点通道，堆叠成图像。
- 提出两种可解释性方法：原型启发的 partial dependence plot 和 class-separation importance score。

**关键结果数字**：在多个公开二分类数据集上与 12 种现有 tabular-to-image 方法对比，TabSOM 在所有数据集上排名第一或第二，且方差最低；其 class-separation score 与 Random Forest、XGBoost、SHAP 的 top 特征有合理一致性，同时捕获互补结构信息。
