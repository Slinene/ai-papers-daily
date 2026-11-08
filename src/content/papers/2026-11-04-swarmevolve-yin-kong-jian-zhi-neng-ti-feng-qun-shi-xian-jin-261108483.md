---
title: 'SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization'
title_zh: SwarmEvolve：隐空间智能体蜂群实现进化发现与优化
authors:
- Qile Jiang
- George Em Karniadakis
affiliations:
- Brown University
arxiv_id: '2611.08483'
url: https://arxiv.org/abs/2611.08483
pdf_url: https://arxiv.org/pdf/2611.08483
published: '2026-11-04'
collected: '2026-11-08'
category: MultiAgent
direction: 多智能体隐空间协作优化
tags:
- MultiAgent
- Latent Reasoning
- KV Cache
- Evolutionary Search
- Program Synthesis
- LLM
one_liner: 数百个低耗agent在latent空间用KV cache通信，以更高吞吐和更低成本完成程序进化搜索
practical_value: '- **KV cache 传递代替文本生成**：在搜索/推荐场景中，多个 agent 需要交换候选 query、文案或策略时，可以直接传递
  hidden states 与 KV cache，避免逐 token decode。适合批量候选生成、prompt 调优、排序策略搜索等环节，能显著降低 token
  成本与延迟。

  - **用 hidden state 距离做 novelty filter**：对 query 推荐、话题推荐、push 文案等需要多样性的任务，可以在隐空间直接度量候选向量距离，去重或保留差异最大的想法，比生成文本后再
  semantic 去重更轻量。

  - **组合 KV caches 做隐空间融合**：summarizer agent 接收各子群 KV cache 实现 crossover，类似多路召回/多专家结果融合，但不生成中间文本。可尝试在召回融合、策略融合中引入
  latent 级 aggregation，减少信息损失和推理开销。

  - **低耗并行 swarm 多角度探索**：数百个轻量 agent 按不同角度并行搜索，适合大候选空间下的快速探索，例如搜索推荐中的超参搜索、策略消融、标签体系探索。但需验证隐空间通信能否稳定保留业务语义，建议先用小规模任务做对比。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 引导的进化搜索需要每轮生成很长的思路链，并重复多次保持种群多样性，导致速度慢、成本高。

**方法关键点**：SwarmEvolve 让每轮数百个低耗 agent 分成多个 swarm，各自从不同角度研究问题；agent 在 latent space 中推理，不解码成文本；通过传递 KV cache 共享信息，降低解码开销。Novelty filter 直接度量 agent hidden state 向量距离，保留差异最大的想法，避免重复。Crossover 也在 latent space 完成：summarizer agent 接收所有 swarm 成员的组合 KV caches，实现隐式思想融合。

**关键结果**：在 21 个数学发现与科学计算问题上，SwarmEvolve 平均得分最高；中位数只需 3–8 分钟即可达到其他 SOTA 框架 60 分钟得到的最好分数。使用 Qwen3 8B 时，在若干问题上超过了 AlphaEvolve 最初用前沿 LLM 找到的解；60 分钟内生成程序数量也明显更高。
