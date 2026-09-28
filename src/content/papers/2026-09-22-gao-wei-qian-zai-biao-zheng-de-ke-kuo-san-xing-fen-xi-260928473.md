---
title: On the Diffusibility of High-Dimensional Latents
title_zh: 高维潜在表征的可扩散性分析
authors:
- Chao Feng
- Zhiyang Xu
- Bowei Chen
- Yuanjun Xiong
- Xiyao Wang
- Jui-Hsien Wang
- Richard Zhang
- Zhe Lin
- Andrew Owens
- Yijun Li
affiliations:
- Cornell University
- Adobe
- Virginia Tech
- University of Washington
- University of Maryland
arxiv_id: '2609.28473'
url: https://arxiv.org/abs/2609.28473
pdf_url: https://arxiv.org/pdf/2609.28473
published: '2026-09-22'
collected: '2026-09-28'
category: Other
direction: 扩散模型latent几何与参数化选择
tags:
- Diffusion Models
- Flow Matching
- Latent Representation
- x0-prediction
- Text-to-Image
- Representation Autoencoder
one_liner: 发现微调重构编码器会降低latent有效维度并使velocity prediction低效，改用x0-prediction可一致提升text-to-image生成
practical_value: '- 生成式推荐/搜索中若使用latent diffusion在商品或用户表征上做生成，若编码器经过重构微调，应优先采用x0-prediction而非velocity
  prediction，可避开拟合流形外噪声方向，提升生成稳定性和收敛效率。

  - 设计item/user表征autoencoder时，不要只看重构质量；重构微调可能降低有效维度、改变几何结构，需监控latent的intrinsic dimension与流形紧致度，避免下游扩散模型被迫学习大量无效方向。

  - 工程实现上，flow matching的velocity目标在高维稀疏latent上常包含大量流形外分量，可在训练时快速对比x0-prediction与velocity
  prediction的收敛曲线，低成本验证该trick对业务生成任务的收益。

  - 对使用CLIP等多模态embedding做文案/图片生成的场景，若对编码器做过重构微调，务必检查其latent几何变化，x0-prediction可能是更稳健的参数化选项。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Representation Autoencoders（RAE）让扩散模型在预训练视觉编码器的特征空间中运行，但现成编码器未针对重构优化，会丢失细粒度视觉细节。对编码器做重构微调能恢复细节，然而作者发现此过程会降低latent的有效维度，改变其几何结构，进而影响下游生成。

**方法关键点**：通过分析高维latent空间，发现标准flow matching使用的velocity prediction要求模型拟合低维信号流形之外的正交噪声方向，导致优化效率低下。相比之下，clean data parameterization（x0-prediction）使学习目标聚焦于底层信号流形本身，避免了无效的流形外拟合。

**关键结果**：在多个强重构编码器上，x0-prediction一致提升了text-to-image生成性能，验证了参数化选择对高维latent扩散的重要性。
