---
title: 'EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language
  Models'
title_zh: EAServe：面向多模态大模型的编码感知分离式服务
authors:
- Kunxiong Zhu
- Zhihao Shu
- Hangyu Zheng
- Minghai Qin
- Miao Yin
- Gagan Agrawal
- Wei Niu
affiliations:
- University of Georgia
- Western Digital
- University of Texas at Arlington
arxiv_id: '2609.31551'
url: https://arxiv.org/abs/2609.31551
pdf_url: https://arxiv.org/pdf/2609.31551
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: 多模态 LLM 推理服务 · 分离式流水线优化
tags:
- MLLM serving
- disaggregated serving
- GPU scheduling
- micro-batching
- Bayesian optimization
- goodput
one_liner: 将多模态 LLM 的 Encode 阶段作为 EPD 流水线控制点，通过自适应微批处理、部分卸载与动态 SM 划分，在 SLO 约束下显著提升
  goodput
practical_value: '- **把轻量前置阶段作为控制点**：参考 EAServe 将 Encode 作为 EPD 流水线控制点的思路，在推荐系统中将图像/视频
  embedding、特征编码等轻量前置阶段与主模型解耦，通过速率控制动态调节下游请求流，避免下游 Prefill/Decode 饥饿。

  - **动态 SM 划分实现可预测共置**：当需要把多个阶段部署在同一 GPU 上时，采用动态 SM partitioning 保证各阶段的算力隔离与可预测性能，适合广告/推荐系统中多个小模型或
  embedding 服务共置的场景。

  - **配置自动搜索减少人工调参**：借鉴 HAS 的两阶段方法——先用 per-stage capacity profiling 剪枝明显不均衡的配置，再用
  TPE 贝叶斯优化精细搜索，可自动化调优推荐系统多阶段推理 pipeline 的 batch size、worker 分配等参数。

  - **SLO 约束下的 goodput 优化**：直接关注在尾延迟 SLO 下最大化吞吐，这对电商/广告在线推理服务更具业务价值，而非单纯追求平均延迟或吞吐。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：多模态大模型（MLLM）推理相比纯文本 LLM 多了 Encode 阶段，形成 Encode-Prefill-Decode（EPD）流水线。现有系统要么只有 PD 两阶段，要么将 Encode 暴露为独立服务却不控制下游流量，导致 Encode GPU 利用率严重不足，下游 Prefill/Decode 饥饿。

**方法关键点**：EAServe 将 Encode 重新定位为 EPD 流水线的控制点，从三个维度优化：何时让工作进入下游、prefill 在哪里执行、GPU 如何共享。运行时层实现 load-adaptive micro-batching、rate-controlled partial offload（将部分 prefill 卸载到共置 worker）和动态 SM partitioning；配置层 Hybrid Auto Selection (HAS) 通过 per-stage capacity profiling 剪枝不均衡分配，再用 TPE 贝叶斯优化在 GPU 分配、encode batch size、offload ratio 的联合空间中搜索最优配置。

**关键结果**：在图像、视频、音频三类 MLLM 架构上，EAServe 在相同 SLO 约束下相比 NVIDIA Dynamo 和 vLLM 分别最高提升 4.3× 和 1.7× goodput，并维持 EPD 流水线各阶段更均衡且更高的 GPU 利用率，配置搜索收敛速度也快于基线方法。
