---
title: Regret Minimization with Adaptive Opponents in Repeated Games
title_zh: 重复博弈中面向自适应对手的后悔最小化
authors:
- Mingyang Liu
- Asuman Ozdaglar
- Tiancheng Yu
- Kaiqing Zhang
affiliations:
- Massachusetts Institute of Technology
- OpenAI
- University of Maryland, College Park
arxiv_id: '2606.06486'
url: https://arxiv.org/abs/2606.06486
pdf_url: https://arxiv.org/pdf/2606.06486
published: '2026-06-03'
collected: '2026-06-06'
category: MultiAgent
direction: 重复博弈中的后悔最小化与多智能体学习
tags:
- Repeated Games
- Regret Minimization
- Adaptive Opponents
- Multi-Agent Learning
- Non-convex Optimization
one_liner: 提出重复策略后悔(RP-Regret)度量，并设计算法应对自适应对手，引导多智能体学习更优均衡
practical_value: '- 在多智能体推荐或竞价场景中，若对手策略自适应，传统外部后悔可能失效，可借鉴 RP-Regret 设计学习目标，引导模型考虑历史交互的长期影响，避免短视决策。

  - 算法中提出的线性化 surrogate 处理非凸后悔目标，可为求解复杂策略空间下的多智能体优化提供工程化近似思路，类似将非凸问题分解为每步凸优化子问题。

  - 实验中所有智能体均最小化 RP-Regret 时可自发学到高合作均衡（如猎鹿博弈），该性质可应用于电商多 Agent 协作任务（如联合定价、库存共享），促进整体收益提升。

  - 方法对对手记忆长度的理论分析，可指导实际系统设计时限制对手或自身历史依赖，以控制学习复杂度并保证收敛。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：重复博弈中标准外部后悔无法捕捉对手的自适应行为，现有后悔度量要么比较基准过弱，要么对对手记忆施加严格限制。为此，论文从博弈论角度提出重复策略后悔(RP-Regret)，衡量实际收益与所有玩家都能根据历史响应时的最佳事后收益之差，更自然地刻画重复交互中的反事实推理。

方法：RP-Regret 定义本身非凸且依赖对手策略，直接最小化困难。作者首先给出达到次线性后悔的必要条件，涉及比较策略的变化幅度与对手记忆长度。随后针对非凸挑战设计三种算法：(i) 基于离线优化预言机的通用方法；(ii) 每步最小化线性化并凸化的 surrogate 函数；(iii) 对手策略缓慢变化时直接最小化 RP-Regret。所有算法均提供理论保证。

结果：在满足必要条件下，所提算法可实现 RP-Regret 随时间次线性增长。当所有玩家均运行最小化 RP-Regret（或其线性化变体）的算法时，重复博弈的某些子博弈完美均衡可被学习。在猎鹿博弈实验中，最小化所提后悔的智能体显著更频繁地选择高收益的合作均衡，验证了度量在促进合作方面的有效性。
