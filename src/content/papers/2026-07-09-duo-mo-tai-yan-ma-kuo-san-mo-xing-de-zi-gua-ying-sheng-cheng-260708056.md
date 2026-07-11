---
title: Reinforcing the Generation Order of Multimodal Masked Diffusion Models
title_zh: 多模态掩码扩散模型的自适应生成顺序强化
authors:
- Yidong Ouyang
- Zhe Wang
- Sourav Bhabesh
- Dmitriy Bespalov
affiliations:
- University of California, Los Angeles
- AGI Foundations for AWS
arxiv_id: '2607.08056'
url: https://arxiv.org/abs/2607.08056
pdf_url: https://arxiv.org/pdf/2607.08056
published: '2026-07-09'
collected: '2026-07-11'
category: Multimodal
direction: 多模态扩散模型 · 生成顺序优化
tags:
- Masked Diffusion Models
- GRPO
- Text-to-Image Generation
- Multimodal Understanding
- Adaptive Generation Order
one_liner: 用GRPO学习生成顺序控制模块，提升文本到图像对齐与多模态理解
practical_value: '- 生成式推荐（如Semantic ID解码）可借鉴 GRPO 优化生成顺序，提高序列质量

  - 多模态商品描述或广告图生成中，可学习顺序模块改善图文对齐与空间关系

  - 掩码扩散模型在推荐补全场景下，自适应顺序可能提升冷启动或缺失特征填充效果

  - 强化学习（GRPO）用于解码策略优化，相比单纯依赖 logits 可迁移至任何自回归/扩散生成任务'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：掩码扩散模型（MDM）能按任意顺序生成 token，但最优顺序难以从模型 logits 直接确定，尤其在文本到图像和多模态理解等非结构化任务中。

方法：提出一个可学习的控制模块，负责在每一步选择下一个生成位置；使用 Group Relative Policy Optimization（GRPO）训练该模块，以最大化奖励（如 CLIP 分数或下游任务指标）。训练时冻结 MDM 主干，仅更新控制模块。

结果：在 GenEval 文本到图像对齐基准上相对提升 4.08%，在 VLMEvalKit 多模态理解基准上相对提升 4.85%，表明学习到的生成顺序能显著改善空间细节捕捉与多模态推理能力。
