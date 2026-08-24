---
title: 'ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event
  Prediction'
title_zh: ForeDreamer：面向未来事件预测的自进化双智能体记忆架构
authors:
- Linhao Zhong
- Zongze Du
- Linyu Wu
- Yu Bo
- Hourong Li
- Chenchen Jing
- Hao Chen
- Yuling Xi
- Chunhua Shen
affiliations:
- Zhejiang University
- Ant Group
- National University of Singapore
- Zhejiang University of Technology
arxiv_id: '2608.20920'
url: https://arxiv.org/abs/2608.20920
pdf_url: https://arxiv.org/pdf/2608.20920
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent 记忆与自进化 · 未来事件预测
tags:
- Agent Memory
- Self-Evolving
- Future Prediction
- Dual-Agent
- MemGuide
- MemTools
one_liner: 双智能体将嘈杂网络证据蒸馏为结构化事实记忆，并用双轨经验自进化提升预测校准
practical_value: '- 在电商搜索/推荐 agent 中，可将召回/检索结果的处理从主决策链路剥离，由专门子 agent 用「指南+工具」流程把原始商品信息、用户行为、query
  上下文蒸馏成结构化事实记忆，主 agent 只消费干净证据，降低长上下文噪声干扰。

  - 自进化双轨经验：一条是文本经验（搜索计划、排序/预测校准提示），一条是过程性工具经验（可执行数据处理工具/流程）。推荐 agent 可基于线上反馈小流量验证定期更新经验池，采用
  ADD/MODIFY/REMOVE 编辑和验证门控，避免线上劣化。

  - Compositional Tool Reuse 减少重复工具生成：当需要新处理流程时，先检索并复用已有工具，只生成缺失部分；可应用于推荐 agent 的工具库管理，降低工具膨胀与相似代码重复。

  - Diversity-Guided Exploration 防止策略收敛到单一 pipeline：定期根据现有策略类别摘要生成多样候选，避免只微调某一种召回/排序策略；可借鉴到推荐策略探索与自动策略生成中。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
开放网络未来事件预测要求 agent 从嘈杂、冗余、冲突且时间敏感的证据中提炼可靠信号；现有 RAG 或长期记忆机制大多把检索结果直接塞给模型，或只做存储/检索/重用，无法有效处理开放网络的证据噪声。因此需要先把原始证据转化为结构化记忆，再让 agent 基于蒸馏后的证据进行推理和预测。

### 方法关键点
- **分离两类记忆**：factual memory 是当前问题条件化的证据接口；experiential memory 是跨任务积累的持久经验，包括文本经验（Experience Bank）和过程性工具经验（MemGuide + MemTools）。
- **双 agent 架构**：main agent 负责搜索计划、集成事实记忆、产生最终预测；memory-processing subagent 用 MemGuide 指定工作流、用 MemTools 执行可操作步骤，将原始搜索结果转化为结构化事实记忆。
- **推断流程**：多轮 search-and-process，主代理每轮发起 cutoff-aware 搜索，子代理逐个处理检索结果，最终输出预测和 rationale。
- **双轨自进化**：文本轨对 Experience Bank 做 ADD/MODIFY/REMOVE 编辑，验证改善才接受；过程轨生成候选 MemGuide/MemTools，通过验证门控加入 MemGuide 树。
- **两个优化**：Compositional Tool Reuse 复用已有 MemTools 减少重复生成；Diversity-Guided Exploration 基于类别摘要生成多样候选，避免过度集中单一 pipeline。

### 关键实验
在 Prophet Arena（1200 题快照，实际用 400 体育子集）和 FutureX（208 题）上，以 Qwen3.5-Flash 和 GPT-5.4-Nano 为骨干。Prophet Arena 平均 Brier：Qwen 下 ForeDreamer 0.1471 vs Full Text 0.2059，最强记忆 baseline LightMem 0.1761；FutureX accuracy 0.4108 vs Full Text 0.3298，最强 baseline A-MEM 0.3495。消融显示双轨经验和两个优化各有贡献，无信息提示检查也排除了纯模型泄漏解释。

> 最值得记住的一句话：将原始证据先蒸馏成结构化事实记忆，再让文本经验和过程性工具经验通过验证门控双轨自进化，是提升开放网络决策可靠性的关键。
