---
title: Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation
title_zh: 弱到强泛化的 On-Policy 反向蒸馏方法
authors:
- Youngrok Park
- Sangmin Bae
- Hojung Jung
- Jongwoo Ko
- Yunseon Choi
- Young Jin Kim
- Pashmina Cameron
- Aaron Courville
- Se-Young Yun
affiliations:
- KAIST AI
- Microsoft
- University of Toronto
- Mila
- Université de Montréal
arxiv_id: '2609.08798'
url: https://arxiv.org/abs/2609.08798
pdf_url: https://arxiv.org/pdf/2609.08798
published: '2026-09-07'
collected: '2026-09-09'
category: Training
direction: 弱到强泛化蒸馏训练方法
tags:
- weak-to-strong generalization
- knowledge distillation
- policy optimization
- reinforcement learning
- LLM post-training
one_liner: 用 On-Policy Reverse Distillation 放大教师策略偏移分量，实现弱到强泛化且不施加教师容量上限
practical_value: '- **模型迭代中利用旧模型知识**：电商推荐/搜索排序模型升级（如从精排小模型到 LLM-based ranker）时，旧模型可作为弱教师，用
  OPRD 思路在 on-policy rollouts 上计算教师策略偏移，加速新模型训练且避免继承旧模型容量上限，减少全量 RL 成本。

  - **多域/多业务模型融合**：广告、推荐、搜索多场景有各自模型，可作为多教师进行蒸馏，OPRD 的多教师扩展可能比直接加权蒸馏更高效；结合 verifier（如业务指标奖励模型）过滤教师更新方向，只放大与
  verifier 一致的教师指导，防止负迁移。

  - **Agent 策略训练**：在 LLM Agent 或生成式推荐策略优化中，实施 on-policy 蒸馏：用学生自我生成 rollout 评估教师策略位移，仅对
  verifier 支持的方向放大梯度，保持策略优化不动点，可避免教师过度约束导致模式坍缩。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：weak-to-strong generalization 希望强模型从弱监督中学习并超越弱教师，但传统蒸馏将弱教师作为优化目标，可能将学生的容量上限限制在教师水平。

**方法关键点**：提出 On-Policy Reverse Distillation (OPRD)。在 student self-rollout 上评估教师策略相对于其 reference policy 的位移（policy shift），并将该方向上的学生 verifier-driven policy gradient 分量放大。只 rescale 被 verifier 支持的更新，保留 policy optimization 的 stationary points，因此教师指导加速而非重定向学生自身优化。

**关键结果**：在 successive model transfer（4B 模型做教师，8B 模型做学生）和多教师蒸馏两个关键场景中，OPRD 相比 GRPO、OPD、Mix-RL、MOPD 等基线，在数学（AIME'24/25、HMMT'25、OlympiadBench）和推理（Knights & Knaves、Quantum Lock、String Manipulation、Countdown）任务上达到更高性能且所需学生更新步数更少。Response-style 分析显示 OPRD 学生更接近纯 verifier-based RL 训练模型而非弱教师，表明教师指导加速而非重定向学生优化。此外，在传统 strong-to-weak 蒸馏中 OPRD 同样有效，说明该方法不受容量顺序限制。
