---
title: 'The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation
  for LLMs'
title_zh: 推理的影子价格：经济视角的LLM最优预算分配
authors:
- Xu Wan
- Speed Zhu
- Jianwei Cai
- Guang Chen
- XiMing Huang
- Wiggin Zhou
- Mingyang Sun
affiliations:
- Zhejiang University
- Tencent HY Team
- Peking University
arxiv_id: '2606.03092'
url: https://arxiv.org/abs/2606.03092
pdf_url: https://arxiv.org/pdf/2606.03092
published: '2026-06-01'
collected: '2026-06-05'
category: LLM
direction: LLM推理预算优化
tags:
- inference-time scaling
- budget allocation
- shadow price
- LLM
- constrained optimization
- reasoning
one_liner: 用影子价格模型实现LLM推理预算的全局优化，显著提升资源稀缺时的准确率，最高3倍于均匀分配。
practical_value: '- 借鉴CLEAR的边际效用均衡分配思想，对线上LLM调用做动态算力配额：优先将预算分配给接近「涌现阈值」的可解query，放弃无解query，避免算力浪费，适用于推荐系统中的解释生成、对话Agent等高频LLM场景。

  - 利用shifted-surge效用函数刻画每个query的推理收益曲线，为生成式推荐中不同物品的推理深度决策提供可量化的成本-收益模型。

  - 全局影子价格概念可拓展到多Agent或RAG系统，统一协调各子模块的计算资源，实现端到端最优分配，而非各模块独立优化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM推理时缩放（inference-time scaling）能显著提升复杂任务性能，但线上部署受严格的计算预算限制。如何将总预算最优地分配给大量不同难度的query是亟待解决的问题。

**方法**：将推理预算分配建模为全局约束优化问题。基于观察到的S形计算-效用曲线，用shifted-surge函数拟合每个query的推理收益。引入影子价格（shadow price）概念，推导出边际效用均衡的最优分配策略，提出CLEAR（Constrained Latent-utility Equilibrium Allocation for Reasoning）。CLEAR会理性放弃无解的query，并将资源重新分配给接近涌现阈值的可解query。

**结果**：在多个推理任务和不同流量流实验上，CLEAR显著改善了总token成本与平均准确率的帕累托前沿。在资源稀缺情况下，相较均匀分配，CLEAR实现了最高3倍的全局准确率提升。
