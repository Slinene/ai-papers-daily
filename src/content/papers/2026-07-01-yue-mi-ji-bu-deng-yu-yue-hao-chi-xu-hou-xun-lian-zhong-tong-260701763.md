---
title: 'Denser neq Better: Limits of On-Policy Self-Distillation for Continual Post-Training'
title_zh: 越密集不等于越好：持续后训练中同策略自蒸馏的局限性
authors:
- Meng Wang
- Haohan Zhao
- Wenzhuo Liu
- Lu Yang
- Geng Liu
- Haiyang Guo
- Guo-Sen Xie
- Gaofeng Meng
- Hongbin Liu
- Fei Zhu
affiliations:
- Centre for Artificial Intelligence and Robotics, HKISI, CAS
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Nanjing University of Science and Technology
arxiv_id: '2607.01763'
url: https://arxiv.org/abs/2607.01763
pdf_url: https://arxiv.org/pdf/2607.01763
published: '2026-07-01'
collected: '2026-07-03'
category: Training
direction: 持续学习 · 自蒸馏 vs RL 优化
tags:
- Continual Learning
- Self-Distillation
- GRPO
- Catastrophic Forgetting
- On-Policy
- LLM Post-Training
one_liner: 同策略自蒸馏在持续后训练中会加剧遗忘甚至崩溃，而GRPO等保守RL方法更稳健
practical_value: '- **持续更新模型时避免密集自蒸馏**：在电商搜索推荐场景，如果用LLM持续学习新品类或新意图，采用SDPO等密集自蒸馏会显著遗忘旧知识，应改用GRPO等更保守的on-policy
  RL方法。

  - **监控参数与响应漂移**：自蒸馏会导致更大的参数空间和输出分布漂移，可设置漂移阈值，一旦检测到骤变即回滚或降低学习率。

  - **警惕格式退化**：自蒸馏的token级监督会通过自我强化循环放大高频格式伪影（如固定模板、重复短语），在生成推荐理由或广告文案时易导致风格单一化，可引入多样性约束或温度调节。

  - **同策略数据非万能**：不要以为只用当前策略生成的数据就能稳定持续学习，需要结合重放缓冲或正则化手段保持旧任务能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
持续后训练要求模型获取新能力而不遗忘旧知识。近期工作认为同策略（on-policy）学习可缓解遗忘，其中同策略自蒸馏尤为亮眼。本文通过设计自蒸馏策略优化（SDPO）实验，重新检验这一乐观结论。  
**方法关键点**  
对比SDPO与GRPO（一种同策略强化学习方法）在持续后训练中的表现：SDPO使用当前策略生成的样本进行蒸馏，教师为冻结的原模型或旧策略；GRPO则基于奖励信号优化策略。实验覆盖领域内微调与多任务持续训练场景，并从参数漂移、响应分布变化、格式伪影等角度分析。  
**关键结果**  
- SDPO在教师目标稳定时能加速领域内专业化，但分布外泛化差。  
- 持续后训练中，SDPO遗忘更严重，甚至出现崩溃；GRPO适应更保守，旧能力保留显著更好。  
- 密集自蒸馏导致更大的参数空间漂移和响应偏移，并通过师生循环放大高频格式伪影（如重复短语、模板化输出）。  
结论：同策略数据本身不足以持续学习；密集自蒸馏不应作为默认稳定器。
