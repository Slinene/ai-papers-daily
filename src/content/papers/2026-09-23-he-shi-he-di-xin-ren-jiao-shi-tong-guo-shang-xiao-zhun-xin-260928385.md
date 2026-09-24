---
title: 'When and Where to Trust the Teacher: Unifying On-Policy Distillation and GRPO
  through Entropy-Calibrated Credit Assignment'
title_zh: 何时何地信任教师：通过熵校准信用分配统一在线蒸馏与 GRPO
authors:
- Jie Zhang
- Jingxiao Yang
- Zhehao Huang
- Yuhang Liu
- Xiaolin Huang
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
arxiv_id: '2609.28385'
url: https://arxiv.org/abs/2609.28385
pdf_url: https://arxiv.org/pdf/2609.28385
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: RLVR 与在线蒸馏统一训练
tags:
- GRPO
- On-Policy Distillation
- RLVR
- Entropy Calibration
- Token Credit Assignment
- LLM Training
one_liner: 提出 UECR-GRPO，在 GRPO 更新中统一 verifier 与 teacher 信号，通过熵校准 token 级信用重分配提升数学推理
  RLVR
practical_value: '- 在电商/Agent 场景用 RLVR 训练 LLM 时（如最终成交、点击、任务完成作为 verifier），可以引入一个 teacher
  LLM 的 log-prob 作为稠密信号；关键是把 teacher 信号和 verifier reward 在 group normalization 与 PPO
  clipping 之前合并，让 teacher 证据影响 response 排序，而不是事后加权。

  - Token 级信用重分配用 response-wise zero-sum projection 保留每个 response 的总任务信用和符号，可借鉴到商品标题生成、对话推荐理由生成等任务：只改变
  token 间梯度分配，不改总 reward，降低训练不稳定。

  - 全词表 teacher entropy 衰减不确定指导：当 teacher 模型对某些 token 输出很平、熵高时，降低其蒸馏权重；适合电商文本生成中 LLM
  teacher 噪声大的场景，避免传播错误偏好。

  - On-policy 实现中使用 length-normalized teacher score，可避免长文本 recommendation/agent 轨迹中获得更高
  teacher score 的长度偏差。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：RLVR 只用最终答案正确性做监督，token 级信号稀疏；在线蒸馏 OPD 能提供稠密反馈，但 teacher 偏好不一定等于正确性。已有混合方法通常在 verifier-based group normalization 之后才引入 teacher 信号，且 token 重加权不保留每个 response 的总任务信用，影响训练稳定。

方法关键点：UECR-GRPO 在单个 GRPO 更新里同时整合 verifier 和 teacher。Path-Utility Unification (PUU) 将 verifier reward 与 teacher-to-anchor path log-ratio 合并进 KL 正则目标；on-policy 实现用 length-normalized teacher score，并把两类 reward 在 group normalization 和 PPO clipping 之前合并，使 teacher 证据参与 response 排名。Entropy-Calibrated Redistribution (ECR) 用 signed teacher–old-policy token gap 重分配 verifier 分量；全词表 teacher entropy 衰减不确定指导，response-wise zero-sum projection 保持总任务信用和 token 符号。

关键结果：五个数学推理基准上，Qwen3-1.7B 与 Qwen3-4B 的学生 Avg@12 准确率分别达 17.21% 和 65.09%，比最强 baseline 分别高 0.89 和 0.56 个百分点。
