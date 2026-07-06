---
title: Alignment Is All You Need For X-to-4D Generation
title_zh: 对齐即一切：面向任意模态到4D生成
authors:
- Qiaowei Miao
- Kehan Li
- Yawei Luo
- Yi Yang
arxiv_id: '2607.02516'
url: https://arxiv.org/abs/2607.02516
pdf_url: https://arxiv.org/pdf/2607.02516
published: '2026-07-02'
collected: '2026-07-06'
category: Other
direction: 多模态对齐 · 4D 生成
tags:
- X-to-4D
- Diffusion Models
- Alignment
- Gaussian Splatting
- Multimodal
one_liner: 提出 Align4D 框架，通过对象距离对齐、运动-几何联合对齐与异步优化，实现任意模态到一致 4D 内容生成
practical_value: '- 在电商动态商品展示生成中，可借鉴对象距离对齐思路，将输入视频/图像与 3D 模型对齐，生成多视角一致且动作连贯的商品 4D
  短片，提升沉浸感。

  - 运动-几何联合对齐方法可被用于个性化商品视频生成：用文本/图片指定外观，用现有视频驱动动作，同时约束几何一致性，避免变形失真。

  - 异步优化技巧（解耦外观与运动训练）可迁移到生成式推荐中的动态素材生成，降低运动变形对几何结构的干扰，提高生成质量的稳定性。

  - 整体框架展示了从稀疏多模态输入（文本、图像、视频、3D）合成动态内容的能力，可启发在广告创意生成中融合多源素材，自动生成统一风格的动态广告视频。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有 4D 生成方法依赖单一模态输入，构建多模态数据集成本高，难以实现任意用户指定的模态到 4D 生成。

**方法**：论文提出 Align4D 框架，将任意模态输入转换为视频-3D 对，利用视频引导运动、3D 数据塑造几何。核心包含三项对齐技术：
- **对象距离对齐**：分别计算视频对齐对象距离（VAOD）和多视图对齐对象距离（MAOD），使 4D 渲染结果同时匹配视频动态和多视图扩散模型的几何先验。
- **运动-几何联合对齐**：通过同步视频与 3D 输入，同时约束已观察视角与未知视角，保证 4D 生成时空一致。
- **异步优化**：将高斯表示的外观属性与变形网络参数分离训练，减少运动-几何耦合，提升质量和训练稳定性。

**结果**：在自建 X4D 数据集及 Consistent4D 基准上，Align4D 在生成质量和一致性方面均达到 SOTA，验证了多模态对齐的有效性。
