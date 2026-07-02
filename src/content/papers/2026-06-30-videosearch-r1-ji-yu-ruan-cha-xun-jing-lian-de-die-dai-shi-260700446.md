---
title: 'VideoSearch-R1: Iterative Video Retrieval and Reasoning via Soft Query Refinement'
title_zh: VideoSearch-R1：基于软查询精炼的迭代视频检索与推理智能体
authors:
- Seohyun Lee
- Seoung Choi
- Dohwan Ko
- Jongha Kim
- Hyunwoo J. Kim
affiliations:
- KAIST
- Korea University
arxiv_id: '2607.00446'
url: https://arxiv.org/abs/2607.00446
pdf_url: https://arxiv.org/pdf/2607.00446
published: '2026-06-30'
collected: '2026-07-02'
category: Agent
direction: 强化学习驱动的多模态检索智能体与查询精炼
tags:
- Video Retrieval
- Soft Query Refinement
- GRPO
- Reinforcement Learning
- Vision-Language Model
- Agent
one_liner: 提出软查询精炼（SQR）在连续潜在空间细化搜索查询，通过强化学习联合优化视频检索与细粒度推理
practical_value: '- 在电商搜索中，对未命中或模糊查询，可使用软查询精炼（SQR）替代文本改写，直接在嵌入空间生成少量连续向量调优检索结果，避免硬改写引入的语义噪声和过长Token消耗。

  - 检索-验证-精炼的迭代循环（检索→核对匹配→若失败则触发精炼）可引入到商品搜索或推荐系统，实现自主纠错，提升长尾query的召回与精度。

  - 强化学习（GRPO）联合优化检索精炼与下游任务（如点击预测、排序）的思路可复用：设计任务级奖励（如检索召回率、点击奖励），端到端训练查询表示生成策略。

  - 软查询精炼只需少量额外Token（实验中仅8个），工程开销小，适合嵌入现有双塔检索或向量召回架构，作为在线查询优化插件。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有视频检索系统将检索作为一次性预处理步骤，当初始检索失败时缺乏精炼机制，导致后续细粒度推理完全失败。同时，大多数视频智能体框架假设目标视频已知，无法应对大规模视频语料库中的检索-推理联合任务。该工作面向Video Corpus Moment Retrieval（VCMR）场景：给定文本查询，需先从海量语料中检索到正确视频，再精确预测查询相关片段的时间边界。

**方法**
- 提出**VideoSearch-R1**框架：多轮交互式检索与推理智能体。每轮：调用外部视频搜索引擎检索Top-1视频 → 核对视频与查询的语义匹配 → 若不匹配，触发**软查询精炼（SQR）**生成连续嵌入Token附加到原查询，形成精炼查询重新检索；若匹配，进入时间定位。
- **SQR**：在VLM最后隐藏层自回归生成N个软查询Token（连续向量），通过InfoNCE对比损失（正样本为真实视频，负样本为其他视频）训练，直接在嵌入空间优化查询表示。与硬文本改写相比，仅需8个Token即可实现更细粒度的查询调整。
- 训练分两阶段：1) SFT冷启动，蒸馏强VLM的思维链推理，并加入InfoNCE损失训练软查询；2) 强化学习阶段采用GRPO，设计格式、验证、检索、时间定位四项奖励，联合优化整个检索-推理流程。

**关键结果**
在ActivityNet-FIG、Charades-FIG、DiDeMo-FIG三个VCMR基准上达到SOTA。以DiDeMo-FIG为例，视频检索R@1从基线55.1%提升至59.0%（零样本）→61.1%（SQR），VCMR指标0.3/R@1从22.0%提升至33.3%。消融表明：InfoNCE损失使检索初始化更强，奖励组合对最终性能至关重要。SQR用8个Token超越平均26.8 Token的硬改写，且对更大尺寸搜索引擎仍有效。

**核心洞察**
软查询精炼在连续空间进行语义再分配，比硬文本改写更精准高效，适合作为Agent式检索系统的轻量级查询优化模块。
