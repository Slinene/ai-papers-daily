---
title: 'Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher
  On-Policy Distillation'
title_zh: 超越领域路由监督：多教师在线蒸馏的跨教师守护
authors:
- Shi-Yu Tian
- Yong Liu
- Ximan Liu
- Tianrui Zhu
- Sule Bai
- Xinwei Yang
- Ruiqi Liu
- Kun-Yang Yu
- Ming Yang
- Zhi Zhou
affiliations:
- Nanjing University
- JD.com
arxiv_id: '2610.13521'
url: https://arxiv.org/abs/2610.13521
pdf_url: https://arxiv.org/pdf/2610.13521
published: '2026-10-08'
collected: '2026-10-15'
category: Training
direction: 多教师在线蒸馏梯度冲突缓解
tags:
- multi-teacher distillation
- on-policy distillation
- gradient projection
- credit assignment
- LLM training
one_liner: 提出 ROADMOPD，引入非路由教师作为跨域批评者，通过 token 级信用分配与梯度投影缓解多教师在线蒸馏的梯度冲突
practical_value: '- 在多领域/多任务 LLM 在线蒸馏或 RLHF 中，不要只靠数据路由区分教师；可在同一批轨迹上额外计算非路由教师的梯度/损失作为冲突检测器，用教师一致性加权
  token 级损失，低成本缓解共享参数下的梯度冲突。

  - 梯度投影是可复用的训练工程技巧：当辅助梯度与主梯度方向冲突时，对主更新做投影去除冲突分量；但落地时应自适应控制投影强度，避免过度约束损害目标域信号，可参考其投影强度的门控/衰减机制。

  - 若业务中需同时蒸馏多个领域专家（如电商搜索、推荐文案、客服），可借鉴“跨教师守护”思路：把非目标域教师作为 critic，不直接更新学生，只参与冲突感知的梯度修正，降低劣势领域退化风险。

  - 对于 token 级信用分配：利用教师间一致性而非单教师概率来调整 token loss 权重，能减少噪声标签/风格差异带来的干扰，适合生成式推荐中文本质量与领域风格冲突的场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：多教师在线蒸馏（MOPD）通过领域路由把特定域数据分配给专门教师，以密集 token 级监督统一蒸馏。但领域路由只区分监督来源，所有域更新仍作用于共享参数；当教师风格和领域专长差异大时，联合优化会产生持续梯度冲突，导致劣势域能力退化。

方法关键点：提出 ROADMOPD，引入非路由教师作为同一学生轨迹上的辅助跨域批评者，协调多教师监督。具体包括：1）跨教师引导的信用分配：用教师一致性强化共同支持的 token 级修正，削弱冲突信号；2）预防性多教师梯度投影：用同一轨迹的辅助梯度约束潜在冲突更新，并自适应控制投影强度，保留目标域学习信号。

结果：在高冲突场景下优势域提升超过5个百分点，在低冲突和三领域设置下整体性能也有改善，缓解劣势域退化。
