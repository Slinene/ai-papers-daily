---
title: StepAudio 3 Gen Technical Report
title_zh: StepAudio 3 Gen 技术报告
authors:
- Bin Lin
- Bo Zhao
- Boyang Wang
- Boyang Zhang
- Boyong Wu
- Chao Yan
- Chen Geng
- Chen Wu
- Cheng Yi
- Chengli Feng
affiliations:
- StepFun-Audio Team
arxiv_id: '2609.12945'
url: https://arxiv.org/abs/2609.12945
pdf_url: https://arxiv.org/pdf/2609.12945
published: '2026-09-10'
collected: '2026-09-15'
category: Other
direction: 通用音频生成 · 离散自回归
tags:
- Audio Generation
- TTS
- RVQ
- Discrete Autoregressive
- Unified Model
- Progressive Pretraining
one_liner: 离散自回归统一音频生成模型，基于 RVQ token 和共享码本，在 TTS 与语音设计上达到 SOTA
practical_value: '- 离散 RVQ 表示将音频压缩为 16×2048 码本、12.5 Hz 帧率，类似 Semantic ID 思路，可借鉴用于多模态商品表示或用户行为序列的离散化，降低序列长度、统一语义和声学信息。

  - RVQ Adaptor 作为 LLM 与多码本之间的适配层，把 16 个残差码本映射进 LLM 隐藏维度，适合在已有文本 LLM 上接入新的离散模态（如商品图像、音频评论）时参考。

  - 干扰感知的渐进式预训练：先冻结 LLM 只训练 Adaptor，再逐步解冻，能保留原有文本能力，对在推荐/搜索 LLM 上增量添加生成式任务有直接借鉴价值。

  - 采用“时间轴自回归 + 码本轴并行生成”的两阶段解码，相比全自回归大幅降低推理步数，可迁移到生成式推荐中处理多层语义 ID 的生成。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：音频生成各领域（TTS、音效、音乐、歌声）长期独立发展，模型表示不兼容，难以满足真实应用中对多类型音频混合生成的需求。

**方法关键点**：StepAudio 3 Gen 采用离散自回归生成范式，放弃扩散 Transformer 的连续生成路线。其核心包括：
- StepAudio Tokenizer 将通用音频压缩到 12.5 Hz 的 16×2048 残差码空间，每层码本同时保留语义和波形声学信息；
- 生成时主干 LLM 沿时间轴自回归预测第一层码本，再用轻量 causal Transformer 沿码本轴并行补全其余 15 层，平衡生成质量与效率；
- 提出三项设计原则：干扰感知的渐进式预训练，在获取音频能力的同时保留 LLM 文本能力；RVQ Adaptor 用于将多码本声学表示有效注入 LLM；跨音频域共享离散自回归表示。

**关键结果**：通过渐进预训练、多任务指令训练和监督微调，模型在 TTS 和语音设计（voice design）上达到 SOTA，并同时保持语音、歌声、音效、音乐的强生成能力。
