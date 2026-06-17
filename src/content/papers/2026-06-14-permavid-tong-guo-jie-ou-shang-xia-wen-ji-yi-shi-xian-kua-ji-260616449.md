---
title: 'PermaVid: Consistent Video Generation Across Edits via Disentangled Context
  Memory'
title_zh: PermaVid：通过解耦上下文记忆实现跨编辑一致视频生成
authors:
- Shuai Yang
- Bingjie Gao
- Ziwei Liu
- Jiaqi Wang
- Dahua Lin
- Tong Wu
affiliations:
- Shanghai Jiao Tong University
- Stanford University
- S-Lab, Nanyang Technological University
- The Chinese University of Hong Kong
- Shanghai Innovation Institute
arxiv_id: '2606.16449'
url: https://arxiv.org/abs/2606.16449
pdf_url: https://arxiv.org/pdf/2606.16449
published: '2026-06-14'
collected: '2026-06-17'
category: Multimodal
direction: 视频生成 · 解耦多模态记忆
tags:
- Video Generation
- Memory Augmentation
- Disentangled Representations
- Multi-modal Fusion
- Edit Consistency
one_liner: 提出解耦语义外观与几何结构的多模态记忆，结合编辑感知更新，实现视频编辑后的长期一致性生成。
practical_value: '- 解耦记忆设计可启发多模态商品表征：在电商中，将商品视觉特征解耦为外观（颜色、纹理）与几何（形状、结构）分别记忆，可提升虚拟试穿、商品编辑等场景的一致性。

  - 编辑感知的记忆更新策略可借鉴到用户兴趣模型：当用户行为发生突变（如切换品类）时，类似更新机制能避免过时记忆干扰，维持长期兴趣建模的连贯性。

  - 多模态记忆引导的生成框架可应用于个性化商品展示：利用混合模态参考条件（图像+深度）生成一致性的商品视频或图片，增强生成式推荐的视觉质量。

  - 整体上，主要贡献在视频生成，但解耦记忆与一致性维护思路对推荐系统的多模态序列建模有一定跨界启发。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频编辑后，传统记忆设计因上下文过时或无效，难以维持跨时间和视角的长期一致性。

**方法**：提出 PermaVid，构建两个互补的记忆库：RGB 上下文记忆捕获外观感知信息并隐式编码几何；深度上下文记忆保留与语义解耦的纯几何结构。通过编辑感知的记忆更新与检索策略，使记忆随编辑演化。在此基础上，设计记忆引导的视频生成模型，从混合模态记忆上下文中抽取参考条件，进行多模态特征融合。

**关键结果**：实验表明，该方法在编辑后能保持长期语义和结构一致性，显著优于现有最优方法，支持全局编辑（如风格转换）和局部编辑（如物体替换）后的连贯视频生成。
