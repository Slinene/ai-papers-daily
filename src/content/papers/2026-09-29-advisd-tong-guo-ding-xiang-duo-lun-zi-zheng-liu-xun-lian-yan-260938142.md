---
title: 'AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation'
title_zh: AdviSD：通过定向多轮自蒸馏训练前沿 LLM 的顾问模型
authors:
- Rishabh Agrawal
- Hejie Cui
- Shasha Li
- Shanchan Wu
- Sercan Ö. Arık
affiliations:
- Google
- University of Southern California
arxiv_id: '2609.38142'
url: https://arxiv.org/abs/2609.38142
pdf_url: https://arxiv.org/pdf/2609.38142
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: 小型 advisor 训练 · 定向自蒸馏 + GRPO
tags:
- Advisor Model
- Self-Distillation
- RL
- Multi-turn Agent
- Frozen LLM
one_liner: 用配对评分筛选哪些反思修正值得监督，训练小型 advisor 通过自然语言建议提升冻结 Gemini/Claude 的工具调用与多轮 agent
  表现
practical_value: '- 对调用黑盒 LLM API 的电商/Agent 场景，可以用小模型做外部 advisor，不必微调 frontier 模型；AdviSD
  的配对评分过滤不依赖 executor logits 或额外 rollout，工程成本低。

  - 训练时把“修正生成”和“选择哪些修正用于监督”解耦：用 pre-update advisor 对同一 executor 回复计算 with/without
  advice 的平均 log-prob 差，只保留差值超过阈值的决策；不要学所有反思修正，尤其避免学对 executor 行为无影响的“正确但无用”建议。

  - 对原始 abstention 决策要单独 bypass：因为无 advice 时 with/without 上下文相同、score 差为 0，容易被过滤掉；保留被
  reflection 标记的 missed advice 可提升 0.6–1.7 点。

  - 做消融时加 matched-count random control，能区分“少学一点”和“选得对”；阈值可以用 donor advice（其他任务 advice）在
  pilot 上校准并固定。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
Frontier LLM 通常只通过 API 使用，无法改权重。可以让一个小模型 advisor 在每轮 executor 回复前给自然语言建议或 abstain，并用任务 reward 做 RL。但交互反馈中的修正可能“合理却不改变 executor 行为”；在共享参数 advisor 里学习这些 insensitive corrections 会稀释对有用建议的偏好，甚至损害最终效果。因此需要选择“哪些修正值得学”。

**方法关键点**  
- AdviSD = GRPO + 定向自蒸馏。Reflection 在 imperfect episode 中最多 flag 5 个 advice 决策。
- 用 pre-update advisor 对同一条已记录 executor response 分别在有/无 issued advice 的上下文下打分，计算平均 token log-prob 差 c_k；保留 |c_k| > ε_c 的 issued-advice 决策，以及所有被 flag 的原始 abstention。
- ε_c 由 pilot 阶段 donor advice（来自其他任务的 advice）的 contrast 绝对值在 0.95 分位标定，训练中固定。
- 被保留决策上，feedback-conditioned 的 pre-update advisor copy 作为 teacher，学生只看原始 context；在 top-K support 上做 KL，损失平均到 decision/episode，与 GRPO 相加。GRPO 仍使用全部 episode。
- 理论：在共享参数简化模型中，insensitive failure 的 teacher 偏好弱于 sensitive teacher；减少其保留比例能提高最终 equilibrium。需要 matched-count random control 区分“选择”和“少监督”。

**关键结果**  
- Qwen3-8B advisor 服务 Gemini 3.7 Flash / Claude Sonnet 4.6，在 BFCL-v3 四个类别和 EnvScaler 上评估。
- 比 advisor-GRPO 高 4.2–6.4 pp（BFCL-v3）和 3.9–5.1 分（EnvScaler）。
- 比 matched-count random selection 高 2.5–4.9 分；inverted gate 低于 GRPO；去掉 abstention bypass 下降 0.6–1.7 分。
- OOD 四个 benchmark macro average 高出 standalone execution 2.7–3.6 点；跨 executor 版本/家族迁移比 GRPO 高 3.1 pp。
- 训练第 20 个 update 起持续领先 GRPO。

**最值得记住的一句话**：当 advisor 的建议必须通过冻结 executor 生效时，不是所有“合理的反思修正”都值得学；用 with/without advice 的预测差选择监督，比随机减少监督更能学到对 execution 有用的建议。
