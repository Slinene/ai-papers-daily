---
title: Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing
title_zh: 可组合非结构化知识编辑的混合策略自编辑
authors:
- Tianci Liu
- Zihan Dong
- Tianchun Li
- Yi-Chung Chen
- Qiming Cao
- Xingchen Wang
- Shiyang Wang
- Zichen Miao
- Linjun Zhang
- Haoyu Wang
affiliations:
- University of Tennessee
- Rutgers University
- Purdue University
- University at Albany
arxiv_id: '2608.11660'
url: https://arxiv.org/abs/2608.11660
pdf_url: https://arxiv.org/pdf/2608.11660
published: '2026-08-11'
collected: '2026-08-15'
category: LLM
direction: 非结构化知识编辑与组合推理
tags:
- Knowledge Editing
- Unstructured KE
- Self-Distillation
- Hybrid Rollout
- Composability
- LLM
one_liner: 提出HPSE，通过特权上下文自蒸馏与混合rollout注入缺失事实，使非结构化知识编辑具备组合推理能力
practical_value: '- 快速修正线上LLM中的商品信息、活动规则、推荐话术时，可将HPSE作为即插即用层叠加在现有知识编辑方法上，提升模型对更新事实的原子问答与多跳组合推理能力，避免每次全量微调。

  - 混合rollout自蒸馏可迁移到LLM微调/RLHF：当注入知识（新类目、新政策、新活动）在模型自身生成分布中覆盖不足时，把标准答案片段插入模型生成的失败位置，其余保持on-policy，构建蒸馏数据或训练信号，比纯SFT或纯on-policy蒸馏更有效。

  - 无需外部监督，利用模型自身上下文作为特权状态，适合业务中无标注事实更新场景，可降低标注成本。

  - 注意：方法假设单一模型内更新，在多用户/多会话推荐系统中需额外验证编辑一致性与遗忘副作用。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
LLM知识快速过时，知识编辑需求上升。非结构化知识编辑（UKE）注入自由段落但无法回答原子问题或组合多跳推理，缺乏组合性。现有方法被动依赖固定段落作为唯一学习源，导致编辑后模型只会复述段落，不能灵活使用其中事实。

**方法关键点**
- 将编辑重新定义为从同一模型的特权上下文状态进行主动自蒸馏：用带编辑段落的上下文作为教师，无外部监督。
- 发现纯on-policy蒸馏受限于新知识新颖性，预编辑模型自身rollouts很少覆盖注入事实。
- HPSE构建混合rollout：在模型自身轨迹覆盖失败的位置插入缺失事实，其余保持on-policy，形成更有效的蒸馏轨迹。
- 理论分析显示混合rollout优于纯on-policy蒸馏。

**结果**
在4个LLM骨干和2个知识编辑器上，HPSE以即插即用方式提升组合推理和原子问答，跨多种场景验证有效性，且无需额外监督信号。
