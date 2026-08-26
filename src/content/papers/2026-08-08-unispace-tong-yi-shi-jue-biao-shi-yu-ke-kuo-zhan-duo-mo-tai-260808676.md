---
title: 'UniSpace: Unified Visual Representation and Scalable Multimodal Modeling'
title_zh: UniSpace：统一视觉表示与可扩展多模态建模
authors:
- Jinbo Yan
- Limeng Qiao
- Jie Qin
- Junyan He
- Feize Wu
- Guanglu Wan
affiliations:
- Meituan
arxiv_id: '2608.08676'
url: https://arxiv.org/abs/2608.08676
pdf_url: https://arxiv.org/pdf/2608.08676
published: '2026-08-08'
collected: '2026-08-26'
category: Multimodal
direction: 统一视觉表示 · 多模态生成编辑
tags:
- Multimodal
- Vision Transformer
- Unified Representation
- MoE
- Text-to-Image
- Image Editing
one_liner: 提出 Patch Reparameterization，使冻结语义 ViT 同时支持理解、生成与编辑，并扩展为 8B MoE 统一模型
practical_value: '- 可借鉴 Patch Reparameterization：在预训练语义 ViT 上增加 reconstruction-aware
  patch embedding，冻结主体 Transformer，低成本复用语义表征的同时保留像素细节；适合电商商品图重建、编辑和增强场景。

  - 单一视觉空间同时支持理解、生成、编辑，省去独立 VAE 通路，能降低多模态模型复杂度和部署成本；在商品图像生成、广告素材编辑、多模态商品理解等任务中可探索统一
  encoder。

  - 8B Mixture-of-Transformer-Experts 的扩展思路可复用到多任务电商多模态模型：按任务或模态路由专家，在统一表征上做商品理解、文案配图、图片编辑。

  - 评测基准 ImgEdit/DPG/OneIG-Bench 提供指令式图像编辑的系统级评估模板，可改造为电商场景的商品图编辑/文案生图评测；但对推荐、召回、排序的直接帮助有限。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：语义 ViT 的最终 token 丢失细粒度视觉细节，导致像素重建差，难以用于图像生成、编辑等重建敏感任务。作者探讨能否在预训练语义 ViT 上构建单一视觉表示空间，同时支持理解、生成和编辑。

方法关键点：发现冻结 Transformer 块本身并非无法保留细节，问题来自原始 patch 参数化使表示趋向语义抽象；提出 Patch Reparameterization，保留原语义通路，同时增加 reconstruction-aware patch embedding，将细粒度视觉信息注入同一冻结 ViT 块。该统一表示兼顾多模态理解、高保真重建及更优的重建-生成权衡。进一步扩展到 UniSpace，一个 8B 的 Mixture-of-Transformer-Experts 模型，在同一视觉空间内完成理解、生成与编辑，无需独立 VAE 通路。

关键结果：系统级评估在 ImgEdit、DPG、OneIG-Bench 等基准上验证了实用文本到图像生成与指令式图像编辑能力，表明重参数化预训练 ViT 可作为可扩展多模态建模的统一视觉接口。
