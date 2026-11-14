---
title: 'SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One
  Models'
title_zh: SO-Arena：系统一模型能力谱与决策可靠性基准测试
authors:
- Lichen Li
- Ziping Dong
- Sicheng Feng
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2611.15777'
url: https://arxiv.org/abs/2611.15777
pdf_url: https://arxiv.org/pdf/2611.15777
published: '2026-11-10'
collected: '2026-11-14'
category: Eval
direction: LLM 评估基准 · 决策可靠性
tags:
- System One
- Benchmark
- LLM Evaluation
- Decision Reliability
- Capability Spectrum
one_liner: SO-Arena 基准从能力谱和决策可靠性两个维度评估 System One 模型，发现性能强不等于决策可靠
practical_value: '- 在构建电商/推荐场景的 LLM 评测集时，借鉴 SO-Arena 的证据 grounding 思路：用可靠来源（如用户真实行为日志、人工审核的标注）并人工验证标签与模型输入的一致性，避免模糊标签导致评测失真；这对商品情感分类、意图识别等任务尤其重要。

  - 评估推荐/搜索中的 LLM 排序或 Agent 决策时，增加决策稳定性测试：固定任务语义，但改变选项顺序、增减干扰项或替换等价选项，观察模型输出是否一致；稳定性差说明模型易受上下文扰动，不适合直接上线。

  - 引入缺失答案识别任务作为可靠性指标：让模型在无合适推荐或信息不足时输出“无建议/拒绝回答”，避免强制生成错误推荐；用户对“没有结果”的容忍度通常高于错误推荐，可降低投诉率。

  - 采用分层难度评估代替单一平均分：按业务场景定义 easy/medium/hard（例如商品属性完整性、问题复杂度），定位 LLM 在哪些难度区间失效，为后续迭代、模型选型或
  system1/system2 路由提供依据。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：System One 模型（快速、自回归生成短序列或直接输出决策，无需长链条推理）在通用决策中受到关注，但现有评测基准大多只报告平均准确率，忽视了两个关键维度：能力谱的广度和决策可靠性。

**方法**：SO-Arena 基准覆盖 11 个领域和 5 个能力家族。能力谱方面，采用证据 grounding 的评测设计——通过可靠来源和人工验证确保标签与模型可见输入一致，避免标签歧义；提供基于领域特定难度标准的细粒度难度分层；设置沙盒环境中的迭代式交互评估；推理密集型任务用于 system one 与 system two 模型对比。可靠性方面，引入两个互补指标：决策稳定性（在受控的选项集变化下模型判断是否一致）和缺失答案识别（当没有有效选项时模型是否能正确拒绝回答）。

**结果**：在 21 个模型的评测中，模型规模和额外推理带来的收益在不同领域差异显著；更关键的是，整体性能最好的 System One 模型在可靠性排名上仅列第七，表明高准确率并不自动意味着可靠决策。
