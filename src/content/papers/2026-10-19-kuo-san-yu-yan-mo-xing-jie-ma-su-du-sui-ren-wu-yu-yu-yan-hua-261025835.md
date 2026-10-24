---
title: Diffusion Language Models Change Speed Across Tasks and Languages
title_zh: 扩散语言模型解码速度随任务与语言变化
authors:
- Mohsen Fayyaz
- Ali Modarressi
- Daniel Israel
- Lucas Bandarkar
- Nanyun Peng
affiliations:
- University of California, Los Angeles
- CIS, LMU Munich
- Munich Center for Machine Learning
arxiv_id: '2610.25835'
url: https://arxiv.org/abs/2610.25835
pdf_url: https://arxiv.org/pdf/2610.25835
published: '2026-10-19'
collected: '2026-10-24'
category: LLM
direction: 扩散LM推理成本与解码速度分析
tags:
- Diffusion LMs
- Inference Efficiency
- Decoding Speed
- Multilingual
- Self-Consistency
- Cost Analysis
one_liner: 扩散LM前向次数由输出新颖性与词稀有度决定，解码速度加权候选可提升推理准确率4.2点
practical_value: '- 生成式任务可借鉴“解码步数作为难度/置信度信号”：在生成推荐理由、广告文案、搜索词推荐时，用前向次数或解码速度对候选结果排序或早停，低成本的候选往往更可靠。

  - 对不同类型的生成任务设置差异化资源预算：复制/改写类任务（如 query 改写、标题生成）成本低，开放式生成（如创意文案）成本高，可在系统中动态分配超时或批大小。

  - 多语言场景需额外考虑每 token 成本：高 tokenization 的语言不仅 token 数多，每 token 前向次数也更高，在估算延迟或做多语言资源分配时应加权而非只看
  token 数。

  - 用解码速度加权候选答案优于多数投票，在集成多个生成结果时可以在不增加额外成本的前提下提升可靠性，适合用于生成式推荐或 Agent 的最终答案选取。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：扩散语言模型可以一次前向生成多个 token，但相同长度输出的前向次数差异很大，理解成本变化因素对部署和优化至关重要。

**方法关键点**：在 DiffusionGemma-26B-A4B-it 和 DreamReasoner-8B 两个扩散模型上，对 10 个任务统计每输出 token 的前向次数；分析输出相对输入的新颖性比例、词在任务内的稀有度对成本的影响；覆盖多语言和数学推理场景。

**关键结果**：任务类型决定成本：复制或轻度编辑输入的任务便宜，开放式写作成本高昂——故事生成每 token 前向次数是语法纠正的 3 倍以上。输出新颖性和词稀有度能解释大部分成本差距；当输出包含推理过程时，最终答案若重复推理轨迹则便宜，新增内容则昂贵。多语言中，高 tokenization 的语言每 token 前向次数也更高，在 token 数量成本之上叠加额外开销。成本与正确性相关：同一数学问题上错误答案比正确答案需要更多前向次数；用解码速度加权候选答案比多数投票高 4.2 分且无额外成本。
