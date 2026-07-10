---
title: A Practical Investigation of Training-free Relaxed Speculative Decoding
title_zh: 无需训练的宽松投机解码实用研究
authors:
- Guoxuan Xia
- Luka Ribar
- Paul Balanca
affiliations:
- Imperial College London
- Graphcore
arxiv_id: '2607.08690'
url: https://arxiv.org/abs/2607.08690
pdf_url: https://arxiv.org/pdf/2607.08690
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM推理加速 · 投机解码优化
tags:
- speculative decoding
- relaxed verification
- inference acceleration
- draft model
- speed-quality trade-off
one_liner: 统一宽松投机解码框架，实证发现放松保真度需仔细能力评估，且依赖强草稿模型
practical_value: '- 在电商搜索自动补全、对话推荐等延迟敏感场景，可尝试放松标准投机解码的无损约束以榨取更多加速，但必须针对具体任务（如Query推荐准确率、CVR）设计能力评估，在线灰度实验必不可少。

  - 草稿模型必须是一个足够好的语言模型（如原LLM的压缩版或同架构小模型），不宜使用纯为多token预测设计的轻量专用草稿器，否则加速但质量崩坏。

  - 统一框架中，Top‑k与Top‑p结合的接受准则在权衡中表现较鲁棒，可作为工程落地的起点，无需额外训练。

  - 当线上主模型与草稿模型输出分布差异大时，放松策略可能引入难以察觉的降质，建议在离线多维度评测（困惑度、任务指标、人工评估）中模拟长尾请求，避免“平均加速好看但头尾体验分化”。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**
标准投机解码通过小模型草稿、大模型并行验证实现无损加速，但严格无损保证可能限制了提速上限。近期研究提出放松这一约束，允许以可控质量损失换取更高速度。本文系统实证研究多种**无需训练的宽松投机解码技术**，旨在为实践者提供清晰指南。

**方法关键点**
- 统一框架：将Top‑k、Top‑p核采样、阈值接受等放松策略归入同一数学表述，方便横向比较。
- 实验设置：选用不同能力等级的草稿模型（如同架构小LLM、专用多token预测器），在多个基准任务上测量加速比与质量变化。
- 评估维度：除吞吐量外，强调**能力评估**（如困惑度、下游任务精度），揭示放松不易察觉的降质。

**关键结果**
- 放松策略可带来最高约**2‑3倍额外加速**（相对标准投机解码），但相应质量损失高度依赖草稿模型能力。
- **草稿模型必须是一个好的语言模型**：纯为多token预测设计的轻量专用草稿器在放松模式下性能暴跌，不适合实际应用。
- 放松方法需要比标准解码更谨慎的能力监控，因为速度提升可能掩盖分布偏移。
