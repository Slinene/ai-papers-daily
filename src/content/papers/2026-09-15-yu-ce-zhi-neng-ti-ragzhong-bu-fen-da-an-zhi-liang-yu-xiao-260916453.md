---
title: Predicting Partial Answer Quality and Utility in Agentic Retrieval-Augmented
  Generation
title_zh: 预测智能体RAG中部分答案质量与效用
authors:
- Fangzheng Tian
- Debasis Ganguly
- Craig Macdonald
affiliations:
- University of Glasgow
arxiv_id: '2609.16453'
url: https://arxiv.org/abs/2609.16453
pdf_url: https://arxiv.org/pdf/2609.16453
published: '2026-09-15'
collected: '2026-09-16'
category: RAG
direction: Agentic RAG 轨迹质量预测与早停
tags:
- Agentic RAG
- Multi-hop QA
- Query Performance Prediction
- Early Stopping
- Trajectory Probing
- Answer Quality Prediction
one_liner: 提出轨迹内探针框架，预测Agentic RAG中间答案质量与增量效用，实现约11%早停节省且保持98%质量
practical_value: '- 在电商/购物助手的多跳 Agentic RAG 场景中，可在每次检索-推理后强制生成一个 partial answer，用轻量回归/分类器实时预测其质量或增量效用，作为动态早停信号，而非固定最大步数；论文显示可省约
  11% 迭代次数且仅损失约 2% 最终质量。

  - 可借鉴的三类轨迹特征：intra-iteration（当前检索结果与 query 的相关性、query 特异性）、inter-iteration（partial
  answer embedding 漂移/趋于稳定）、query-iteration（query 改写相似度），组合成在线 guardrail，适合低延迟、高吞吐的推荐/问答服务。

  - 质量预测比效用预测更可靠（Pearson r > 0.43 vs. 效用更低），工程落地时建议以质量阈值/置信度为主要停止判据，效用 delta 可作辅助信号或用于异常检测，避免因效用预测噪声导致过早切断有效推理。

  - 商品搜索/导购场景中，用户问题常需多轮查询细化，可把该框架扩展到“是否已获得足够商品信息”的判定，减少无效检索与 LLM 调用，同时保持答案完整度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Agentic RAG 在多跳问答中通过迭代检索与推理提升最终答案质量，但现有评估只看端到端结果，缺少对中间答案状态的可见性，难以判断何时继续检索收益已很小。

**方法关键点**：提出 in-trajectory probing 框架，在每一轮检索-推理后强制模型停止推理并基于当前状态生成中间答案；定义 partial answer quality（当前迭代答案质量）和 partial utility（跨迭代质量变化）。在多跳 QA benchmark 上发现质量常在自然终止前就趋于平台，后续迭代提升很小。进一步构建两个预测任务：partial answer quality 与 utility 预测，使用 intra-iteration、inter-iteration、query-iteration 三类轨迹信号训练监督模型。

**关键结果**：partial answer quality 比 utility 更可预测，质量预测 Pearson r > 0.43；用预测质量和效用做早停，平均迭代次数减少约 11%，同时保留自然停止下约 98% 的最终答案质量。
