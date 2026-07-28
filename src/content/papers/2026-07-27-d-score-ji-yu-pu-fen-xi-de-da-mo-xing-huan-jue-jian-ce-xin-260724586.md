---
title: 'D-Score: A Spectral Hidden-State Signal for Hallucination Detection in Large
  Language Models'
title_zh: D-Score：基于谱分析的大模型幻觉检测信号
authors:
- Bianca Raimondi
- Davide Evangelista
- Maurizio Gabbrielli
- Elena Loli Piccolomini
affiliations:
- Department of Computer Science and Engineering, University of Bologna
arxiv_id: '2607.24586'
url: https://arxiv.org/abs/2607.24586
pdf_url: https://arxiv.org/pdf/2607.24586
published: '2026-07-27'
collected: '2026-07-28'
category: Eval
direction: LLM幻觉检测 · 隐藏状态谱方法
tags:
- Hallucination Detection
- Hidden Activations
- Singular Values
- Spectral Methods
- Mechanistic Interpretability
one_liner: 提出D-Score，利用隐藏状态奇异值方向数检测LLM幻觉，单次前向传播无需外部工具
practical_value: '- 在电商/推荐场景中，LLM生成推荐理由或商品描述时，可集成D-Score作为轻量级幻觉过滤器，仅需单次前向的隐藏状态，不增加额外推理延迟。

  - 方法不依赖外部知识库或多轮生成，适合高并发在线系统，可在生成后实时判定文本可信度，降低人工审核成本。

  - 隐藏状态谱特征对事实冲突敏感，可作为RAG检索增强生成中的补充校验信号，辅助判断生成内容是否与检索证据一致。

  - 可将D-Score思路迁移至Agent行为检测，例如监控Agent生成的计划或动作是否与内部模型知识矛盾，增强Agent可靠性。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM生成的文本可能流畅但包含事实错误（幻觉），现有检测方法多依赖外部知识库或多次采样，成本高。研究者发现，当模型处理与自身内部知识冲突的文本时，隐藏层表示可能同时编码断言及其矛盾证据，导致表示向量在更多奇异方向上扩散，为检测幻觉提供了信号。

**方法**：提出D-Score，一种基于奇异值分解的简单谱统计量。对固定模型层，将隐藏激活向量按token排列成矩阵，计算奇异值，设置容忍参数ε，统计与最大奇异值接近（比值≥1-ε）的奇异方向数作为幻觉分数。分数越高，表示表示扩散越强，越可能幻觉。D-Score仅需单次前向传播，无需外部验证器或检索，计算开销低。

**结果**：在FAVA-Annotation和RAGTruth两个基准上评估，D-Score展现出强大的幻觉检测能力，能有效区分事实正确与错误的生成，且泛化性良好，在不同任务和模型上均保持有效性。
