---
title: 'DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation'
title_zh: DMAD：分布匹配即对抗蒸馏，用于快速视觉生成
authors:
- Zhengming Yu
- Junkun Yuan
- Haotian Yang
- Gordon Guocheng Qian
- Yizhi Wang
- Angtian Wang
- Yiding Yang
- Bo Liu
- Xin Li
- Wenping Wang
affiliations:
- Texas A&M University
- Intelligent Creation, ByteDance
arxiv_id: '2610.02188'
url: https://arxiv.org/abs/2610.02188
pdf_url: https://arxiv.org/pdf/2610.02188
published: '2026-10-01'
collected: '2026-10-04'
category: Training
direction: 扩散模型对抗蒸馏加速生成
tags:
- Diffusion Distillation
- Distribution Matching
- Adversarial Distillation
- Few-step Generation
- SDXL
- Video Generation
one_liner: 把分布匹配蒸馏重构为对抗式分类，免去辅助 score 模型并实现 1.04 FID 一步生成
practical_value: '- 工程上，若做商品图/视频/AIGC 的少步扩散蒸馏，可借鉴共享 backbone + 两个判别头的设计，避免维护不断更新的辅助
  score 模型，降低显存和计算，简化训练管线。

  - gap-based reweighting 根据真实样本与教师样本的判别 logit gap 动态调节蒸馏监督，这种自适应加权方式可迁移到推荐排序蒸馏、LLM
  生成质量判别蒸馏等场景，替代固定权重。

  - 对于生成式推荐中的 Semantic ID / 商品文案 / 营销物料生成，若希望用少步生成模型降低推理延迟，可尝试把分布匹配目标写成判别损失，并利用 real-teacher
  gap 调整监督；比单独训练交叉熵或 score 模型更省资源。

  - 论文证明的 logit→log-density ratio 恒等式是通用理论：已有判别器或 LLM reward model 时，用线性 logit 损失就能近似分布梯度，可尝试接入
  Agent 或多模态生成 Reward 模型做策略优化。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：DMD 需要维护一个不断拟合学生分布的辅助扩散模型，额外显存与计算成本高，且训练管线复杂。

方法：DMAD 将分布匹配重写为分类问题，在共享 backbone 上放两个判别头，分别区分真实样本和教师样本与学生样本；对 logits 使用线性损失训练学生，无需辅助 score 模型。理论上在判别器最优时，这些损失通过 logits 与 log-density ratio 恒等式恢复 DMD 的分布匹配梯度。还提出 gap-based reweighting：用真实样本与教师样本的 logit gap 自适应调节教师监督，提升不同噪声级别上的训练效率。

结果：ImageNet-64 一步生成 FID 1.04，SDXL 四步 COCO-10K FID 14.47，Wan2.1-T2V-14B 四步 VBench 总分 85.15，且超过对比少步方法和多步教师；MiniMax-H3 四步学生在 joint audio-video 人类偏好上超 DMD2 79.1%、超 rCM 84.6%。
