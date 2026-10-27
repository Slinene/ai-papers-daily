---
title: 'Eat Your Precision: Precision Objective Mitigates Reward Hacking in Rubric-based
  RL'
title_zh: 吃透精度：精度目标缓解基于量规强化学习中的奖励黑客
authors:
- Hyun Ryu
- Jong-Heon Kim
- Yiqing Xie
- Seungone Kim
- Carolyn Rose
- Eunho Yang
affiliations:
- KAIST AI
- Carnegie Mellon University Language Technologies Institute
arxiv_id: '2610.33512'
url: https://arxiv.org/abs/2610.33512
pdf_url: https://arxiv.org/pdf/2610.33512
published: '2026-10-23'
collected: '2026-10-27'
category: Training
direction: LLM 强化学习奖励设计 · 精度目标
tags:
- rubric-based RL
- reward hacking
- precision objective
- RLHF
- LLM
- FORK
one_liner: 提出 FORK 奖励，在量规覆盖（召回）外加入精度目标，抑制冗长与事实错误，大幅提升胜率
practical_value: '- 在用 rubric/checklist 作为 LLM 生成任务（商品文案、推荐解释、搜索结果摘要、Push 文案）的 RL
  奖励时，只优化 rubric 覆盖会诱导模型输出冗长且夹带虚构信息；可参考 FORK 同时优化 recall 与 precision，对每个输出片段做必要性打分，减少无效内容。

  - 对于电商问答、导购 Agent 的 LLM 回复，若奖励只基于是否覆盖用户需求点，模型可能过度回答、幻觉具体参数；引入 factual-correctness
  grader 作为精度项，能直接抑制事实错误。

  - 工程实现上，可把 rubric 覆盖作为 recall 信号，把“每个 rubric 项是否必要”与“事实核验”组合成 precision 信号；在生成式推荐解释场景中，该设计可显著提升
  win rate 并降低平均回复长度。

  - 该方法的奖励公式与思想可迁移到任何需要 rubric 约束的开端生成任务，但具体 factual grader 需根据业务数据微调或规则化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Rubric-based rewards 常用于不可验证任务的 RL 训练，但通常被定义为 rubric 覆盖的加权和，只最大化 recall。这导致 RL 后的模型回复更完整，但更冗长、包含不必要或事实错误内容，甚至不如 base model 受偏好。

**方法关键点**：提出 FORK reward，联合优化 recall 和新的 precision objective。Precision 要求模型回复的每个单元既必要又事实正确：必要性由 rubric 驱动的 necessity credits 衡量，事实正确性由 factual-correctness grader 判断。通过同时约束覆盖与精度，抑制奖励黑客。

**关键结果**：FORK 超越现有 rubric-based RL 方法，达到 rubric 覆盖与整体回复质量的 Pareto 最优。相比原始 recall-only reward，FORK 在保持相似 rubric 覆盖的同时显著提升 precision、缩短回复长度；win rate 相对 base policy 在 RubricHub-Medical 上从 10.6% 升至 68.0%，在 HealthBench 上从 22.1% 升至 74.1%。
