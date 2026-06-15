---
title: Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO
title_zh: 小模型天然为GRPO提供策略级多样性
authors:
- Yiming Ren
- Yiran Xu
- Zicheng Lin
- Chufan Shi
- Yukang Chen
- Dingdong Wang
- Tianhe Wu
- Junjie Wang
- Yujiu Yang
- Yu Qiao
affiliations:
- Tsinghua University
- Shanghai AI Laboratory
- The Chinese University of Hong Kong
- City University of Hong Kong
arxiv_id: '2605.30789'
url: https://arxiv.org/abs/2605.30789
pdf_url: https://arxiv.org/pdf/2605.30789
published: '2026-06-01'
collected: '2026-06-15'
category: Training
direction: GRPO训练中策略级探索增强
tags:
- GRPO
- Policy Diversity
- Model Distillation
- RLVR
- Small-to-Large
one_liner: 利用同家族小模型的策略级多样性替代token噪声，通过渐进退火实现大模型训练加速与性能提升
practical_value: '- 在推荐/Agent场景中，可借鉴用能力较弱但行为更多样的模型（如蒸馏小模型）生成候选离线样本，训练更强的决策模型，实现低成本探索。

  - 渐进退火策略：训练早期多用小模型rollout保证多样性，后期逐步切换至大模型on-policy，避免分布偏移导致性能退化，这一机制可直接用于离线强化学习或推荐系统的A/B策略优化。

  - 利用同一模型家族内天然存在的策略差异（通过蒸馏带来的参数级扰动）作为多样性源，比粗暴提高采样温度更稳定、生成的序列更具逻辑连贯性，对需要保持文本质量的电商文案生成等多步推理任务有参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
GRPO（Group Relative Policy Optimization）依赖组内候选样本的多样性来估计梯度。传统做法是通过提高采样温度注入token级噪声，但这会破坏长序列的逻辑连贯性，导致梯度信号混乱、训练不稳定。作者发现，同模型家族内的小模型（如Qwen3-1.7B）在pass@k指标上，当采样数k足够大时，其性能可以超越更大模型（如8B、14B），表明小模型天然具备更高的**策略级多样性**——即在不同推理路径上的覆盖更广、解答更丰富。这种多样性源于模型蒸馏导致的参数级扰动，是时不变的、保持时间相关性的结构化探索信号。

**方法关键点**  
- **S2L-PO框架**：将固定的小模型作为explorer，大模型作为learner，利用小模型生成部分rollout与大模型自己生成的rollout混合，组成训练组。  
- **渐进退火策略**：训练前半程线性降低小模型生成比例（从1到0），后半程完全切换为大模型on-policy采样，既利用了小模型早期的多样化探索，又避免了训练后期大模型与小模型之间的分布偏移。  
- 框架只修改rollout生成过程，完全兼容现有GRPO实现，计算开销低，且小模型rollout可跨实验复用。

**关键结果**  
- 在Qwen3-8B上，用1.7B explorer训练，AIME24 Pass@1从15.0%提升到23.8%（+8.8%），AIME25从12.1%提升到22.5%（+10.4%），同时训练FLOPs减少。  
- 在InternLM2.5-7B上用1.8B explorer，AIME24从0.1%提升至4.6%。  
- 控制实验：如果从1.7B rollouts中筛除多样性样本使其多样性水平与大模型一致，则S2L-PO增益消失，证明多样性是收益来源。  
- 渐进退火优于直接切换：逐渐过渡避免训练震荡；退火周期过短也会导致性能下降。

**一句话总结**  
小模型的策略级多样性是比token级噪声更稳定、更连贯的探索信号，能显著提升GRPO训练。
