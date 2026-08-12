---
title: Scaling Inherently Interpretable Language Models
title_zh: 缩放内建可解释性语言模型
authors:
- Guide Labs Team
- Andreas Madsen
- Aya Abdelsalam Ismail
- Giang Nguyen
- Isaac Plant
- Muawiz Chaudhary
- Nathaniel Monson
- Saqib Azim
- Zhichen Guo
- Julius Adebayo
affiliations:
- Guide Labs
arxiv_id: '2608.07594'
url: https://arxiv.org/abs/2608.07594
pdf_url: https://arxiv.org/pdf/2608.07594
published: '2026-08-05'
collected: '2026-08-12'
category: LLM
direction: 可解释性内置训练的 LLM 缩放
tags:
- inherent interpretability
- concept bottleneck
- diffusion LM
- scaling laws
- Steerling-8B
- attribution
one_liner: 将可解释性作为训练约束与语言建模联合优化，实现与规模同步提升的内建可解释性
practical_value: '- 在推荐模型训练中加入概念瓶颈层，强制用户/物品表示与预定义业务概念（类目、品牌、意图）对齐，实现原生可解释的 embedding，用于召回或排序解释。

  - 利用归因与训练数据溯源能力，快速诊断推荐结果：定位影响当前推荐的用户历史行为或训练样本，通过移除/增强对应概念快速调试策略，无需重新训练。

  - 扩散语言模型 + 概念转向的思路可迁移至生成式推荐（如语义 ID 生成），在生成物品序列时直接通过概念向量控制推荐属性（多样性、新品偏好等）。

  - 可解释性随规模改善的缩放律意味着，在大规模推荐模型（如多模态 Transformer）中实验此类训练约束风险更低，可放心追求能力与可解释性双赢。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：主流可解释性方法多为事后解释，可靠性难验证，且常以牺牲性能为代价。本文挑战这一预设，将可解释性纳入训练目标，与语言建模联合优化，探索可解释性是否能够随规模良性增长。

**方法**：提出内建可解释性的训练框架，要求模型满足三个归因要求：token 级归因（输出 token 归因到输入 token）、概念归因（归因到人类可理解的概念）、训练数据归因，并支持概念转向干预。具体实现上，在 Transformer 中插入概念解码器（线性层），将隐藏状态映射到预定义概念空间，再用于预测；采用 causal 注意力掩码，结合扩散生成目标。在自回归和扩散语言模型上，从 125M 到 8B 参数、三个数量级计算量进行实验。最终实例化为 **Steerling-8B**：一个扩散语言模型，可对任意生成 token 提供输入、概念、训练样本三级归因，并支持诊断后通过调节概念向量纠正行为。

**关键结果**：可解释性指标（归因忠实度、概念对齐度）随模型规模提升而改善；Steerling-8B 在下游任务上性能与 2–16 倍计算量训练的开源模型相当，证明可解释性与能力可以同步缩放，设计良好的训练约束不会损害性能。
