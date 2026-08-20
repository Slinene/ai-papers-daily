---
title: 'Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy
  Distillation'
title_zh: Open-MOPD：诊断并修复多教师在线蒸馏中的能力失衡
authors:
- Huan-ang Gao
- Haohan Chi
- Yong Yan
- Shiyuan Feng
- Hanlin Wu
- Zheng Jiang
- Bingxiang He
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
affiliations:
- SIA-Lab of Tsinghua AIR and ByteDance Seed
- Institute for AI Industry Research (AIR), Tsinghua University
- Department of Computer Science and Technology, Tsinghua University
arxiv_id: '2608.19098'
url: https://arxiv.org/abs/2608.19098
pdf_url: https://arxiv.org/pdf/2608.19098
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 多教师在线蒸馏 · 优化预算平衡
tags:
- Multi-Teacher Distillation
- On-Policy Distillation
- RLHF
- Capability Integration
- Token Budget Balancing
- Open-Source Recipe
one_liner: 提出 token-share balancing、gap-aware 分配与 reward refresh 三种机制，将多教师在线蒸馏能力集成恢复率从
  35.6% 提升到 83.4%
practical_value: '- 多任务/多领域训练时不要只看 prompt/sample 比例，要统计 token-level 梯度贡献。短输出任务（如 query
  推荐、push 文案）即使 prompt 占比合理，梯度 token 占比可能极低（论文中 IF 占 20.3% prompt 但仅 0.99% 梯度 token）。可借鉴
  token-share balancing，按目标 token share 加权 loss，避免单纯过采样挤压长序列任务的 prompt 多样性。

  - 动态预算分配：在多目标 RL 或蒸馏中，根据每个 domain 当前 teacher-student gap（或 reward magnitude）动态调整
  loss weight，优先分配给 gap 大的任务，并对权重做 clip 防止正反馈发散。推荐系统多任务（CTR/CVR/时长）可监控各任务 reward 幅度变化，设计类似
  gap-following allocation 的机制，避免训练后期预算被已收敛任务吸走。

  - reward refresh 在 rollout 复用 + 多步 inner update 的工程设置下，用当前策略重算 student-dependent
  项（如 log-prob），缓存 teacher 输出，几乎无额外开销，可减少 off-policy 陈旧性。适合大规模 RL/蒸馏 pipeline，特别是对
  latency 敏感的多智能体/多能力整合训练。

  - 进行多专家能力合并前，先构建 oracle routing 测试床隔离路由误差，量化每个 domain 的 recovered headroom，定位训练中最早停滞、恢复率最低的任务，再有针对性地调整优化预算。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：多教师在线蒸馏（M-OPD）是整合多个领域 RL 专家到单一通用学生模型的范式，但为何多个专家能力不能无损合并、缺少开源可复现配方。论文构建 oracle routing 受控实验，排除路由误差，量化能力集成 gap。

方法关键点：
- 基于 SmolLM3-3B-Base，三阶段：混合域 SFT → 独立训练 math/code/IF 三个 RL 教师 → 多教师 OPD。学生从同一 SFT 初始化，教师按 domain label 硬路由，dense per-token reward 使用 top-k 学生分布。
- 诊断发现：IF 占 20.3% prompt 但只有 0.99% gradient tokens（长度 409 vs math/code ~10,500）；token-level 教师冲突很小（均值 0.126 nat，>1 nat 仅 0.62%），干预冲突反而掉点；主因是优化预算错配：token 份额不均、不同 domain 收敛速度不同导致 reward 幅度收缩不一致、rollout 重用导致 reward 陈旧。
- 提出三种机制：token-share balancing，按目标 token 份额 g⋆d/stokd 加权；gap-following allocation，用当前 reward 幅度 md 与跨域均值比值的 clip 因子动态调整预算，分配给 gap 更大的 domain；reward refresh，在每个 inner update 重算 student-dependent log-probs，复用缓存的 teacher log-probs。

关键实验：
- 评估：math AIME24/25 mean@64，code LCBv5/v6 mean@10，IF IFEval/IFBtest mean@1，宏观平均。
- Naive M-OPD 总 28.05，恢复率（相对 RouteRL）仅 35.6%；IF 比 RouteOPD 低 6.16，最早停滞。
- Open-MOPD 总 31.24，恢复率 83.4%，IF 从 43.64 提升到 49.58；全流程可在 8×A100-80GB 复现。
- 消融：token-share balancing +1.17，gap-following +0.72，reward refresh 在 K=4 下再 +0.81，总 +3.19。

最值得记住的一句话：多教师在线蒸馏的能力集成失败主要不是教师 token 冲突，而是 token-level 优化预算在 domain 间严重错配，需按 token 份额、动态 gap 和 reward 新鲜度三个维度联合治理。
