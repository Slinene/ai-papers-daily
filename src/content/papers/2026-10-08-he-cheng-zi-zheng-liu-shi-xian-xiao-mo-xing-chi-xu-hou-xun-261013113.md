---
title: Continually Post-training Small Models via Synthetic Self-distillation
title_zh: 合成自蒸馏实现小模型持续后训练
authors:
- Woosung Koh
- Hyunsoo Lee
- Kyungjae Lee
- Haeju Park
- Dahyun Lee
- Dasol Hwang
- Moontae Lee
affiliations:
- KAIST AI
- LG AI Research
arxiv_id: '2610.13113'
url: https://arxiv.org/abs/2610.13113
pdf_url: https://arxiv.org/pdf/2610.13113
published: '2026-10-08'
collected: '2026-10-12'
category: Training
direction: 持续后训练 · 合成自蒸馏
tags:
- Continual Learning
- Self-Distillation
- Small LMs
- Post-training
- Distribution Shift
- Rejection Sampling
one_liner: 提出合成自蒸馏，通过稍大同家族模型生成in-distribution监督，解决小模型持续后训练中获取与遗忘问题
practical_value: '- 在电商/搜索场景持续更新轻量级 query 理解或 on-device 模型时，可借鉴「同家族稍大模型生成 in-distribution
  伪标签」的蒸馏方式，避免直接使用真实用户反馈造成分布偏移和旧知识遗忘。

  - 使用 rejection sampling 过滤低质量合成样本，能提升伪标签可靠性，适合电商/搜索中大量噪声标签或弱监督数据的场景。

  - 持续学习前先量化模型输出分布偏移，发现偏移过大时强制启用 in-distribution 重写或防遗忘策略，可部署为在线监控指标。

  - 低延迟场景（如移动端推荐特征提取、query 改写）可线下用稍大模型生成高质量训练数据，线上仅部署小模型，兼顾效果与推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：持续后训练同时面临获取新能力和保留旧知识双重挑战。现有自蒸馏微调（SDFT）依赖强上下文学习和指令跟随能力，在小模型上失效，而小模型对低延迟、端侧场景至关重要。作者首先定位失败根因：发现获取能力差和遗忘程度与后训练模型的分布偏移呈线性相关，说明必须进行 in-distribution 学习。

**方法关键点**：提出合成自蒸馏（SynthSelf），将 in-distribution 改写任务外包给一个稍大的同家族校准模型（aligner），由其生成符合小模型原始分布的高质量监督信号。同时引入 off-policy 监督和拒绝采样，确保合成数据不仅质量高，还能保持原分布，从而解决小模型持续学习中的分布偏移问题。

**关键结果**：在 4 个获取数据集（含混合任务）和 14 个保留基准上，SynthSelf 在 3 种小模型规模下一致超越 6 种基线方法（含离线和在线蒸馏）。进一步分析证实，该方法能有效缓解灾难性遗忘，为小模型持续学习铺平道路。
