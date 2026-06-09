---
title: Augmenting Attention with Exponentially Decaying Memory Improves Query-Aware
  KV Sparsity
title_zh: 用指数衰减记忆增强注意力提升查询感知KV稀疏性
authors:
- Xiuying Wei
- Caglar Gulcehre
affiliations:
- EPFL
- CLAIRE
arxiv_id: '2605.28640'
url: https://arxiv.org/abs/2605.28640
pdf_url: https://arxiv.org/pdf/2605.28640
published: '2026-05-26'
collected: '2026-06-09'
category: LLM
direction: 查询感知KV稀疏 · 指数衰减记忆增强
tags:
- KV cache
- sparse attention
- exponential decay
- long-context
- RAT+
- inference efficiency
one_liner: 利用RAT+的指数衰减记忆模块，一致提升Quest、MoBA、SnapKV等查询感知稀疏方法在长上下文任务上的准确性。
practical_value: '- 若电商或Agent系统中部署长上下文LLM（如处理长对话或大量商品描述），可借鉴引入指数衰减记忆模块，继续少量预训练后，配合现有稀疏方法（SnapKV、Quest）大幅减少KV
  cache内存占用，几乎无损精度。

  - 只需追加10B tokens的持续预训练即可让标准模型适应记忆模块，实现即插即用，对资源有限的业务微调较友好。

  - 论文提出的两个假设（记忆使注意力头更专注、帮助模型更早定位关键token）可指导设计更适合稀疏推理的架构，例如在注意力头中融合指数衰减偏置。

  - 在工程实现上，该记忆模块以递归方式维护KV状态，可与主流稀疏推理框架整合，适合需要高吞吐、低延迟的长上下文服务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长上下文语言模型推理中，注意力计算和KV cache访问是主要瓶颈，现有查询感知稀疏方法（如Quest、MoBA、SnapKV）在高稀疏度下精度下降明显。RAT+近期提出基于指数衰减记忆的注意力架构，可实现灵活扩张注意力。本文探索该记忆模块能否增强现有的查询感知稀疏推理。

**方法**：将RAT+的指数衰减记忆模块与三种代表性稀疏方法（Quest、MoBA、SnapKV）结合，在8个Needle-in-a-Haystack任务上评估。实验使用RAT+发布的checkpoint，并在OLMo2-7B基础上继续预训练10B tokens引入记忆模块。

**关键结果**：在所有稀疏预算下，RAT+记忆模块一致提升三种稀疏方法的准确性；即使在98%稀疏度或75% KV缓存压缩等高难度设置下，仍保持显著收益。进一步通过消融实验提出两个解释：记忆模块提供的长期上下文帮助稀疏注意力头更结构化地选择关键token；并使模型更早识别“needle”位置，减少关键信息丢失。
