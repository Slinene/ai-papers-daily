---
title: 'Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution'
title_zh: 无搜索锐化：序列级幂分布的在线策略蒸馏
authors:
- Erfan Baghaei Potraghloo
- Seyedarmin Azizi
- Arya Fayyazi
- Saeid Shokoufa
- Mehdi Kamal
- Souvik Kundu
- Massoud Pedram
affiliations:
- University of Southern California
- Intel AI
arxiv_id: '2610.06804'
url: https://arxiv.org/abs/2610.06804
pdf_url: https://arxiv.org/pdf/2610.06804
published: '2026-10-04'
collected: '2026-10-07'
category: Training
direction: LLM 训练 · 无奖励推理锐化
tags:
- on-policy distillation
- power distribution
- SMC
- reasoning
- LLM training
one_liner: OPPD 通过 on-policy 蒸馏把推理时序列级幂分布采样的成本转移到训练阶段，单个生成即可达到或超过 64 候选采样
practical_value: '- 在电商搜索 query 推荐或文案生成中，可以训练模型学习教师模型对完整序列的幂分布，即对完整候选文本（如 query）的概率进行
  α 次幂加权，使推理时只需单次生成即可达到近似多个候选采样再加权的效果，大幅降低线上推理延迟。

  - 借鉴 on-policy weighted likelihood 训练方式：让待训练模型自己生成候选，用冻结教师（如 LLM）给出概率并计算权重，重点加权学生自身的高概率答案；这比直接蒸馏教师生成样本更贴合实际分布，适用于
  Agent 工具调用轨迹或推荐解释文本的训练。

  - 工程实现 trick：生成候选时使用教师温度 1/α 的 proposal 降低重要性权重方差，避免权重退化；将长文本分块（例如 64 tokens）让教师一次前向评分，减少调用次数；训练权重与
  SMC 重要性权重分别累加，并在重采样后重新归一化。这些都能复用在大规模在线生成任务的稳定训练中。

  - 在没有人工偏好或点击信号可用时，可以使用模型自身的序列概率（经由 teacher 锐化）作为软奖励进行训练，提升推理和生成质量；对电商问答、商品推荐理由、营销文案生成等场景可低成本迁移。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM 采样时，即使正确答案单个概率最高，错误答案总概率和更大，导致采样错误；将完整答案概率取 α 次幂并重新归一化（power distribution）可提升推理准确性，但推理时需要运行 SMC 采样多个候选，成本高。能否把采样成本转移到训练阶段？

**方法关键点**  
- 训练目标：最小化学生与教师 power distribution 的 Rényi divergence，通过重要性加权最大似然实现。  
- 学生自己生成候选（on-policy），教师冻结，计算每个 token 概率用于 SMC importance weights 和训练权重。  
- 使用 proposal 温度 1/α 降低重要性权重方差；生成 16 个候选，每 64 tokens 为一个 block，teacher 一次前向评分。  
- 损失函数：加权最大似然（序列级）+ token 级 anchor KL（防止分布过度集中），系数 λ 控制锐化程度。  
- 测量 absorbed exponent α_eff 验证模型确实吸收了锐化。

**关键实验**  
- 在 Qwen2.5-Math-7B 自蒸馏，单次生成在 MATH500 上达到 78.5，超过 power sampling 64 候选的 76.1，并达到 94% 的 16 候选增益；GSM8K 也类似。  
- 同预算下，OPPD 比 GRPO（使用验证奖励）在 MATH500/GSM8K/AIME 高 3.8/4.0/5.4 点；与 GRPO 可组合，GRPO 后 OPPD 再加 9.3 点。  
- 仅在数学上训练，HumanEval 准确率提升最多 5.3 点。  
- 跨模型家族有效，包括 deepseek-math-7b-rl 已用验证奖励训练后仍能提升 4.4 点。

**最值得记住的一句话**  
OPPD 表明，可以把推理时序列级幂分布采样的“搜索”成本蒸馏到模型参数中，单个生成即可获得多候选采样的推理增益，且无需任何真实奖励。
