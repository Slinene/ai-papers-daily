---
title: 'Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers'
title_zh: Chimera：混合视觉扩散 Transformer 的设计与 Chinchilla 缩放
authors:
- Chongjian Ge
- Hanwen Jiang
- Tianyu Wang
- Jiuxiang Gu
- Yiran Xu
- Ziwen Chen
- Shaoteng Liu
- Jing Shi
- Yicong Hong
- Zefan Cai
affiliations:
- Adobe Research
arxiv_id: '2607.28611'
url: https://arxiv.org/abs/2607.28611
pdf_url: https://arxiv.org/pdf/2607.28611
published: '2026-07-29'
collected: '2026-08-01'
category: Training
direction: 视觉扩散模型的架构与缩放规律
tags:
- diffusion transformers
- hybrid architecture
- scaling laws
- Mixture-of-Experts
- long-context
- compute-optimal
one_liner: 提出混合扩散 Transformer 及异配缩放规则，在图像/视频生成中实现 7.3× 计算效率提升与 30 秒零样本长度外推
practical_value: '- **长上下文高效建模方案可迁移**：Kimi Delta Attention (KDA) 实现 O(N) 复杂度的全局状态跟踪，可用于电商场景中长序列用户行为建模或长视频推荐，降低注意力成本。

  - **多模态统一流处理**：将文本、图像、视频 token 按光栅顺序混合，无需位置编码，可直接借鉴到电商多模态商品描述（图文视频）的统一表征中，简化预处理流程。

  - **MoE 稀疏活化策略**：稀疏 MoE 层在增大模型容量的同时控制激活参数量，适合推荐大模型（如生成式推荐）的扩展，可平衡效果与推理时延。

  - **异构架构的模块化缩放（HeteroP）**：根据张量功能扇入与深度动态分配宽度/深度参数，为推荐模型的不同模块（特征交互、序列建模等）提供差异化缩放指导，避免均匀缩放浪费。

  - **计算最优数据配比洞察**：图像预训练中激活参数量与训练 token 数近乎均分算力，视频则略偏向参数量——可为多模态推荐模型的训练预算分配提供参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：高分辨率图像、长视频生成使扩散 Transformer 的全注意力二次代价不可接受，语言模型的线性注意力方案不能直接迁移到视觉扩散模型（需保留时空局部性和多模态双向交互）。

**方法关键点**：
- Chimera 混合架构：在统一的光栅排序 token 流上，组合三种互补机制——Kimi Delta Attention (KDA) 以 O(N) 复杂度提供长上下文状态跟踪（无需位置编码）、间插的多头潜在注意力 (MLA) 实现全局交互、模态感知短卷积捕获局部时空上下文。
- 稀疏 MoE 层扩展容量，仅 2B 激活参数（总参数 11B）。
- 异构缩放方案 HeteroP：根据每个张量的功能扇入和模型深度，按模块迁移超参数，生成一致调优的模型族，拟合 Chinchilla 风格的计算最优律（激活模型大小、训练 token 数、图文数据比例）。

**关键结果**：
- 预训练扩散损失上，稠密骨干比全注意力 Wan-2.1 (2B) 基线计算效率高 1.7×，完整系统达 7.3×。
- 零样本长度外推：仅用 5 秒视频训练，生成 30 秒视频时最后 5 秒 FID 仅退化 6.5%。
- 缩放律表明：图像预训练中激活模型大小与训练 token 数接近均分算力；视频预训练在较大预算下略倾向模型大小。
