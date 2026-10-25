---
title: 'Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via
  CubeAtlas'
title_zh: 通过CubeAtlas实现无畸变无缝全景生成
authors:
- Xuhui Zuo
- Chenjie Cao
- Tengfei Wang
- Junta Wu
- Yisu Zhang
- Chunchao Guo
affiliations:
- Tencent
arxiv_id: '2610.31565'
url: https://arxiv.org/abs/2610.31565
pdf_url: https://arxiv.org/pdf/2610.31565
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 全景图像生成 · 扩散Transformer
tags:
- Panorama Generation
- Diffusion Transformer
- CubeAtlas
- Sparse Attention
- Super-Resolution
one_liner: 提出CubeAtlas表示与布局感知稀疏注意力，单次前向生成几何一致的全景图
practical_value: '- 直接可借鉴点有限：全景生成与电商推荐核心链路基本无关，主要学术贡献。

  - 布局感知稀疏注意力：当 token 布局有明确空间结构时（如商品多视图、场景图），可依据几何关系裁剪注意力矩阵，减少计算同时保持跨视图一致性，对多模态商品内容生成有参考价值。

  - 训练自由超分与融合：在不重新训练的情况下提升高分辨率细节，可借鉴用于电商图片/视频后期增强。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：生成360°全景图需同时保证局部透视保真与全局球面连续性。现有 ERP 表示无缝但畸变大且与预训练图像生成器存在域差距；cubemap 保持透视几何但跨面不一致、接缝明显。

**方法关键点**：提出 CubeAtlas 表示，将全部 cubemap 面展开为单一紧凑画布，旋转极地区域并与赤道面方向对齐，既保留 cubemap 的透视几何，又组织跨面关系以支持无缝拼接。该表示使预训练 Diffusion Transformer 能在单次前向中联合建模完整全景，无需修改骨干网络或位置编码。CubeAtlas 的 token 数与 ERP 相当，但结构化布局使得大量密集注意力不必要，因此引入布局感知稀疏注意力掩码，保留全景连续性所需的交互，移除几何无关的 token 对，在更低的注意力计算下取得优于 ERP 的质量。此外，提出免训练超分技术与融合方案，在无畸变透视空间中增强细节后再合成最终 ERP 全景。

**关键结果**：在多个基准测试上，相比先前方法提升了几何保真度、跨视图一致性与高分辨率视觉质量；同时注意力计算低于 ERP 建模。
