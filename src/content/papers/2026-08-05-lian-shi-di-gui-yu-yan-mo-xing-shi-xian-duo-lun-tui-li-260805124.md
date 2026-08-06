---
title: Chained Recursive Language Models for Multi-Iteration Reasoning
title_zh: 链式递归语言模型实现多轮推理
authors:
- Purbesh Mitra
- Sennur Ulukus
affiliations:
- University of Maryland
arxiv_id: '2608.05124'
url: https://arxiv.org/abs/2608.05124
pdf_url: https://arxiv.org/pdf/2608.05124
published: '2026-08-05'
collected: '2026-08-06'
category: Reasoning
direction: 多步推理 · 新鲜推理链架构
tags:
- Chain-of-Thought
- Multi-hop Reasoning
- LLM
- Inference-time Architecture
- Context Management
one_liner: 将长上下文推理拆成多轮新鲜调用，通过摘要与黑板传递状态，避免错误累积
practical_value: '- 在电商对话Agent中，将复杂查询（如多条件筛选+排序）拆成子任务，每个子任务独立调用LLM，用黑板共享中间结果，对抗长上下文遗忘

  - 商品知识图谱多跳推理（如“同等价位好评率最高品牌”）可采用新鲜推理根，每步仅关注相关子图，阻断错误传播

  - 推荐解释生成需融合多源信息，可引入可检查可修正的中间产物机制（如结构化摘要），提升解释准确性与可调试性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 处理长上下文推理时，单次推理需同时探索上下文、存储状态、验证证据并产出答案，在提取、计数、排序、多跳推理等任务中极易先前错误累积导致最终输出偏离。

**方法**：提出 Chained RLM 推理时架构，将同一 LLM 作为一系列“新鲜推理根”反复调用。每个根接收原始问题与上下文，但不继承完整对话历史，而是从前驱根获得紧凑纯文本摘要、纯文本黑板及持久特定任务产物。通过将推理拆分为阶段性子任务，中间产物可被后续调用检查、修正与扩展。

**结果**：论文定义了系统模型、交接机制、产物工作空间与评估协议，对比直接 LLM 回答与递归工具调用，分析了新鲜上下文产物延续带来可测量准确率增益的条件（摘要中未提供具体数字）。
