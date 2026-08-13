---
title: 'Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention
  Spikes and Inter-Spike Plateaus'
title_zh: 混合线性注意力大模型中的巨量激活：前注意力尖峰与尖峰间平台
authors:
- Zunhai Su
- Bohan Sun
- Xialie Zhuang
- Shuibai Zhang
- He Xiao
- Jing Xiong
- Hengyuan Zhang
- Zhongzhu Zhou
- Tiantian Zhang
- Ngai Wong
affiliations:
- Startlux
- Tsinghua University
- University of Chinese Academy of Sciences
- The University of Hong Kong
- University of Sydney
arxiv_id: '2608.12149'
url: https://arxiv.org/abs/2608.12149
pdf_url: https://arxiv.org/pdf/2608.12149
published: '2026-08-12'
collected: '2026-08-13'
category: LLM
direction: 混合线性注意力LLM激活分析
tags:
- Massive Activations
- Hybrid Linear Attention
- Pre-Attention Spikes
- Inter-Spike Plateaus
- Output Gating
- LLM Interpretability
one_liner: 首次系统揭示混合线性注意力LLM中巨量激活呈前注意力尖峰与尖峰间平台两种形态，并给出生命周期机制
practical_value: '- 部署 Hybrid Linear Attention LLM 做长上下文用户序列或 Agent 记忆时，可在全注意力层前增加激活幅值监控；这些位置被证实会出现
  PAS，适合作为 FP16/INT8 量化的高危层，建议对这些投影层保留 FP32 或 per-channel 量化。

  - 若使用 GDN 等带输出门控的混合架构，保留或加强全注意力层的 output gating 能显著压低 PAS/ISP 的绝对幅值，而不会破坏层级组织结构；可作为训练稳定性和量化友好的低成本
  knob。

  - PAS/ISP 生命周期与层类型强相关，说明巨量激活不是随机噪声；可用层位置先验做 outlier-aware 剪枝、KV cache 淘汰或 top-k
  门控：线性注意力区间内容忍持续平台，在全注意力前保守处理尖峰。

  - 训练混合模型时，两形态早期出现，可据此设计按层类型分化的 clipping/gate initialization 策略，而不是全局统一激活裁剪。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：混合线性注意力(HLA) LLM 将线性注意力与全注意力交错，提升长序列效率，但其内部激活动态如何被层间杂交重塑尚不清楚。巨量激活(MA)与注意力机制耦合，可作为观察窗口。

方法：首次系统研究层交错 HLA LLM 中的 MA。覆盖 5 种线性注意力架构、6 种混合配置、5 个数据域，以及 1.2B–397B 开源混合模型；并对 GDN 混合模型做至多 1.3B 可控预训练。通过逐层激活分析与系统离群点分析，提出生命周期机制。

结果：发现两种与架构对齐的形态：全注意力层前出现前注意力尖峰(PAS)；巨量激活可穿过中间线性注意力层形成尖峰间平台(ISP)。全注意力越密集，连续 PAS 通过 ISP 越连通，最终恢复全注意力 LLM 的稳定 MA 形态。预训练显示两形态早期出现，并对输出门控不对称响应：全注意力输出门控显著压低绝对幅值但不消除层级组织；移除 GDN 门控仅带来较小放大。机理上，统一生命周期由 MA 消除时机决定：PAS 为局部 write–sink–cancel；ISP 持续由延迟消除解释。代码已开源。
