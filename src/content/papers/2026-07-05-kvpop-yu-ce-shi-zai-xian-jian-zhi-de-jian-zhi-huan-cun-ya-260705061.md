---
title: KVpop -- Key-Value Cache Compression with Predictive Online Pruning
title_zh: KVpop：预测式在线剪枝的键值缓存压缩
authors:
- Lukas Hauzenberger
- Niklas Schmidinger
- Anamaria-Roberta Hartl
- David Stap
- Thomas Schmied
- Sebastian Böck
- Günter Klambauer
- Sepp Hochreiter
affiliations:
- NXAI
- Johannes Kepler University Linz
arxiv_id: '2607.05061'
url: https://arxiv.org/abs/2607.05061
pdf_url: https://arxiv.org/pdf/2607.05061
published: '2026-07-05'
collected: '2026-07-08'
category: LLM
direction: LLM 推理 KV 缓存压缩与剪枝
tags:
- KV Cache
- Eviction Policy
- LLM Inference
- Memory Compression
- Future Attention
- Online Pruning
one_liner: 通过监督未来注意力信号学习固定预算的 KV 缓存淘汰策略，结合延迟评分器，在推理任务上以高压缩比保持性能
practical_value: '- 在电商搜索/推荐系统的 LLM 推理中，KV 缓存是长上下文（如用户行为序列、多轮对话）的瓶颈，KVpop 的固定预算淘汰策略可直接应用于减少显存占用，支持更长上下文而不崩溃。

  - 延迟记忆评分器思路可借鉴：对用户行为序列建模时，不急于丢弃近期 token，等积累更多上下文后再判重要性，更准确地保留关键信息（如近期点击可能关联后续购买意图）。

  - 未来注意力监督的训练方式可迁移到“查询预判”场景：训练一个小型打分器预测 token 对未来查询的效用，用于动态压缩 RAG 召回文档或对话历史。

  - 工程部署中，KVpop 固定预算保证了内存使用上界，适合线上服务稳定运行，可集成到 vLLM 等推理框架中，降低大规模部署成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：自回归解码中 KV 缓存随上下文线性增长，内存与带宽成为瓶颈。现有淘汰方法依赖静态启发式或弱代理分数，难以准确预判 token 的未来效用，导致重要信息被误删。

**方法关键点**：
1. 提出 KVpop，直接学习一个固定预算的 KV 淘汰策略。训练一个打分器对每个 token 做“保留 / 丢弃”二分类，监督信号来自高效计算的未来注意力目标，无需显式构建密集注意力图。
2. 引入延迟记忆打分器：不立即对 token 打分，而是延迟固定步数，积累一定近未来上下文后再判定，从而利用局部序列信息提高淘汰准确性。这是现有学习型淘汰方法中独特的设计。

**关键结果**：
- 在数学推理基准 AIME 和 HMMT 上，Qwen3-4B 在 75% KV 缓存压缩率下仍保持 98% 的全注意力性能，88% 压缩率下保持 97%。
- Qwen3-8B 表现更优，接近无压缩教师模型的性能，显著超过 StreamLLM、H2O、SnapKV 等基线。
- 实验表明，直接监督未来注意力信号是实现低损高压缩的有效路径。
