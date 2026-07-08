---
title: 'Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive,
  Diffusion, and Self-Speculation Decoding'
title_zh: Nemotron-Labs-Diffusion：统一自回归、扩散与自推测的三模式语言模型
authors:
- Yonggan Fu
- Lexington Whalen
- Abhinav Garg
- Chengyue Wu
- Maksim Khadkevich
- Nicolai Oswald
- Enze Xie
- Daniel Egert
- Sharath Turuvekere Sreenivas
- Shizhe Diao
arxiv_id: '2607.05722'
url: https://arxiv.org/abs/2607.05722
pdf_url: https://arxiv.org/pdf/2607.05722
published: '2026-07-06'
collected: '2026-07-08'
category: LLM
direction: 扩散语言模型 · 自推测解码
tags:
- diffusion
- autoregressive
- self-speculation
- throughput optimization
- tri-mode
- parallel decoding
one_liner: 单模型支持自回归、扩散、自推测三种解码模式，在吞吐和效率上显著超越开源AR和扩散LM。
practical_value: '- **Agent 系统低延迟推理**：在对话或实时推荐 Agent 中，可切换至自推测模式，用扩散模型快速生成草稿再由 AR
  验证，有效降低首 token 延迟和端到端耗时。

  - **离线批量生成任务**：生成大量商品描述、广告文案等场景，启用纯扩散模式并行解码，大幅提升吞吐，降低 GPU 成本。

  - **灵活部署与资源管理**：三模式架构允许根据 Concurrent Users 动态切换：高并发用 AR 减少排队，低并发用自推测提升交互体验，离线任务用扩散最大化硬件利用率。

  - **训练范式迁移**：联合 AR 与扩散训练的策略可借鉴至推荐系统，用于同时捕捉序列依赖（用户行为序列）和全局规划（推荐列表多样性），提升生成式推荐的质量。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前大语言模型解码要么依赖自回归（AR）逐 token 串行，效率低；要么使用扩散并行解码，但生成质量常不如 AR。为在不同部署场景下最大化吞吐与质量，需一种能将两者优势结合的统一架构。

**方法关键点**：提出 Nemotron-Labs-Diffusion，通过 AR 与扩散联合训练目标，使单一模型支持三种解码模式：（1）**AR 模式**：纯自回归解码，适合高并发在线服务；（2）**扩散模式**：纯并行解码，未来潜力最大；（3）**自推测模式**：扩散模型负责生成草稿，AR 模型验证，兼具高接受率和实用效率。关键设计包括草稿长度自适应、块级验证与 KV‑cache 共享。

**结果**：在 3B/8B/14B 参数规模上，模型精度与吞吐均优于同规模 Qwen3、Dream、LLaDA 等开源模型。8B 模型每前向传播解码令牌数是 Qwen3‑8B 的 6 倍，在 GB200 上吞吐提升 4 倍。自推测模式的草案接受率与效率均超多 token 预测（MTP）方法。速度分析表明，理想采样下扩散可比自推测多生成 76.5% 令牌。
