---
title: 'UltraQuant: 4-bit KV Caching for Context-Heavy Agents'
title_zh: 面向上下文密集型智能体的4位KV缓存压缩方案
authors:
- Inesh Chakrabarti
- David Limpus
- Aditi Ghai Rana
- Bowen Bao
- Spandan Tiwari
- Thiago Crepaldi
- Ashish Sirasao
affiliations:
- Advanced Micro Devices
- University of California, Los Angeles
- Purdue University
arxiv_id: '2606.20474'
url: https://arxiv.org/abs/2606.20474
pdf_url: https://arxiv.org/pdf/2606.20474
published: '2026-06-18'
collected: '2026-06-19'
category: Agent
direction: Agent推理缓存压缩优化
tags:
- 4-bit quantization
- KV cache
- Agent
- AMD GPU
- throughput
- TTFT
one_liner: 针对多轮Agent场景设计4位KV缓存压缩，通过非对称K/V处理、Walsh-Hadamard旋转及AMD GPU优化，大幅降低延迟并提升吞吐
practical_value: '- **Agent/多轮对话推理优化**：长上下文智能体（如购物助手、搜索Agent）的KV缓存可压缩至4位，在缓存压力下TTFT降低3.47倍，吞吐提升63%，可直接用于线上服务降本提速。

  - **非对称K/V量化策略**：对Key应用Walsh-Hadamard旋转等保精度措施，Value可更激进的量化，这一设计可直接移植到推荐模型中Transformer结构的KV缓存压缩。

  - **硬件适配与部署**：利用FP8查询+FP4 KV张量的近似路径，以及CDNA4的scaled-MFMA指令，为在特定GPU上最大化吞吐提供工程范例，可参考其流水线设计。

  - **多轮负载评估框架**：论文强调联合测量任务质量、缓存驻留和吞吐，电商Agent在评估压缩方案时可借鉴这种多维度基准测试。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：上下文密集型Agent需长期保留系统指令、工具定义等长前缀，KV缓存随上下文线性膨胀，严重限制并发和吞吐。现有压缩方案缺乏针对多轮Agent场景的联合优化，未同时平衡任务质量、缓存驻留与吞吐。

**方法**：以TurboQuant旋转+码书量化为质量锚点，vLLM FP8 KV缓存为部署基线，提出4位KV缓存压缩的实用设计：
1. 非对称处理Key/Value：Key对量化更敏感，应用Walsh-Hadamard旋转；Value可更激进压缩。
2. 移除QJL、引入块级缩放以提升精度。
3. 在AMD GPU上开发UltraQuant路径：使用FP8查询，FP4 KV张量，UE8M0组尺度，并利用CDNA4原生scaled-MFMA支持实现高效解码注意力内核。

**关键结果**：在长上下文多轮Agent负载下，对比FP8基线，UltraQuant将后期轮次（缓存压力大）的P50首token时间降低3.47倍，全局降低2.3倍，输出吞吐提升1.63倍。
