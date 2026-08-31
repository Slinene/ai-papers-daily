---
title: 'J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data'
title_zh: J-Zero：从零数据实现 Challenger-Solver-Judge 统一协同进化
authors:
- Gyouk Chu
- Myeongho Jeon
- Eunho Yang
affiliations:
- KAIST
arxiv_id: '2608.26582'
url: https://arxiv.org/abs/2608.26582
pdf_url: https://arxiv.org/pdf/2608.26582
published: '2026-08-26'
collected: '2026-08-31'
category: Training
direction: 自进化 LLM 训练 · 多角色对抗协同
tags:
- self-evolving LLM
- adversarial self-play
- Challenger-Solver-Judge
- zero data
- co-evolution
- judge co-adaptation
one_liner: 提出 J-Zero 统一 Challenger-Solver-Judge 协同进化框架，以对抗自对弈和已知偏好对在可验证/不可验证域持续提升
  LLM
practical_value: '- 使用 Challenger 生成越来越难的用户 query/场景，Solver 学习响应，可构建推荐/搜索 Agent 的难例生成器，提升对长尾
  query 和对抗性输入的鲁棒性，无需额外人工标注。

  - Judge/Reward Model 训练用「生成结构保证偏序」的合成偏好对（如多步检索-重组答案 > 单步答案）替代自评或人工打分，减少 reward hacking
  和噪声；推荐系统的 LLM 评估器可复用此思路。

  - 零数据自进化闭环可迁移到电商冷启动或新品类：两个角色互相出题与作答，自动生成微调数据，缓解冷启动样本不足。

  - 同时进化多个角色（Challenger/Solver/Judge）比单角色自训练更稳定，持续 10 轮不退化；在线推荐 Agent 持续优化时可借鉴此三模块协同更新机制。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：自进化 LLM 可减少人类监督，但在不可验证的开放生成领域缺少可靠学习信号；可验证领域已有自博弈方法，难以直接迁移。

方法关键点：J-Zero 从零数据同时进化三个角色。Challenger 生成越来越难的任务，Solver 学习更高质响应，形成对抗闭环。Judge 不靠自身评分训练，而用偏好对：Solver 答案优于 Challenger 答案，Solver 分解-重组答案优于一次性答案，其顺序由生成过程事先保证。这样 Judge 能适配新难度，避免评分偏差和奖励黑客。

关键结果：在可验证领域平均超过基线 4.2 分，不可验证领域平均超过 8.0 分；至少持续改进 10 轮，基线在 2 轮后即退化。说明多角色协同进化在两类领域均稳定有效。
