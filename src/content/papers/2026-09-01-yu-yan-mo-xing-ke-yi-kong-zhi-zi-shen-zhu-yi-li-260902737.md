---
title: Language Models Can Control Their Own Attention
title_zh: 语言模型可以控制自身注意力
authors:
- Namgyu Ho
- Huzama Ahmad
- Woosung Koh
- Se-Young Yun
- Tal Schuster
- Cicero Nogueira dos Santos
affiliations:
- KAIST AI
- Google DeepMind
arxiv_id: '2609.02737'
url: https://arxiv.org/abs/2609.02737
pdf_url: https://arxiv.org/pdf/2609.02737
published: '2026-09-01'
collected: '2026-09-04'
category: LLM
direction: LLM 长上下文稀疏注意力
tags:
- Declarative Attention
- Sparse Attention
- KV Cache
- Long-context
- LLM Inference
one_liner: 提出声明式注意力协议，让模型在思维链中显式声明注意力范围，零训练实现长上下文稀疏注意力
practical_value: '- 在长上下文多轮对话（电商客服、购物助手、推荐解释 Agent）中，把历史对话、商品信息、检索结果切分为可寻址片段，让模型通过
  `<focus>` 标签声明需要关注的片段，可减少 50% 以上的 KV cache 读取，适合大 batch 在线服务降延迟。

  - 与 RAG/工具调用结合：将检索到的商品/广告/知识片段作为模拟工具返回的“magic chunk”，模型在推理中自行选择关注哪些片段，避免每步全量扫描，可显著降低多文档推理成本。

  - 工程上可直接复用论文的 vLLM 集成思路：通过 hook 改写 KV cache block table 实现块对齐掩码，不改内核、兼容 FlashAttention，适合快速在现有推荐/搜索
  Agent 服务中落地。

  - DA 的注意力计划以文本形式输出，可审计模型在推荐解释、搜索排序中具体关注了哪些输入，用于优化上下文构造和检索策略；未来还可结合 KV cache offloading
  实现可逆上下文压缩，适合长会话 Agent。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

长上下文推理时，Transformer 每步都需读取整个 KV cache，但实际注意力高度稀疏。现有稀疏注意力方法要么依赖静态启发式，要么每步扫描全缓存，复杂度仍为 O(N)。本文提出一种新思路：让模型在思维链中用自然语言显式声明接下来要关注哪些上下文片段，推理引擎据此动态构造注意力掩码，从而跳过大部分 KV 读取。该方法无需任何训练，只靠提示在现成模型上零样本生效。

## 方法关键点

- **三模式协议**：定义 `<global>`（全上下文导航）、`<focus>`（只关注指定 chunk）、`<local>`（仅关注当前输出流）三种注意力模式，模型可自由切换。
- **可寻址上下文**：将长上下文切分为约 2K token 的“magic chunk”，并以模拟工具调用格式呈现，使模型能通过 chunk 编号引用具体片段。
- **状态机解析**：推理引擎解析输出中的模式标签，在标签边界切换注意力掩码；掩码按块对齐应用，与 FlashAttention 等现有核兼容。
- **工程集成**：在 vLLM 中通过 hook 改写 KV cache block table，不改内核，实现注意力节省。

## 关键结果

在 15 个长上下文基准（RULER、LongBench v1/v2、LooGLE、ZeroScrolls）上，对 Gemma-4-31B 和 Qwen-3.6-27B 零样本评估：

- 解码期间总 attended tokens 分别减少 **52.0%** 和 **31.1%**，准确率仅下降 1.27pp 和 2.75pp。
- 与同提示但无掩码的消融相比，DA 的掩码带来 71.1%（Gemma）和 46.5%（Qwen）的 attended tokens 减少，说明效率主要来自掩码而非提示格式。
- 相对准确率随模型规模增大而提高（Gemma 4B 仅保留 29%，31B 达 99%），表明该协议受益于模型基础能力。
- 节省随上下文长度增大，最长任务中单响应可节省约 21M 个 attended tokens；预估 B200 上解码墙钟时间降至 0.71×（Gemma）和 0.77×（Qwen）。

**最值得记住的一句话**：模型能在思维链中显式声明注意力范围，将稀疏注意力的选择成本降为零，零训练即可获得约 50% 的注意力节省。
