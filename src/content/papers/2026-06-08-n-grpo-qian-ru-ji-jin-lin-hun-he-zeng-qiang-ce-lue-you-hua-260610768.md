---
title: 'N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization'
title_zh: N-GRPO：嵌入级近邻混合增强策略优化
authors:
- Xukun Zhu
- Hang Yu
- Peng Di
- Linchao Zhu
affiliations:
- Zhejiang University
- Ant Group
arxiv_id: '2606.10768'
url: https://arxiv.org/abs/2606.10768
pdf_url: https://arxiv.org/pdf/2606.10768
published: '2026-06-08'
collected: '2026-06-13'
category: Training
direction: LLM 训练 · 策略优化 · 探索增强
tags:
- GRPO
- Policy Optimization
- Exploration
- Embedding Mixing
- Mathematical Reasoning
- LLM Training
one_liner: 通过语义近邻混合同一 token 的嵌入，在 GRPO 中注入多样性且保持语义一致，提升数学推理
practical_value: '- **RL 训练中的探索策略**：在 LLM 微调（如推荐理由生成、对话策略、Agent 行动规划）时，使用语义近邻混合替代
  token 级采样或随机噪声，可生成更多样但语义连贯的轨迹，缓解模式坍塌。

  - **嵌入级扰动技巧**：直接操作 token 嵌入而非离散 token，通过 k 近邻插值在连续空间内注入多样性，可迁移至生成式推荐中 Semantic ID
  解码时的探索，或对话系统中多样性回复生成。

  - **训练稳定性与效率**：该方法避免了完全随机的嵌入扰动带来的语义崩溃，训练过程更稳定；工程实现上需预先构建语义近邻索引（如使用 FAISS），推理阶段可快速查表。

  - **泛化能力**：在分布外任务上也有效，适合电商场景中多变的商品描述和 query 改写，可作为后训练探索的即插即用模块。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：GRPO 在数学推理上的成功依赖 rollout 阶段的多样有效探索，但现有方法存在权衡：token 级采样产生仅措辞不同的冗余轨迹，嵌入级随机噪声易破坏语义一致性。

**方法**：提出 N-GRPO，一种融入 GRPO 的探索策略。核心是语义近邻混合——在生成轨迹时，对锚点 token，动态选取其嵌入空间内的 k 个最近邻，通过线性混合构造新输入表示。这既引入多样性，又将探索约束在局部语义流形内，保持连贯性。N-GRPO 可无缝替换原有采样步骤，不影响整体 RL 流程。

**结果**：在 DeepSeek-R1-Distill-Qwen（1.5B 与 7B）的数学推理基准（MATH、GSM8K 等）上，N-GRPO 一致超越 token 级采样和随机噪声等基线，且在两份分布外任务（如 OOD 对话基准）上展现强泛化。消融分析验证了近邻混合的有效性。
