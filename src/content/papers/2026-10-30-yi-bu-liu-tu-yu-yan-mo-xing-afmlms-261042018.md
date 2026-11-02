---
title: Asynchronous Flow Map Language Models
title_zh: 异步流图语言模型（aFMLMs）
authors:
- Chanhyuk Lee
- Wonjung Kim
- Patrick Pynadath
- Jaehoon Yoo
- Satoshi Hayakawa
- Ruqi Zhang
- Jinwoo Kim
- Seunghoon Hong
affiliations:
- KAIST
- Purdue University
- The University of Tokyo
arxiv_id: '2610.42018'
url: https://arxiv.org/abs/2610.42018
pdf_url: https://arxiv.org/pdf/2610.42018
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: 并行语言模型 · 异步流图
tags:
- Language Modeling
- Flow Map
- Parallel Decoding
- Distillation
- One-step Generation
one_liner: 将 token 预测顺序通过异步流图编码进单步并行语言模型，实现高质量一步生成
practical_value: '- 延迟敏感场景（如搜索结果摘要、推荐理由、广告文案）可借鉴 aFMLM 将教师迭代生成的顺序知识蒸馏到单步学生模型，保持生成质量的同时把推理从多步降到一步，显著降低
  RT。

  - 学习 state-adaptive 的 token 时间调度可作为一种隐式排序机制：模型根据上下文决定哪些 token 先“成熟”，适合需要动态优先级生成的推荐解释或对话式推荐。

  - 蒸馏流程可复用到生成式推荐中的 Semantic ID 序列生成：用教师模型（AR 或扩散）生成顺序信号，训练单步模型快速输出 item ID 序列，降低线上生成延迟。

  - 该方法在 Sudoku 和代码生成等结构化推理任务上有效，提示在需要约束生成的任务（如商品标题、属性组合生成）中，显式建模 token 顺序可能比纯并行生成更优。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：token 预测顺序极大影响语言建模质量。AR 与掩码扩散模型可以在多步生成中利用顺序，但一步并行语言模型如何利用顺序尚不明确。

**方法**：提出异步流图语言模型（aFMLMs）。核心是通过学习异步流的 flow map，把预测顺序引入一步建模。异步流用 token 级时间调度控制每个 token 的相对去噪进度，从而编码生成顺序。作者定义了一类通用异步流，既支持预设调度，也支持学习到的状态自适应调度；证明其 flow map 的有效性，并提出 flow map 蒸馏方法。训练后模型在单次前向中生成全部 token，将顺序编码内化到隐层计算。

**结果**：在 Sudoku 求解和 GSM8K 数学题代码生成上，aFMLM 刷新了一步生成的最新性能。
