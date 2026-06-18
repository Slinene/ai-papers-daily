---
title: 'Sumi: Open Uniform Diffusion Language Model from Scratch'
title_zh: Sumi：从头预训练的开源7B均匀扩散语言模型
authors:
- Mengyu Ye
- Keito Kudo
- Wataru Ikeda
- Ryosuke Matsuda
- Keisuke Sakaguchi
- Jun Suzuki
affiliations:
- Tohoku University
arxiv_id: '2606.19005'
url: https://arxiv.org/abs/2606.19005
pdf_url: https://arxiv.org/pdf/2606.19005
published: '2026-06-16'
collected: '2026-06-18'
category: LLM
direction: 均匀扩散语言模型预训练
tags:
- Diffusion Language Model
- UDLM
- Pretraining
- 7B
- Open Source
one_liner: 首个从头预训练的大规模均匀扩散语言模型，在知识、推理、编码上与同规模自回归模型竞争，常识略弱
practical_value: '- 扩散生成允许任意位置并行更新，可用于搜索/推荐中的 query 改写、item 描述生成，利用温度调控多样性；微调时可将扩散步数作为可控
  knob，平衡质量与延迟。

  - 在 Agent 场景中，均匀扩散的迭代修订特性适合生成多步推理或计划，支持中途修正输出，相比自回归更灵活。

  - 教育数据偏重导致常识弱，启示我们在推荐领域微调时需注入大量领域交易日志、用户评论等语料，避免常识缺失影响自然度。

  - 开源训练配方和完整数据混合说明，可直接复现或调整配比，构建面向电商/广告的垂直 LLM 基座。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：均匀扩散语言模型（UDLM）在理论上更灵活（任意 token 可随时更新），但此前没有从头预训练的大规模版本，阻碍了其与自回归模型（AR）和掩码扩散模型（MDLM）的公平对比与社区研究。  
**方法**：Sumi 采用均匀扩散过程，在每个扩散步允许对所有 token 重新采样，训练 7B 参数模型，使用 1.5T token 公开语料（含大量教育类数据），并公开完整数据配方与训练细节。  
**关键结果**：在 MMLU（知识）、GSM8K（推理）、HumanEval（编码）等基准上与同 token 量的 AR 模型表现相当，但常识基准（如 HellaSwag）明显落后，归因于教育数据主导的训练混合。模型权重、检查点全部开源。
