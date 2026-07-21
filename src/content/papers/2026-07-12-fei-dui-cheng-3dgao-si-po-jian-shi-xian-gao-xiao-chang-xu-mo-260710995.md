---
title: 'AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene
  Modeling'
title_zh: 非对称3D高斯泼溅实现高效长序列场景建模
authors:
- Yingji Zhong
- Dave Zhenyu Chen
- Fuzhao Ou
- Youyu Chen
- Zhihao Li
- Lanqing Hong
- Dan Xu
affiliations:
- HKUST
- Huawei Noah’s Ark Lab
- CityU
arxiv_id: '2607.10995'
url: https://arxiv.org/abs/2607.10995
pdf_url: https://arxiv.org/pdf/2607.10995
published: '2026-07-12'
collected: '2026-07-21'
category: Other
direction: 非对称架构 · 高效3D重建
tags:
- 3D Gaussian Splatting
- novel view synthesis
- asymmetric architecture
- parameter efficiency
- long-sequence
- neural rendering
one_liner: 解耦几何与外观建模的非对称架构，大幅降低长序列新视角合成中冗余计算
practical_value: '- 属于计算机视觉与图形学领域，核心创新是 3D 重建效率优化，与电商/搜索推荐/AI Agent 业务场景无关。

  - 业务中若涉及 3D 商品展示、虚拟试穿试戴等，其非对称设计思想（关键任务高精度、次要任务轻量化）可借鉴到模型资源分配中，但整体迁移价值有限。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
现有可泛化 3D Gaussian Splatting 方法在处理高分辨率、长序列输入时存在大量冗余计算。观察到两点： (1) 高质量新视角合成不依赖高精度几何；(2) 外观学习比几何恢复更容易。由此提出非对称架构，将几何与外观建模解耦。  
**方法**  
- 几何分支使用粗粒度 token 并分配多数参数，负责多视角重建；外观分支使用细粒度 token 但参数极少，捕获纹理细节。  
- 两个分支通过双边连接交互，实现任务感知的非对称计算分配，提升参数效率。  
**关键结果**  
在 32 视角 960P 输入下，匹配优化方法的同时推理速度提升近 800 倍；零样本性能超越 SOTA 可泛化模型，参数量和训练推理开销显著减少，整体效率大幅领先。
