---
title: 'Weaken to Strengthen: Weakening-Induced On-Policy Self-Distillation for Large
  Reasoning Models'
title_zh: 弱化以强化：面向大型推理模型的弱化诱导在线策略自蒸馏
authors:
- Yecheng Wu
- Song Han
- Han Cai
affiliations:
- Massachusetts Institute of Technology
- NVIDIA
arxiv_id: '2610.38681'
url: https://arxiv.org/abs/2610.38681
pdf_url: https://arxiv.org/pdf/2610.38681
published: '2026-10-27'
collected: '2026-10-31'
category: Training
direction: LLM 推理模型自蒸馏训练
tags:
- Self-Distillation
- On-Policy
- Quantization
- Pruning
- Reasoning
- LLM
one_liner: 通过量化/剪枝构造弱化模型，利用强弱对比信号进行在线策略自蒸馏，无需外部教师
practical_value: '- 在没有更强教师或外部标注时，可对内部 LLM（商品推荐文案、Agent 规划、搜索 query 改写）做“弱化自蒸馏”：将线上模型做低比特量化或幅度剪枝得到弱版，用同批
  on-policy 轨迹的强弱概率差/输出对比做 token 级信号，无需人工标注或大模型 API。

  - 剪枝版弱模型比量化版提升更明显（+5.5 vs +4.0），在算力有限时优先 magnitude pruning 作为弱化教师；但剪枝需调稀疏度，注意训练稳定性。

  - 该方法可嵌入现有 post-training pipeline：用业务真实 unlabeled prompts 跑 on-policy rollout，收集模型自身错误中间步骤，再与弱化模型对比，重点修复推理链偏离，适合
  Agent 工具调用/多步推荐逻辑的 RL 后训练。

  - 需要验证弱化模型不能太弱，否则对比信号噪声大；建议按任务难度与模型规模调整量化位数/剪枝比例，先小规模消融。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：自蒸馏能提升推理模型，但常见做法依赖特权信息或更强教师；只有无标注 prompt 时受限。

方法：提出 WISD，构造原模型的弱化版本（低比特量化或幅度剪枝），对相同 prompt 进行 on-policy 采样，利用原模型与弱化模型在轨迹上的输出差异/概率对比作为训练信号，不引入外部教师。将原模型作为强策略，弱化模型作为弱参考，进行 token 级蒸馏/策略优化。

结果：在数学与代码推理基准上，量化/剪枝弱化模型平均准确率比原模型提升 4.0/5.5 个百分点；剪枝使 Qwen3.5-4B 在 HMMT 2025 从 57.7% 到 70.5%，LiveCodeBench v6 从 39.1% 到 56.7%；量化使 Qwen3.6-35B-A3B 同基准从 68.5%/61.8% 提升到 74.6%/69.5%。说明无需特权信息也能取得 SOTA 自蒸馏效果。
