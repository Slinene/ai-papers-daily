---
title: 'Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context'
title_zh: 窗口化 MTP：消除百万级上下文中的全量草稿 KV 开销
authors:
- Alagappan Valliappan
affiliations:
- NVIDIA
arxiv_id: '2607.21535'
url: https://arxiv.org/abs/2607.21535
pdf_url: https://arxiv.org/pdf/2607.21535
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: 推测解码 · 长上下文 KV 优化
tags:
- speculative decoding
- MTP
- window attention
- long context
- KV cache
- inference optimization
one_liner: 对推测解码草稿头施加窗口注意力，训练免费、无损地将长上下文草稿 KV 读取量降低 99%，推理加速 28–44%
practical_value: '- **在长上下文生成式推荐/Agent 中降低延迟**：当使用 LLM 生成推荐理由或进行多步推理时，若启用 MTP 推测解码，可直接将草稿头的注意力替换为窗口注意力，保留验证阶段全注意力，实现训练免费、无损的推理加速，尤其适合百万
  token 级别的用户行为序列。

  - **工程实现简单，即插即用**：无需重新训练或调整模型结构，仅需在草稿注意力中添加滑动窗口和注意力槽（StreamingLLM 风格），可立即部署到现有 SGLang
  等框架。

  - **释放 GPU 显存用于更大批处理**：窗口化草稿头可丢弃约 99% 的草稿 KV 缓存（实测占总量 7.7–11%），使用紧凑环形缓冲区回收，不影响接受准确率，支持更高的吞吐。

  - **适用于混合注意力目标模型**：当主模型使用混合线性注意力（如 Mamba2-hybrid）时，窗口化草稿头可避免其全注意力读取代价成为瓶颈，保持整体加速效果随上下文变长而放大。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
长上下文的大语言模型在推理时广泛采用内置多令牌预测（MTP）头进行推测解码，默认假设草稿成本极低。但在百万 token 上下文下，草稿头仍需全量 KV 缓存注意力，其读取量随上下文线性增长，甚至让推测解码净收益为负。该问题在混合线性注意力目标模型上更突出：验证阶段已很快，草稿的全注意力读取成为主要瓶颈。

## 方法关键点
提出 Windowed-MTP：仅对草稿头施加固定窗口大小（W）加注意力槽（sink）的滑动窗口注意力，保持验证阶段全注意力完整性。这纯粹是一种推理时的注意力掩码修改，训练免费、即插即用，且严格保证无损——目标模型仍决定所有被接受的 token，窗口化仅影响提议过程。

## 关键结果数字
在 1M 上下文、单 GPU SGLang 下测试三种架构（Qwen GDN-MoE 35B/122B、Mamba2-hybrid NoPE 120B），窗口化 MTP 将每解码步成本（γ 次草稿前向 + 验证）相对原生 MTP 草稿降低 28%–44%，且收益随上下文增长而扩大。端到端延迟改善幅度一致，并在某些负载下因接受长度提升而进一步加速。同时，可安全回收未读取的草稿 KV 缓存（约占总量 7.7–11%），无准确率或输出分布影响。
