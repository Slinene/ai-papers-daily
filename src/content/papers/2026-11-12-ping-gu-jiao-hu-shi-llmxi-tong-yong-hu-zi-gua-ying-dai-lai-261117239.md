---
title: 'When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems'
title_zh: 评估交互式LLM系统：用户自适应带来的挑战
authors:
- Hannah Li
arxiv_id: '2611.17239'
url: https://arxiv.org/abs/2611.17239
pdf_url: https://arxiv.org/pdf/2611.17239
published: '2026-11-12'
collected: '2026-11-15'
category: Eval
direction: LLM交互系统评估·用户自适应
tags:
- Evaluation
- User Adaptation
- A-B Testing
- LLM
- Interactive Systems
- Prompt Endogeneity
one_liner: 定义常见分布效应与诱导分布效应，揭示离线评估与在线A/B测试的差异及排名反转条件
practical_value: '- 离线评估与在线A/B测试可得出不同排名：离线测试集反映 common-distribution effect，线上用户自适应后反映
  induced-distribution effect。选型模型时同时关注两类指标，不能仅依赖离线 benchmark 决策。

  - 部署对话推荐/搜索助手时，监控用户行为变化（查询复杂度、交互深度、任务类型）作为模型效果的补充信号，防止 reward hacking 或 novelty
  effect 导致的短期指标虚高。

  - 论文给出的排名一致性充分条件可作为启发式：若离线与线上排名冲突，检查用户自适应程度和提示分布差异，重新设计离线评估以模拟用户适应过程。

  - 用户自适应会增大线上估计方差，实验设计时需考虑更长观察期和更稳健的方差估计方法。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**  
LLM 交互系统中用户会观察模型响应并调整后续提示，导致评估所用的 prompt 分布受模型自身影响（prompt endogeneity）。传统离线 benchmark 和在线 A/B 测试可能因此测量不同对象。  

**方法关键点**  
- 定义两个估计量：common-distribution effect（在同一 prompt 分布上比较模型）与 induced-distribution effect（在各自交互生成的 prompt 分布上比较）。  
- 证明离线评估的差分均值估计收敛到 common-distribution effect，而在线 A/B 测试收敛到 induced-distribution effect。  
- 推导两者排名反转发生的条件，给出排名一致的充分条件，可作为判断离线评估是否足以代替线上实验的实用启发式。  
- 在简单线性交互模型中展示用户自适应会增加估计方差。  
- 分析自适应性如何统一解释 reward hacking、novelty effect 等常见评估挑战。  

**关键结果**  
- 离线评估与在线实验可能得出相反的模型排名，导致部署决策错误。  
- 给出保证排名一致的充分条件，为实验设计提供理论依据。  
- 用户自适应性增加方差，且是多种评估偏差的共同机制。  
- 强调评估时必须同时测量模型性能和模型诱导的用户行为变化。
