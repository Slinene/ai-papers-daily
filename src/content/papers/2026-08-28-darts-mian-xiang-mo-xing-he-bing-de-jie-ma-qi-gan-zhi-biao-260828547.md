---
title: 'DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging'
title_zh: DARTS：面向模型合并的解码器感知表征手术调优
authors:
- Aaryan Ajay Sharma
- Sai Nishanth Padala
- Seganrasan Subramanian
affiliations:
- ServiceNow
- University of Twente
arxiv_id: '2608.28547'
url: https://arxiv.org/abs/2608.28547
pdf_url: https://arxiv.org/pdf/2608.28547
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: 模型合并 · 解码器表征偏差校正
tags:
- Model Merging
- Representation Bias
- Decoder LLM
- Entropy-Weighted Loss
- Post-Training Correction
one_liner: 提出熵加权 L1 与逐位置偏置，解决解码器模型合并后的表征偏差累积问题
practical_value: '- 多任务 LLM 合并部署：如果有商品标题生成、广告文案、搜索 Query 改写等多个 FT/LoRA 模型，DARTS 提供后训练校正路径：合并后用极小参数（0.1%）的逐位置偏置修正
  hidden states，避免逐任务部署，降低线上 GPU/显存成本。

  - 熵加权对齐思路：在蒸馏、对齐或模型合并时，不要对所有 token 同等对待；对高熵（决策临界）位置加大 L1 回归权重，更直接影响生成质量，可迁移到生成式推荐/文案生成的
  loss 设计与难例挖掘。

  - 位置相关偏置比线性投影更省参且低延迟：因果 mask 下偏差沿 token 位置累积，用 per-position additive bias 捕捉位置误差，serving
  时只是 elementwise add，适合低延迟推理。

  - 注意合并模型通常仍弱于任务独立模型，适合对延迟/显存敏感、质量可接受权衡的场景；上线前用业务集做 A/B 验证。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：模型合并可将多个 task-specific fine-tuned LLM 合成为单个多任务模型，但 merged model 存在 representation bias，即 hidden states 与各源模型的系统偏差。此前工作仅针对 encoder 视觉模型；本文首次分析 decoder 模型中的该问题。

方法关键点：
- 发现两个 decoder 特有挑战：causal attention mask 导致 bias 沿 token 位置累积，需位置相关校正；不同 token 位置重要性不同，高熵位置更关键。
- 提出 DARTS：用 entropy-weighted L1 loss，在高熵位置加大校正权重；采用 per-position additive bias 捕捉位置相关误差，避免过参数化。

结果：在 Llama-2-7B 上覆盖 code generation（HumanEval）、math reasoning（GSM8K）、instruction following（AlpacaEval），相比标准 surgery 方法显著提升，并仅增加 0.1% 总参数。
