---
title: 'RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative
  Decoding'
title_zh: RheoSampling：解决随机动态树投机解码中的独热困境
authors:
- Qiao Hu
- Yepeng Weng
- Bo Zhang
- Takehisa Yairi
affiliations:
- National Center for Mathematics and Interdisciplinary Sciences (NCMIS), AMSS, CAS
- The University of Tokyo
- Lenovo AI Technology Center
- SKLMS and AMSS, Chinese Academy of Sciences
- School of Mathematical Sciences, University of Chinese Academy of Sciences
arxiv_id: '2609.21827'
url: https://arxiv.org/abs/2609.21827
pdf_url: https://arxiv.org/pdf/2609.21827
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM 投机解码推理加速
tags:
- speculative decoding
- dynamic tree
- stochastic sampling
- lossless acceleration
- LLM inference
one_liner: 通过解耦动态树构建与验证概率，首次实现上下文感知 top-K 动态树与随机采样兼得的无损投机解码
practical_value: '- 线上 LLM 服务若采用投机解码加速，在 temperature>0 的生成式推荐/文案/对话场景，现有动态树方法会退化为
  one-hot，导致接受率下降；RheoSampling 可作为随机采样下保持加速的参考实现，直接替换 EAGLE-3 等动态树 draft 策略。

  - 其“构建概率”与“验证概率”解耦思路可迁移到其他需要在同一分布上同时做结构选择与质量评估的系统（如束搜索、MCTS 或推荐候选树生成），避免结构选择吃掉采样多样性。

  - OT-based verification 和 sparse draft 机制对工程实现有借鉴：验证阶段用最优传输分配概率，稀疏 draft 减少无效分支，可降低延迟同时保持无损。

  - 对于需要平衡多样性与效率的 Agent 多步推理/工具调用生成，该框架提供的等价类分析可作为分析随机树结构的新模板，帮助设计可证明无损的随机搜索策略。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：投机解码中动态树方法如 EAGLE-3 在 greedy 下表现好，但 stochastic decoding (T>0) 时确定性 top-K expansion 与 global pruning 使草稿分布 collapsed to one-hot，接受率严重下降。根本原因是同一概率分布被用于两个冲突任务：树构建与 token 验证。

**方法关键点**：RheoSampling 解耦这两个角色，对从草稿分布采样的 token 赋予 proxy probability 用于树扩展/剪枝，同时保留其真实采样概率用于验证。即在 deterministic top-K slots 中注入一个采样 token，并在构建与验证时使用不同概率处理。首次实现动态树方法同时具备上下文感知 top-K 构建和随机采样，且保持无损。通过 equivalence-class analysis 压缩随机树空间到可处理类建立无损保证；采用 OT-based verification 和 sparse draft 机制将理论增益转化为实际效率。

**关键结果**：在多个 LLM 和基准上，接受率与加速比均优于 SOTA 动态树方法（摘要未给具体数字）。该框架还可能为分析其他随机树结构提供模板。
