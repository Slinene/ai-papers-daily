---
title: Policy Improvement-Guided Replay for Continual Reinforcement Learning
title_zh: 策略改进引导的持续强化学习重放
authors:
- Qin-Wen Luo
- Haoxuan Gao
- Sheng Ren
- Xiang Chen
- Sheng-Jun Huang
affiliations:
- Nanjing University of Aeronautics and Astronautics
arxiv_id: '2611.25989'
url: https://arxiv.org/abs/2611.25989
pdf_url: https://arxiv.org/pdf/2611.25989
published: '2026-11-19'
collected: '2026-11-22'
category: Training
direction: 持续强化学习 · 重放样本选择
tags:
- Continual RL
- Replay Selection
- KL Regularization
- Vision-Language Models
- Policy Improvement
- CoLiR
one_liner: 提出 CoLiR，用正确/错误响应似然对比选择历史 prompt 重放，提升 VLM 持续 RL 的旧任务保留
practical_value: '- 在电商/Agent 场景做多任务持续策略更新（如多个 agent 能力、不同品类推荐策略）时，可借鉴 CoLiR 的 replay
  选样：选择当前策略对其正确输出置信度提升大、错误输出置信度下降大的历史样本，比均匀随机重放更高效保留历史性能。

  - 工程实现上，CoLiR 只复用训练过程中缓存的 log-likelihood，并在任务边界做一次跨策略打分，不增加额外生成；适合在线或离线持续训练 pipeline
  中低开销构造重放池。

  - 将 KL 正则化限制在重放样本上，既约束旧任务分布漂移，又减轻对全量新任务数据学习的限制；在多轮微调/RLHF 时，可以对历史关键 prompt 做局部 KL，而非全局
  KL，降低优化冲突。

  - 若业务有多个任务顺序上线，可在阶段 checkpoint 对历史评测集筛选优势样本，建立长期 replay memory，用于后续每次更新，缓解灾难性遗忘。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：持续 RL 需要 VLM 增量获取新能力同时防止旧任务性能衰退。传统持续学习看重稳定性，本文转向策略改进视角，用 performance difference lemma 说明历史性能变化由当前策略在历史任务上的期望 advantage 决定，因此应重放当前策略下 advantage 明显的 prompt。

方法关键点：提出 Contrastive Likelihood Replay (CoLiR)。在任务边界，为每个 prompt 计算分数：对比正确响应在最终任务策略下的似然增益与错误响应在初始策略下的似然下降，即正负似然差。该分数可关联 KL 正则化最优更新下的 reference-policy advantage。从有限 rollouts 和缓存的 log-likelihood 估计分数，选择最高分 prompt 进入 replay memory；后续训练均匀重放，并将 KL 正则化仅施加于重放 prompt。Memory 构建只需少量跨策略打分，无需额外响应生成。

关键结果：在 MRCL 三个 Qwen3-VL 模型规模上，CoLiR 取得最高平均最终准确率与平均任务准确率（final average 69.35 vs FullSFT 46.26，stage average 70.86 vs 57.14），且新任务表现保持竞争力。
