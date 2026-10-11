---
title: 'Latent Core Tokenizer: Compress, but Meaningfully'
title_zh: 潜在核心分词器：压缩，但要有意义
authors:
- Felermino D. M. A. Ali
- Millicent Ochieng
- Ogbemi Ekwejunor-Etchie
- Ade Famoti
- Jacki O'Neill
- Debjit Paul
affiliations:
- Microsoft Research Africa
- Microsoft Research Accelerator
- Microsoft Research India
arxiv_id: '2610.12376'
url: https://arxiv.org/abs/2610.12376
pdf_url: https://arxiv.org/pdf/2610.12376
published: '2026-10-08'
collected: '2026-10-11'
category: Training
direction: 多语言 tokenizer 结构发现与词表构建
tags:
- tokenizer
- multilingual
- BPE
- morphology
- vocabulary
- MDL
one_liner: 提出 LCT 将结构发现与词表构建解耦，用形态约束提升多语言分词质量
practical_value: '- 多语言电商/搜索场景若自建或扩展 tokenizer，可把结构发现与词表构建解耦，用 MDL/熵边界/形态约束代替纯 BPE
  frequency merge，优先保障低资源语言可复用单元。

  - 用 fertility 和 MorphScore 评估现有 tokenizer 的语言公平性；对高 fertility 语言做定向词表扩展或 capacity
  重分配，可降低线上 LLM 推理成本。

  - 生成式推荐/推送文案涉及多语言时，词表质量直接影响序列长度与表示质量；LCT 的结论说明分配词表 capacity 要考虑语言形态结构，而非仅语料频率。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：主流 tokenizer 以压缩为目标，但紧凑词表在多语言间分配不均，高频语言抢占容量，低资源语言 fertility 高、序列长。压缩好不代表表示质量好。

**方法关键点**：LCT 将结构发现与词表构建解耦。先基于 Minimum Description Length、熵边界信号和 morphotactic 约束识别可复用的语言结构单元，再构建共享词表；不依赖单一频率统计。

**关键结果**：在 104 语言、200K 词表下，LCT 的 fertility 更低、MorphScore 更高，跨语言 tokenization 成本差距与 BPE/Unigram/parity-aware BPE 相当；在四个多语言下游 benchmark 上，总分分别比 BPE、Unigram、parity-aware BPE 高 1.48、1.83、2.00 分。
