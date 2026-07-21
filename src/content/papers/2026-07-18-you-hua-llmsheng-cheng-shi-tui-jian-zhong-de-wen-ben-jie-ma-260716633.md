---
title: 'Beyond Fixed Depths and Widths: Optimizing Textual Decoding Tries in LLM-based
  Generative Recommendation'
title_zh: 优化LLM生成式推荐中的文本解码Trie结构
authors:
- Jingzhe Liu
- Hanbing Wang
- Jiliang Tang
- Liam Collins
- Tong Zhao
- Neil Shah
- Mingxuan Ju
affiliations:
- Michigan State University
- Snap Inc.
arxiv_id: '2607.16633'
url: https://arxiv.org/abs/2607.16633
pdf_url: https://arxiv.org/pdf/2607.16633
published: '2026-07-18'
collected: '2026-07-21'
category: GenRec
direction: 生成式推荐 · 解码Trie优化
tags:
- Generative Recommendation
- LLM
- Constrained Beam Search
- Trie Optimization
- Term ID
- Minimum Set Cover
one_liner: 提出BONSAI框架，通过最小集合覆盖构建自适应、低分支的文本解码Trie，将推荐准确率提升最高21.6%
practical_value: '- 解码Trie结构是性能瓶颈：不要只关注term ID的语义质量，Trie的分支因子和深度对束搜索成功率影响巨大，应联合优化。

  - 用最小集合覆盖控制分支：在构建词典树时，每层用贪婪最小集合覆盖算法选择特征，能显著降低浅层分支数，提升束搜索命中率，可直接迁移到现有term ID方法（如表2实验，仅重组ID即提升7.7%~9.1%）。

  - 让ID长度自适应物品语义丰富度：不必强制所有物品用固定长度ID，简单物品短路径、复杂物品长路径，能减少信息损失，对于冷启动物品和新品类尤其有效。

  - 两阶段训练对齐多路径表示：SFT用最长ID作为目标，RL阶段直接优化束搜索下的推荐成功率，让模型学会利用同一物品的多条有效ID路径，适合处理物品有多个别名或关键词的场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM生成式推荐中，自回归生成物品文本ID时需要受限束搜索，解码Trie的结构直接决定搜索空间。现有工作只关注ID语义，却忽视Trie结构——固定深度丢失信息、浅层分支过大导致搜索失误，成为性能瓶颈。

**方法关键**：
- **特征过滤**：用LLM从物品描述中提取关键词，保留信息量高的词，不限制提取数量。
- **Trie构建 (BONSAI)**：将物品视为特征集合，递归地使用最小集合覆盖算法划分物品集合，确保每层分支数最小，自然形成可变深度的Trie。贪婪近似实现算法复杂度低，支持大规模物品集。
- **两阶段训练**：先SFT，用最长ID路径作为监督目标；再RL（GRPO），在真实束搜索约束下采样多条解码路径，以是否命中目标物品作为奖励，强化模型处理多路径表示的能力。

**关键结果**：在Amazon Beauty、Sports、Toys三个数据集上，BONSAI以Qwen3-1.7B为backbone，Recall@5相对最强基线GRLM提升18.7%（Beauty）、16.4%（Sports）、21.3%（Toys）。消融实验证实：浅层分支因子每增加一点，Recall持续下降；强制固定深度会导致性能退化。更关键的是，将BONSAI的最小覆盖重组思路直接应用于GRLM的term IDs，仅改变ID顺序，相对提升7.7%~9.1%，表明Trie结构优化具有普适性。

**核心洞察**：解码Trie的结构设计比ID语义质量更能决定生成式推荐的上限；同时优化分支与深度是低成本大幅提升的方式。
