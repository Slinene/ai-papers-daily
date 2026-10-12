---
title: 'Surfing the Activation Wave: Analyzing the Information and Geometry of LLM
  Hidden States for Speculative Decoding'
title_zh: 驾驭激活波：分析 LLM 隐藏状态信息与几何以支持推测解码
authors:
- Raghavv Goel
- Sudhanshu Agrawal
- Mukul Gagrani
- Risheek Garrepalli
- Mingu Lee
affiliations:
- Qualcomm AI Research
- Stanford University
arxiv_id: '2610.12939'
url: https://arxiv.org/abs/2610.12939
pdf_url: https://arxiv.org/pdf/2610.12939
published: '2026-10-08'
collected: '2026-10-12'
category: LLM
direction: LLM 推理加速 · 推测解码层选择
tags:
- Speculative Decoding
- Hidden States
- Matrix Entropy
- CKA
- LLM Inference
- Layer Selection
one_liner: 提出基于矩阵熵与 CKA 的 LLM 多隐藏层选择框架，在 EAGLE3 推测解码中优于固定层选择
practical_value: '- 在 EAGLE3 类推测解码中不要盲用 [2, N//2, N-3] 等固定层，可用矩阵熵（informativeness）+
  CKA（diversity）选择低冗余、高信息层，改善 draft 模型质量与加速比。

  - token-entropy filtering 可过滤低预测熵 token 后再计算层选择统计，避免高频简单 token（如电商搜索中的常见 query、模板化文案）污染层重要性评估。

  - CKA 跨层相似度分析能定位 decoder 中的几何/信息 compartment，帮助工程上决定哪些层适合共享、蒸馏或做 KV cache 优化。

  - 对于用 LLM 做实时生成式推荐、搜索词/广告文案生成的业务，选择 hidden states 子集而非全部层，可在不显著掉质量的情况下减少 draft 模型输入维度，节省推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推测解码方法如 EAGLE3 通常用多个目标模型层作为 draft 模型输入，但层选择依赖位置启发式规则，组合空间大，缺乏原则性依据。

**方法**：作者提出基于两个互补标准的层选择框架——信息量用矩阵熵度量，多样性用 centered kernel alignment (CKA) 度量。分析逐层 Shannon 熵、拼接后的聚合熵以及成对 CKA 随深度的变化，发现 decoder 表示中存在明显的几何与信息分隔。基于此设计熵与 CKA 驱动的层选择算法，倾向选择信息量高且冗余低的层集。为进一步提高统计质量，引入 token-entropy filtering，过滤低预测熵 token 的隐藏状态。

**结果**：在 EAGLE3 推测解码设置下，自动选择的层集优于固定基线，包括默认的 [2, N//2, N-3] 规则；同时解释了某些默认规则仍具竞争力的原因。该框架为多隐藏层选择提供了实用配方，并揭示 LLM decoder 状态的信息几何结构。
