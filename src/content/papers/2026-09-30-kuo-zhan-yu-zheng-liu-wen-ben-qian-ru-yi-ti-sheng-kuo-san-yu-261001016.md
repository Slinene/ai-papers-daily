---
title: Scaling and Distilling Text Embeddings for Better Diffusibility
title_zh: 扩展与蒸馏文本嵌入以提升扩散语言模型适用性
authors:
- Zekai Zhang
- Yunjie Tian
- Yanjin He
- Xiaoyan Zhang
- Dongdi Zhao
- Qing Qu
- Di Fu
affiliations:
- University of Michigan
arxiv_id: '2610.01016'
url: https://arxiv.org/abs/2610.01016
pdf_url: https://arxiv.org/pdf/2610.01016
published: '2026-09-30'
collected: '2026-10-02'
category: LLM
direction: 扩散语言模型 · 文本嵌入蒸馏
tags:
- diffusion language models
- text embeddings
- distillation
- latent diffusion
- generative perplexity
one_liner: 通过扩展嵌入模型并用解码概率软标签蒸馏，使连续扩散语言模型生成有效文本，Gen PPL 17.8 优于 GPT-2-M
practical_value: '- 在生成式推荐或 Semantic ID 场景中，若用扩散模型生成 item/query 嵌入，不要直接使用过度判别的预训练编码器；可借鉴“教师解码概率作为软标签”的蒸馏方式，使相近候选嵌入更聚拢，提升解码有效性和生成质量。

  - 对 query 推荐/改写、push 文案生成等文本生成任务，可在训练连续扩散 LM 时加入 embedding 蒸馏阶段，让潜在空间更连通，减少无效输出（如解码到不存在的
  token 或语义 ID）。

  - 评估生成式模型时，除 PPL 外可引入“生成熵 vs. Gen. PPL”曲线，判断模型能否在真实文本熵水平下保持低困惑度，作为业务中生成质量的上线 benchmark。

  - 这种先缩放再蒸馏的思路也可迁移到多模态或商品图文表示：用更大 teacher 的 soft targets 蒸馏轻量 embedding，提升下游扩散/生成模型的稳定性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：连续扩散语言模型将隐式扩散用于连续文本嵌入，核心是选择最易扩散的潜在空间。实验发现同一家族中扩展嵌入模型（T5→T5Gemma-1→T5Gemma-2）能显著提升生成性能，但原始 T5Gemma-2 嵌入过度判别，连备选词嵌入都彼此远离，对采样误差敏感，生成时常落到无效嵌入。

**方法关键点**：将 T5Gemma-2 蒸馏到学生编码器，使用教师解码概率作为软标签；这种软标签约束拉近备选词嵌入，同时保持编码-解码机制，形成更连通、更易扩散的潜在空间。

**关键结果**：中型 DLM 在 OpenWebText 上达到 Gen. PPL 17.8（真实文本 PPL 15.4），在真实文本熵水平下优于 GPT-2-M 的 Gen. PPL；蒸馏嵌入使生成嵌入至少解码到有效候选词。
