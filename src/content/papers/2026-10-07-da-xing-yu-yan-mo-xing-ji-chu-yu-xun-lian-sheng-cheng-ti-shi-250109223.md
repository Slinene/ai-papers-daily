---
title: Foundations of Large Language Models
title_zh: 大型语言模型基础：预训练、生成、提示、对齐与推理
authors:
- Tong Xiao
- Jingbo Zhu
affiliations:
- Northeastern University
- NiuTrans Research
arxiv_id: '2501.09223'
url: https://arxiv.org/abs/2501.09223
pdf_url: https://arxiv.org/pdf/2501.09223
published: '2026-10-07'
collected: '2026-10-09'
category: LLM
direction: LLM 基础理论与技术体系
tags:
- LLM
- pre-training
- prompting
- alignment
- inference
- reasoning
one_liner: 系统梳理LLM预训练、生成建模、提示、对齐、推断与推理六大基础主题的技术参考书
practical_value: '- 对齐章节可指导生成式推荐中的偏好优化：将点击/转化作为偏好信号，用 RLHF/DPO 类方法微调 LLM，避免纯 SFT 导致推荐结果多样性差。

  - 推理章节中 CoT/self-consistency 可迁移到电商 Agent 的查询理解与任务规划：对复杂购物意图引入结构化推理轨迹，提升 query 拆解与商品召回准确率。

  - 预训练与生成模型基础解释了 Semantic ID 建模本质：把 item 表示成 token 序列并用 LLM 生成 next token，可复用书中的解码策略（温度、top-k/top-p）和训练技巧。

  - 工程部署时可参考推理章节的 KV cache、批处理与量化基础，对线上低延迟生成式推荐与导购 Agent 有直接帮助。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM 已成为通用 AI 基础范式，但缺少面向学生与从业者、系统讲解基础概念而非追逐前沿的参考书。

### 方法关键点
全书分六章：
1. **预训练**：介绍大规模语言建模目标、常见模型架构与预训练方法；
2. **生成模型**：阐述当前 LLM 的构建流程，从语言模型到生成式模型；
3. **提示**：覆盖 prompting、上下文学习等核心范式；
4. **对齐**：介绍 RLHF/DPO 等使模型与人类偏好对齐的技术；
5. **推理**：讲解解码、KV cache 等高效推理方法；
6. **推理**：探讨思维链等复杂推理能力。

### 关键结果数字
无实验数字，作为教材提供系统框架；六个章节对应从预训练到推理的完整技术栈。
