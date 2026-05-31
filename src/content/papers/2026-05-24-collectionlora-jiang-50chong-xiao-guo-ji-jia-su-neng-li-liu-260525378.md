---
title: 'CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy
  Distillation'
title_zh: CollectionLoRA：将50种效果及加速能力蒸馏进单一LoRA
authors:
- Fangtai Wu
- Hailong Guo
- Shijie Huang
- Jiayi Song
- Yubo Huang
- Mushui Liu
- Zhao Wang
- Yunlong Yu
- Jiaming Liu
- Ruihua Huang
affiliations:
- Zhejiang University
- Qwen Applications Business Group of Alibaba
- Xi'an Jiaotong University
arxiv_id: '2605.25378'
url: https://arxiv.org/abs/2605.25378
pdf_url: https://arxiv.org/pdf/2605.25378
published: '2026-05-24'
collected: '2026-05-31'
category: Multimodal
direction: 多LoRA合并与蒸馏
tags:
- LoRA
- Distillation
- Diffusion Models
- Image Editing
- Multi-Concept Personalization
one_liner: 多教师在线蒸馏框架，将多个效果LoRA与少步生成合并为一个LoRA，消除参数干扰并降低部署成本
practical_value: '- **多任务LoRA合并部署**：若业务中存在多个LoRA用于不同下游任务（如客服、商品描述生成、搜索改写等），可借鉴多教师蒸馏将多个LoRA的知识压缩到单一LoRA中，减少动态加载开销，并避免级联多个LoRA时的特征干扰。

  - **随机数据流切换增强泛化**：Probabilistic Dual-Stream Routing 在训练时随机切换数据源，类似技巧可用于多任务推荐模型的训练，通过在不同任务数据流间随机切换，提升模型对未见任务组合的泛化能力。

  - **提示空间概念隔离**：Asymmetric Orthogonal Prompting 通过正交提示隔离不同概念，此思想可迁移到生成式推荐中的多属性控制，例如用正交提示向量区分“风格”与“品类”，避免生成时属性混淆。

  - **粗到细蒸馏缓解分布差距**：Coarse-to-Fine Distillation 从输出分布粗对齐逐步过渡到特征细对齐，可应用于推荐模型蒸馏，尤其当教师模型远大于学生模型时，分阶段对齐有助于提升蒸馏效果。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：自定义图像编辑常为每种效果单独训练 LoRA，当效果数量增至数十种时，存储和动态加载开销剧增；同时，级联多个 LoRA 与加速模块（如少步生成）会引发严重参数干扰，导致概念混杂和风格退化。

**方法关键点**：提出 CollectionLoRA，一个多教师在线策略蒸馏框架，将多种效果 LoRA 与少步生成能力压缩到单一 LoRA 中。核心组件包括：
- **Probabilistic Dual-Stream Routing**：训练时按概率在教师数据流和少步生成数据流间随机切换，增强模型对未见场景的泛化；
- **Asymmetric Orthogonal Prompting**：为不同概念设计不对称正交提示，在提示空间实现概念隔离，防止特征串扰；
- **Coarse-to-Fine Distillation Objective**：先粗粒度匹配输出分布，再细粒度对齐特征，缓解教师-学生分布差距。

**结果**：在蒸馏多达 50 种效果的任务上，CollectionLoRA 生成的单一 LoRA 在概念保真度上达到或优于独立训练的教师模型，同时消除了参数干扰，并将部署所需的 LoRA 数量从数十个缩减为 1 个，显著降低部署成本。
