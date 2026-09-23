---
title: 'Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning'
title_zh: 超越重复采样：学习用于LLM推理的搜索策略
authors:
- Ismail Labiad
- Matthieu Kowalski
- Marc Schoenauer
- Rémi Munos
- Julia Kempe
affiliations:
- Meta FAIR
- Université Paris-Saclay
- Inria
- CNRS
- NYU Courant Institute and CDS
arxiv_id: '2609.26704'
url: https://arxiv.org/abs/2609.26704
pdf_url: https://arxiv.org/pdf/2609.26704
published: '2026-09-22'
collected: '2026-09-23'
category: Reasoning
direction: LLM推理 · 可训练搜索策略
tags:
- LLM reasoning
- test-time compute
- reinforcement learning
- concept generation
- search policy
- pass@k
one_liner: 用RL训练小型概念生成器作为大模型推理的搜索策略，在hard数学问题上pass@128翻倍并跨模型迁移
practical_value: '- 推理时多样性不要只调 temperature/top-p，可以在 prompt 层注入多个高层概念、策略或意图，并用单轨迹批量生成，避免近重复采样；对应推荐/广告中可对同一
  query 生成多个语义方向再分别生成候选文案或推荐理由。

  - 训练小型 orchestrator/概念生成器作为黑盒或闭源大模型的搜索策略，RL 奖励直接来自下游大模型的 pass@k；max-of-mean 比 max-of-max
  信息量更大、更稳定，适合作为奖励聚合方式。

  - 训练成本主要在下游大模型 rollout 和 judge，可以用固定 judge 复用并离线采样；在业务中训练轻量 agent 来引导重模型探索，不必微调大模型，且学习到的策略可跨模型家族迁移。

  - 实验设计要公平：基线必须使用高温度、高 top-p 的探索性解码，否则概念引导或策略提升的效果可能虚高；报告 pass@k 时要匹配相同的 answer generation
  预算。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM 推理越来越依赖测试时计算，但主流仍是 naive repeated sampling，通过局部 token 噪声探索，容易产生大量近重复解答而非真正不同的思路。RL 训练和推理都受限于探索质量。已有概念引导采样虽被提出，但复现发现其优势在允许基线探索解码后几乎消失，且原方法概念数少、迭代生成效率低。

**方法关键点**：
- 改进推理时概念生成：单轨迹一次生成多条具体、非重复概念，并明确要求不直接给答案；
- 聚焦 hard problems：用答案生成器 128 rollouts 0% 正确的问题作为评估集；
- 训练概念生成器：用 GRPO-style RL 训练 Qwen2.5-7B 概念生成器，奖励来自冻结 Qwen2.5-32B 答案生成器的下游成功率；比较 max-of-max 和 max-of-mean 两种奖励聚合；
- 训练数据来自 DeepMath-103k，过滤出 AG 成功率 <5% 的问题，评估用 1k held-out 全 0% 问题；OOD 用 Omni-MATH 2 过滤。

**关键结果**：
- DeepMath held-out 上，naive repeated sampling pass@128 为 19.0%，RL 训练后的概念生成器 max-of-mean 达到 39.2%，几乎翻倍；pass@64 从 11.4% 提升到 29.6%；
- 7B trained CG 超过 untuned 32B CG（39.2% vs 33.8% pass@128），并迁移到 Llama-3.3-70B，达到 34.3% vs naive 26.2%，超过其自身概念 28.9%；
- 消融显示问题相关概念贡献约 15 个点提升，答案泄漏极低，概念数从 1 增到 10 可提高 pass@128 但 pass@1 不变；
- 生成概念的计算开销不到单个 AG rollout 的 0.3%。

**最值得记住的一句话**：小型可训练搜索策略能以几乎可忽略的推理成本，显著提升大型冻结模型在难题上的探索效率，并具备跨模型迁移能力。
