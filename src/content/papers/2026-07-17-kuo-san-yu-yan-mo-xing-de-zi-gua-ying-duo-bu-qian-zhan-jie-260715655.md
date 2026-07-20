---
title: Adaptive Multi-Step Lookahead Decoding for Diffusion Language Models
title_zh: 扩散语言模型的自适应多步前瞻解码
authors:
- Yingqian Cui
- Wei Deng
- Lantao Mei
- Hang Li
- Charu C. Aggarwal
- Hui Liu
- Yue Xing
affiliations:
- Michigan State University
- Morgan Stanley
- IBM T.J. Watson Research Center
arxiv_id: '2607.15655'
url: https://arxiv.org/abs/2607.15655
pdf_url: https://arxiv.org/pdf/2607.15655
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 扩散语言模型自适应解码优化
tags:
- Diffusion Language Models
- Adaptive Decoding
- Lookahead Decoding
- Parallel Generation
- Text Generation
- Efficiency
one_liner: 提出自适应前瞻解码框架，动态决定前瞻深度，在扩散语言模型上实现更优的准确率-步数权衡
practical_value: '- 自适应前瞻机制可迁移至多步Agent决策：当中间状态不确定性高时触发更深入的规划，避免固定深度造成的浪费或不足。

  - 基于候选评分方差的动态探索停止策略，可直接用于推荐系统的多步重排序或生成式推荐的解码过程，节省计算量。

  - 并行解码与前瞻结合的思路，可启发电商搜索中的批量query生成或文案生成，在效率与质量间取得更好平衡。

  - 从中间状态重新触发前瞻的机制，类似于Agent在任务执行中根据中间结果重新规划，可用于复杂推荐流程的实时调整。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

## 动机
扩散语言模型（DLMs）通过并行修正掩码token实现高效文本生成，但现有一步前瞻解码只优化即时信息增益，长期解码轨迹可能次优。直接扩展为固定深度前瞻会引入额外计算且不能适应异质的中间状态。

## 方法
提出 **AdaLook** 自适应前瞻框架：
- **动态深度决策**：基于候选评分方差（candidate-score variance）判断是否继续向前展开（rollout），方差大意味着当前状态高度不确定，需要更深前瞻。
- **分支展开**：当中间展开状态仍需更多探索时，从该状态重新触发前瞻以扩展搜索分支。
该设计避免不必要的深度展开，同时允许在信息量的中间状态重新探索，实现更精细的准确-步数权衡。

## 结果
在多个基准测试（如MATH500）和模型（LLaDA-8B-Instruct等）上，AdaLook 相较于现有一步前瞻解码方法，在相同解码步数下取得更高准确率，或在相同准确率下减少解码步数，验证了自适应多步前瞻的有效性。
