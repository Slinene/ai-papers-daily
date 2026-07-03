---
title: 'ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving'
title_zh: ELDR：面向 PD 分离 MoE 推理的专家局部感知解码路由
authors:
- Sangjin Choi
- Sukmin Cho
- Yifan Xiong
- Ziyue Yang
- Youngjin Kwon
- Peng Cheng
affiliations:
- KAIST
- Microsoft Research
- Shanghai Xingyunzhili Artificial Intelligence Institute
arxiv_id: '2607.00466'
url: https://arxiv.org/abs/2607.00466
pdf_url: https://arxiv.org/pdf/2607.00466
published: '2026-06-30'
collected: '2026-07-03'
category: LLM
direction: LLM 推理 · 专家局部感知路由
tags:
- MoE
- decode routing
- PD-disaggregation
- LLM serving
- expert-locality
- TPOT
one_liner: 利用预填充专家激活模式路由请求，使解码 worker 加载更少的不同专家，降低 TPOT 5.9-13.9%
practical_value: '- 若业务部署 MoE 模型（如 Mixtral）作为生成式推荐或对话引擎，可借鉴 ELDR 的 batch 调度思路：根据请求在
  prefill 阶段激活的专家模式，将同类请求聚到同一 decode worker，减少每个 step 需加载的专家权重数量，降低 TPOT。

  - 签名缓存与 KV 缓存联合索引的设计，可直接用于推荐系统长提示（如用户画像、历史行为缓存）场景，保持前缀命中时的专家签名一致性，避免重复计算。

  - 平衡负载与专家局部性的“局部带路由”策略，可迁移至多 GPU 推荐模型推理，特别是参数量大的稀疏专家模块，通过离线聚类+在线轻载优先选择，兼顾吞吐与延迟。

  - 整体工程实现基于 vLLM，适合快速集成到现有 LLM serving 管线，为推荐系统中的大模型推理提供低成本的延迟优化方案。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：在 Prefill-Decode 分离的 LLM 推理中，现有解码路由仅平衡请求数量或负载，但 MoE 模型每个解码步需加载当前 batch 激活的所有不同专家权重，同等负载下激活专家越分散的 worker 延迟越高，单纯负载均衡不够。

**方法**：ELDR 从请求的 prefill 阶段记录专家激活，构建专家签名（expert signature），预测生成阶段会激活的专家。离线使用平衡 Κ-means 将签名空间划分给各 decode worker；在线采用 locality-band routing，根据请求的签名选择匹配最好的 worker 组，再从组内挑负载最轻的一个。同时设计签名缓存，以 KV-block 粒度与 KV 缓存协同索引，确保前缀缓存命中时签名仍然精确。

**结果**：在 vLLM 上实现，部署规模至 40 GPU，三个 MoE 模型（Mixtral 8x7B、DeepSeek-V2-Lite、Qwen2-57B-A14B）和两个工作负载下，ELDR 相比最强的四个负载均衡基线，中位 TPOT 降低了 5.9–13.9%，且模型输出完全不变。
