---
title: Boosting Reinforcement Learning with Verifiable Rewards via Randomly Selected
  Few-Shot Guidance
title_zh: 通过随机少样本指导增强可验证奖励强化学习
authors:
- Kai Yan
- Alexander G. Schwing
- Yu-Xiong Wang
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2605.15012'
url: https://arxiv.org/abs/2605.15012
pdf_url: https://arxiv.org/pdf/2605.15012
published: '2026-05-13'
collected: '2026-05-15'
category: LLM
tags:
- RLVR
- GRPO
- DPO
- Few-Shot
- Math Reasoning
one_liner: 提出 FEST 算法，仅用 128 个随机 SFT 演示，通过半在线 DPO 和衰减权重实现 RLVR 的显著提升
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
Reinforcement Learning with Verifiable Rewards (RLVR) 在数学推理等任务上表现优异，但面对复杂问题时样本效率低下——一旦一个 batch 中全是错误答案，优势为零，无法提供学习信号。现有演示引导的 RLVR 方法（如 HPT、ReLIFT）尝试在 RL 失败时引入 SFT，却依赖大量昂贵的高质量推理数据，制约了可扩展性。本文希望探索：能否仅用极少随机选择的 SFT 演示（few-shot）就大幅提升 RLVR 的性能？

**方法关键点**  
- 提出 **few-shot demonstration-guided RLVR 范式**：用随机采样的 128 个 SFT 示例提供专家信号，其余问题仅用布尔奖励的 RLVR。  
- 设计 **FEST** 框架，组合 GRPO（用于答案唯一数据集）和半在线 DPO 损失（用于少样本 SFT 数据）：SFT 推理作为正例，agent 自身生成为负例。  
- 阐明了三个关键成分：(1) **监督信号**——从 SFT 学习专家推理；(2) **在策略信号**——用 agent 自己的 rollout 作为负例对抗训练，缓解曝光偏差并扩大探索基础；(3) **衰减权重**——防止在小数据集上过拟合。  
- 针对 DPO（序列级）与 GRPO（token 级）梯度不匹配问题，提出 **FEST‑GRPO** 变体，将 DPO 分解为加权 SFT 和带负优势的 GRPO，使梯度尺寸一致。  
- 引入**自适应β**：根据问题可解性（全错/有对有错/全对）赋予不同 β 值，精细控制学习强度。

**关键实验与结果**  
在 Qwen2.5‑Math‑1.5B 上，用 OpenR1‑Math‑46K 的随机 128 个样本作为 SFT 数据集，其余作为答案验证 RL 数据。对比 Vanilla RL、RL‑G、LUFFY、CHORD‑ϕ、HPT、ReLIFT 等 baseline。主要指标 Avg@8：  
- FEST‑DPO 达到 41.98，FEST‑GRPO 达到 **42.38**，显著优于纯 RL 的 39.79 及其他方法（如 HPT 38.75、ReLIFT 40.51）。  
- Pass@8 方面，FEST‑GRPO 取得 **61.06**，远超 RL‑G 的 54.84，表明探索潜力更高。  
- FEST 在 64 shot 下仍有效，且 FEST‑DPO 随 shot 数增加可逼近全量 SFT 下的 HPT 性能。  
- 更换不同的随机 128-shot 子集或使用 LIMOv2 示例，FEST 依旧稳定获益。  
- 消融实验证实三个成分缺一不可；MMLU‑Pro 上 FEST 泛化最佳。

**最值得记住的一句话**  
“仅凭 128 个随机选取的 SFT 演示，FEST 就能让 RLVR 性能显著超过所有对比方法，甚至匹配用全量数据训练的效果。”
