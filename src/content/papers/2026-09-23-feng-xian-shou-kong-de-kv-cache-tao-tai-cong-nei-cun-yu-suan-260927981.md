---
title: 'Risk-Controlled KV-Cache Eviction: From Memory Budgets to Risk Targets'
title_zh: 风险受控的 KV Cache 淘汰：从内存预算到风险目标
authors:
- Beomgu Kang
- SoJin Yun
- Hojoon Kim
- Hyunseok Seo
affiliations:
- Department of Artificial Intelligence, Korea University
arxiv_id: '2609.27981'
url: https://arxiv.org/abs/2609.27981
pdf_url: https://arxiv.org/pdf/2609.27981
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM 推理 · KV cache 风险控制
tags:
- KV cache
- eviction
- risk control
- LLM serving
- conformal prediction
- memory efficiency
one_liner: 将 KV cache 淘汰重新定义为部署风险控制，用事后认证选择保留策略并按需回退全 KV
practical_value: '- 在电商/广告线上长上下文 LLM 服务（商品详情问答、评论总结、Agent 长时记忆）中，用风险预算替代平均精度来选择 KV
  cache 压缩策略：按业务可容忍的退化概率（如 5%）和置信度进行校准，只上线被认证的策略，避免长尾请求质量事故。

  - 引入全 KV fallback 机制：当校准集上没有任何压缩策略通过风险认证（例如高难度长上下文任务），自动回退到不压缩，保障最坏情况体验，可作为线上安全网。

  - 离线评测时不要只看平均退化率，要报告有限样本认证的风险上界；对于固定内存预算方法，认证可能显示需要多保留 5-10 个百分点的 KV cache，帮助更稳健地设置内存配额。

  - 该方法是 compressor-agnostic 的，可与任意 KV 淘汰算法结合，适合在现有推理加速框架上低成本包装为上线前认证流程。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
KV cache 淘汰通常用平均质量-内存权衡评估，但平均损失可能隐藏个别请求的严重退化。论文将其视为部署风险控制：定义“重大退化”为同一请求上 eviction 使任务效用降低超过部署指定容忍阈值，部署风险是此类事件的总体频率。

**方法关键点**  
给定可靠性合同（目标风险水平和置信度要求），使用 compressor-agnostic 的事后认证过程，从校准数据中选择保留策略，具有有限样本保证；若无压缩策略被认证，则回退到全 KV。

**关键结果数字**  
跨多种 eviction 方法、Llama 和 Mistral 模型、LongBench 和 RULER-32K，同一合同支持显著不同的 eviction 级别：Llama 上 LongBench 认证 SnapKV 75% 保留，但 RULER-32K 上无测试压缩策略被认证，触发全 KV 回退。经验退化率低于 5% 目标的策略仍可能未通过有限样本认证；在 Llama LongBench 上，经验阈值选择了未认证策略，导致少保留 5-10 个百分点缓存。框架将部署级可靠性要求转换为 KV 内存操作点。
