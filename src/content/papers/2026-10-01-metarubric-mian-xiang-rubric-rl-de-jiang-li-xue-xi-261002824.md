---
title: 'MetaRubric: Learning to Reward for Rubric-Based Reinforcement Learning'
title_zh: MetaRubric：面向 Rubric RL 的奖励学习
authors:
- Yuxuan Fan
- Jaehong Yoon
affiliations:
- NTU Singapore
arxiv_id: '2610.02824'
url: https://arxiv.org/abs/2610.02824
pdf_url: https://arxiv.org/pdf/2610.02824
published: '2026-10-01'
collected: '2026-10-05'
category: Training
direction: LLM RL · 奖励学习与 Rubric 自适应
tags:
- Rubric-based RL
- Vacuous Credit
- Evidence-aware Reward
- GRPO
- Counterfactual
- PubMedQA
one_liner: 提出 MetaRubric，交替证据感知策略优化与响应引导的 Rubric 自适应，解决 Rubric RL 的虚假信用问题，在医学 QA 上超越静态
  GRPO
practical_value: '- 在用 LLM-as-judge 对生成内容（推荐理由、广告文案、Agent 回复）按 rubric 打分时，注意“虚假信用”风险：模型可能未包含要求的实体、动作或信息却获得高分。可增加证据感知的检查层：匹配响应中是否出现支撑某
  criterion 的关键短语/实体/工具调用，否则该 criterion 记零分或低权重。

  - 构建反事实 prompt 校准 rubric：电商场景可修改商品关键属性（价格、库存、适用人群）生成反事实问题，让 rubric 对上下文事实敏感，避免通用
  rubric 给出与事实不符的高分。

  - 采用“策略优化 ↔ rubric 自适应”交替训练：定期用线上 badcase 或当前策略响应更新评估 prompt 和 rubric 的 criterion
  权重，形成闭环，提升后续 RL 训练的奖励质量。

  - 证据感知的奖励塑形可减少 reward hacking：仅当生成内容包含支撑证据时才给予 partial credit，能降低模型用套话或格式正确但信息缺失的响应骗取高分的概率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Rubric-based RL 通过分项标准给予开放式任务 partial credit，但 rubric judge 可能对响应中缺失的信息或动作仍给出高分，作者称之为 Vacuous Credit。这种现象在去掉所需信息后仍存在，甚至会反转 GRPO advantage 的符号，导致策略偏向不满足要求的回答。

**方法**：MetaRubric 交替进行证据感知策略优化与响应引导的 rubric 自适应。首先为每个 prompt 修改一个任务相关事实构建 counterfactual 版本；策略优化时，仅当响应包含足够证据满足 rubric criterion 时才给分；每个策略优化阶段后，基于当前策略响应修订原始与反事实 criteria，同时保持原始 prompt 初始 rubric 在各自事实下的语义；并在阶段边界根据策略错误调整 criterion 权重。

**结果**：在多个 backbone 上，相较 static-judge GRPO，MetaRubric 将 PubMedQA 准确率提升 6.00–20.40 个百分点，并在 HealthBench-Hard 与两个多模态医学基准上取得进一步增益。
