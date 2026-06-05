---
title: Latent Reasoning with Normalizing Flows
title_zh: 基于归一化流的潜在推理框架 NF-CoT
authors:
- Guancheng Tu
- Xiangjun Fu
- Suhao Yu
- Yao Tang
- Haoqiang Kang
- Lianhui Qin
- Yizhe Zhang
- Jiatao Gu
affiliations:
- University of Pennsylvania
- UC San Diego
- Meta
arxiv_id: '2606.06447'
url: https://arxiv.org/abs/2606.06447
pdf_url: https://arxiv.org/pdf/2606.06447
published: '2026-06-03'
collected: '2026-06-05'
category: Reasoning
direction: 潜在推理 · 归一化流 · 连续思维
tags:
- Latent Reasoning
- Normalizing Flows
- Chain-of-Thought
- Continuous Thoughts
- LLM
one_liner: 用归一化流建模连续潜在思维，保留自回归生成、精确似然与 KV 缓存，提升代码生成并降低推理成本
practical_value: '- **压缩中间推理，减少 token 开销**：将部分思考步骤表达为紧凑的连续向量而非文本 token，在需要长推理链的任务中可显著降低
  API 调用成本或推理延迟，适合电商客服、推荐解释生成等对延迟和成本敏感的场景。

  - **保留左到右自回归与 KV-cache 兼容性**：NF-CoT 的连续思维嵌入原语言模型的因果流，不影响标准推理加速技术，可直接部署到现有 LLM 推理服务中，无需特殊工程改造。

  - **连续空间概率建模支持策略梯度优化**：提供精确的似然估计，可在连续思维空间上直接进行 RL 微调，为 agent 工具调用推理或推荐策略学习提供更细粒度的优化信号。

  - **连续思维可蒸馏自显式 CoT**：能够将繁琐的文本推理链压缩成连续表示，未来可用于压缩电商中的长对话历史或复杂推荐逻辑，作为高效上下文注入后续生成。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：显式思维链（CoT）通过离散 token 流进行中间推理，虽有效但存在低效、必须逐词串行生成、无法表达局部不确定性等问题。潜在推理用连续状态替代文本 tokens 进行中间计算，但现有方法（如 Coconut、扩散模型）常丢失自回归模型的核心优势：左到右生成、概率采样、KV 缓存兼容性及可追踪似然估计。

**方法**：提出 NF-CoT，将归一化流（TARFlow 式）植入 LLM 主干，从显式 CoT 蒸馏出紧凑连续思维，并定义连续思维的概率模型。连续思考位置由 NF 头生成，文本位置由标准 LM 头生成，全部处于同一因果流中。该设计保留了左到右的解码方式、原生 KV 缓存支持，并提供连续思维的精确似然，支持潜在空间中的直接策略梯度优化。

**关键结果**：在代码生成基准测试上，NF-CoT 相比显式 CoT 和之前的潜在推理基线均提升了通过率，同时大幅降低了中间推理成本。
