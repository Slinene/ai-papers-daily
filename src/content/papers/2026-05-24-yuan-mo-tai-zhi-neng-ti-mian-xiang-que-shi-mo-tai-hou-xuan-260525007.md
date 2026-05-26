---
title: 'Meta-Modal Agent: Sequential Evidence Routing for Missing-Modality Candidate
  Reranking'
title_zh: 元模态智能体：面向缺失模态候选重排的序列化证据路由
authors:
- Jinze Wang
- Yangchen Zeng
- Tiehua Zhang
- Lu Zhang
- Yuze Liu
- Zhishu Shen
- Jiong Jin
- Zhu Sun
affiliations:
- Swinburne University of Technology
- Southeast University
- Tongji University
- Chengdu University of Information Technology
- Wuhan University of Technology
arxiv_id: '2605.25007'
url: https://arxiv.org/abs/2605.25007
pdf_url: https://arxiv.org/pdf/2605.25007
published: '2026-05-24'
collected: '2026-05-26'
category: RecSys
direction: 缺失模态推荐 · 序列证据路由与LLM Agent
tags:
- missing modality
- LLM agent
- candidate reranking
- cold-start
- evidence routing
- reinforcement learning
one_liner: 将冷启缺失模态视为序列证据路由问题，用PPO训练LLM Agent融合自动工具与检索分数进行候选重排
practical_value: '- **缺失模态应对策略**：将缺失模态视为 “Null 观察” 而非特征缺失，通过 agent 路由到可用证据源，避免了对不可靠补全的依赖。电商中新品冷启、用户无行为时可直接借鉴。

  - **Agent 训练技巧**：使用 PPO 训练时加入任务平衡采样（balanced missingness-task），确保极度缺失场景（如仅图像）获得与全观测场景相同训练暴露，防止策略偏向简单情况。可迁移至推荐
  agent 的强化学习调优。

  - **重排序与融合设计**：Agent 只对上游检索返回的候选池打分，最终排序通过加权融合模型分数与原始检索分数（公式 (2)）。该“检索-重排”解耦架构允许灵活插入
  LLM agent，且通过融合权重控制新旧信号比例，适合现有推荐管线改造。

  - **路由机制验证**：与固定规则路由器（RuleRouter-Fuse）对比，学习到的路由不仅提升 NDCG@10，还降低了无效工具调用率（47% vs 65.8%）和平均轮次（2.5
  vs 3.8），说明 RL 训练出的策略更高效，可作为 agent 工具调用的优化范式。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多模态推荐系统中，冷启场景下用户历史、商品文本、图像等模态频繁缺失，现有方法常通过补全或生成伪特征弥补，但在极端缺失时容易引入不可靠证据。本文将缺失模态问题重新定义为候选池重排过程中的序列化证据路由问题：agent 需要决定调用哪种证据工具，并将“Null”返回作为有效观察以切换路由，而非简单丢弃或补全。

**方法关键点**
- **候选池重排协议**：MMA 工作在上游检索器产出的固定候选池上，仅对候选打分并重排，不直接从全量目录召回。最终分数由 MMA 得分与一级检索得分加权融合（权重在验证集上选择）。
- **证据路由 Agent**：基于 Llama-3-8B 的 POMDP 决策，动作空间包括分析文本、分析图像（通过 CLIP 标签）、检索图邻居以及可选的用户交互工具 Ask_User。工具返回 Null 时，agent 将其作为环境观察并调整后续工具选择。
- **平衡缺失任务训练**：定义 7 种缺失模式任务族（如纯文本、纯图像、纯行为等），在 PPO 训练中均匀采样，确保 severe OOMA 场景不被简单模式淹没。奖励函数结合 NDCG 排序质量和调用成本惩罚（无效调用惩罚 −0.2，重复失败调用惩罚 −0.2）。
- **两个变体**：MMA-Auto（仅自动化工具）为部署版本；MMA-Interactive（含 Ask_User）仅作为诊断上界。

**关键结果**
在 Amazon-Baby、Sports 和 Yelp 三个数据集上，对比 DGMRec、GRE-MC 等静态补全基线，以及 ReAct、AgentCF 等 LLM agent 基线：
- 目标正例 OOMA NDCG@10 平均提升 4.0%（0.1645→0.1711），所有 9 个模态-数据集组合均获胜。
- 固定池全量重排场景下，平均相对提升 12.7%，且 Recall 保持不变，证明改善来源于池内排序。
- 与确定性的 RuleRouter-Fuse 相比，MMA-Auto 将 OOMA NDCG@10 从 0.1578 提升至 0.1711，同时减少无效调用率 18.8 个百分点，轮次减少 1.3，表明学习到的路由策略更高效且收益非单纯来自工具融合。

**核心结论**
学习到的证据路由能稳健处理缺失模态，其增益源于灵活的 Null 观察利用与任务平衡训练，而非大模型规模的突破。
