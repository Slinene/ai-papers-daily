---
title: 'User as Engram: Internalizing Per-User Memory as Local Parametric Edits'
title_zh: 用户作为印迹：将每用户记忆内化为局部参数编辑
authors:
- Bojie Li
affiliations:
- Pine AI
arxiv_id: '2606.19172'
url: https://arxiv.org/abs/2606.19172
pdf_url: https://arxiv.org/pdf/2606.19172
published: '2026-06-17'
collected: '2026-06-18'
category: LLM
direction: 用户事实的局部参数编辑与共享推理
tags:
- Engram
- Memory Edit
- Personalization
- LoRA
- Retrieval
- LLM
one_liner: 把用户事实稀疏写入 Engram 的哈希记忆表，推理技能由共享适配器承载，实现高精度个性化且不干扰推理
practical_value: '- 可将用户长期偏好（商品偏好、搜索历史等）压缩为 Engram 行编辑写入模型，免去每次推理时检索或 prompt 拼接的延迟与
  token 成本。

  - 共享推理适配器 + 多用户稀疏编辑的架构支持高并发个性化推理，适合电商搜索推荐等需实时读取用户记忆的场景。

  - 编辑透明可控：写入的事实只影响特定触发词，不污染其他主题回答，有利于金融、医药等高合规领域的推荐安全性。

  - 多用户编辑可叠加存储于同一模型，无需维护独立 LoRA 权重，大幅降低部署成本，工程实现更友好。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：个性化记忆包含“内容”（用户特定事实）与“推理技能”（使用事实的能力）。现有方法要么将事实存于外部检索，要么用 per-user LoRA 将两者混合写入权重，导致推理污染、多用户无法共存。大脑将 episodic 记忆（海马体局部印迹）与皮层技能分离，本文受此启发，旨在将用户事实以稀疏、局部的方式参数化，避免推理衰退。

**方法**：提出 User as Engram。使用 Engram 模型的哈希键控记忆表，将每个用户的事实编辑成表中稀疏的若干行，这些行仅在相关 trigger 时才被激活，其余位置保持原状。推理技能则由一个共享适配器承载，独立于用户内容。编辑可组合：不同用户的事实散列到不同槽位，可无损叠加于同一张表。

**结果**：直接召回准确率与 per-user LoRA 持平；间接推理准确率平均高 5.6 倍，且从未使任何用户推理变差。内存占用约为 LoRA 的 1/33000。在事实数约超 100 条时，查询速度超越 2.5 倍参数量的检索流水线模型。
