---
title: Utility-Aware Multimodal Contrastive Learning for Product Image Generation
title_zh: 效用感知多模态对比学习用于产品图像生成
authors:
- Xiaohang Feng
- Yiling Xie
affiliations:
- City University of Hong Kong
arxiv_id: '2605.28733'
url: https://arxiv.org/abs/2605.28733
pdf_url: https://arxiv.org/pdf/2605.28733
published: '2026-05-27'
collected: '2026-05-28'
category: GenRec
direction: 效用感知对比学习 · 商品图像生成
tags:
- multimodal contrastive learning
- utility-aware
- product image generation
- CLIP
- demand model
- inverted U-shape
one_liner: 将需求模型嵌入对比学习，使生成图像同时优化语义一致性与市场表现，在Amazon与Airbnb上超越基线
practical_value: '- 将业务目标（如销量、预订率）的回归系数作为**对比学习相似度中的正则项**，直接引导文本-图像嵌入空间向高需求视觉属性偏移，避免事后筛选的不可控性。

  - 在生成阶段使用 **Utility-Aware CLIP score** 做候选图像排序，该分数同时包含语义相似度与需求驱动属性，无需额外 prompt 工程即可获得高商业潜力图像。

  - 需求函数常呈**倒 U 型**（如美感、独特性过高反降需求），故设置二次项约束，避免模型盲目追求某属性极值；可应用于其他平台时只需替换对应需求系数。

  - 架构上**轻量即插即用**：仅将 Flux 中的标准 CLIP 编码器替换为 Utility-Aware CLIP，并保持生成架构不变，适合快速迁移到现有电商/租房图像优化流程。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：现有生成模型只追求语义对齐与视觉美感，但“最好看”的图像未必最带货。电商平台需要图像直接提升购买或预订，而非依赖大量 prompt 试错。本文从市场规模数据出发，将需求模型嵌入多模态对比学习，使生成图像同时满足语义一致性和市场偏好。

**方法关键点**：
- 在 CLIP 的 InfoNCE 损失中引入效用项，构造 **Utility-Aware InfoNCE**：相似度分数 = α_v·h_v(v) + β_s·s_θ(v,t)，其中 h_v(v) 为从销量/预订回归中提取的视觉效用（含二次项，以捕捉倒 U 型偏好）。
- 用该损失微调预训练 CLIP，得到 **Utility-Aware CLIP**，其嵌入空间对需求相关视觉细节更敏感（通过遮挡实验验证）。
- 将 Flux 中的 CLIP 编码器替换为 Utility-Aware CLIP，构成 **Utility-Aware Generator**；生成时用 Utility-Aware CLIP score 后选最优图像。
- 在 Amazon 和 Airbnb 上分别根据需求回归系数构建效用项（Amazon 用色彩、亮度等 4 个特征，Airbnb 用视觉独特性和美感）。

**实验结果**：
- Amazon 编辑任务：Utility-Aware Generator 需求得分 1.278，高于 Stable Diffusion (1.149)、GPT-Image (1.007)、Flux (1.159)；同时保真度最高（0.231）。
- Airbnb 生成与编辑任务：需求得分均最高（生成 0.573 vs. Flux 0.544；编辑 0.521 vs. Flux 0.507），且避免独特性极高，符合倒 U 型需求规律。
- 真人实验：Amazon 购买选择中，Utility-Aware Generator 被选次数 256 vs. Flux 59；Airbnb 预订意愿评分 5.039 vs. Flux 4.807，均显著提升。
