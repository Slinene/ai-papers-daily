---
title: 'KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization'
title_zh: KernelOPT：面向 GPU 内核优化的调度感知多智能体搜索
authors:
- Aheli Poddar
- Sanskar Prasad
- Arindam Samanta
- Subha Chakraborty
- Vishal Goyal
- Rohit Singh Rathaur
affiliations:
- Red Hat
arxiv_id: '2609.30059'
url: https://arxiv.org/abs/2609.30059
pdf_url: https://arxiv.org/pdf/2609.30059
published: '2026-09-24'
collected: '2026-09-27'
category: MultiAgent
direction: LLM 多智能体 GPU 内核优化
tags:
- Multi-Agent
- LLM
- GPU Kernel Optimization
- Triton
- Verification Gates
- PyTorch Inductor
one_liner: 用五个 profiling 引导 LLM Agent 仅优化 Inductor 生成 Triton 子内核，四级验证门保证端到端正确性并实现
  1.07–1.40× 加速
practical_value: '- **多 Agent + 多级验证门的保守发布模式**：任何 KernelOPT 候选都必须通过静态校验、多随机种子正确性、模型级
  float64 对照和性能门槛；不通过就回退到编译器 baseline。这套模式可直接迁移到搜索/推荐 Agent 的 query 改写、策略生成或代码生成：候选必须比现有生产规则快且稳，否则自动回退，保证不劣化。

  - **把系统当结构化产物而非黑盒**：KernelOPT 不优化整个编译模型，而是保留 cuBLAS/cuDNN 高性能调用，只优化 Inductor 生成的
  Triton 子内核。对应到电商 Agent，可保留已成熟的精排/召回服务，只对 LLM 生成的过滤条件、排序表达式或 SQL 片段做局部优化，降低风险并提升收益。

  - **用 profiling 数据驱动 Agent 搜索**：不是全量试错，而是通过 profiling 定位热点子内核，再由 Agent 做受限搜索。实际工作中可用耗时/失败率/转化率等
  profiling 信号，引导 LLM Agent 只优化高价值环节，减少 token 和延迟开销。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：PyTorch Inductor 默认生成的 GPU kernel 常明显弱于专家手写实现；现有 LLM 辅助 kernel 优化器大多把编译模型当黑盒，只优化独立 kernel，不尊重编译器结构决策，也不做端到端验证。

**方法关键点**：KernelOPT 把编译模型视为结构化产物，保留 cuBLAS/cuDNN 等 vendor library 调用，只对 Inductor 生成的 Triton 子内核进行优化。系统由五个 profiling 引导的 LLM Agent 协作搜索。候选经过四级验证门：静态校验、多随机种子正确性、模型级 float64 fallback 对照、性能门槛。通过后重新拼接模型并做端到端验证；若没有候选通过全部验证，则保留编译器 baseline。支持 PyTorch nn.Module、独立 Triton kernel 和 Helion kernel。

**关键结果**：在 250 个 KernelBench 问题上，相对 torch.compile 的几何平均加速为 Level 1 1.40×（51/100）、Level 2 1.15×（31/100）、Level 3 1.07×（12/50），且在全部问题上不会因为优化失败而劣化 baseline。
