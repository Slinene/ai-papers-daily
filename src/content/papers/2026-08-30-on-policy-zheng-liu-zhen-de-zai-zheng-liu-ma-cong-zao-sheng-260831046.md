---
title: Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement
title_zh: On-Policy 蒸馏真的在蒸馏吗？从噪声教师到自改进
authors:
- Yi Ding
- Ruqi Zhang
affiliations:
- Purdue University
arxiv_id: '2608.31046'
url: https://arxiv.org/abs/2608.31046
pdf_url: https://arxiv.org/pdf/2608.31046
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: LLM 强化学习 · 零外部监督自改进
tags:
- On-Policy Distillation
- Self-Improvement
- RLVR
- Token-level RL
- LLM Reasoning
- Entropy-adaptive Advantages
one_liner: 揭示 OPD 增益主要来自抑制低概率 token 而非教师蒸馏；提出零外部监督的熵自适应负优势法 OPSA，AIME24 Avg@32 提升
  263%
practical_value: '- 在做 agent/LLM 策略后训练时，如果已使用 OPD/蒸馏提供 token 级信号，可先做噪声审计：统计 teacher
  优势方向与最终 reward 不一致的比例；若噪声高，可直接对低 logp token 施加固定或熵自适应负优势，省掉 teacher forward 和 reward
  model，降低 off-policy mismatch。

  - 对商品文案生成、query 改写等需要保持多样性的生成任务，可借鉴 OPSA 的 token 选择：只更新每个 rollout 中最低 20% log-prob
  tokens，避免高置信 token 的无效更新；同时在高熵位置施加更强负优势，抑制低概率 tail，保留 head 间概率重分配，防止 pass@k/多样性崩溃。

  - 多轮购物导购、自动客服等需要长程推理和自我修正的 agent，可把 OPSA 作为廉价的 reasoning post-training 插件：不依赖外部
  reward/hint，让模型在无标注下延长反思轨迹、提升最终答案质量；但要注意它主要重分配已有概率质量，初始策略过强或分布过尖时收益可能有限。

  - 工程上可直接用 slime/Megatron 实现；无 teacher 额外 forward，训练吞吐优于 OPD，适合资源受限团队。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-policy distillation (OPD) 用教师模型给 token 级优势，替代 RLVR 的稀疏奖励。但学生采样轨迹对教师而言是 off-policy，教师信号是否可靠、学生收益到底来自哪里并不清楚。论文发现教师优势噪声很高：4B 教师噪声率 30.6%，235B 教师达 50.6%；并且学生对这些噪声不敏感，只用噪声轨迹、只去噪声轨迹、标准 OPD 效果接近。

### 方法关键点
- 拆解 OPD 增益来源：高 log-prob token 梯度几乎消失，51.7% token 的优势 |A|≤1e-4；有效学习集中在最低 20% logp token。
- 固定负优势实验：对最低 20% logp token 给固定 A=-0.5，效果接近 OPD；给正优势会崩溃。说明 OPD 本质是抑制低概率 token，而非蒸馏教师知识。
- 进一步发现负优势大小应由 token entropy 决定：高熵位置给更强负信号（δ=1）效果最好。
- 提出 OPSA：只使用学生策略，无教师、无 verifiable reward、无 hint；选 rollout 中最低 20% logp token，赋 A_i^dyn = -1/2 - (H_i-H_min)/(2(Hmax-Hmin))。它在低熵位置抑制 tail token、集中 head 概率；在高熵 fork 位置把概率质量在竞争 head token 间重分配，保持探索多样性。

### 关键结果数字
- 模型：Qwen3-1.7B/4B、Qwen3.5-9B；训练 DAPO-17k（仅用题目），评估 AIME24/25、HMMT25、MBPP+、GPQA-Diamond。
- Qwen3-1.7B + OPSA：AIME24 Avg@32 13.44→48.85（+35.41，+263.5%），AIME25 +264.4%，HMMT25 +307.2%；Pass@32 全部翻倍以上。
- 对比 GRPO、TTRL、OPD、OPSD：OPSA 平均 Avg@32 比最强 baseline 高 11.04，Pass@32 高 8.89；相比 OPD，AIME24 Avg@32 高 16.77。
- 消融：只训练最低 10% token 性能明显更差，20%-40% 不敏感；mask fork token 后长度和准确率收益消失。

最值得记住的一句话：OPD 的收益很可能不是来自教师蒸馏，而是来自抑制学生自己采样的低概率 token；token 级熵自适应的负优势可以替代外部监督。
