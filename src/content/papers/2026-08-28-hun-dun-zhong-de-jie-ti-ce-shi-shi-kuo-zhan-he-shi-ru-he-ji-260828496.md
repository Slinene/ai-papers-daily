---
title: 'Ladders in Chaos: When, How, (and Perhaps Why) Does Test-Time Scaling Improve
  LLM Machine Translation'
title_zh: 混沌中的阶梯：测试时扩展何时、如何及为何提升 LLM 机器翻译
authors:
- Di Wu
- Sergey Troshin
- Christof Monz
- Antske Fokkens
- Vlad Niculae
affiliations:
- University of Amsterdam
- Vrije Universiteit Amsterdam
arxiv_id: '2608.28496'
url: https://arxiv.org/abs/2608.28496
pdf_url: https://arxiv.org/pdf/2608.28496
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM 测试时扩展 · 机器翻译
tags:
- test-time scaling
- machine translation
- sequential sampling
- self-refinement
- reranking
- LLM
one_liner: 系统比较顺序与并行采样在 LLM 机器翻译中的表现，揭示顺序采样在小预算下上限更高并解释其机制
practical_value: '- 在 LLM 生成推荐理由、广告文案、push 文案等短文本任务中，可优先用顺序自精炼（把前一轮输出拼到上下文）而非仅做 i.i.d.
  采样+重排；小预算下可用更少采样得到更高上限和更好的自然度。

  - 注意顺序扩展不是无代价：推理预算很大时会损害准确性/忠实度，因此业务中应对准确性敏感场景设置预算上限，并用自动指标或人工抽检监控“流畅但偏离原意”。

  - 机制上，顺序采样的收益部分来自扩大目标侧上下文，提示我们在生成式推荐/query 改写中不必只重写，可让模型“看到并续写”前序候选，把前序输出作为 soft
  context；但上下文构造方式要谨慎，温度可保持鲁棒。

  - 如果链路中已有 rerank 模块，可尝试 hybrid：小预算先并行采样+rerank 拿一个较优候选，再用顺序自精炼补强自然度，而不是简单堆 N。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 测试时扩展主要有顺序与并行两种范式，但它们在机器翻译中的差异和机制缺少系统拆解，复杂 multi-agent/pipeline 又难以隔离变量。

方法：对比顺序采样（后续生成依赖前序结果）与并行 i.i.d. 采样+Best-of-N 重排；用多维人工分析、受控实验和消融，考察采样预算、温度、上下文构造等因素。

关键结果：顺序采样具有更高性能上限，且样本更丰富有效，尤其在小采样预算下；人工评估显示顺序采样明显改善流利度与自然度，但大推理预算下会损害准确性；收益机制部分可归因于模型获得更大的 target-side context；顺序采样对温度鲁棒，但对上下文构造敏感。
