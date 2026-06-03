---
title: 'Linear Ensembles Wash Away Watermarks: On the Fragility of Distributional
  Perturbations in LLMs'
title_zh: 线性集成洗去水印：LLM 分布扰动的脆弱性
authors:
- Zhihao Wu
- Gracia Gong
- Qinglin Zhu
- Yudong Chen
- Runcong Zhao
affiliations:
- Department of Informatics, King's College London
- Department of Mathematics, Imperial College London
- Department of Statistics, University of Warwick
arxiv_id: '2605.30501'
url: https://arxiv.org/abs/2605.30501
pdf_url: https://arxiv.org/pdf/2605.30501
published: '2026-05-27'
collected: '2026-06-03'
category: LLM
direction: LLM 安全 · 水印攻击
tags:
- Watermarking
- Ensemble
- Distributional Perturbation
- Vulnerability
- WASH
one_liner: 理论证明并实验验证，简单平均多个水印模型的输出概率即可破坏常见水印方案，并提出了解决异质模型集成难题的 WASH 方法。
practical_value: '- 如果业务用多个 LLM 生成内容（如商品文案、对话回复），通过输出概率平均或 token 级融合，不仅可能无意中抹除内置水印，还能提升生成质量（本文集成
  3 模型质量提升 27.5%），可作为工程上的一种提升多样性与可靠性的 trick。

  - 依赖水印进行 AI 文本鉴别（如虚假评论检测、内容溯源）的业务需警惕多模型集成攻击：即使对手只能调用 API，也能通过侧信道获取 logits 或近似分布，类似方法可低成本削弱水印；防御方需考虑跨模型协同或更鲁棒的嵌入方式。

  - 提出的 WASH 方法解决了不同模型词表、分词不一致的实际难题，利用动态映射和对齐技术实现快速集成（比最佳基线快 6 倍），这种异构模型融合思路可直接用于多模型
  A/B 测试在线集成，或构建具备容灾能力的推荐/Agent 生成链路。

  - 对于需要反向利用水印的场景（如规避平台查重），本文揭示了只需 3-5 个模型的输出平均即可让检测 z-score 从数百降至 2 以下，提示业务中若采用第三方水印检测服务，其可靠性会因用户多模型选择而大打折扣。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基于水印的 AI 文本检测旨在通过统计签名追溯生成来源，但现实用户常可访问多个 LLM（如不同的商业 API）。水印本质是施加在模型输出分布上的扰动，不同提供商的水印扰动通常相互独立。论文从理论和实验展示，只需平均少量水印模型的输出概率，即可恢复原始分布，使水印失效，构成根本性脆弱。  
**方法**：理论证明，对于任意二阶可微的扰动，平均 K 个独立水印分布能以 O(1/K) 的速率收敛至无水印分布。实验上，简单平均 3–5 个模型的 logits 或概率即可显著压制检测信号。为解决异构模型在词表、分词上的差异，提出 WASH（Watermark Attenuation via Statistical Hybridisation），通过词表对齐映射和基于熵的融合策略，实现高效的集成生成。  
**关键结果**：在 6 种主流水印方案（KGW、Aar、Unigram 等）和 3 个 LLM（LLaMA、Mistral 等）上，集成 3 个模型可将检测 z-score 从 5–300 降至 2 以下（低于检测阈值 4），TPR@5%FPR 降至 50% 以下；同时生成质量（由 GPT-4 评估）提升 27.5%，长序列生成速度比最优基线快 6 倍。结果强烈表明，依赖水印进行鲁棒 AI 文本检测要么需接受此脆弱性，要么需前所未有的模型供应商协作。
