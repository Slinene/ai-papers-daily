---
title: 'RefDecoder: Enhancing Visual Generation with Conditional Video Decoding'
title_zh: RefDecoder：条件视频解码增强视觉生成
authors:
- Xiang Fan
- Yuheng Wang
- Bohan Fang
- Zhongzheng Ren
- Ranjay Krishna
affiliations:
- University of Washington
- University of North Carolina at Chapel Hill
arxiv_id: '2605.15196'
url: https://arxiv.org/abs/2605.15196
pdf_url: https://arxiv.org/pdf/2605.15196
published: '2026-05-14'
collected: '2026-05-17'
category: Other
direction: 条件视频解码器架构优化
tags:
- Video Generation
- VAE Decoder
- Conditional Decoding
- Reference Attention
- Image-to-Video
- Visual Quality
one_liner: 为视频VAE解码器注入参考图像条件，绕过潜在信息瓶颈，显著提升重建保真度与生成一致性
practical_value: '- **条件解码器即插即用**：RefDecoder 可无缝替换已有视频生成管线（如 Wan 2.1）的解码器，无需重新训练扩散模型，工程实现成本低，适合快速提升线上视频生成质量。

  - **高保真参考信号注入**：通过参考注意力将原始图像细节直接送入解码过程，避免了 VAE 潜在压缩导致的信息丢失，该思想可迁移至电商商品图/视频的高细节重建，改善纹理、文字等易损失元素。

  - **轻量级参考编码器设计**：采用独立的小网络将参考帧映射为细节 token，与潜在 token 在解码器各上采样阶段协同处理，可借鉴到多模态生成任务中，如
  Agent 根据一张高质量参考图指导视频生成或虚拟试穿。

  - **多任务泛化能力**：在风格迁移、视频编辑等任务上表现良好，可赋能电商素材的自动化精修、换背景、风格化等场景，减少人工后期成本，提升内容生产效率。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有视频生成主流方案（Latent Diffusion）中，去噪网络通常接受强条件输入，但 VAE 解码器往往无条件，这种架构不对称导致重建视频丢失细节且与输入不一致。作者观察到，解码器同样需要条件信号才能保留结构完整性。

**方法**：提出 RefDecoder——一种参考条件视频 VAE 解码器。核心是通过参考注意力机制将高保真参考图像信号直接注入解码过程。具体地，一个轻量级图像编码器将参考帧映射为细节丰富的高维 token，这些 token 在解码器的每个上采样阶段与去噪后的视频潜在 token 共同处理。该设计绕过 VAE 潜在空间的损失，让解码器能够利用原始图像的精细细节，且无需修改扩散模型训练。

**关键结果**：在 Inter4K、WebVid 和 Large Motion 重建基准上，RefDecoder 在多个解码器骨架（Wan 2.1、VideoVAE+）上取得一致提升，PSNR 最高提升 +2.1dB。直接替换现有视频生成系统后，在 VBench I2V 基准上，主体一致性、背景一致性和整体质量分数全面改善。此外，RefDecoder 能泛化到风格迁移和视频编辑精修等任务。
