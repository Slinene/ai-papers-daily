---
title: Counterfactual Auditing of Bias in Open-Source Large Language Models for Clinical
  Triage
title_zh: 开源大语言模型临床分诊偏差的反事实审计
authors:
- Manar Aljohani
- Brandon Ho
- Kenneth McKinley
- Dennis Ren
- Xuan Wang
affiliations:
- Virginia Tech
- University of Washington and Seattle Children's Hospital
- Children's National Hospital
arxiv_id: '2610.01963'
url: https://arxiv.org/abs/2610.01963
pdf_url: https://arxiv.org/pdf/2610.01963
published: '2026-10-01'
collected: '2026-10-04'
category: Eval
direction: LLM 反事实公平性审计
tags:
- Counterfactual Auditing
- Bias
- Clinical Triage
- LLM
- Fairness
- QLoRA
one_liner: 反事实审计10个开源LLM的临床分诊偏差，发现敏感性与模型规模/医疗预训练非单调，QLoRA微调版本最低
practical_value: '- 在生成式推荐/Agent 决策中，可复用成对反事实审计：仅改变用户画像中的性别、会员等级、设备、地区或商品价格带等单一敏感属性，固定其他上下文，统计输出列表/排序变化，低成本发现模型对敏感特征的依赖。

  - 不要只看 aggregate shift 率：要按敏感属性分组，分别观察方向性（类似 overtriage/undertriage），例如是否系统性打压某类用户或过度曝光某类商品，否则聚合指标会掩盖局部严重偏差。

  - QLoRA 微调可能降低总体敏感性，但不一定消除方向性偏差甚至引入新偏差；微调后必须重新跑反事实评估和分层分析，不能只测总体准确率。

  - 选 LLM 做排序/决策支持时，更大模型或领域预训练不自动更公平；建议对候选模型统一跑反事实测试集，结合真实与合成样本，作为选型和上线前评估的一部分。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：急诊分诊是高风险优先排序任务，人口统计、社会经济和系统上下文信息可能不当影响 acuity 判定；开源 LLM 被越来越多地考虑用于本地隐私保护的临床决策支持，但跨模型反事实偏差情况不明。

**方法**：从真实和手册风格临床 vignette 出发，构造成对反事实变体：仅改变一个注入的人口、社会经济、医疗获取、行为、社会或系统上下文变量，保持临床呈现不变。在 10 个开源 LLM 上测试：Qwen2.5-7B、Qwen2.5-14B-Instruct、QLoRA 微调 Qwen2.5-7B、MedGemma 系列、MedLLaMA2-7B、GPT-OSS-20B、GPT-OSS-120B。测量 any shift、undertriage、overtriage、>1 ESI 级别 shift、mean shift 和 mean absolute shift。

**结果**：反事实敏感性差异很大，且不随模型规模或医疗领域预训练一致降低。QLoRA 微调 Qwen2.5-7B 总体敏感性最低：any-shift 率 5.27%，mean absolute shift 0.0534；对应 base 模型为 16.02% 和 0.1706。若干更大或医疗领域模型产生更高的显著 shift 率。分层和相关分析进一步揭示：聚合 shift 率会掩盖具有临床意义的方向性和共同失败模式。结论：反事实审计可作为轻量、可解释的框架，在部署开源 LLM 前比较其公平性风险。
