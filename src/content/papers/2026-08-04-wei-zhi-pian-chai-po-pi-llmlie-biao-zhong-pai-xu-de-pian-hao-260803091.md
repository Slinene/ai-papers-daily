---
title: Position Bias Undermines Preference Consistency in Listwise LLM-Based Reranking
title_zh: 位置偏差破坏LLM列表重排序的偏好一致性
authors:
- Ethan Bito
- Yongli Ren
- Estrid He
affiliations:
- RMIT University
arxiv_id: '2608.03091'
url: https://arxiv.org/abs/2608.03091
pdf_url: https://arxiv.org/pdf/2608.03091
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: LLM重排序可靠性评估
tags:
- Position Bias
- LLM Reranking
- Permutation Invariance
- Preference Consistency
- Kemeny Optimization
- Recommendation
one_liner: 提出成对/全局/输出三层一致性指标，揭示LLM重排序的排列敏感性远超曝光偏差修正所能解决
practical_value: '- 评估LLM重排序器时须同时关注排列一致性：仅看HR/nDCG不够，应加PPI（成对不稳定度）、GPI（全局不一致度）、LOC（列表输出一致性）来量化候选顺序敏感度，确保排序函数在各输入排列下输出稳定偏好。

  - 常见偏差修正方法可能掩藏更严重的偏好结构破坏：STELLALW能平坦化位置曝光并提升HR@5，但PPI/GPI/LOC在实验中均最差，说明仅减小平均曝光偏差不足以恢复全局一致的偏好，业务落地不可单指标驱动。

  - SGS（顺序贪心选择+重排）在一致性和曝光偏差上取得了较好平衡，但需要K次推理（K=候选集大小），适合对一致性要求极高且可接受推理延迟的场景；Bootstrapping（多次随机打乱聚合）是轻量替代，在一致性上也有明显提升。

  - 工程生产建议对同一请求多次打乱候选顺序，计算排名的一致性（如Kendall’s τ）作为在线监控指标，防止因模型更新或Prompt调整引入排列不稳定性，并结合边际曝光曲线指导系统优化。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM作为列表重排序器（listwise reranker）已广泛用于推荐系统，但解码器模型对输入顺序敏感，同一候选集的不同序列可能产生不同排序结果。以往研究多关注边际位置曝光偏差（即输入位置影响被放到顶部的概率），但忽略了一个更深层的问题：输入顺序变化可能导致偏好关系的局部不稳定与全局不一致，破坏排序函数的基本有效性。

**方法关键点**
- 将同一候选集在多种排列下生成的排序视为“诱导偏好系统”的观测，定义三个层次的排列一致性指标：
  - **PPI（成对偏好不稳定性）**：对每对候选，按输入位置分桶（头/中/尾）计算偏好概率的极差，越高表示越不稳定。
  - **GPI（全局偏好不一致性）**：通过加权Kemeny优化寻找最拟合所有成对偏好的全局排序，以该排序与观察偏好的冲突量衡量全局不一致程度。
  - **LOC（列表输出一致性）**：用Kendall’s τ计算多次打乱下最终排序的平均一致度。
- 同时测量边际位置曝光偏差（Top-k Exposure）作为对比维度。
- 实验对比了Zero-shot、Bootstrapping（多次打乱Borda聚合）、SGS（顺序贪心选择并每次重排剩余候选）、STELLALW（基于位置校准的贝叶斯校正）四种方法。

**关键结果**
- 在MovieLens-32M和Amazon Books上，三个一致性指标高度一致：SGS最优，Bootstrapping次之，Zero-shot较差，STELLALW最差。但推荐效果（HR@5）STELLALW最高，SGS或Bootstrapping并不总是最好，说明HR与排列一致性无必然正相关。
- 边际曝光曲线显示：SGS和STELLALW都能平坦化输入位置曝光，但STELLALW仍产出最不一致的偏好结构，证明曝光修正不等于恢复全局一致性。
- 一致性指标在不同候选列表长度（15/25/50）下保持相同的方法排序，表明该评估框架具有稳定性。

**核心结论**
仅靠减少平均曝光偏差无法建立排列稳定的LLM重排序器；推荐系统部署中必须同时考量推荐效果与排列一致性，且现有方法在二者之间存在显著权衡。
