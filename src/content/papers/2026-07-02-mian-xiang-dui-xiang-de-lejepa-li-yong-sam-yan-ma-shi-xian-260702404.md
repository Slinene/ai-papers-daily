---
title: Object-centric LeJEPA
title_zh: 面向对象的 LeJEPA：利用 SAM 掩码实现数据高效的自监督学习
authors:
- Jakob Geusen
- Ender Konukoglu
affiliations:
- Biomedical Image Computing Group, ETH Zurich
arxiv_id: '2607.02404'
url: https://arxiv.org/abs/2607.02404
pdf_url: https://arxiv.org/pdf/2607.02404
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: 自监督对象中心表示学习
tags:
- Self-Supervised Learning
- Object-Centric
- SAM Proposals
- Instance Separation
- Data Efficiency
- Vision Encoder
one_liner: 用现成 SAM 对象掩码代替场景级对齐，搭配实例分离损失，大幅提升小数据下的视觉表示质量
practical_value: '- **商品图像预训练**：当你用自监督预训练商品图时，直接用 COCO 等通用数据可能效率不高；借鉴对象级 LeJEPA，用
  SAM 自动提取商品主体 mask，只在对象区域进行对比，能更快学到细致特征，对小样本商品分类或相似款识别有效。

  - **多商品场景分离**：如果你做搭配推荐或店铺风格理解，一张图里有多件商品，实例分离损失（同图其他对象当负例）能强制每个商品特征相互远离，避免特征混淆，可复用到多兴趣用户向量或穿搭组合建模中。

  - **伪掩码辅助训练**：迁移其“廉价先验”思路——不追求端到端联合发现对象，直接用现成分割模型（如商品分割 API）生成伪标签，降低训练不稳定性和工程复杂度，在商品表示学习时快速落地。

  - **数据效率验证**：论文在 10% COCO 上仍显著优于全量图像级模型，提示你在标注稀缺的垂直行业（如小众品类、UGC 商品图）先用自监督预训练再微调，就可能得到较好基座。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：图像级自监督方法（如 LeJEPA）需要海量数据，因为随机裁剪的两个视图常包含不同物体，强制对齐迫使模型依赖全局语境，忽略了对象级组合结构。对象中心学习利用场景的组成性，有望提升数据效率，但无监督联合分割与表示学习存在循环依赖，训练不稳定。

**方法关键点**：
- **廉价对象先验**：训练时直接采用现成 SAM 生成的实例分割候选（无需真实标注）作为对象掩码，绕开联合发现的不稳定性。
- **对象级 LeJEPA**：将原有图像级分布对齐目标（VICReg 风格，避免坍塌）移植到对象集合上——对每个对象裁剪出的区域提取特征，再让同一对象在不同视图下的表示一致。
- **实例分离损失**：把同一场景中的其他对象作为负样本，强制不同实例的表示相互推开，增强细粒度区分能力。

**关键结果**：
- 在 COCO 的 10%~100% 子集上训练 ViT-B/S，对象级 LeJEPA 在多个下游任务中均超越图像级版本：DAVIS 跟踪、ImageNet-1k 分类、ADE20k 分割、NAVI 重识别。
- 尤其在 10% COCO（11.8 万张图）下，对象级模型的表现显著优于全量图像级模型，证明了极高的数据效率。
