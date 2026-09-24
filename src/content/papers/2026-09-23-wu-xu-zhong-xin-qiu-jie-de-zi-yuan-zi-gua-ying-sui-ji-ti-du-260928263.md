---
title: Resource-Adaptive Stochastic Gradient Descent for Online Linear Programming
  without Re-solving
title_zh: 无需重新求解的资源自适应随机梯度下降在线线性规划
authors:
- Jiameng Lyu
affiliations:
- Department of Management Science, School of Management, Fudan University
arxiv_id: '2609.28263'
url: https://arxiv.org/abs/2609.28263
pdf_url: https://arxiv.org/pdf/2609.28263
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: 在线线性规划 · 资源自适应SGD
tags:
- Online Linear Programming
- Stochastic Gradient Descent
- Resource Pricing
- Logarithmic Regret
- First-order Method
one_liner: 提出RASGD，用O(m)一阶SGD更新资源价格，避免重求解LP，达到O(log T) regret
practical_value: '- 在电商/广告资源约束分配场景（如预算、库存、LLM推理算力配额），可用一阶SGD替代per-arrival LP重求解，每到达仅O(m)时间与内存，适合高并发实时决策。

  - 步长策略可借鉴：早期小步长学习资源价格，后期增大步长以快速响应库存消耗，无需人工调参，在不同资源消耗阶段自适应。

  - 算法在标准非退化条件下每条样本路径可行，并达到O(log T) regret，适合对安全性和长期收益都有要求的在线广告投放、流量分配系统。

  - 适用于LLM推理服务中的资源定价：每个请求到达时根据剩余算力/令牌配额动态更新影子价格，指导准入或资源预留，无需离线求解大规模LP。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM推理、搜索服务、在线广告等场景中，在线线性规划（OLP）规模急剧增大，传统per-arrival LP重求解或样本平均近似计算成本过高，需要O(m)级轻量算法。

**方法**：提出RASGD，每个请求到达时，仅利用当前请求与剩余资源库存，通过一阶SGD更新资源价格（对偶变量）。核心是把重求解中的当前资源定价逻辑表达为SGD更新：对偶目标中剩余库存项动态刷新，步长早期较小以稳定学习，后期增大以匹配库存调整速度。算法无需LP求解或样本平均优化，每到达仅O(m)操作与内存。

**结果**：在标准非退化条件下，RASGD在所有样本路径上可行，且对已实现的分式后见最优解达到O(log T)期望后悔，与下界匹配，即使对手是已知分布且无计算限制的策略。数值实验表明其后悔与per-arrival LP重求解竞争，优于测试的一阶baseline，同时保持一阶方法的计算效率。
