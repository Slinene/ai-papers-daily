---
title: 'InfoSFT: Learn More and Forget Less with Information-Aware Token Weighting'
title_zh: InfoSFT：信息感知的令牌加权，学得更多，忘得更少
authors:
- Mahdi Sabbaghi
- George Pappas
- Adel Javanmard
- Hamed Hassani
affiliations:
- University of Pennsylvania
- University of Southern California
arxiv_id: '2605.14967'
url: https://arxiv.org/abs/2605.14967
pdf_url: https://arxiv.org/pdf/2605.14967
published: '2026-05-14'
collected: '2026-05-15'
category: Training
tags:
- SFT
- Token Weighting
- Catastrophic Forgetting
- KL Divergence
- Proximal Policy Optimization
- LLM Fine-tuning
one_liner: 提出基于模型置信度的令牌加权规则，为中等置信度令牌分配最高权重，提升泛化并减轻灾难性遗忘
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：标准 SFT 对所有令牌均匀加权，低似然样本易驱动过度更新，导致过拟合与灾难性遗忘。DFT 等降权低似然样本，却会抑制新颖行为的学习。需要在学习新行为与保留旧能力之间取得最佳平衡。

**方法关键点**：
- 将 SFT 建模为近端策略优化：在固定 KL 预算下，最小化与专家总体分布的 KL 散度，而非最大化学到样本的似然。
- 导出最优令牌权重形式：w(q) ∝ q (logit(¯p) − logit(q))₊，其中 q 是模型对目标令牌的预测概率，¯p 为平均专家概率（实验中取 0.93）。
- 权重特性：中等置信度令牌获得最高权重，极低置信度令牌权重趋于零，高置信度令牌权重裁剪到零，避免负更新。
- 实现：仅需一行代码修改标准交叉熵损失，将 DFT 的 q 因子替换为 q · max(logit(¯p) − logit(q), 0)。

**关键实验与数字**：
- 数学微调（Qwen-2.5-Math-1.5B、7B，Llama-3.1-8B，NuminaMath-CoT）：InfoSFT 在 MATH500 acc@1 上分别达到 66.2、69.7、27.8，均优于 SFT（61.6、53.4、24.0）和 DFT（59.2、65.4、15.5）；AMC 上优势更大（Qwen-1.5B 从 34.9 提升到 41.0，DFT 仅 30.1）。
- 代码微调（UltraFeedback）：Llama-3.1-8B 的 HumanEval pass@1 达到 44.8，超过 DFT（41.8）和 SFT（40.9）。
- 灾难性遗忘（Science Q&A、Tool Use）：InfoSFT 在所有超参数扫描下获得最佳新任务/旧能力 trade-off 曲线。
- 输出多样性：InfoSFT 保持高输出熵，避免 DFT 的模式坍塌，有利于后续 RL 或 best-of-n 采样。
- 与 SFT 互补：先 SFT 后 InfoSFT 的两阶段训练在 AIME 上 pass@8 达到 50.0，比纯 SFT 第二阶段提升 6.7 个点。

最值得记住的一句话：InfoSFT 用一条简单的令牌权重公式，在固定分布偏移预算下，使模型学到更多而遗忘更少。
