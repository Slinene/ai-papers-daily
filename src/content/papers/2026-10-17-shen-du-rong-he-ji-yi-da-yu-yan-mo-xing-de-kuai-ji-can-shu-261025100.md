---
title: 'Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models'
title_zh: 深度融合记忆：大语言模型的块级参数化记忆
authors:
- Rubin Wei
- Siyuan Sun
- Hao Sun
- Yuliang Liu
- Xiang Shi
- Jiarui Wang
- Junming Zhang
- Zhouhan Lin
affiliations:
- LUMIA Lab, Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.25100'
url: https://arxiv.org/abs/2610.25100
pdf_url: https://arxiv.org/pdf/2610.25100
published: '2026-10-17'
collected: '2026-10-23'
category: LLM
direction: 参数化记忆 · 隐藏层深度融合
tags:
- Parametric Memory
- LLM
- Knowledge Injection
- Gated Cross-Attention
- Domain Adaptation
one_liner: 提出块级参数化记忆DFM，训练数据构造检索量降低32倍，并深度融合进隐藏状态，无需在线检索
practical_value: '### 对电商 / 广告 / Agent 的可借鉴点


  - 在电商导购、广告文案或客服 Agent 中，需要给 LLM 注入领域知识（商品库、活动政策、广告规范）。DFM 提供一种冻结主干的参数化记忆方案：推理时无显式检索步骤，延迟低，比
  RAG 更适合高 QPS 线上场景；可训练轻量 memory predictor + fusion 模块，把领域知识压缩进隐藏状态。

  - 块级记忆监督是关键技巧：用 chunk embedding 作为预测目标，而非 token 级目标，训练数据构造的检索 query 可减少 32×、检索条目减少
  2048×。业务数据量大、离线检索成本敏感时，优先考虑把知识切块并做块级记忆，能大幅降低知识注入成本。

  - 门控 cross-attention 融合比输出层插值更深，能让知识影响中间表征；工程上可只插入少数层，冻结原模型，避免灾难性遗忘。适合给已有的推荐/Agent
  底座模型做领域适配而不破坏通用能力。

  - 可迁移到实时交互场景：让 memory predictor 根据对话或行为前文预测 chunk 级记忆，动态融合到解码过程，省去显式检索模块，简化架构并降低运维复杂度。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM 需要获取外部知识，但继续预训练容易导致灾难性遗忘，推理时检索又会带来额外开销。参数化记忆能避免在线检索，但现有方法在训练数据构造上需要大量离线检索，且输出层插值只能做浅层融合。

### 方法
DFM 采用 chunk 级参数化记忆架构：因果 memory predictor 根据前文上下文生成记忆，并以检索到的 chunk embedding 作为监督信号；预测的记忆在同一 chunk 内跨 token 共享，通过 gated cross-attention 融合到中间隐藏状态。训练时冻结 backbone，只端到端训练记忆预测与融合模块；推理时不需要显式检索。

### 结果
与 token 级参数化记忆相比，DFM 构造训练数据所需的检索 query 减少 32 倍，检索条目减少 2048 倍。在 6 个 QA 任务上，DFM 比最强基线在 Mistral-7B-v0.3 上提升 12.71%，在 Qwen3-8B-Base 上提升 11.19%；在领域适配任务上，相对 Qwen3-4B-Base 和 Qwen3-8B-Base 平均分别提升 6.51 和 4.38 个点。
