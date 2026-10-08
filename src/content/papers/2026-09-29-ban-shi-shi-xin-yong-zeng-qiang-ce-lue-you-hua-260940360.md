---
title: Semifactual Credit-Augmented Policy Optimization
title_zh: 半事实信用增强策略优化
authors:
- Junshu Pan
- Zhizhang Fu
- Shulin Huang
- Yiran Ding
- Zifan Cheng
- Wenqi Shao
- Qiaosheng Zhang
- Yue Zhang
affiliations:
- Zhejiang University
- Westlake University
- Shanghai Innovation Institute
- Shanghai AI Laboratory
arxiv_id: '2609.40360'
url: https://arxiv.org/abs/2609.40360
pdf_url: https://arxiv.org/pdf/2609.40360
published: '2026-09-29'
collected: '2026-10-08'
category: Training
direction: LLM 强化学习训练 · token 级信用分配
tags:
- RLVR
- GRPO
- Token-level Credit Assignment
- Semifactual Interventions
- LLM Reasoning
- Policy Optimization
one_liner: 提出 SCAPO，将半事实稳定性融入 GRPO 的 token 级信用分配，提升数学推理与 OOD 泛化
practical_value: '- 在电商/Agent 场景用 RLVR 微调 LLM（如以是否成交/点击作为 verifiable reward）时，GRPO
  会把同一 outcome advantage 平均分给所有 token，容易强化 prompt 模板、位置等伪相关；可借鉴 SCAPO，用语义不变改写构造半事实干预，计算
  token 概率漂移作为稳定性分数，在早期训练中对不稳定 token 降低 advantage。

  - 论文发现解码时直接抑制高 drift token 候选，无需更新权重就能提升推理准确率；这可以迁移到 LLM 排序/召回/query 改写等生成任务，对 prompt
  改写或模板扰动下概率漂移大的 token 做推理时惩罚或 mask，降低线上 prompt 敏感性。

  - 稳定性分数被归一化后只用于削减不稳定 token 的 advantage，不给稳定 token 额外奖励，避免 reward hacking；实际调优时可沿用这一设计，把稳定性作为正则化/掩码信号而非正奖励。

  - 主要实验在数学推理，业务迁移需自行验证；但对需要强泛化、且 reward 容易受 prompt 表面特征影响的 LLM Agent 训练，SCAPO 提供了一种轻量的
  token 级 credit 修正思路。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：RLVR 显著提升 LLM 推理能力，但模型预测仍对任务无关 prompt 特征敏感；GRPO 将 outcome 级 advantage 同等地分配给所有 response token，可能同时强化有用推理与伪相关依赖。

方法关键点：作者通过保留问题与答案的半事实干预，发现 token 级敏感性差异很大；仅解码时抑制高 drift token 候选即可在不更新权重下提升推理准确率。据此提出 SCAPO：在 GRPO 中测量固定响应在半事实干预下的 token 概率漂移，将稳定性分数归一化后，在训练早期对相对不稳定 token 降低 advantage；同时不给稳定性本身额外奖励。

关键结果：在 Qwen3-4B-Base 与 Qwen3-1.7B-Base 上，AIME 2024–2026 准确率分别比 GRPO 高 5.63 和 4.17 个百分点；两个模型规模下，SCAPO 在大多数数学基准及所有 OOD 基准上均优于对比方法。
