---
title: 'Recursive State-Augmented Language Models: Persistent Latent-State Adaptation
  of Pretrained Language Models'
title_zh: 递归状态增强语言模型：持久潜在状态自适应预训练 LM
authors:
- Omer Haq
affiliations:
- Independent Researcher
arxiv_id: '2611.16375'
url: https://arxiv.org/abs/2611.16375
pdf_url: https://arxiv.org/pdf/2611.16375
published: '2026-11-12'
collected: '2026-11-15'
category: LLM
direction: LLM 长期记忆 · 递归状态适应
tags:
- latent state
- LoRA
- recurrent memory
- LLM adaptation
- context compression
one_liner: 用持久潜在状态生成预训练 LM 的自适应，在移除早期上下文后仍支持序列推理
practical_value: '可借鉴点：

  - 长对话 Agent/推荐助手可维护低维 latent state（如 64-d）代替全量历史 token，通过 read-transition-write
  模块压缩历史，避免 KV cache 无限增长；状态用于门控 LoRA，动态调整 frozen LLM 推理。

  - 模块化拆分观测编码、状态转移、预测器适配，便于在已有 LLM 上增量训练和部署；只更新 LoRA 和状态模块，基座冻结。

  - 四轮任务中 latent-gated LoRA 达到 89.1% 准确率，接近全上下文 LoRA 88.0%，说明轻量状态在特定任务可替代显式上下文；但未见
  codeword 生成弱，更适合 ranking/匹配而非精确生成。

  - 对电商跨 session 用户建模：将长期偏好压缩为 latent state，生成式推荐时通过门控 LoRA 调整模型，无需把全部历史 token 输入生成器。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：自回归语言模型受限于有限 token 上下文，长交互保留历史会增加注意力成本和 KV cache，截断可能丢失后续预测所需证据。

**方法关键点**：提出 Recursive SALM，用持久潜在状态随观测更新，并生成对预训练 LM 的自适应。采用模块化 read–transition–write 架构，分离观测编码、潜在动态和预测器适配；状态可生成软提示、调制中间特征或门控低秩更新。实验用冻结 GPT-2 small，排除早期证据从 decoder context，只通过 64 维状态传递。

**关键结果**：四轮假设推理任务中，latent-gated LoRA 达到 89.1% 准确率，与训练的全上下文 LoRA 基线 88.0% 相当；置零或打乱状态大幅降低准确率。二轮未见 codeword 任务中，几种接口候选排序超过随机，但很少生成确切 codeword。结果表明持久潜在条件自适应可在早期证据不在 decoder context 时支持序列推理。
