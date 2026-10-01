---
title: Component-Aware Feedback for Self-Evolving Programs
title_zh: 组件感知反馈驱动的自进化程序
authors:
- Ethan Lin
- Jinming Nian
- Yi Fang
affiliations:
- Santa Clara University
arxiv_id: '2609.38639'
url: https://arxiv.org/abs/2609.38639
pdf_url: https://arxiv.org/pdf/2609.38639
published: '2026-09-29'
collected: '2026-10-01'
category: LLM
direction: LLM 程序进化 · 组件级归因反馈
tags:
- LLM
- Evolutionary Search
- Attribution
- Reranking
- Program Synthesis
- Multi-Objective
one_liner: 对进化搜索中的每次代码变更做组件级归因并写入记忆，让 LLM mutator 在重排任务上收敛更快、效果更好
practical_value: '- 在 LLM-guided evolutionary search 或自动优化 pipeline 中，不要只给 mutator
  看完整代码和总分；把每次 mutation 的组件 diff（新增/删除/修改的函数、常量）与 evaluator 返回的 metric 变化组成 `(component_set,
  delta_metrics)` 记录，显式注入 prompt，能显著减少 LLM 从长上下文推断编辑效果的负担。

  - 双参考帧设计值得复用：local frame（child vs parent）回答“上一步有没有用”，global frame（child vs seed）回答“整条
  lineage 是否值得继续”。在搜索停滞时调用 global frame，可帮助 mutator 换策略而不是在局部瞎试。

  - 多目标优化目标函数可借鉴：将质量项和成本项分别对 seed 归一化，加一个小的 λ 项和 `min(a,b)` 项，既能同时优化质量和 token 成本，又避免搜索只玩一个维度。电商重排/广告出价等成本敏感场景可以直接套用。

  - 本地可服务模型（如 Qwen3.6-35B-A3B）就够用，不依赖 frontier LLM；组件级归因反馈提高了样本效率和跨域泛化，对线上持续自动调参/调
  pipeline 有直接工程价值。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM-guided evolutionary search 通过不断变异程序并评估 fitness 来发现更好算法，但现有方法大多只保留程序源码和总分，丢弃了“哪个组件改动导致了哪个指标变化”。这迫使 mutator LLM 从杂乱的长历史中隐式推断先前编辑的效果，搜索慢且不稳定，尤其对本地可服务的开源模型更明显。本文聚焦于：每次评估应保留什么信息，才能最好地指导下一轮变异。

## 方法关键点
- 将程序分解为 named components（函数和模块级常量），对 parent/child 做 diff，识别新增、删除、修改的组件，并把它们与 evaluator 返回的 metric 向量差组成一个 edit 记录。
- 维护 attribution memory，将这些 edit 记录累积起来，在 mutation prompt 中显式呈现，避免 LLM 依赖隐式推理。
- 采用双参考帧：**local frame** 对比 child 与 parent，回答“上一步编辑是否有效”，以滑动窗口（最近10条）进入 prompt；**global frame** 对比 child 与 seed，用于搜索停滞时展示整条 lineage 的累积变化，帮助决策是否换方向。
- 不依赖 LLM 总结、额外评估或学习模型，完全由已有评估结果程序化提取。
- 应用于 LLM reranking：多阶段 pipeline 需要同时权衡检索质量与 serving 成本；设计 cost-aware objective 将 nDCG 增益和 token 节省分别归一化，并用 `min(a,b)+λ(a+b)` 平衡双向优化。

## 关键实验
在 BRIGHT 全部 12 个数据集上，用 Qwen3.6-35B-A3B 同时作为 mutator 和 reranker，与 AdaEvolve 对比：
- 质量目标下，held-out nDCG@10 达到 0.346，相对 AdaEvolve 的 0.323 提升 7.2%，在 9/12 数据集上领先；中位 31/100 轮次即达到 AdaEvolve 最终分数，收敛速度快约 3 倍。
- cost-aware 目标下，平均 nDCG@10 0.305 且 tokens/query 12,676，相比 AdaEvolve 的 0.296 和 14,243 tokens，质量更高且成本低 11%。
- 跨域泛化：在 biology 上优化后直接迁移到其他域，保留 90% 分数，AdaEvolve 只有 79%。
- 消融：decomposed metrics 与 attribution 各贡献约一半增益；attribution 减少 train-test gap。

**最值得记住的一句话**：当程序包含多个交互组件时，告诉 mutator“哪个组件改动移动了哪个指标”与决定“变异哪个程序”同样重要。
