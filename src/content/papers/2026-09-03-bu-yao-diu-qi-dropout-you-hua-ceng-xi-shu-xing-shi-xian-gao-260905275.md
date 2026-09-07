---
title: 'Don''t Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training
  and Inference'
title_zh: 不要丢弃 Dropout：优化层稀疏性实现高效 LLM 训练与推理
authors:
- Mostafa Elhoushi
- Alex Pretko
- Nolan Dey
- Bin Claire Zhang
- Gavia Gray
- Gurpreet Gosal
- Abdulrahman Mahmoud
- Shane Bergsma
- Joel Hestness
affiliations:
- Cerebras Systems
- MBZUAI
arxiv_id: '2609.05275'
url: https://arxiv.org/abs/2609.05275
pdf_url: https://arxiv.org/pdf/2609.05275
published: '2026-09-03'
collected: '2026-09-07'
category: Training
direction: LLM 层稀疏训练与推理加速
tags:
- Layer Dropout
- Efficient Training
- Inference Acceleration
- LLM
- Stochastic Depth
- Self-Speculative Decoding
one_liner: 系统优化层丢弃的分布、调度与超参数，同等 FLOPs 降低损失，训练省 25% FLOPs，推理提速达 1.5 倍
practical_value: '- 若团队在自研或微调大规模 Transformer 推荐模型 / 用户行为序列 LLM，可重新引入 layer dropout，按论文给出的非均匀层分布、渐进式线性衰减调度和优化器超参配置，在不增加训练
  FLOPs 预算下获得更低验证损失，或节省约 25% 训练 FLOPs。

  - 利用 layer dropout 训练得到的模型具有 elastic depth 能力，可直接做静态 early exit 或 intermediate layer
  skipping；在电商搜索推荐、Agent 场景中对 LLM 调用频繁的在线服务，可降低推理延迟并节省算力。

  - 训练后的模型可配合 self-speculative decoding，将推理速度再提升至 1.5x 且精度损失可忽略，适合广告文案生成、查询理解、对话式推荐等对响应时间敏感的线上链路。

  - 对于已有 transformer 模型，可尝试用 layer dropout 做轻量正则化，提升模型对后续剪枝 / 跳层推理的鲁棒性，为线上弹性部署提供基础。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Layer dropout（stochastic depth）在视觉和小模型中能加速训练、提升精度并增强对层剪枝的鲁棒性，但随着 LLM 预训练规模扩大，dropout 在主流 recipe 中几乎消失，部分工作报道其会损害精度，缺乏系统性量化与优化。

**方法关键点**：作者在 271M 至 8.2B 参数、最多 160B tokens 的规模下，系统搜索 layer dropout 的层丢弃概率分布、时间调度（如线性衰减）及优化器超参数。核心是让不同层使用不同的丢弃概率，并在训练过程中动态调整，而非简单的均匀丢弃。实验均基于 Cerebras CS-3。

**关键结果**：在相同训练 FLOPs 下，加入优化后的 layer dropout 能获得更低的验证损失；在固定训练步数下，可节省最多 25% 训练 FLOPs 且验证损失不升。训练得到的模型天然支持 early exit、中间层跳过等后训练优化，并配合 self-speculative decoding 实现最高 1.5 倍推理加速，精度损失可忽略。
