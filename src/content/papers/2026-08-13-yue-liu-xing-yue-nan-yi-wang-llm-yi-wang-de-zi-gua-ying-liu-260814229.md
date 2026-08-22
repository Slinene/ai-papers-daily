---
title: 'The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning'
title_zh: 越流行越难遗忘：LLM 遗忘的自适应流行度策略
authors:
- Anna Borisiuk
- Andrey Savchenko
- Alexander Panchenko
- Elena Tutubalina
affiliations:
- AIRI
- Sber AI Lab
- Skoltech
- ISP RAS Research Center for Trusted Artificial Intelligence
arxiv_id: '2608.14229'
url: https://arxiv.org/abs/2608.14229
pdf_url: https://arxiv.org/pdf/2608.14229
published: '2026-08-13'
collected: '2026-08-22'
category: Training
direction: LLM 遗忘训练 · 流行度自适应
tags:
- LLM Unlearning
- Popularity Bias
- Adaptive Regularization
- Forget-Retain Trade-off
- Dual Ascent
one_liner: AdaPop 按事实流行度自适应调整遗忘梯度，并用双上升控制器自动平衡遗忘/保留，显著降低遗忘内容泄露
practical_value: '- **把「流行度」引入遗忘/更新训练**：电商场景中需要让 LLM 遗忘下架商品、过期活动或用户隐私数据时，不要对所有遗忘样本用统一梯度。可以用商品销量、点击量、评论数、搜索热度等作为流行度代理，让热门实体获得更强的遗忘压力，冷门实体减小遗忘力度，避免过度擦除长尾信息。

  - **用外部代理估算知识流行度**：如果内部训练数据频率不可得，可以借鉴 AdaPop 使用 Wikidata sitelinks 或 LLM-as-Judge
  的思路，在业务中用知识图谱连接数、商品关联关系数、LLM 对事实重要性的打分作为替代，计算 per-example 的 exponent，指导梯度缩放。

  - **自动调节 retain penalty 的 dual-ascent 控制器**：线上持续学习或定期遗忘时，手动设置遗忘/保留损失权重很脆弱。可参考每 epoch
  根据保留集表现自动调整保留惩罚，减少对超参搜索的依赖，在删除目标知识的同时维持推荐/问答质量。

  - **用隐藏状态距离做内部监控**：除了最终行为指标，可以跟踪遗忘集和保留集的隐藏状态相对未更新模型的距离，作为遗忘充分性与保留完整性的 early signal，便于训练中及早发现遗忘不足或过度遗忘。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：预训练中流行事实被记忆得更深，遗忘时更难移除。但现有 LLM unlearning 方法对所有遗忘样本施加相同梯度，导致「流行度差距」：罕见事实被过度擦除、损害保留能力，流行事实却擦除不足，在改写或对抗 query 下仍可被召回。

**方法关键点**：AdaPop 为每个遗忘事实计算局部 token 置信度，并与来自外部代理（如 Wikidata sitelinks、LLM-as-Judge）的流行度相关 exponent 结合，用于缩放遗忘梯度，使热门事实获得更强更新。同时采用 dual-ascent 控制器，每 epoch 根据保留集表现自动调节 retain penalty，平衡遗忘与保留目标。内部评估引入隐藏状态距离：衡量 forget-set 与 retain-set 表示相对未遗忘前模型的变化。

**关键结果**：在 3 个模型家族、2 个基准上，AdaPop 在改写 query 下泄露的遗忘内容比竞争方法少约 5 倍，在对抗性改写下少约 1.6 倍。隐藏状态分析显示 forget-set 表示离未遗忘前模型更远，而 retain-set 表示保持接近，说明遗忘更彻底且保留能力受损更小。
