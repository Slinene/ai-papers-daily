---
title: 'FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution'
title_zh: FreeToken：面向边缘环境的带宽自适应 MoE 高效推理系统
authors:
- Shuo Yang
- Xiaoze Fan
- Melissa Pan
- Haocheng Xi
- Zhe Wang
- Shanlin Sun
- Kurt Keutzer
- Song Han
- Matei Zaharia
- Chenfeng Xu
affiliations:
- UC Berkeley
- UT Austin
arxiv_id: '2608.16157'
url: https://arxiv.org/abs/2608.16157
pdf_url: https://arxiv.org/pdf/2608.16157
published: '2026-08-16'
collected: '2026-08-20'
category: Other
direction: 边缘 MoE 推理系统 · 带宽自适应执行
tags:
- MoE
- Edge Serving
- Bandwidth-Adaptive
- CPU-GPU Offloading
- Agentic Workloads
one_liner: 通过带宽自适应执行与全栈协同设计，将前沿 MoE 模型高效部署到个人异构硬件
practical_value: '- 若业务中需本地或边缘侧部署 MoE LLM（如 query 改写、商品文案生成），可借鉴 FreeToken 不固定 offloading
  策略的思路：根据当前 PCIe 带宽、CPU/GPU 算力动态决定 expert 常驻位置，而非依赖静态预设。

  - 对 Agent 类工作负载（多轮工具调用、长上下文），关注其请求模式动态变化，利用请求间共享前缀缓存与状态复用，减少重复 KV cache 重构，降低长尾推理成本。

  - 在异构硬件集群中做推理调度时，可将模型状态视为可迁移资源，按机器实际可用内存、带宽和计算强度做细粒度映射，而非只按 GPU 数量分配。

  - 若团队使用开源 MoE 模型做离线批量生成（如推荐理由生成、广告文案扩展），可参考其对模型权重分片与流式加载的工程优化，降低对单机 GPU 显存的硬性要求。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：前沿开源 MoE 模型能力快速逼近闭源模型，但推理部署仍默认昂贵的数据中心 GPU 集群，个人开发者与小团队难以承受；同时 agent 应用大幅推高推理需求，本地化推理的经济性愈发重要。

**方法关键点**：FreeToken 将个人机器视为统一弹性推理平台，不局限于单张 GPU，而是协同设计模型布局与加载、expert 驻留策略、CPU-GPU 执行分配、agent 状态复用以及运行时内存管理。核心是带宽自适应执行：不固定 offloading 策略，持续根据当前可用异构资源（GPU 显存、CPU 内存、PCIe 带宽、算力）动态映射计算与模型状态。针对 agent 工作负载执行模式持续变化的特点，引入状态复用减少重复计算。

**关键结果**：支持超过 20 个 MoE 模型及真实编码/工具调用 agent，硬件覆盖 8GB 笔记本 GPU 到单工作站 GPU。实现在笔记本上运行 35B 模型、游戏台式机 284B 模型、单工作站 GPU 运行 753B GLM-5.2，显著降低本地部署前沿模型的硬件门槛。
