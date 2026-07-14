---
title: Active Offline-to-Online Reinforcement Learning
title_zh: 主动离线到在线强化学习：有限交互下策略选择与微调
authors:
- Alper Kamil Bozkurt
- Shangtong Zhang
- Yuichi Motai
affiliations:
- Virginia Commonwealth University
- University of Virginia
arxiv_id: '2607.11720'
url: https://arxiv.org/abs/2607.11720
pdf_url: https://arxiv.org/pdf/2607.11720
published: '2026-07-13'
collected: '2026-07-14'
category: Other
direction: 离线到在线强化学习策略选择
tags:
- Offline-to-Online RL
- Policy Selection
- Fine-tuning
- Upper Confidence Bound
- Performance Forecast
one_liner: 提出基于上置信界主动选择策略以平衡离线到在线强化学习中评估与微调的交互分配
practical_value: '- 在推荐模型迭代中，若有多个候选模型（不同结构或超参）需在线评估与微调，可借鉴主动策略选择思想：先用少量流量评估，再动态分配更多流量给高潜力模型微调，代替一次性选定一个模型全量上线

  - 使用局部线性性能预测 + UCB 权衡探索与利用，适合非平稳环境下的在线模型持续优化，例如电商推荐中用户兴趣漂移

  - 工程实现上可维护模型池，通过在线交互数据不断更新各模型的性能预测，自动筛选和提升最优模型，降低人工选模型的风险

  - 方法不依赖特定RL算法，同样适用于Bandit或监督学习的在线微调场景'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：离线到在线强化学习（O2O-RL）常需离线预训练多个策略，再在有限在线交互预算下选择最优者微调。但单一策略选择风险高，且算法超参敏感。如何有效分配在线交互于策略评估与微调是核心挑战。  
**方法**：将该问题形式化为评估（识别好策略）与微调（提升策略性能）的预算权衡。提出主动策略选择框架：对每个候选策略，利用在线评估获得的性能数据拟合局部线性预测模型，估计未来性能的上置信界（UCB）；每步选择UCB最高的策略分配交互进行微调，并更新其观测与预测。  
**结果**：在多种任务（如MuJoCo、Adroit）和不同算法基线上，该方法一致优于只选最高估值策略或均分预算的方​​法，在有限交互下获得更高最终性能。  
**结论**：主动选择与微调能更高效利用有限在线交互，避免过早承诺单一策略，提升部署可靠性。
