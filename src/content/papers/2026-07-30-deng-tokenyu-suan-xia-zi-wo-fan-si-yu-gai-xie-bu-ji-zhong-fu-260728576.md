---
title: 'Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling
  at Equal Token Cost, from 1.5B to 7B'
title_zh: 等Token预算下，自我反思与改写不及重复采样：1.5B至7B模型实验验证
authors:
- Iliya Mirzaei
affiliations:
- Stony Brook University
arxiv_id: '2607.28576'
url: https://arxiv.org/abs/2607.28576
pdf_url: https://arxiv.org/pdf/2607.28576
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: 推理方法效率评估
tags:
- self-refine
- reflexion
- repeated-sampling
- reasoning-evaluation
- token-cost
- llm-inference
one_liner: 在相同生成token成本下，所有自我审视方法均不优于简单重复采样，且模型增大后改写类方法仍显著落后。
practical_value: '- **Agent 决策中避免过度自我反省**：在搜索推荐 Agent 的设计中，让模型反复审查自身输出、改写答案可能不如直接多次采样并取多数投票高效，尤其在延迟敏感的在线推理场景，应优先考虑简单的并行采样策略。

  - **预算控制应以实际生成 token 数为准**：对比不同推理策略时，需严格统计所有提示、反思、改写、辩论等环节的 token 消耗，否则可能高估复杂提示工程的实际收益。

  - **小模型更适合简单 Best-of-N**：1.5B 级别模型自我挑选答案会带来显著负收益，直接取多数票即可；模型增大到 7B 后差异缩小，但仍无需引入昂贵自我评估。

  - **反思重写机制需谨慎验证**：在商品描述生成、查询改写等任务中，若采用 Self-Refine 或 Reflexion 类方法，需在同等计算预算下与多次采样基准对比，确保额外
  token 消耗带来真正提升而非仅由采样多样性贡献。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Self-Refine、Reflexion 等自我审视方法通过让模型生成更多文本来改进推理，但现有研究未严格控制生成 token 成本，增益可能仅来自多写文本而非方法本身。Wang et al. 提出在等预算下重复采样并取多数答案常优于复杂方法，但缺乏统计显著性检验。

**方法**：作者设计了对照实验，在 1.5B、3B、7B 开源模型上，针对两个数学基准（各 150 题），比较了七种方法（含 Best-of-N、Self-Refine、Reflexion 等），严格统计所有 token 消耗，以重复采样为等成本基线，进行配对差异检验，并用 Bootstrap 置信区间和多重比较校正。

**关键结果**：在全部 36 组比较中，无一方法可靠优于等成本重复采样；10 组可靠更差，且全属自我审视类。18 次自我审视对比均为负向。随模型增大，Best-of-N 中让模型自选答案的危害从 1.5B 的 8.0-11.3 点降至 7B 的 2.0-1.3 点（不显著），但改写型方法如 Self-Refine 在 7B 仍显著落后 3.6-10.1 点。Reflexion 在最小模型上未触发重试，退化为单次 CoT。
