---
title: 'Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context
  Reasoning'
title_zh: 组校准在线策略蒸馏用于长上下文推理
authors:
- Zhu Zhang
- Jixun Wang
- Xiaoang Xu
- Xiaorong Wang
- Zihan Zhou
- Zhiyuan Wang
- Shuo Wang
- Chaojun Xiao
- Yuezhi Zhou
affiliations:
- Tsinghua University
- Beijing University of Posts and Telecommunications
- OpenBMB
arxiv_id: '2608.19181'
url: https://arxiv.org/abs/2608.19181
pdf_url: https://arxiv.org/pdf/2608.19181
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 知识蒸馏 · 长上下文推理
tags:
- On-policy distillation
- Long-context reasoning
- Verifier reward
- Credit assignment
- LLM post-training
one_liner: 将 verifier 奖励与 OPD 分数做组内归一化并构造有符号残差，用相对优势分配回 token，提升长上下文蒸馏效果
practical_value: '- 在业务中做 LLM 蒸馏或 RLVR 时，若同时有 dense token 监督和稀疏 verifier 奖励（如点击、转化、人工评分），可借鉴
  group 内归一化再相减的方式，避免两种信号尺度差异和 sign 错位。

  - RACA 的相对优势信用分配适合多步交互场景，例如购物 Agent 的多轮工具调用、对话式推荐的 multi-turn 轨迹，可将最终奖励按 token 优势权重回传，比均匀分配更稳定。

  - 不丢弃 dense 教师似然、只做组校准残差微调的思路可复用到生成式推荐或 RAG 后训练：保留 Next Token 监督，同时注入结果导向的 verifier
  信号。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：长上下文任务中，on-policy distillation 的 token 级教师似然可能奖励局部合理但忽略全局证据的响应，与 verifier 的 response-level 奖励产生分歧。文中在长上下文证据聚合任务上观察到：输入更长时，trajectory-level OPD 分数与 verifier reward 的错位加剧。

方法：GC-OPD 在每个 rollout group 内分别对 verifier reward 和 trajectory-level OPD score 做归一化，用差值构造 signed teacher–verifier disagreement residual；RACA 再按各 token 的相对 OPD advantage 把该 residual 分配到 token 上，同时保留原始 OPD 信号。

关键结果：在五个长上下文基准上，Qwen3-4B 平均值从 29.08 提升到 40.47，Qwen3-8B 从 35.12 提升到 44.65；vanilla OPD 为 39.31 和 43.56。消融显示 signed residual 优于额外 OPD 项或直接加组归一化 verifier reward，RACA 优于均匀 token 分配。
