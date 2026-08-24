---
title: 'CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety
  Alignment'
title_zh: CLEAR：连续潜在适配器路由实现效用保留的 LLM 安全对齐
authors:
- Chengxiao Wang
- Enyi Jiang
- Xiaojing Liao
- Sanmi Koyejo
affiliations:
- Siebel School of Computing and Data Science, University of Illinois at Urbana-Champaign
- Computer Science, Stanford University
arxiv_id: '2608.21278'
url: https://arxiv.org/abs/2608.21278
pdf_url: https://arxiv.org/pdf/2608.21278
published: '2026-08-20'
collected: '2026-08-24'
category: LLM
direction: LLM 安全对齐 · 条件 LoRA 路由
tags:
- LLM Safety
- LoRA
- Adapter Routing
- Conditional Alignment
- Utility-Preserving
one_liner: 用轻量隐状态门控连续控制安全 LoRA 激活，在降低有害输出的同时保留基座效用
practical_value: '- 将安全/合规策略做成可插拔的 LoRA+门控旁路，而不是全局 SFT：线上推荐文案、Agent 回复生成时，冻结基座保留推荐/推理能力，仅对命中风险
  prompt 激活安全 adapter，避免整体性能回退。

  - 连续门控比离散 router 更灵活：输出 α∈[0,1] 控制 LoRA 强度，可在线上按场景调整阈值，实现“轻度改写/强干预”的分级风控，适合电商内容审核和广告合规。

  - 训练时只用 hidden state 作为 gate 输入，仅训练 gate 和安全 LoRA，成本低、可回滚；可迁移到多策略组合：为不同地域/品牌安全规范各训练一个小
  adapter，由 gate 混合或路由。

  - 评估安全对齐时不能只看 ASR，要同时看推理/推荐指标（类似 GSM8K）；条件化训练明显优于全局 SFT/LoRA，可作为安全与效用 trade-off
  的强 baseline。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 安全对齐通常采用全局 SFT 或 LoRA，会对有害和良性输入同时产生响应偏移，导致数学推理等通用效用下降。需要一种只对危险 prompt 生效、不干扰正常请求的 conditional alignment 机制。

**方法关键点**：CLEAR 冻结基座模型，训练一个低秩安全 adapter，并引入一个轻量 hidden-state gate。gate 由冻结 backbone 的隐状态计算连续标量 α∈[0,1]，动态控制安全 LoRA 的激活强度；有害输入触发较高 α，良性输入保持接近 0，从而减少对 base model 的不必要修改。训练时仅更新 gate 与安全 LoRA。

**关键结果**：在 Llama-3-8B-Instruct 上，HarmBench ASR 从 32.3% 降至 0.5%；相比全局 SFT 或标准 LoRA，GSM8K 准确率最高提升 7.1 个百分点，并保留大部分基座效用。
