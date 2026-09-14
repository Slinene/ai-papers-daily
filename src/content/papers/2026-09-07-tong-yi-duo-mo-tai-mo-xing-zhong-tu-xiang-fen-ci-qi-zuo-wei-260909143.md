---
title: Studying Image Tokenizers as Visual Languages in Unified Multimodal Models
title_zh: 统一多模态模型中图像分词器作为视觉语言的研究
authors:
- Siting Li
- Zhengyang Wang
- Simon Shaolei Du
- Xi Chen
- Yang Liu
affiliations:
- University of Washington
- Amazon FAR
arxiv_id: '2609.09143'
url: https://arxiv.org/abs/2609.09143
pdf_url: https://arxiv.org/pdf/2609.09143
published: '2026-09-07'
collected: '2026-09-14'
category: Multimodal
direction: 多模态模型训练与图像分词器评估
tags:
- image tokenizer
- multimodal
- autoregressive
- training dynamics
- evaluation
one_liner: 通过跟踪分任务验证损失，揭示图像分词器与文本联合建模时的损失-性能关系及设计影响
practical_value: '- 在多模态联合训练中，按 task 分别监控 validation loss（text、image、T2I、I2T），而不是只看整体
  loss，可以更早定位数据配比、分词器或训练不稳定的问题；尤其适用于电商图文统一模型（如商品图 + 文案生成）。

  - 选图像 tokenizer 时，用 I2T loss（基于共享文本词表）作为跨模型一致的评估信号，比 T2I loss 或重建指标更稳定，且与下游生成和视觉理解性能都相关；适合作为早停、模型选择或在线监控指标。

  - 不要单独根据重建质量（如 FID、SSIM）选择图像 tokenizer，因为更好的重建不保证更低的任务损失或更强的下游性能；应该结合任务损失和实际业务指标（如商品图到文案的匹配度、点击率）做融合判断。

  - 图像 tokenizer 的选择会影响联合优化下的文本建模，因此当在同一模型中同时处理商品图片和文本时（如视觉问答、图文搜索），更换 tokenizer 后需要重新检查文本侧的
  fine-tune 效果和 loss 变化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
统一多模态模型使用离散图像 tokenizer 定义视觉语言，但现有评估多为孤立的重建指标或单一生成/理解评测，无法反映图像与文本联合建模时的行为。

**方法关键点**
构建控制性纯自回归 testbed，在多模态持续预训练中跟踪 text、image、text-to-image (T2I) 和 image-to-text (I2T) 四类任务的验证损失；考察损失随训练的变化、与下游性能的关系，并基于损失视角分析 tokenizer 设计（判别器、语义监督、词表大小）。

**关键结果**
1）损失应按任务分析，不同任务的 scaling 行为不同，对 tokenizer 的排序也不同。2）固定 tokenizer 时，T2I 和 I2T 损失与生成质量相关；但跨 tokenizer 比较时，T2I 损失-性能关系会随图像 token 空间偏移，而 I2T 损失基于共享文本词表，信号更一致，且在 SFT 后与生成和视觉理解性能都相关。3）更好的重建不意味着更低的任务损失或更强下游性能。4）图像 tokenizer 选择会影响联合优化下的文本建模。
