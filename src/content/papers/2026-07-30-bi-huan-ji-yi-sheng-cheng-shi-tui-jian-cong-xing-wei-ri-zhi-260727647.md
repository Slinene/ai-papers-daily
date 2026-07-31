---
title: 'LoopMemGR: From Behavior Logs to Evolving Memory for Generative Recommendation'
title_zh: 闭环记忆生成式推荐：从行为日志到演化推荐体验
authors:
- Hui Qian
- Changfa Wu
- Chang Liu
- Binbin Cao
- Jian Wu
- Yuliang Yan
- Han Zhu
- Bo Zheng
affiliations:
- Alibaba Group
arxiv_id: '2607.27647'
url: https://arxiv.org/abs/2607.27647
pdf_url: https://arxiv.org/pdf/2607.27647
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · 闭环经验记忆
tags:
- Generative Recommendation
- Experience Memory
- Semantic ID
- Closed-Loop
- Multi-View Attention
- Industrial Recommendation
one_liner: 首次将系统侧推荐决策轨迹建模为可跨请求复用的经验内存，提出三视图压缩读写机制，在工业级数据上显著提升生成式推荐效果
practical_value: '- **闭环经验日志设计思路**：在生成式推荐/对话Agent中，可将系统侧决策与反馈路径（推荐了什么、用户是否互动）作为「经验日志」持久化，形成
  **behavior log + experience log 双轨记忆**，避免每次请求仅从行为历史重建偏好。

  - **三视图固定预算压缩**：当交互历史过长无法全量送入模型时，可借鉴「最近记录锚定+频次模式+全局可迁移原型」三叉融合方式，用 **固定数量 tokens（如
  16 个）** 概括经验，既控制计算成本又保留关键信息。

  - **读取算子设计**：归一化键值注意力 + 门控+幅度上限（Cap），可有效避免长日志覆盖原始查询，适合在电商实时推理中稳定注入记忆。

  - **工程部署模式**：经验写入仅静态追加，读取时只扫最近 N 条，梯度不反向传播写入操作，保持因果顺序，适合在线系统低延迟更新。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
当前生成式推荐多采用 history-as-context 范式，仅利用用户行为历史建模，而系统侧每次的推荐决策及后续反馈在请求后被丢弃，形成非对称记忆：系统只记得用户做了什么，却不记得自己推荐过什么、从反馈中学到了什么。这导致推荐可能重复已尝试方向、忽视负反馈信号，也无法利用跨请求的探索经验。

## 方法
LoopMemGR 提出闭环推荐经验记忆框架，核心是维护与用户行为日志并行的推荐经验日志，记录每次请求的推荐结果。对每个新请求，使用 Tri-View Memory Reader (TVMR) 从经验日志中提取固定数量（如 16 个）的 experience tokens：
- **Recency view**：保留最近去重后的推荐条目，并以此作为锚点读取更早的经验。
- **Frequency view**：统计类别级推荐频次，关注反复推荐的品类模式。
- **Global view**：用跨用户共享的可学习查询，提取可迁移的群体规律。
三个视图的门控融合将信息压缩到固定 token 预算，再与行为历史串联输入生成式骨干（基于 RankGR/Qwen2.5-0.5B）。每次请求后，推荐结果经静态摘要模块追加回经验日志，形成“读取-推荐-反思-写入”闭环，且严格保持时序因果，未来信息不泄漏。

## 关键结果
在工业 Taobao 数据集（21 亿用户、270 亿商品、260 亿交互）上评测。LoopMemGR 相比最强基线 RankGR，在 Click HR@100 上从 25.30% 提升至 39.24%（提升 13.94 个百分点），HR@2000 从 59.28% 提升至 70.85%；PV 目标上同样大幅领先。消融表明，仅保留固定 token 预算的经验记忆即可保留 Raw Experience（全量日志）约 74% 的增益，且 TVMR 显著优于通用的均值池化或长序列读取器。全局查询的双重多样性正则有效避免了注意力坍缩。

> **最值得记住的一句话：把系统过去“推荐了什么、结果如何”变成压缩的经验记忆，能大幅弥补历史行为之外的决策盲区。**
