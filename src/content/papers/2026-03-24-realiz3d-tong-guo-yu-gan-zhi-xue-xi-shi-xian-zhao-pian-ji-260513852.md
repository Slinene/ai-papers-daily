---
title: 'Realiz3D: 3D Generation Made Photorealistic via Domain-Aware Learning'
title_zh: Realiz3D：通过域感知学习实现照片级真实3D生成
authors:
- Ido Sobol
- Kihyuk Sohn
- Yoav Blum
- Egor Zakharov
- Max Bluvstein
- Andrea Vedaldi
- Or Litany
arxiv_id: '2605.13852'
url: https://arxiv.org/abs/2605.13852
pdf_url: https://arxiv.org/pdf/2605.13852
published: '2026-03-24'
collected: '2026-05-17'
category: Other
direction: 解耦域与控制，缩小合成到真实域差距
tags:
- Diffusion Models
- Domain Adaptation
- 3D Generation
- Multi-view Synthesis
- Control Decoupling
- Photorealism
one_liner: 解耦控制信号与视觉域，引入域协变量适配器，在保持真实感的同时实现3D可控生成
practical_value: '- 商品图生成中，使用合成3D数据微调扩散模型时，可通过解耦控制信号（如视角、材质）与域指示符，避免生成图像变得“像渲染图”，保持照片级真实感。

  - 引入可学习的残差适配器来编码域信息，是一种轻量多域融合方案，电商场景下可复用：一个基座模型，通过切换适配器生成不同风格（写实、插画、3D渲染等）。

  - 针对扩散模型不同层和去噪步骤的分析启示：早期步骤负责全局结构，后期步骤聚焦纹理细节，可将几何控制注入深层，材质控制注入浅层，从而在不牺牲真实性的前提下提升可控性。

  - 推理时可通过调整域适配器的权重，平滑插值于合成与真实域之间，实现可控的风格迁移，用于商品背景替换或虚拟试穿场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：利用合成3D资产渲染图像微调预训练图像生成模型，是赋予模型3D一致性和可控性（如多视角、材质）的常见方法，但合成渲染与真实照片之间存在域差距，导致生成图像缺乏真实感。作者发现，域差距主要由模型将控制信号与合成外观不当关联引起。

**方法**：提出Realiz3D轻量框架，核心是将“控制信号”与“视觉域”解耦。具体做法：引入一个域协变量（指示图像是真实还是合成），通过小型残差适配器注入扩散模型，使其学会独立地感知控制信号，而不是将控制信号绑定到特定域。训练时，模型同时学习可控性和域自适应，从而在应用控制时仍能生成逼真图像。此外，利用扩散模型不同层和去噪阶段的分工（如浅层管结构，深层管细节），设计新的训练与推理策略，进一步缩小域差距。

**关键结果**：在文本到多视图生成和3D纹理化任务上，Realiz3D生成的输出既保持几何/视角一致性，又实现了照片级真实感，消融实验验证了域解耦和层选择策略的有效性。
