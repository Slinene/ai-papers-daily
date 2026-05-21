---
title: 'OScaR: The Occam''s Razor for Extreme KV Cache Quantization in LLMs and Beyond'
title_zh: OScaR：极端KV缓存量化的奥卡姆剃刀
authors:
- Zunhai Su
- Rui Yang
- Chao Zhang
- Yaxiu Liu
- Yifan Zhang
- Wei Wu
- Jing Xiong
- Dayou Du
- Xialie Zhuang
- Yulei Qian
affiliations:
- Tsinghua University
- Meituan LongCat Team
- The University of Hong Kong
- The University of Edinburgh
- UCAS
arxiv_id: '2605.19660'
url: https://arxiv.org/abs/2605.19660
pdf_url: https://arxiv.org/pdf/2605.19660
published: '2026-05-18'
collected: '2026-05-21'
category: LLM
direction: LLM推理优化 · INT2 KV缓存量化
tags:
- KV Cache
- Quantization
- INT2
- LLM
- Multi-modal
- Inference Efficiency
one_liner: OScaR通过Canalized Rotation与Omni-Token Scaling解决Token Norm Imbalance，实现INT2近乎无损KV缓存量化，解码加速3.0×
practical_value: '- **INT2 KV缓存部署**：电商对话或实时推荐场景中，用OScaR的INT2量化可降低96%的KV缓存内存（5.3×），结合3.0×解码加速，适合高并发低延迟需求。

  - **轻量集成路径**：Canalized Rotation + Omni-Token Scaling无需复杂重采样或辅助模型，仅需少量显式变换，可直接插入现有Transformer推理管线，降低工程复杂度。

  - **多模态量化统一**：OScaR已覆盖文本、多模态及全模态LLM，对购物图文推荐中的多模态模型KV缓存压缩同样有效，避免为不同模态设计多套量化方案。

  - **CUDA Kernel优化**：论文提供的定制化CUDA kernel将旋转与缩放无缝融合，可借鉴其极简高效的设计思路加速自研模型推理。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长上下文推理与多模态模型使KV缓存成为内存瓶颈，极端低比特量化（如INT2）是必要手段，但传统的per‑channel量化在极度压缩时失效，根源在于Token Norm Imbalance (TNI)——序列中不同token的范数差异巨大，导致共享量化参数时误差系统性放大。

**方法关键点**：OScaR复用Occam's Razor思想，用极简双组件解决TNI：①**Canalized Rotation**——对Key/Value做特定维度的旋转，使channel间范数趋于均匀，减少跨token组的方差；②**Omni‑Token Scaling**——在旋转后为每个token引入标量缩放因子，进一步对齐量化网格，整套操作仅线性复杂度，并配套优化的CUDA kernel。旋转与缩放均在线性变换下可逆，量化反量化后几乎无损。

**关键结果**：在多个纯文本、多模态及全模态LLM上，OScaR均优于现有量化方法（如TurboQuant），INT2下性能近乎无退化，甚至超越BF16基线；相比FlashDecoding‑v2，OScaR实现解码加速最高3.0×、内存减少5.3×、吞吐提升4.1×，确立新的Pareto前沿。
