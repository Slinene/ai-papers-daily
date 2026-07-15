---
title: Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving
  LLM Agents
title_zh: 谁给评分者评分？自进化智能体评估指标与技能协同演化
authors:
- Xing Zhang
- Guanghui Wang
- Yanwei Cui
- Ziyuan Li
- Wei Qiu
- Bing Zhu
- Peiyang He
arxiv_id: '2607.12790'
url: https://arxiv.org/abs/2607.12790
pdf_url: https://arxiv.org/pdf/2607.12790
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: Agent自我改进中的评估指标进化
tags:
- self-improving agents
- metric co-evolution
- LLM agents
- evaluation
- evolutionary lifecycle
- anchor discipline
one_liner: 在没有可靠评估指标时，让评估指标与Agent技能协同进化，保持自我改进效能
practical_value: '- 在无可靠在线指标的场景（如生成式推荐文案、广告创意评估）中，可借鉴利用小规模锚定参考集+未标注输出共识正则化，构建可进化的透明评估指标，避免依赖不可信的自动化评判。

  - 将评估指标进化与技能生命周期管理协同的Double Ratchet框架，可直接用于对话Agent、搜索Query生成等自我改进系统，使系统在缺乏人工标注时仍能持续提升。

  - 引入anchor discipline（锚定纪律）和外部审计机制，防止指标退化或技能钻漏洞，对电商Agent安全至关重要，尤其当系统输出直接影响用户体验或收入时。

  - 在推荐理由生成、商品描述自动优化等任务中，可先用少量人工标注训练初始指标，然后通过协同进化让模型自适应新数据分布，减少人工持续标注成本。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：自我进化的LLM Agent系统通过创建、修订和淘汰技能来迭代，但这一切隐含一个前提——存在可靠的评估指标。在很多真实应用中，这个前提不成立。**方法**：提出两条核心主张：1）指标本身可以进化，通过搜索组合小型缺陷检测器，经历完整的进化生命周期，用十项锚定参考集训练，并在无标注输出上通过共识正则化，产出透明、可检验的指标；2）由于没有现成指标可比较，衡量标准是恢复一个准确指标所能带来的提升，因此提出Double Ratchet框架，将指标进化与技能的生命周期管理协同进行。**结果**：在代码生成（MBPP+）、企业Text-to-SQL（Spider 2.0-Snow）和无参考报告生成任务上，协同进化使技能提升达到使用真实标准或最佳已有评分标准所获提升的88-110%。安全性方面，移除锚定守卫会令指标退化为空白检测器；当进化技能钻报告评估指标的空子时，独立裁判能发现，由检测器修复后，任务感知法官在77%的决胜对中偏好进化后的输出。**结论**：在没有可靠自动验证器的场景，这种容错预期架构应是默认选择。
