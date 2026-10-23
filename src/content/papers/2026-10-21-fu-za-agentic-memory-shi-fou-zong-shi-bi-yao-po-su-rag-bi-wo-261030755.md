---
title: Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought
title_zh: 复杂 Agentic Memory 是否总是必要？朴素 RAG 比我们想的更强
authors:
- Zhengye Bao
- Shengtao Zhang
- Haokai Zhang
- Shiqi Lou
- Muning Wen
- Minnan Luo
affiliations:
- Xi'an Jiaotong University
- Shanghai Jiao Tong University
- Zhejiang University
- The Chinese University of Hong Kong
arxiv_id: '2610.30755'
url: https://arxiv.org/abs/2610.30755
pdf_url: https://arxiv.org/pdf/2610.30755
published: '2026-10-21'
collected: '2026-10-23'
category: RAG
direction: 长对话记忆中朴素 RAG 基线对比复杂 Agentic Memory
tags:
- RAG
- Agentic Memory
- Long-term Conversation
- Dense Retrieval
- Reranking
- LLM Memory
one_liner: 在长对话理解中，基于原始历史的朴素 RAG 在多数基准上超越复杂 agentic memory，并揭示保留原始信息的重要性
practical_value: '- 在电商客服、用户 long-term profile、Agent 对话等场景，可以先实现朴素 RAG：直接对原始历史做 dense
  retrieval + reranking，再交给 LLM 生成回答，工程成本远低于构建复杂记忆系统，却可能获得更高准确率。

  - 保留原始交互序列和日志很重要。复杂记忆转换（如 summary、知识图谱、记忆更新）会引入信息损失，导致后续推导所需的依赖路径丢失；在推荐/客服场景应保留
  raw evidence 作为检索源。

  - 证据覆盖率比单条证据利用率更关键。朴素 RAG 可能检索到更多冗余但相关证据，即使部分证据未被 LLM 充分利用，也能通过提升 recall 来弥补 precision
  的不足，因此评估记忆系统时不要只优化 top-k 精度。

  - 重排序在 raw-history RAG 中是有效的 trick：先 dense retrieval 提高 recall，再用 reranker 压榨 top-k
  质量，可以在低 ingestion 成本下达到甚至超越复杂记忆的表现。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 长对话理解中，Agentic memory 系统通常引入 mutation、结构化组织、学习式检索等复杂操作。论文质疑这些复杂度是否始终必要，提出原始历史上的朴素 RAG 基线。

**方法关键点**：Raw-RAG 直接在原始对话历史上做 dense retrieval + reranking，将检索到的证据喂给 reader LLM。在 LoCoMo、LongMemEval、MEME、MemoryAgentBench 四个基准上，对比 EverMemOS、MemOS、Memora、Mem0 等复杂记忆系统。

**关键结果数字**：7 个 benchmark-model settings 中 Raw-RAG 在 6 个上排名第一，比最强的对比 agentic memory 系统高 0.13–5.53 个准确率点。证据分析显示：raw-history retrieval 更高的必要证据覆盖率可以抵消其较低的证据利用率；有用证据不仅包括答案值，还包括推导其所需的依赖路径和关系；即使完全访问转换后的记忆存储，仍与原始证据存在准确率差距。此外，Raw-RAG 的 ingestion 成本极低，在 BEAM-1M 上仅需 0.3 小时，而 Mem0 等系统需要 18–27 小时。

**结论**：在评估的对话任务中，复杂 agentic memory 并非必要，朴素 RAG 应作为必不可少的基线。
