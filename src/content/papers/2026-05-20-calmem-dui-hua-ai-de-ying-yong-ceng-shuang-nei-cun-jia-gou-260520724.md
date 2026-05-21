---
title: 'CALMem : Application-Layer Dual Memory for Conversational AI'
title_zh: CALMem：对话 AI 的应用层双内存架构
authors:
- Rajendra Narayan Jena
- Rajan Padmanabhan
- Sankar Arumugam
affiliations:
- Infosys Limited
arxiv_id: '2605.20724'
url: https://arxiv.org/abs/2605.20724
pdf_url: https://arxiv.org/pdf/2605.20724
published: '2026-05-20'
collected: '2026-05-21'
category: LLM
direction: 应用层记忆架构 · 情景与语义双检索
tags:
- dual memory
- episodic memory
- semantic memory
- MOIM
- RAG
- application layer
one_liner: 纯应用层双内存（情景+语义）实现无模型改动的近乎无限上下文，并通过 token 自适应注入恢复会话连续性。
practical_value: '- 在客服 agent 或购物助手中，可借鉴语义记忆显式存储用户偏好、情景记忆基于向量检索历史交互，二者互补恢复上下文。

  - 采用 token 预算自适应注入，按上下文填充率动态控制注入量，避免记忆注入反而加速窗口溢出，适合长会话电商场景。

  - 嵌入搜索使用内存缓存（Vec）减少 I/O，毫秒级延迟可忽略，适合需要低延迟的实时对话推荐系统。

  - 纯应用层实现，不改模型、零回归开关，方便在现有 LLM 产品中渐进式迭代和灰度实验。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 的上下文窗口有限，会话中早期内容会被压缩丢弃，跨会话则完全遗忘。改造模型（更大的窗口或架构）成本高且无法解决跨会话记忆。应用层记忆是更经济的补充方案，需要同时处理会话内压缩后的回溯和跨会话事实检索。

## 方法关键点
- **双内存架构**：情景记忆采用滑动窗口分块 + MiniLM 向量检索，语义记忆为结构化键值事实表，agent 可显式读写。
- **MOIM（Message of Injected Memory）**：每轮根据上下文填充率自适应注入检索结果，当接近压缩阈值时自动抑制注入，避免加速上下文消耗。
- **会话内检索**：对当前会话中已被压缩的 turns 仍保持可检索，填补了现有方法的空白。
- **缓存优化**：通过内存向量缓存一次加载嵌入、过滤非活跃块后直接计算余弦相似度，避免每次搜索时从 SQLite 读取大量 BLOB。
- **零回归设计**：关闭 RAG 功能后系统退化为标准 LLM 行为，无延迟开销，通过单标志位控制。

## 关键实验
- 在 120 条查询–会话对的标注集上，CALMem 的 P@5 0.74、Recall@5 0.69、MRR 0.81，全面优于 BM25 和 TF‑IDF。
- 双内存消融实验显示：单独情景记忆恢复率 67%，语义事实一致性 89%；两者结合恢复率 71%，一致性 91%。
- 搜索延迟在 5 万块时内存缓存仅 20–40ms，远小于 LLM 推理时间，对用户无感知。

## 一句话
应用层记忆不是对长上下文的妥协，而是一种可独立演进、与模型窗口大小互补的生产级设计模式。
