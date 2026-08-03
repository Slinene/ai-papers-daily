---
title: Scaling Properties of Text Conditioning in Visual Generation
title_zh: 视觉生成中文本条件的缩放特性
authors:
- Zilong Chen
- Chaorui Deng
- Kunchang Li
- Hongyi Yuan
- Haoqi Fan
affiliations:
- ByteDance Seed
arxiv_id: '2607.29679'
url: https://arxiv.org/abs/2607.29679
pdf_url: https://arxiv.org/pdf/2607.29679
published: '2026-07-30'
collected: '2026-08-03'
category: Multimodal
direction: 文本条件缩放 · 结构化提示优化
tags:
- scaling laws
- text conditioning
- structured prompts
- visual generation
- prompt engineering
one_liner: 扩散损失随结构化提示的信息量线性下降，而非标记数，引导出更强的提示器和模型
practical_value: '- **结构化输入比长文本更有效**：在生成式推荐（如商品描述、广告文案生成）中，使用结构化数据（属性键值对）替代冗长自然语言描述，可避免性能饱和，并持续提升生成质量。

  - **量化输入信息量来指导优化**：借鉴 GPG（生成概率增益）和 ED（实体密度）等度量，为推荐场景的 prompt 设计提供可监控指标，寻找信息量-生成质量的最优点，而非盲目增加上下文。

  - **三阶段训练提示器**：将 SFT + 冷启动 + 验证器门控策略蒸馏的管线迁移至推荐系统，训练专用提示器，自动优化用户意图解析、查询重写或对话式推荐的输入生成。

  - **避免“长 prompt 幻觉”**：在 Agent 与 LLM 结合的场景，输入 token 数增加不保证效果提升，应通过结构化注入领域知识（如商品图谱、用户行为标签）来提升信息密度，减少冗余推理。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：文本条件视觉生成中，常见做法是增加 prompt 长度，但扩散损失与 token 数不直接相关。该工作首次量化 prompt 中“结构化信息”对生成质量的影响，发现性能提升的关键不在 token 数量，而在信息的组织和密度。

**方法关键点**：
- 定义两种互补的信息度量：GPG（基于语言模型似然比的结构化信息白盒指标）和 ED（基于实体检测的属性黑盒指标）。
- 在控制实验中发现，收敛扩散损失随 GPG 线性下降、随 ED 幂律下降，而自然语言 prompt 因信息饱和中途停滞。
- 利用该缩放规律，构建结构化 prompt（从图像中提取语义和几何注释），并通过监督微调（SFT）、冷启动（cold-start）和验证器门控的策略蒸馏（on-policy distillation）训练一个专用提示器。

**关键结果**：
- 在组合性、推理和世界知识基准上，该系统（结构化 prompt + 微调提示器）全面超越所有开源模型，并在多数测评上匹配或超越最强闭源模型。
- 对比实验显示，单纯增加自然语言 prompt 长度时，所有开源模型性能均下降，而结构化 prompt 使生成质量单调上升，信息增益与 loss 强相关（r=0.984）。
