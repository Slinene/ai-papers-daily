---
title: Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI
  Education
title_zh: 面向算法教学意图感知的检索增强辅导系统
authors:
- Mragisha Jain
- Tirth Bhatt
- Griffin Pitts
- Aum Pandya
- Peter Brusilovsky
- Narges Norouzi
- Arto Hellas
- Juho Leinonen
- Bita Akram
affiliations:
- North Carolina State University
- University of Pittsburgh
- University of California, Berkeley
- Aalto University
arxiv_id: '2605.12988'
url: https://arxiv.org/abs/2605.12988
pdf_url: https://arxiv.org/pdf/2605.12988
published: '2026-05-13'
collected: '2026-05-16'
category: RAG
tags:
- RAG
- Intelligent Tutoring System
- Algorithm Tracing
- Socratic Method
- Evaluation
- Simulated Student
one_liner: 结合多模态检索与苏格拉底式反馈，为算法追踪与问题求解提供课程对齐的AI辅导
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

AI 课程中学生常依赖 ChatGPT 等 LLM 获取即时辅导，但易得到未经审查的答案，绕过推演过程。现有 RAG 系统虽能提升事实准确性，却缺乏对问题类型的自适应教学策略，尤其在算法追踪与调试类任务上难以提供恰当的引导。为此，有必要构建一个意图感知、课程对齐且能提供苏格拉底式渐进支架的辅导系统。

## 方法关键点

- **KITE 架构**：五阶段流水线，包括文档预处理、嵌入生成、多阶段检索、意图感知生成和会话管理。
- **多阶段检索**：先经密集检索（OpenAI text-embedding-3-large）召回 top-50 块，再混合稀疏 BM25（权重比 7:3），经 MMR 去重（λ=0.7）和跨编码器重排序（ms-marco-MiniLM-L-6-v2），最终取 top-8 并给予官方教材来源加权。
- **意图分类**：基于关键词和模式匹配，将查询分为直接问题、概念问题、算法验证、调试、算法追踪五类，另有独立答案评估模式。
- **响应策略**：对齐课程材料的同时，针对不同意图采用直接解释或苏格拉底式追问、分步提示、逐步追踪，避免给出最终答案。

## 关键实验

- **数据集**：109 道来自《人工智能导论》课程的问题，含 42 道算法题、51 道过程题、16 道直接检索题。
- **RAGAs 评估**（58 道非过程题）：Faithfulness 0.85，Context Relevance 0.94，Answer Similarity 0.76（与教师答案高度一致），Factual Correctness 0.45（受限于指标敏感性）。
- **模拟学生评估**（44 组交互）：用 Llama-3.1-70B 模拟学生，KITE 反馈后 88.89% 的答案得到改善（从部分正确改为完全正确占 31.82%），专家评分脚手架、引导、连贯、语气均达 93.18% Yes。

## 值得记住的一句话

KITE 让课程 RAG 系统从“回答者”升级为“引导者”：在高召回高相关的检索之上，通过意图感知的苏格拉底式反馈，使模拟学生在算法追踪类问题上的答案改善率达 88.89%，证明支架式辅导对教学场景的有效性。
