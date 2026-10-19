---
title: 'Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State
  Design'
title_zh: 迈向正确的循环模型：拓扑、输入注入与循环状态设计（第一部分）
authors:
- Benhao Huang
- Chufan Shi
- Junlin Chen
- Shicheng Wen
- Zhengzhong Liu
- Eric Xing
- Xuezhe Ma
affiliations:
- Institute of Foundation Models
- USC
- CMU
arxiv_id: '2610.23036'
url: https://arxiv.org/abs/2610.23036
pdf_url: https://arxiv.org/pdf/2610.23036
published: '2026-10-15'
collected: '2026-10-19'
category: LLM
direction: 高效循环 LLM 架构设计
tags:
- Looped Models
- Recurrent Transformer
- MoE
- Input Injection
- Architecture Design
- Training Efficiency
one_liner: 系统消融循环LLM的拓扑、输入注入和循环状态设计，证明Huginn架构在稠密和MoE模型上均优于Ouro且参数效率更高
practical_value: '- 循环 Transformer 是低成本部署 LLM 的有效架构：在电商搜索、推荐系统等需线上低延迟、低显存的场景，可采用 prelude–recurrent
  block–coda sandwich 结构，以相同 FLOPs 将 resident 参数减少约 75%，适合高频更新和边缘部署。

  - 把 input injection 看作增强知识检索与上下文利用的专项机制：在做 query 改写、搜索 suggestion、商品描述生成或 RAG-based
  推荐时，可专门设计输入注入层，将用户上下文、商品知识等注入循环块，而不用改变整体拓扑。

  - 循环状态设计应从简：论文显示 separate H/L recurrent states 和 random initialization 无稳定收益，因此工程实现中不要过度设计循环状态，优先使用简单共享状态和标准初始化，降低实现复杂度。

  - MoE 与循环结合可行且路由更均衡：推荐系统的大规模稀疏 MoE 模型可借鉴 Huginn-style loop，用更少 resident 参数维持性能，同时改善专家负载均衡，适合多域/多任务推荐联合训练。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Looped language models 重用物理 Transformer blocks 实现逻辑深度，但现有架构把循环位置、输入注入、循环状态组织耦合在一起，难以分析各自贡献。

**方法与结果**：在匹配参数规模、逻辑深度和 token 预算的条件下从零训练，系统消融三个轴。发现 prelude–recurrent block–coda sandwich 架构在上下文提取和推理任务上持续提升；input injection 主要增强知识检索与上下文利用；random initialization 和 separate H/L recurrent states 带来混合或负面效果。完整 Huginn 设计在 730M 参数、336B tokens 规模下，十个 benchmark 全面超过 Ouro。该优势可迁移到 MoE：8B resident / 0.8B active 参数、500B tokens 规模下，Huginn MoE 在知识、推理、编码等几乎所有 benchmark 优于 Ouro MoE，且专家路由更均衡。在 matched FLOPs 下，Huginn 风格模型 resident 参数比 112 层 feedforward MoE 少 75%，在 DROP 和 GSM8K 上超过前馈基线，MATH500 持平，其余 competitive。
