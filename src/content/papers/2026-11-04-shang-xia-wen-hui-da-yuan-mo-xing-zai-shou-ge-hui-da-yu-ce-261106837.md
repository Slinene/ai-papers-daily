---
title: 'Context--Answer Metamodels: Forecasting LLM Activations Before the First Answer
  Token'
title_zh: 上下文-回答元模型：在首个回答token前预测LLM激活
authors:
- Tommy He
- Thomas Jiralerspong
affiliations:
- Tufa Labs
- Mila, Université de Montréal
arxiv_id: '2611.06837'
url: https://arxiv.org/abs/2611.06837
pdf_url: https://arxiv.org/pdf/2611.06837
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM 激活预测与行为预筛
tags:
- activation forecasting
- LLM
- stochastic decoding
- metamodel
- behavior screening
- cross-model transfer
one_liner: 用上下文激活序列训练元模型，在生成前高保真预测回答激活分布及其行为信号
practical_value: '- 在 Agent/LLM 推荐链路中，可在生成前用 context hidden states 预测后续回答的 mean-pooled
  activations 分布，用于低成本的 rare-behavior 筛选与 pass@k 估计，替代多次采样评分；尤其适合电商导购 Agent 提前拦截高风险/不合规推荐。

  - 跨模型迁移信号：用 Qwen2.5 上下文激活预测 Qwen3.5/Gemma 4 回答激活，说明可搭建轻量“行为回归”metamodel，在基座模型升级时复用旧激活数据，减少新模型行为评估的重复采样成本。

  - 分布预测可输出 rollout 变异性，用于在线置信度校准：当预测分布方差大时触发额外采样或人工审核，平衡成本与推荐质量。

  - 工程上，metamodel 输入是已有的 context activation 序列，输出仅 mean-pooled answer activation，可在缓存
  context KV/hidden states 后做低延迟前向，基本不增加首 token 延迟。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：随机解码下单一上下文可产生多种回答，评估行为变异性需多次昂贵 rollout；希望仅凭读取上下文时的激活在生成前预测回答激活。
方法关键点：训练 context-answer metamodels，将上下文激活序列映射到 mean-pooled 回答激活的点估计或分布预测；研究四类元模型，覆盖点预测与分布预测。
结果：四类元模型高保真预测 mean-pooled 回答激活；分布元模型捕捉 rollout 变异性；训练集增至 500k prompts 性能提升，零样本泛化到域外数据集；预测保留行为预测信号；Qwen2.5 上下文激活可预测 Qwen3.5 和 Gemma 4 的回答激活，显示跨模型迁移能力。
结论：上下文激活轨迹可支持在首个回答 token 生成前可扩展地预测 LLM 回答行为。
