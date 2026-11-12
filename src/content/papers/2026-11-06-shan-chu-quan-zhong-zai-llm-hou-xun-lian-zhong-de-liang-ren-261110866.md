---
title: The Surprising Effectiveness of Deleting Weights in LLM Post-Training
title_zh: 删除权重在 LLM 后训练中的惊人有效性
authors:
- Jack Lu
- Zhenbang Yang
- Mike Lasby
- Tejas Pote
- Yani Ioannou
- Mengye Ren
affiliations:
- New York University
- University of Calgary
arxiv_id: '2611.10866'
url: https://arxiv.org/abs/2611.10866
pdf_url: https://arxiv.org/pdf/2611.10866
published: '2026-11-06'
collected: '2026-11-12'
category: Training
direction: LLM 后训练 · 权重删除掩码
tags:
- Deletion Tuning
- LLM Post-Training
- Masking
- Continual Learning
- RLVR
- SFT
one_liner: Deletion Tuning 仅置零少于0.05%的权重即可在RLVR、SFT和蒸馏中匹配全量微调，且遗忘显著更少
practical_value: '- 线上 LLM 策略/文案模型（搜索改写、推荐文案、Agent 工具调用）做持续更新时，可用 Deletion Tuning
  替代全量微调或 LoRA：只保存 binary mask，体积比 FFT checkpoint 小数百到数千倍，部署时只需 mask 掉部分权重，无需额外参数，显著降低存储与传输成本。

  - 多场景顺序微调场景（先做 query 改写，再做文案生成，再做工具调用）可直接受益：该方法在 RLVR 下几乎不遗忘旧任务，而 FFT/LoRA/随机稀疏微调最多掉
  5.4 分，适合多任务/多场景 LLM 的持续训练。

  - 实现 trick：只在 transformer block 的 gate projection 上学习 binary mask，其他层冻结，改动小、易集成到现有训练框架；业务中可优先尝试对
  gate projection 做删除掩码，而不去调整 value。

  - 几何分析表明“删除哪些权重”比“学习新值”更重要，且 Deletion Tuning 最接近 FFT 的权重变化；这提示在做稀疏微调时，优先识别并保留关键权重、删除冗余权重，可能比学习低秩更新更有效。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM post-training 中能否只通过删除少量权重获得新能力？之前的工作显示微调解离预训练模型很近，但未走到极致。

**方法**：Deletion Tuning 只学习一个二进制掩码，作用于 transformer block 的 gate projection，将少于 0.05% 的权重置零，不修改其他任何权重。训练时通过掩码选择保留哪些预训练权重，删除其余权重。

**关键结果**：在 RLVR、SFT、on-policy distillation 三种后训练范式下，Deletion Tuning 匹配全量微调（FFT）的效果。训练的掩码比 FFT checkpoint 小数百到数千倍。在 RLVR 下，先前任务准确率保持在 base 附近，而 FFT、LoRA、随机稀疏微调最多下降 5.4 分。通过 stable rank、spectrum drift、principal-weight overlap 三个几何指标分析，Deletion Tuning 的权重变化最接近 FFT，优于 LoRA 和随机稀疏微调。
