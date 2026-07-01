---
title: Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment
title_zh: RAG上下文增强的分解：元数据、结构与检索策略对齐
authors:
- Saber Zerhoudi
- Michael Granitzer
- Jelena Mitrovic
affiliations:
- University of Passau
- Interdisciplinary Transformation University Austria
arxiv_id: '2606.29645'
url: https://arxiv.org/abs/2606.29645
pdf_url: https://arxiv.org/pdf/2606.29645
published: '2026-06-28'
collected: '2026-07-01'
category: RAG
direction: RAG上下文增强与模型能力对齐
tags:
- RAG
- context enrichment
- metadata
- evaluation
- model alignment
- processability hierarchy
one_liner: 控制实验揭示大多数RAG上下文增强反而降低准确率，模型-上下文对齐比元数据堆砌更重要
practical_value: '- 在电商搜索/推荐的 RAG 场景中，避免盲目添加置信度、时间戳等元数据，应先在目标模型上测试该元数据是否提升下游准确率。

  - 提示词微调时，若显式要求模型利用某类元数据（如分数），需警惕模型“遵从但答错”的现象，可通过 ablation 实验验证元数据的实际效用。

  - 元数据格式选择应与模型的预训练特性对齐：若模型在预训练时少见结构化记录，可能无法有效利用，反而可改用简单自然语言描述。

  - 多跳检索策略需谨慎：复杂证据链可能引入噪声，仅在模型能力足够时采用，且可通过早期停止或置信度筛选控制上下文质量。

  - 小模型在元数据-任务对齐时可超过大模型，在资源受限的线上推理中，优先考虑选择与上下文格式兼容的轻量模型，而非一味堆参数。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：当前 RAG 系统普遍通过附加质量元数据（如置信度、时间戳）、将段落结构化为显式记录、采用多跳检索策略来丰富上下文，并假设更丰富的上下文直接导致更好的生成答案。但现有评估无法分离这三种因素的影响，无法验证这一假设。

**方法**：在六个知识密集型基准上设计控制实验，依次隔离元数据（5种元数据类型）、结构（自由文本 vs 结构化记录）与检索策略（单跳 vs 多跳）三个维度，使用四种模型（覆盖三家模型家族），生成超过24,000个回答进行评估。

**关键结果**：
- 大多数上下文丰富操作反使准确率下降，与“越丰富越好”的假设相悖。
- 模型能遵从“使用置信度得分”的指令，但实际答案质量恶化，揭示了元数据利用度与准确率之间的脱节。
- 当元数据类型与模型能力对齐时，较小模型可超越前沿模型19 F1分。
- 由此提出**可处理性层级**：仅凭模型预训练特性即可预测其对某类元数据的利用效能，将 RAG 设计重新定义为模型-上下文对齐问题，而非元数据累积问题。
