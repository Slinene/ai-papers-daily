---
title: 'LLaDA-UI: Bringing Block-wise Diffusion to Vision-Language GUI Agents'
title_zh: LLaDA-UI：将分块扩散引入视觉语言GUI智能体
authors:
- Zhangxuan Gu
- Haoxing Chen
- Qi Qin
- Yi Xin
- Kai Gan
- Lin Liu
- Long Cui
- Xiaomei Wang
- Beitong Zhou
- Yunzhu Zhang
affiliations:
- AGI Research Center, Inclusion AI
- Venus Team
- Westlake University
arxiv_id: '2609.13287'
url: https://arxiv.org/abs/2609.13287
pdf_url: https://arxiv.org/pdf/2609.13287
published: '2026-09-08'
collected: '2026-09-15'
category: Agent
direction: Agent · 分块扩散多模态模型
tags:
- Diffusion LLM
- GUI Agent
- Block-wise Diffusion
- Vision-Language
- MoE
- Grounding
one_liner: 提出16.7B MoE分块扩散视觉语言GUI智能体，在多个GUI基准上超越Qwen2.5-VL-7B并在4/6基准上超过Qwen3-VL-8B
practical_value: '- 分块扩散解码的并行性可降低端到端延迟，适合需要实时感知屏幕并快速决策的 Agent 场景（如自动操作商品后台、客服工单处理、广告账户管理）；可在小规模任务中替换自回归解码验证扩散解码的加速效果。

  - 两阶段训练策略（通用多模态预训练 + 领域 SFT）可复用于训练电商多模态 Agent：先对齐视觉与语言，再用业务 GUI 数据微调，无需从零构建视觉语言模型。

  - 原生分辨率视觉编码器对细粒度 UI 元素定位重要；电商场景中商品图、广告素材上的小文字/按钮/价格可能被降采样丢失，采用原生或高分辨率编码可提升 grounding
  精度。

  - MoE 架构使 16.7B 总参数在多个 GUI 基准上超过同量级/更大稠密模型，在可控激活成本下保持性能，对需要并发处理大量 Agent 请求的业务有成本优势。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：扩散大语言模型（dLLM）通过块并行、任意顺序生成实现高效解码，适合低延迟应用。GUI 智能体需要反复感知屏幕状态并实时输出结构化、空间定位动作，是验证该范式的理想场景。但 dLLM 能否扩展为高性能多模态 GUI 智能体仍未知。

**方法关键点**：提出 LLaDA-UI，一个 16.7B 参数的 MoE 分块扩散视觉语言 GUI 智能体。采用两阶段训练：通用多模态预训练将原生分辨率视觉编码器与 LLaDA2.0-mini-base 扩散语言骨干对齐；随后在涵盖移动、桌面、网页及 grounding 数据的混合数据集上进行 GUI 智能体监督微调。

**关键结果**：在 grounding 和 navigation 基准上，LLaDA-UI 显著优于 Qwen2.5-VL-7B，并在 6 个 GUI 基准中的 4 个上超过 Qwen3-VL-8B。具体分数包括 SS-V2 94.0、SS-Pro 65.2、AndroidWorld 57.8、MobileWorld 25.6、OSWorld 41.8、WebVoyager 56.9。结果表明分块扩散可成为多模态 GUI 智能体的实用生成范式。
