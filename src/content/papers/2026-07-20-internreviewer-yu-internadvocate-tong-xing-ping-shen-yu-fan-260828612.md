---
title: 'InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic
  Reinforcement Learning in Peer Review and Rebuttal'
title_zh: InternReviewer 与 InternAdvocate：同行评审与反驳的客观奖励与评估
authors:
- Xuerui Su
- Liya Guo
- Qizhi Pei
- Qipeng Guo
- Zhongbo Tian
- Lijun Wu
- Kai Chen
- Zun Wang
affiliations:
- Shanghai AI Laboratory
- Beijing Jiaotong University
- Tsinghua University
- Renmin University of China
arxiv_id: '2608.28612'
url: https://arxiv.org/abs/2608.28612
pdf_url: https://arxiv.org/pdf/2608.28612
published: '2026-07-20'
collected: '2026-09-03'
category: Agent
direction: Agentic RL 学术评审智能体
tags:
- Agentic RL
- Peer Review
- LLM
- Citation Verification
- Reward Design
- Hallucination
one_liner: 用客观多维 reward 与严格引文验证训练学术评审/反驳 Agent，减少主观评判偏差和幻觉
practical_value: '- 评估与奖励去偏：用多维客观指标（reference-anchored semantic alignment、structural
  compliance、citation verification）替代单一大模型打分，减少 reward hacking 和主观偏差。在生成式推荐/导购文案中，可定义商品属性一致性、结构模板、引用可验证等可计算的
  reward。

  - 可验证的引用日志交叉核对：将生成内容中的声明与实时检索/工具调用日志强制对齐，能直接迁移到电商 RAG 问答和商品描述生成，降低幻觉（如虚构参数、不存在的促销）。

  - Agentic RL 闭环：先检索证据再生成、用严格验证作为 reward 信号，可复用为“检索-生成-校验” pipeline，适用于需要事实性的营销文案、售后应答等。

  - 数据集构建：建设高质量垂直领域数据 + 高效检索工具，是提升 Agent 落地效果的基础，电商可借鉴构建商品知识库与交互日志。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：学术同行评审和反驳需要领域推理与事实依据结合，但当前自动化面临主观评判偏差和幻觉问题。  
**方法关键点**：构建大规模高质量学术数据集；集成高效 arXiv 检索工具支持主动证据收集；采用 Agentic RL 范式，设计统一客观 reward，包含参考锚定语义对齐、结构合规、基于实时交互日志的引文严格验证，避免模型主观评判偏差。  
**关键结果**：在闭环节奏下训练的 Agent 在推理深度和引文准确率上显著提升（摘要定性描述，未给具体数值）。
