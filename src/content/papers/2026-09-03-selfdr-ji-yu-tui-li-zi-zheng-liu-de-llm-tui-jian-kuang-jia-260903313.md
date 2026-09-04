---
title: 'SelfDR: Self-Distillation from Reasoning for LLM-Based Recommendation'
title_zh: SelfDR：基于推理自蒸馏的 LLM 推荐框架
authors:
- Chumeng Jiang
- Jiayin Wang
- Xinjie Lin
- Zhiqiang Guo
- Hengliang Luo
- Min Zhang
affiliations:
- Tsinghua University
- Quan Cheng Laboratory
- Meituan
arxiv_id: '2609.03313'
url: https://arxiv.org/abs/2609.03313
pdf_url: https://arxiv.org/pdf/2609.03313
published: '2026-09-03'
collected: '2026-09-04'
category: RecSys
direction: LLM 推荐 · 自蒸馏推理增强
tags:
- LLM4Rec
- Self-Distillation
- Reasoning
- Reranking
- Dynamic Weighting
- Inference Efficiency
one_liner: 用推荐性能为 reward 训练 reasoner，再通过动态加权自蒸馏将推理增强迁移到直接推荐模型，在线推理零额外开销
practical_value: '- 在线延迟敏感场景可直接复用：训练时用 GRPO 以推荐命中率为 reward 训练一个 reasoner 生成用户偏好解释，将解释拼入
  teacher 输入得到更强排序分布；在线部署 student 直接输出候选 ID，不产生额外推理 token，实测推理时间与普通 SFT 模型相同。

  - 动态蒸馏权重公式值得借鉴：根据 teacher 对正样本的排序位置、teacher 与 student 的 rank 差动态调整蒸馏 loss 权重，teacher
  排序差时大幅降权，避免从噪声中学习；超参 β≈0.1、温度系数 1~2 较稳。

  - 蒸馏损失用 reverse KL 而非 forward KL，让 student 分布集中到 teacher 高概率区域，适合候选 ID 排序场景（候选集有限，需要聚焦
  top 候选）。

  - 训练 reasoner 时对 rationale 做细粒度 mask（连续 3 个词与 item 标题重叠则 mask），防止信息泄露，提升 rationale
  质量；此策略可迁移到任何用生成解释辅助推荐的 pipeline。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 推荐中引入显式推理能提升效果，但多步推理或先生成 reasoning trace 再预测的范式在线推理开销大，难以满足真实推荐系统低延迟要求。如何在不牺牲推理效率的前提下利用 LLM 的推理能力，是本文要解决的核心问题。

## 方法关键点
- 整体框架：SelfDR 由同一个 LLaMA-3.1-8B 基座模型组成，包含 reasoner、teacher recommender、student recommender 三个角色。
- Reasoner 训练：用 GRPO 强化学习，以最终推荐准确率（HitRate）为 reward，训练 reasoner 根据用户历史和 ground-truth item 生成针对性的 rationale；生成时 prompt 禁止直接复述输入文本，并对 rationale 中与 item 标题连续重叠≥3 词的片段进行 mask，防止信息泄漏。
- Teacher 构造：将训练好的 reasoner 生成的 rationale 拼接进推荐输入，得到 reason-enhanced teacher，其排序分布作为蒸馏信号。
- Self-Distillation：student 直接基于用户历史与候选集输出 item 标识符，不接收 rationale。蒸馏时对齐 teacher 与 student 在候选 ID 上的 logits，采用 reverse KL 散度；同时结合 ground-truth 的交叉熵损失，并用动态权重 α 调节两者比例。
- 动态权重：α 由 teacher 对正样本的 rank 与阈值 k 的距离、teacher 与 student 的 rank 差共同决定，teacher 表现差于 student 时施加惩罚 β 大幅降低教师信号权重。

## 关键结果
在 Clothing、Home、ML1M 三个数据集上，以 SASRec 生成 top-20 候选做重排序，SelfDR 在 HitRate 和 NDCG@3/5 上全面超越所有 baseline。Clothing 上 HR@1 为 0.0132，比最强 baseline 提升约 15%；ML1M 上 HR@1 达 0.0845，远超 COT4Rec 的 0.0717。训练出的 reasoner 在 teacher 性能和下游蒸馏效果上均优于 GPT-4o-mini、Claude-3-Haiku、DeepSeek-V3 等外部大模型。在线推理时输出 token 数仅 1（候选 ID），推理时间与无推理的 SOFT 持平（109.46ms），大幅低于所有 reasoning-based 方法。

**最值得记住的一句话**：把推理能力蒸馏进直接推荐模型，训练时用 RL+推荐 reward 生成针对性 rationale，推理时零额外开销，效果超过外部大模型监督。
