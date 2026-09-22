---
title: 'iSDFT: Information-Proximal Self-Distillation for Continual Learning in LLMs'
title_zh: 信息近端自蒸馏用于LLM持续学习
authors:
- Ahmed Khaled Khamis
- Xiaotong Ji
- Hassan Jaber
- Rasul Tutunov
- Matthieu Zimmer
- Jun Wang
- Haitham Bou-Ammar
affiliations:
- Georgia Institute of Technology
- Imperial College London
- Politecnico di Torino
- UCL Centre for AI
arxiv_id: '2609.24646'
url: https://arxiv.org/abs/2609.24646
pdf_url: https://arxiv.org/pdf/2609.24646
published: '2026-09-21'
collected: '2026-09-22'
category: Training
direction: LLM 持续学习 · 信息约束自蒸馏
tags:
- Continual Learning
- Self-Distillation
- Knowledge Distillation
- Catastrophic Forgetting
- LLM Fine-tuning
one_liner: 提出iSDFT将教师视为预算信息源，在每步选择满足信息约束的最近分布，提升LLM持续学习中稳定性与可塑性的平衡
practical_value: '- 在电商/推荐场景中，当用新数据微调LLM（如用于query理解、内容生成、推荐理由）时，可采用iSDFT的“信息预算”思想：对每个token动态决定从教师（新任务模型）吸收多少信息，避免新策略完全覆盖旧能力，尤其适合需要持续更新但必须维持基线性能的线上系统。

  - 锚定冻结基础模型（frozen base policy）的做法可作为一个轻量正则化项加入现有微调损失，实现简单且可稳定训练，有助于在迭代推荐模型时控制累积漂移，减少对旧用户行为模式的遗忘。

  - 闭合形式的指数目标（exponential tilting）无需额外优化循环，工程实现成本低，可直接用于LLM4Rec的在线学习或定期更新，平衡稳定性和塑性。

  - 该方法对多任务、多模态的推荐系统持续学习有借鉴意义：可以按任务重要度设置不同的教师信息约束，实现可控的旧知识保留和新知识注入。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 持续学习面临稳定性-可塑性困境，SDFT 虽然能减轻遗忘但固定向完整演示条件教师蒸馏，缺乏对教师信息传递量的控制。

**方法关键点**：iSDFT 将教师视为预算信息源，在每个 token 选择距离当前学生最近且满足预设教师信息约束的分布，得到闭合形式指数目标（局部倾斜）；同时将学生锚定到冻结基础策略控制累积漂移。

**关键结果数字**：在 4 个 LLM 骨干和 2 个专业化任务上，7/8 设置优于 vanilla SDFT，1 项持平；在原始 SDFT 基准上，73% 评估保持在 base model 0.5 分内（最强基线 52%），并在 10 个数学/编码/竞赛数学基准上取得最大平均改进。
