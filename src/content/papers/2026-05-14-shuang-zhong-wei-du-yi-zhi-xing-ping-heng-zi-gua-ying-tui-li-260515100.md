---
title: 'Dual-Dimensional Consistency: Balancing Budget and Quality in Adaptive Inference-Time
  Scaling'
title_zh: 双重维度一致性：平衡自适应推理缩放中预算与质量
authors:
- Rongman Xu
- Yifei Li
- Tianzhe Zhao
- Yanrui Wu
- Bo Li
- Hang Yan
affiliations:
- 西安交通大学
arxiv_id: '2605.15100'
url: https://arxiv.org/abs/2605.15100
pdf_url: https://arxiv.org/pdf/2605.15100
published: '2026-05-14'
collected: '2026-05-16'
category: LLM
tags:
- Reasoning
- Inference-time Scaling
- Confidence Estimation
- Bayesian Termination
- Pruning
- LLM
one_liner: 提出统一框架DDC，通过置信加权贝叶斯终止与趋势感知分层修剪，在维持准确率的同时将令牌消耗降低10倍以上
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：LLM推理时的自适应缩放（adaptive inference-time scaling）面临采样预算与推理质量之间的权衡。现有方法或采用固定预算导致冗余，或割裂地优化“采样宽度”与“路径深度”：宽度方法基于早期共识终止，却可能因模型幻觉而错误退出；深度方法通过置信度修剪路径，但常误删复杂但正确的推理链。亟需一个统一框架，在预算与质量之间建立动态平衡。

**方法关键点**：
- **多粒度置信度**：从token级（局部/全局置信度）、窗口组级到路径级（最低组置信度），为质量评估提供分层信号。
- **置信加权贝叶斯终止（Inter-Path）**：将共识转化为贝塔后验分布，以路径置信度作为权重更新“领先答案”的证据强度；当领先答案获绝对多数的概率超过95%时终止采样，避免基于虚假共识的过早退出。
- **趋势感知分层修剪（Intra-Path）**：将推理过程建模为动态系统，通过特征分解区分稳定趋势与随机噪声。对路径分三层处理：top-10%高置信路径直接保留，bottom-20%立即丢弃；中间层基于“结构不稳定度”（R）和Tukey Fences自适应阈值进行异常检测，惩罚持续下跌的置信度趋势，保护暂时下跌后恢复的困难路径。
- **最终共识**：以路径置信度加权多数投票决定最终答案。

**关键实验**：在MATH500、AMC23、AIME24、AIME25、GPQA-diamond五个基准上，使用Qwen3-1.7B~32B及DeepSeek-R1-0528-Qwen3-8B等模型评估。对比Self-Consistency、Adaptive-Consistency、DeepConf-Low/High等基线，DDC在Qwen3-4B上平均准确率高出8.6%（83.4% vs. 74.8%），令牌消耗约降至1/10；在AIME25上准确率提升15.6%且令牌减少27倍。与计算密集型方法（ϕ-Decoding等）相比，DDC在相近或更高准确率下节省29倍令牌。消融研究表明，移除加权贝叶斯或趋势分析均会导致显著性能下降。

**一句话**：DDC通过将路径质量信号耦合到终止与修剪中，将计算资源动态集中于高质量推理链，在显著降低成本的同时保持甚至提升推理性能。
