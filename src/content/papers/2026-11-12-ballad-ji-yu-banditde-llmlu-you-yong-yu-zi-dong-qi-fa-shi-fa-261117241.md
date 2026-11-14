---
title: 'Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery'
title_zh: Ballad：基于Bandit的LLM路由用于自动启发式发现
authors:
- Samidha Verma
- Ankit Anand
- Sayan Ranu
affiliations:
- Indian Institute of Technology Delhi
- Google DeepMind
arxiv_id: '2611.17241'
url: https://arxiv.org/abs/2611.17241
pdf_url: https://arxiv.org/pdf/2611.17241
published: '2026-11-12'
collected: '2026-11-14'
category: LLM
direction: LLM 路由 · 组合优化启发式发现
tags:
- LLM routing
- bandit algorithm
- heuristic discovery
- combinatorial optimization
- model selection
one_liner: 提出Ballad，用在线bandit路由动态选择多个LLM进行启发式发现，效果匹配或超越最强单体模型且降低API成本最高65.6%
practical_value: '- 在需要调用多个 LLM 的业务链路（如 query 改写、商品文案生成、Agent 规划）中，可以用在线 bandit 策略替代固定调用最强模型，在保持输出质量的同时显著降低
  API 成本（论文最高省 65.6%）。

  - 面对非平稳奖励：当 LLM 输出会作为后续 prompt 上下文时，不能假设每次调用独立同分布；可采用 DAG 信用传播将最终得分沿生成谱系回传到祖先节点，正确归因各模型贡献。

  - 选择策略不应只看平均分，而应偏向能产生稀有高分结果的模型（favor rare, high-scoring heuristics），这在创意生成、探索式搜索等场景能避免陷入平庸解。

  - 使用折扣因子淡化陈旧观测，保持对模型当前效用（如模型版本更新、数据分布漂移）的敏感，适合在线学习环境。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：自动启发式发现（AHD）系统利用 LLM 迭代突变和优化启发式，常见假设是更强更贵的模型总能产生更好结果。但通过对多个 NP-hard 组合优化问题的实证，论文发现该假设不成立：更大更贵的模型没有一致优势。这引出一个问题：如何在包含前沿模型与开源/免费模型的池中，自适应地选择每一步调用哪个模型？挑战在于最优模型会随搜索进程变化，且一个 LLM 的输出会成为后续调用的上下文，导致各模型的奖励信号非平稳且相互纠缠，违背经典在线决策的独立性假设。

方法：Ballad 是一个在线 bandit 算法，用于编排多个 LLM 形成集成。其核心包括三点：① LLM 选择策略偏向能产生稀有高分启发式的模型，而非只看稳定平均分；② 基于 DAG 的信用传播机制，沿启发式种群的谱系将最终性能归因到每个祖先模型调用；③ 对陈旧观测施加折扣，保持对模型当前效用的敏感。

结果：在五个 NP-hard 组合优化问题、四个能力与成本各异的 LLM 池上，Ballad 不仅匹配事后（hindsight）最佳单个 LLM，在多个案例中甚至超越所有单模型，同时相比总是使用最强模型降低 API 成本最高达 65.6%。
