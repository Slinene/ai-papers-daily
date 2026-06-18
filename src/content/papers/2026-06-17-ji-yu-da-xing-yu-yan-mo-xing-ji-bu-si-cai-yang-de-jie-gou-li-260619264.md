---
title: Structured Inference with Large Language Gibbs
title_zh: 基于大型语言模型吉布斯采样的结构化推理
authors:
- Sanghyeok Choi
- Henry Gouk
- Esmeralda S. Whitammer
affiliations:
- University of Edinburgh
- CIFAR
arxiv_id: '2606.19264'
url: https://arxiv.org/abs/2606.19264
pdf_url: https://arxiv.org/pdf/2606.19264
published: '2026-06-17'
collected: '2026-06-18'
category: Reasoning
direction: LLM 结构化概率推理
tags:
- MCMC
- Gibbs sampling
- structured inference
- LLM conditionals
- probabilistic reasoning
- generative models
one_liner: 用 LLM 的条件分布作 MCMC 转移算子迭代采样结构化变量，避免一次生成顺序偏差
practical_value: '- 在推荐系统中需要生成结构化对象时（如用户属性填充、搭配生成、解释文本），可以用 LLM 的条件分布迭代修正初始生成，提升一致性，避免一次自回归导致的顺序偏差。

  - 若业务中存在多个相互依赖的变量（如商品多字段补全、会话上下文中用户意图推断），可采用 Gibbs 采样式多次查询 LLM，利用各个局部条件相互校准，得到更符合全局分布的样本。

  - 工程上，可将此方法封装为一种“反思-修正”循环，适用于需要高度一致性和概率连贯性的场景，如对话推荐中的实体消歧、属性约束满足。

  - 注意该方法依赖于 LLM 提供可靠的条件分布，实际部署时需权衡计算开销与生成质量，可优先在离线数据增强或高价值交互中尝试。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 隐式编码了世界知识，可用于结构化变量推理，但常见的一次自回归生成会引入顺序依赖偏差（如近因效应、上下文忽略），无法保证全局一致性。

**方法**：提出 Large Language Gibbs，将 LLM 视为一组局部条件分布（通过 next-token 概率获得），用 Gibbs 采样方式迭代重采样每一个变量，条件于其他变量当前值。此过程构成马尔可夫链，最终收敛到稳态分布，该分布是所有局部条件分布的折中，避免了顺序影响。

**实验**：在合成分布采样、一致性推理任务、贝叶斯结构学习上测试，采用 GPT 系列模型。定量对比一次性生成与 Gibbs 迭代方法，评估生成样本的分布匹配度与任务正确率。

**结果**：LLM Gibbs 在多项指标上优于单次生成，尤其在需要维持多变量约束的一致性任务中表现突出，验证了用 LLM 条件分布进行 MCMC 的可行性。
