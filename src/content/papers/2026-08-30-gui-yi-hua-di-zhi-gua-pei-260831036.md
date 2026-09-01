---
title: Normalized Low-Rank Adaptation
title_zh: 归一化低秩适配
authors:
- Jiale Kang
- Ziyin Yue
- Zheng Zhan
- Yangyi Huang
- Weiyang Liu
affiliations:
- Yuanshi Intelligence
- Microsoft Research
- The Chinese University of Hong Kong
- Shenzhen Loop Area Institute
arxiv_id: '2608.31036'
url: https://arxiv.org/abs/2608.31036
pdf_url: https://arxiv.org/pdf/2608.31036
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: 训练优化 · LoRA 归一化
tags:
- LoRA
- Normalization
- PEFT
- Training Dynamics
- Stability
- LLM
one_liner: NoRA 通过归一化 LoRA 下投影矩阵改善训练动态，无需额外参数或推理开销，加速收敛并缓解遗忘
practical_value: '- 在电商/广告场景用 LoRA 微调 LLM 做排序、召回或 query 改写时，可直接采用 NoRA 或仅初始归一化版本，几乎零成本提升训练稳定性和收敛速度，不增加推理延迟。

  - 对 RL 微调或持续预训练中的灾难性遗忘问题，归一化下投影矩阵可作为轻量正则手段，适合多任务/多领域顺序微调的推荐 Agent 底座模型。

  - 若使用 LoRA 微调生成式推荐模型或 Semantic ID 解码器，可尝试对下投影矩阵做初始化缩放或范数约束，改善低秩子空间的早期优化，进而影响 ID
  嵌入质量。

  - 工程实现上只需在 LoRA 插入点对 A 矩阵加一行归一化或初始化缩放，改动极小，适合快速在现有 PEFT 管线中 A/B 验证。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
LoRA 广泛用于参数高效微调，但其优化动态缺少有效正则。标准 LoRA 用随机初始化下投影矩阵 A、零初始化上投影矩阵 B，导致早期梯度主要由 A 主导，随机特征影响优化路径。

**方法关键点**  
提出 NoRA，在训练过程中对下投影矩阵 A 做归一化，抑制其范数漂移，使低秩子空间学习更稳定。进一步发现，仅在初始化时对 A 做一次归一化，也能提升标准 LoRA，且无需在训练中反复归一化，几乎不增加工程复杂度。

**关键结果**  
在预训练、监督微调和强化学习三类任务上，NoRA 均表现出更快收敛、更好的性能和训练稳定性，同时减轻灾难性遗忘。方法不引入额外可训练参数，也不改变推理时计算图，是一种简单通用的 LoRA 增强。
