---
title: Exact Quantile Balancing and Load-Error Injection for Mixture-of-Experts
title_zh: 精确分位数平衡与负载误差注入用于混合专家模型
authors:
- Pit Neitemeier
- Jiaze Li
- Alessio Serra
- Philipp Scholl
- Sohir Maskey
affiliations:
- Aleph Alpha
arxiv_id: '2609.28053'
url: https://arxiv.org/abs/2609.28053
pdf_url: https://arxiv.org/pdf/2609.28053
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: MoE 训练负载均衡优化
tags:
- MoE
- Load Balancing
- Quantile Balancing
- Distributed Training
- Router Gradient
one_liner: 提出 EQB 精确全局分位数计算和 LEI 局部负载误差梯度注入，提升 MoE 训练平衡与质量
practical_value: '- 若自研大规模 MoE 推荐/排序模型，可借鉴 EQB：用两次 256-bin all-reduce 的 BF16 radix
  selection 计算精确全局分位数，替代 rank-local 平均近似，消除数据划分偏差，通信开销可忽略。

  - 局部负载均衡可尝试 LEI：把局部负载误差直接注入 router-score 梯度，替代 GShard 辅助 loss，在保证模型质量的同时改善 expert-parallel
  microbatch 级均衡，降低计算 skew。

  - 训练 MoE 时将全局平衡与局部平衡解耦处理：仅全局平衡可能掩盖 microbatch 级偏斜，导致 EP 效率下降；应同时监控并优化两个层级。

  - 对于已有 MoE 推理服务，若发现某些 expert 过载，可参考该工作的平衡机制思路，通过微调 router 偏差或梯度注入来优化负载分布。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：MoE 训练需要全局负载均衡避免专家利用不足，同时需要局部均衡保证 expert-parallel 执行效率。现有分布式 Quantile Balancing (QB) 使用分片依赖或近似全局分位数，存在偏差或精度限制；token 无关的 expert biases 无法确保 microbatch 级平衡。

**方法关键点**：
- 提出 Exact Quantile Balancing (EQB)：使用两遍 BF16 radix selection，通过每层两次 256-bin all-reduce 精确计算全局 batch 的经验分位数，通信开销可忽略。
- 提出 Load-Error Injection (LEI)：将局部负载误差直接注入 router-score 梯度，替代传统辅助 loss，实现更直接、高效的局部负载均衡。

**关键结果数字**：在 7.5B 参数 MoE 上训练至 500B tokens，EQB 相比 naive QB 提升全局负载均衡和下游性能；LEI 相比 GShard loss 改善局部均衡，同时保持可比甚至更优的模型质量。
