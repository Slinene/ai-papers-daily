---
title: Are Dense Rewards Worth Their Tokens in GRPO?
title_zh: 密集过程奖励在 GRPO 中的 token 开销是否值得？
authors:
- Vikash Singh
- Weicong Chen
- Debargha Ganguly
- Yanyan Zhang
- Mohsen Hariri
- Sreehari Sankar
- Wang Yang
- Chaoda Song
- Alexander Nemecek
- Osama Zafar
arxiv_id: '2611.13560'
url: https://arxiv.org/abs/2611.13560
pdf_url: https://arxiv.org/pdf/2611.13560
published: '2026-11-09'
collected: '2026-11-11'
category: Training
direction: RLVR/GRPO 训练方法评估
tags:
- GRPO
- RLVR
- dense rewards
- matched compute
- reasoning
one_liner: 提出 matched-compute 协议，发现密集过程奖励在同等 token/GPU 预算下不优于 GRPO，而选择预测成功率接近 1/2
  的 prompt 更有效
practical_value: '- 在 LLM 微调或 agent 推理训练中，评估任意训练干预（如 dense reward、过程监督）必须固定生成 token
  数和 GPU 时数做 matched-compute 对比，否则 per-update 结果可能完全反转。

  - 密集 Monte-Carlo 过程奖励的续写 token 成本极高（本文占 91%），生产环境 RLVR 优先用标准 GRPO 或做 prompt/数据选择，而非加
  dense reward。

  - 选择预测成功率接近 1/2 的 prompt（高不确定性、可学习潜力大）训练，在同等计算预算下稳定提升；可用预测失败概率做难样本筛选。

  - 收益集中在训练早期，提高初始学习率（如 2 倍）配合标准 GRPO 可低成本逼近数据选择收益。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：RLVR 中 GRPO 给解中每个 token 同等 credit，dense process reward 被提出来改进中间步骤，但现有比较通常按单次更新或单 batch 梯度检验，忽略了 token 成本。本工作中续写 token 占总生成 token 91%。

方法关键点：建立 matched-compute 协议，固定生成 token 数与训练 GPU 时数预算，对 6 个模型、1668 次运行做预注册对照；同时比较 Monte-Carlo 过程奖励、多种 dense-reward 变体、基于预测成功率的 prompt 选择。

关键结果：在 Qwen2.5-1.5B 上，Monte-Carlo reward 按更新次数略优，但在等 token 预算下低 14.3 个百分点，等训练时间下低 7.8 个百分点；四种 dense-reward 变体无一超过标准 GRPO。单 batch 梯度检验能排序但高估各 reward 1-2 点。相反，训练预测成功率接近 1/2 的 prompt 在 matched compute 下提升 Qwen3-0.6B 1.7 点、Qwen2.5-1.5B 0.8 点，并能复现到新种子与未见问题；标准 GRPO 用 2 倍初始学习率可逼近这些收益。
