---
title: Mixture-of-Experts Knowledge Graph Retrieval-Augmented Generation for Multi-Agent
  LLM-based Recommendation
title_zh: 基于专家混合知识图谱检索增强的多智能体 LLM 推荐
authors:
- Shijie Wang
- Chengyi Liu
- Yujuan Ding
- Shanru Lin
- See-Kiong Ng
- Xu Xin
- Wenqi Fan
affiliations:
- The Hong Kong Polytechnic University
- City University of Hong Kong
- National University of Singapore
arxiv_id: '2605.28175'
url: https://arxiv.org/abs/2605.28175
pdf_url: https://arxiv.org/pdf/2605.28175
published: '2026-05-27'
collected: '2026-05-28'
category: MultiAgent
direction: 多智能体 KG-RAG 推荐 · 查询感知检索与对齐优化
tags:
- Multi-Agent
- KG-RAG
- Mixture-of-Experts
- LLM-based Recommendation
- Contrastive Learning
- Policy Optimization
one_liner: 提出多智能体框架 MixRAGRec，通过查询感知的多粒度 KG 检索与联合优化，实现高效知识增强推荐
practical_value: '- **查询感知的多粒度检索**：根据用户查询复杂程度动态选择 KG 检索粒度（无检索/三元组/子图/连通图），避免简单查询过度检索、复杂查询检索不足，平衡成本与效果。电商搜索中可借鉴类似
  MoE 路由，针对不同意图（属性筛选 vs. 宽泛需求）切换知识源。

  - **结构化知识对齐 Agent**：用专门的小型 LLM 将图结构知识转为自然语言摘要，减少噪声、保留推荐相关结构信息。在商品知识图谱场景下，可先用模板初转再让
  Agent 精炼，作为 LLM 上下文注入。

  - **多智能体联合优化（MMAPO）**：使用共享奖励函数（推荐准确性 + 边际信息增益）并通过 GAE 估计优势，实现检索决策与内容生成的端到端训练。此框架可推广到需要协调离散选择（检索策略/API
  调用）与连续生成（文案/推荐列表）的 Agent 系统。

  - **对比偏好学习与硬负挖掘**：在推荐模型中引入对比损失，自动挖掘困难负样本，能有效区分高度相似的候选物品。该方法可直接用于商品推荐排名模型的 fine-tune，提升
  Top-K 精度。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 推荐易受幻觉和知识过时影响，KG-RAG 虽能提供结构化知识，但现有方法对所有查询使用固定检索粒度，导致简单查询引入噪声、复杂查询知识不足；图结构到文本的转换也常丢失结构信息。检索粒度的选择缺乏直接监督，难以端到端优化。

**方法关键点**
- **多智能体框架**：包含三个 Agent——Mixture-of-Experts 检索 Agent、知识偏好对齐 Agent、对比学习推荐 Agent。
- **检索 Agent**：四种专家（不检索、三元组、k-hop 子图、连通子图），通过 MoE 路由根据查询语义动态选择粒度。连通子图采用 Personalized PageRank + 最小生成树保留全局相关性。
- **对齐 Agent**：将检索到的结构化知识先用模板线性化，再用小型 LLM 精炼为自然语言片段，桥接图-文鸿沟。
- **推荐 Agent**：基于对齐知识生成推荐，使用对比偏好反馈（类似 DPO）训练，通过硬负采样强化区分相似物品的能力。
- **优化方案 MMAPO**：用 GAE 估计优势回传奖励，共享奖励由推荐准确性和边际信息增益（KL 散度减计算成本）组成，鼓励成本敏感的检索选择。

**关键实验**
在 MovieLens-1M/20M 和 LastFM-1K 上，以 LLaMA3-8B 和 Mistral-7B 为基座，对比零样本、LLM 微调、固定粒度 KG-RAG 基线。MixRAGRec 在三个数据集上均达最优，相对最强基线 K-RagRec，Accuracy 最高提升 13.8%（ML-20M），Recall@5 提升 8.3%–13.2%。消融证明对齐 Agent 贡献最大；效率上，MixRAGRec 检索时间接近轻量级三元组方法，远快于同性能的图检索基线。

**最值得记住的一句话**
MixRAGRec 证明，通过显式建模检索粒度的选择并进行成本感知的多智能体联合优化，能让 LLM 推荐同时获得高准确率和低检索开销。
