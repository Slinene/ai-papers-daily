---
title: Self-Augmenting Retrieval for Diffusion Language Models
title_zh: 扩散语言模型的自增强检索
authors:
- Paul Jünger
- Justin Lovelace
- Linxi Zhao
- Dongyoung Go
- Kilian Q. Weinberger
affiliations:
- Cornell University
arxiv_id: '2606.06474'
url: https://arxiv.org/abs/2606.06474
pdf_url: https://arxiv.org/pdf/2606.06474
published: '2026-06-04'
collected: '2026-06-05'
category: RAG
direction: 扩散语言模型 · 动态检索增强
tags:
- Diffusion Language Models
- Retrieval-Augmented Generation
- Self-Augmenting
- Multi-hop QA
- Training-free
one_liner: 利用扩散去噪中丢弃的低置信度 token 作为前瞻信号，实现无训练的动态检索增强生成
practical_value: '- 电商对话或商品描述生成中，可利用扩散模型的并行去噪过程，提前从中间低置信度 token 中提取关键实体，触发多跳知识检索，提升答案的完整性和事实准确性。

  - 方法完全无训练、不依赖特定检索器，可直接嵌入现有的扩散语言模型推理流程，非常适合业务中快速尝试不同的知识库或检索策略。

  - 扩散模型的高吞吐特性（8× 提升）加上前瞻检索，能在高并发电商客服或内容生成场景下，在保持答案质量的同时显著降低延迟。

  - 对于 Agent 中的多跳推理或工具调用，可以借鉴前瞻 token 的思路，在最终决策前动态获取更多环境信息，提升决策可靠性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散语言模型通过并行去噪生成文本，每步预测所有遮蔽位置的临时 token，但仅将高置信度 token 提交到输出，低置信度 token 被丢弃。研究发现，这些被丢弃的 token 常包含后续需要的显著实体信息，可作为前瞻信号提前触发检索。

**方法**：提出 SARDI（Self-Augmenting Retrieval for Diffusion Language Models）框架，在扩散去噪的每一步，利用所有临时 token（包括低置信度前瞻 token）构造查询，检索外部知识库，并将检索到的证据融入去噪过程，动态指导后续生成。整个流程无需训练，与检索器解耦，适用于任何具有推理能力的离散扩散语言模型。

**结果**：在五个多跳 QA 基准上，SARDI 在准确率上超过现有无训练的扩散和自回归检索基线，同时推理吞吐量最高提升 8 倍，显著优于逐 token 生成的自回归方案。
