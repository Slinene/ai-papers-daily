---
title: 'CodeQuant2: Enhanced Outlier Mitigation and Adaptive Clustering for Low-Precision
  LRMs'
title_zh: CodeQuant2：低精度大型推理模型的异常值缓解与自适应聚类量化
authors:
- Xingyu Liu
- Xiangyang Yin
- Tianhua Xia
- Haiyu Wang
- Sai Qian Zhang
affiliations:
- Tandon School of Engineering, New York University
- Courant Institute School of Mathematics, Computing, and Data Science, New York University
arxiv_id: '2611.09868'
url: https://arxiv.org/abs/2611.09868
pdf_url: https://arxiv.org/pdf/2611.09868
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM 低精度量化与推理加速
tags:
- quantization
- low-precision
- LRM
- LLM inference
- outlier mitigation
- LUT
one_liner: 面向大型推理模型的聚类 LUT 低比特量化框架，通过旋转缩放抑制激活异常值、聚类权重并自适应码本，推理精度提升且最高 2.85 倍加速
practical_value: '- 在电商/广告/Agent 场景中若部署 LRM 做多步推理（如工具调用、数学计算、代码生成），可考虑聚类 LUT 低比特量化配合定制
  CUDA kernel，在精度可控下获得最高 2.85 倍加速，直接降低在线推理成本。

  - 观察表明推理早期解码步骤的激活波动更大，校准样本不能只采样预训练语料，应纳入实际任务分布下的多步推理前几个 token；在量化电商 Agent 模型时，可专门收集工具调用、搜索交互等真实链路数据做校准。

  - 用旋转和缩放抑制激活异常值，再用非均匀聚类表示权重长尾分布，比 uniform 量化保留更多有效精度；对偏好、商品、广告特征等长尾表示也可能有借鉴意义。

  - 不同层量化难度不同，可按层动态调整 codebook 大小，类似混合精度策略；工程上可先对目标模型各层做量化敏感度分析，再分配码本规模，在延迟预算内最大化精度。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**
大型推理模型（LRM）在数学、代码生成、工具增强决策等任务上表现更强，但推理链长导致推理成本高，低精度量化成为关键。然而低位量化在推理任务上精度损失严重。论文观察到推理早期解码步骤的激活波动更大，若校准样本忽略这些早期状态，会遗漏激活波动。

**方法关键点**
CodeQuant2 是基于聚类查表（LUT）的低比特量化框架，包含：1) 用旋转与缩放缓解激活异常值；2) 用聚类表示非均匀权重分布，避免 uniform 量化精度浪费；3) 对每层按量化难度自适应调整 codebook 大小；4) 依据推理时激活统计改进校准样本选择，更匹配实际解码分布；5) 配套定制 LUT CUDA kernel 提升部署性能。

**关键结果**
在多个推理基准上，CodeQuant2 相比 BF16 基线大幅改善低精度模型精度，同时实现最高 2.85 倍加速。
