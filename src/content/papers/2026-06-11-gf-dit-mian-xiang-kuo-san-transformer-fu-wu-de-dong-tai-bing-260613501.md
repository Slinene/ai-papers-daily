---
title: 'GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving'
title_zh: GF-DiT：面向扩散 Transformer 服务的动态并行调度
authors:
- Xinwei Qiang
- Yifan Hu
- Shixuan Sun
- Jing Yang
- Han Zhao
- Chen Chen
- Yu Feng
- Jingwen Leng
- Minyi Guo
affiliations:
- Shanghai Jiao Tong University
- Guizhou University
arxiv_id: '2606.13501'
url: https://arxiv.org/abs/2606.13501
pdf_url: https://arxiv.org/pdf/2606.13501
published: '2026-06-11'
collected: '2026-06-14'
category: Other
direction: 扩散模型服务 · 动态并行调度
tags:
- Diffusion Transformers
- Serving
- Dynamic Parallelism
- GPU Scheduling
- vLLM-Omni
- Group-Free Collective
one_liner: 将 GPU 并行度作为可调度资源，通过弹性运行时和轻量组通信大幅提升 DiT 服务效率
practical_value: '- 动态并行调度思想可直接应用于电商场景中的图像/视频生成服务（如商品图生成、虚拟试穿），根据请求量波动弹性分配 GPU，提升资源利用率并保障延迟
  SLO

  - Group-free collectives 的低开销通信组建立机制（从 778ms 降至 60μs）可用于需要频繁重配并行组的多 Agent 协作推理或分布式模型推理，减少通信初始化开销

  - 异步执行抽象（请求分解为可独立调度的轨迹任务）可借鉴到长推理链的 Agent 系统中，提高步间并发和 GPU 利用

  - 策略可编程运行时设计允许按业务目标（如优先降低 P99 延迟）配置并行调整策略，适合推荐系统中对生成式模块的差异化服务质量要求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散 Transformer（DiT）成为图像/视频生成的主流架构，但现有服务系统为每个请求分配固定并行配置，无法适应请求、执行阶段和系统状态的异构性，导致 GPU 利用率低、服务质量差。

**方法**：提出 GF-DiT，一个策略可编程的弹性 DiT 运行时。核心是将 GPU 并行度视为第一类可调度资源，动态调整运行中请求的并行度。引入异步执行抽象，将请求分解为独立可调度的轨迹任务，支持在线 GPU 重分配。为降低动态并行带来的通信开销，设计 group-free collectives 轻量通信抽象，支持任意执行组的低延迟在线形成与重配置。

**结果**：在 vLLM-Omni 上实现，针对典型图像和视频扩散工作负载评估。相比固定流水线静态并行，GF-DiT 吞吐量提升最高 6.01 倍，平均延迟降低最多 95%，SLO 违反率降低最多 90%，通信组建立开销从 778 ms 降至约 60 μs。
