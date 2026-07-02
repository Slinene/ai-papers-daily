---
title: '$\text{Log}_\text{b}$Quant: Quantizing Language Models in Logarithmic Space'
title_zh: LogbQuant：在Log空间中量化语言模型
authors:
- Jeremias Bohn
- Tizian Dippold
- Mahdi Koubaa
- Elias R. Wahl
- Georg Groh
affiliations:
- Technical University of Munich
arxiv_id: '2607.01127'
url: https://arxiv.org/abs/2607.01127
pdf_url: https://arxiv.org/pdf/2607.01127
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: 对数空间量化 · 权重压缩
tags:
- quantization
- logarithmic
- 4-bit
- LLM
- model compression
one_liner: 提出可调基的对数量化方法，在4-bit下性能优于非对称线性量化，适合消费级GPU
practical_value: '- 在电商搜索/推荐场景中，若需本地部署LLM（如商品描述生成、对话式Agent），可尝试用LogbQuant做4-bit量化，在单张消费级GPU上运行，降低显存占用同时保持生成质量。

  - 对数量化对存在少数大幅度权重的层（如FFN上投影）天然友好，可针对此类层单独使用对数域量化，或混合线性量化（例如关键层保留线性，其他层用LogbQuant）。

  - 可调基数b的思想可迁移到其他量化场景：对不同张量/层自动搜索最优基数，以匹配各异的权重分布，提升整体精度。

  - 实现上，查询表（LUT）与位打包可带来推理加速，适合对延迟敏感的在线推荐服务（如实时重排序或即时文案生成）。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM的部署受限于消费级GPU内存，权重量化是低成本解决方案。但传统均匀线性量化对低频高值权重处理不佳，导致信息丢失，尤其在小batch推理时内存带宽瓶颈突出。

**方法关键点**：提出LogbQuant，将对数量化引入LLM压缩。核心公式为 $w_q = \text{round}(\log_b(|w|/s))$，其中可调基数$b$和缩放因子$s$自适应权重分布。基础版支持无符号量化（仅正权重），通过拆分正负权重矩阵扩展至有符号情形。在4-bit下，张量粒度采用搜索确定最优$b$，并将量化参数与码本存储为LUT以加速解量化。

**关键结果**：在Llama-3.1-1B/3B、Qwen-2.5-0.5B等多个基准上，4-bit LogbQuant（签名版本）平均优于非对称线性张量量化，尤其在知识理解（MMLU）和推理（ARC）任务上优势明显；同时实现约2.5×内存节省和推理加速，在消费级RTX 4090上单batch推理延迟可接受，适合本地部署。
