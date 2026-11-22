---
title: Posterior Matching Distillation
title_zh: 后验匹配蒸馏
authors:
- Hidir Yesiltepe
- Julius Berner
- Arash Vahdat
- Pinar Yanardag
affiliations:
- Virginia Tech
- NVIDIA
arxiv_id: '2611.26629'
url: https://arxiv.org/abs/2611.26629
pdf_url: https://arxiv.org/pdf/2611.26629
published: '2026-11-18'
collected: '2026-11-22'
category: Training
direction: 扩散模型蒸馏 · 后验匹配
tags:
- Diffusion Distillation
- Posterior Matching
- Mode-covering
- Any-step Sampling
- SDXL
- FLUX
one_liner: 提出后验匹配蒸馏，通过匹配指数重加权样本均值恢复教师后验，支持任意步采样并在4步FID上最优
practical_value: '- 生成式推荐/文案生成中的多样性：reverse-KL 蒸馏会偏向头部模式；可借鉴 PMD 的 mode-covering 后验匹配，在教师为多样性丰富的
  LLM/推荐模型时保留长尾覆盖，避免只生成高频标题或爆款商品。

  - 低开销分布监督：PMD 用指数倾斜后验均值，单次教师前向即可提供监督，无需辅助 student-score 网络；在小模型蒸馏或多模态商品内容生成中可降低教师调用成本与训练复杂度。

  - 任意步采样部署：PMD 学生支持训练时间步网格内任意步采样，无需重新训练；业务中可按 RT/质量需求动态调整步数，适用于广告创意生成、商品图生成等延迟敏感场景。

  - 多矩匹配的稳定性：用一组均值约束即可唯一确定条件分布，较对抗/score 匹配更稳定；对构建推荐/Agent 系统中的小生成模型有工程参考价值。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：分布蒸馏常用 reverse-KL，其 mode-seeking 偏置会牺牲样本多样性。PMD 针对此问题，将 mode-covering 后验采样与 any-step 生成结合。

方法：学生为随机生成器，在训练好的时间步网格内支持任意步采样，无需重新训练。学习时，对固定噪声状态下的学生样本做指数重加权平均，匹配相应教师后验均值。高斯 corruption 下，指数倾斜后验均值等价于教师在 shifted input 上的单次评估，大幅降低教师调用成本。理论证明，匹配开邻域上倾斜均值可唯一确定完整后验；因此 PMD 通过一组均值约束监督整个条件分布，而不需要辅助学生 score 网络。

结果：在 SDXL 与 FLUX.2 [klein] 4B 上进行 4 步蒸馏，PMD 在两个模型的 FID 上均达到最佳，同时 prompt-alignment 与感知质量指标保持竞争或领先。
