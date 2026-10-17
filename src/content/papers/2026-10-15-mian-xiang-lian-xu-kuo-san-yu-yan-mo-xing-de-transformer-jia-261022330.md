---
title: Designing Transformers for Continuous Diffusion Language Models
title_zh: 面向连续扩散语言模型的 Transformer 架构设计
authors:
- Weijian Luo
- Yujian Chen
- Hao Jiang
- Guang Cheng
- Tianyang Hu
affiliations:
- Polyadic Research Group
- Dots Studio, Xiaohongshu
- Peking University
- SAGA Lab, The Chinese University of Hong Kong, Shenzhen
- The University of California, Los Angeles
arxiv_id: '2610.22330'
url: https://arxiv.org/abs/2610.22330
pdf_url: https://arxiv.org/pdf/2610.22330
published: '2026-10-15'
collected: '2026-10-17'
category: LLM
direction: 连续扩散语言模型 · Transformer 架构优化
tags:
- Diffusion Language Models
- LangDiT
- Transformer Architecture
- Generation Perplexity
- Continuous Diffusion
- Text Generation
one_liner: 提出 LangDiT 架构，通过多项归一化与梯度路由改进，显著降低生成困惑度，刷新连续扩散语言模型 SOTA
practical_value: '- 如果业务中尝试用扩散模型做文本生成（如商品描述、推荐理由、query 扩写），LangDiT 的 QK 归一化、更宽噪声条件和梯度路由技巧可直接迁移，降低生成困惑度。

  - 连续扩散语言模型支持并行解码，适合低延迟文本生成场景，可探索用于实时推荐理由或广告文案生成。

  - 置信度门控训练自条件可在训练时随机用模型自身预测作为条件，提升采样质量且不增加推理成本，适合作为生成式推荐模型的训练 trick。

  - 架构级改进（而非单纯堆参数）对扩散生成质量提升明显，验证了在生成式模型中骨干网络设计的重要性，可借鉴到自研生成式推荐模型的 backbone 优化中。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有连续扩散语言模型（CDLM）大多直接沿用因果 LLM 或图像 Diffusion Transformer（DiT）的架构，未针对扩散去噪过程优化，限制了生成质量。

**方法关键点**：论文系统研究 Transformer 架构对 CDLM 的影响，提出 LangDiT，核心改进包括：1) 特征与 QK 归一化，稳定训练；2) 更宽的噪声条件嵌入，增强模型对噪声水平的感知；3) 似然捷径梯度路由与校准，让似然相关梯度更直接地回传；4) 置信度门控训练自条件，训练时根据置信度使用模型自身预测作为条件，提高采样效率。LangDiT 作为 plug-and-play backbone，保持底层表示、训练目标和采样器不变，仅替换 Transformer 架构。

**关键结果**：在 OpenWebText 上无条件生成 1024 token 序列，LangDiT 在 LangFlow 范式中 GenPPL 降至 21.72（1024 NFE）和 44.72（128 NFE）；在 Plaid 风格 CDLM 中 GenPPL 为 11.33（1024 NFE）和 27.51（128 NFE），均达到新 SOTA。结果表明架构设计是 CDLM 的重要改进来源。
