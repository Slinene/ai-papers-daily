---
title: 'EPIC: Rethinking Trust Regions for Autoregressive LLM Policies via Exact-KL
  Prefix Importance-Ratio Clipping'
title_zh: EPIC：基于精确 KL 前缀重要性比率裁剪的 LLM 策略优化
authors:
- Chengxi Li
- Hanlin Wu
- Zhicheng Cai
- Huan-ang Gao
- Wei-Ying Ma
- Jingjing Liu
- Hao Zhou
affiliations:
- Tsinghua AIR
- ByteDance Seed
- Tsinghua University
arxiv_id: '2610.29999'
url: https://arxiv.org/abs/2610.29999
pdf_url: https://arxiv.org/pdf/2610.29999
published: '2026-10-21'
collected: '2026-10-22'
category: Training
direction: LLM 强化学习 · 前缀级信任域裁剪
tags:
- PPO
- RLHF
- LLM
- MoE
- Trust Region
- Off-Policy
one_liner: 提出前缀累积似然比作为精确重要性权重，用 r-1-log r 坐标构建校准裁剪目标，稳定离线 MoE RL 训练
practical_value: '- 电商/Agent 场景若用 RL 微调 LLM 生成商品文案、对话策略或搜索词，常面临异步 rollout 与离线策略偏移，可借鉴前缀级重要性比率裁剪：它比
  token 级 GRPO 更能感知前缀累积漂移，又比序列级 GSPO 保留早期位置信号。

  - 在 MoE 架构的 LLM 训练中，EPIC 无需存储专家路由索引即可稳定训练，大幅降低 driver 进程内存（对比 R2/R3 降 77.5%/93.0%），适合资源受限的大规模部署。

  - 实现上只需对现有 PPO/GRPO 损失做轻量改造：累计 log ratio 得到前缀比率，按校准边界裁剪，无额外模型或 replay，可直接嵌入 verl
  等框架。

  - 信任域边界采用精确 reverse-KL 坐标和几何均值行为概率校准，比固定 clip 范围更适应长尾响应，对长序列生成任务（如多轮 Agent 交互、长文案生成）的
  RL 调优有参考价值。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
现代 LLM RL 流程中，异步 rollout 与 MoE 推理/训练路由不一致带来离线策略分布偏移，PPO 级裁剪是常用稳定手段。但 token 级 GRPO 只看当前 token 条件概率，忽略前缀由策略自身生成造成的累积漂移；序列级 GSPO 又对整条响应共享一个比率，容易抑制早期前缀的有效信号。EPIC 从 TRPO 单调改进原理出发，为自回归生成构造前缀级信任域。

**方法关键点**  
- 将自回归生成建模为有限 horizon MDP，推导出性能差分恒等式：Jx(π)−Jx(µ)=E_{y∼µ}[Σ_t rpre_t Aµ(s_t,a_t)]，其中 rpre_t 为前缀累积似然比，是每个 stepwise improvement term 的精确重要性权重。  
- 基于 TRPO 单调改进，用前缀分布 KL 作为信任域；引入精确 reverse-KL 坐标 φ(r)=r−1−log r，其在行为策略下的期望恰好等于前缀 KL。  
- 对每个位置设定 KL budget，结合几何均值行为概率校准，解出非对称 ratio 边界 ℓ、u；使用几何平均比率 g_i,t=(rpre)^{1/t} 缓解长度导致的梯度尖峰，并通过 straight-through 让梯度只经过当前 token。  
- 整个计算只需对已有 log-prob 做累积和，无需额外模型、路由 replay 或二次近似。

**关键实验**  
在 Qwen3-30B-A3B-Base（稀疏 MoE）上用 DAPO-Math-17K 训练，四个数学推理基准（AIME 2024/2025、AMC 2023、HMMT 2025）评估。EPIC 四基准平均 39.34%，比 GRPO 高 10.69 个百分点，比 GSPO 高 6.50 个百分点；相对 routing replay（R2/R3）性能有竞争性，而 driver 进程内存降低 77.5% 和 93.0%。

**最值得记住的一句话**  
前缀累积似然比才是离线 LLM RL 中正确的 change-of-measure 因子，通过精确 reverse-KL 坐标校准，可以在不牺牲早期信号的前提下稳定大规模 MoE 训练。
