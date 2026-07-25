---
title: 'QuantiBias: Benchmarking Quantization-Induced Bias in LLMs'
title_zh: QuantiBias：量化 LLM 的开放式偏见基准测试
authors:
- Emilio Ferrara
affiliations:
- University of Southern California
arxiv_id: '2607.21063'
url: https://arxiv.org/abs/2607.21063
pdf_url: https://arxiv.org/pdf/2607.21063
published: '2026-07-23'
collected: '2026-07-25'
category: Eval
direction: 量化偏差评测
tags:
- Quantization
- Bias
- LLM Safety
- Benchmark
- Open-ended Generation
- Multilingual
one_liner: 量化模型通过标准安全检测却常在开放式生成中输出刻板印象，须单独评估
practical_value: '- 业务中部署量化 LLM（如对话推荐、广告文案生成）时，仅靠拒绝检测和选择题安全评估不够，需补充开放式生成场景的偏差抽样，否则可能放大隐性刻板印象。

  - 可借鉴 QuantiBias 的控制条件设计：配对无害/有害拒绝探测、多项选择与开放式生成，构建内部审查工具，精确分离生成过程中的偏见来源。

  - 尝试在 prompt 中引导模型逐步推理（CoT），可能在某些 backbone 上显著降低量化引入的开放式偏见（实验中减半），可作为无成本的缓解措施先上线验证。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：部署 LLM 时广泛采用训练后量化以达到效率要求，该步骤通常被认为无损且不再重新评估安全性。本文发现，量化模型能通过常规的安全检查（拒绝有害请求、不过度拒绝、多选题无偏差），但在开放式生成中会输出更多刻板印象，标准评测无法暴露这一隐患。

**方法关键点**：设计 **QuantiBias** 基准，整合三个控制条件：(1) 多语言刻板印象开放式探测；(2) 拒绝探测与多项选择，用于隔离生成偏差；(3) 有无思维链的对比，并评估生成内容严重性。在 Qwen、Gemma 两族模型，五个量化家族（GPTQ、AWQ 等）、八项基准上测试。

**关键结果**：量化模型在开放式回答中约有 24%~27% 的回复被独立评判员认定为包含刻板印象，且标准安全测试完全无法察觉这一偏差；偏差的选择性存在（仅见于开放生成）是稳健结论，但其随压缩程度进一步增加的趋势则对评测方法敏感。引入推理在某些模型族上可将开放偏差减半，但在其他族上无效。结论强调：任何量化模型发布前必须重新进行开放式偏见评估，不可仅依赖短形式的安全检测。
