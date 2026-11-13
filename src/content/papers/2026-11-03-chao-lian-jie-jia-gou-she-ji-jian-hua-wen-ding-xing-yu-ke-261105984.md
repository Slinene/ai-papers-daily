---
title: 'On the Design of Hyper-Connections: Simplification, Stability, and Scalability'
title_zh: 超连接架构设计：简化、稳定性与可扩展性
authors:
- Xiangdong Zhang
- Xiaohan Qin
- Sunan Zou
- Tuo Dai
- Bizhao Shi
- Zhuo Xia
- Yebin Yang
- Yizhou Chen
- Yuliang Liu
- Yu Cheng
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
- Peking University
- Nanyang Technological University
arxiv_id: '2611.05984'
url: https://arxiv.org/abs/2611.05984
pdf_url: https://arxiv.org/pdf/2611.05984
published: '2026-11-03'
collected: '2026-11-13'
category: Training
direction: LLM 残差连接架构简化与训练提效
tags:
- Hyper-Connections
- Residual Connections
- MoE
- Training Efficiency
- Stability
one_liner: 系统拆解 Hyper-Connections，提出 SimpleHC 以去除混合、共享访存，以 2.4% 额外训练成本达到 mHC 性能
practical_value: '- 自研 MoE/Transformer 底座或大规模推荐模型时，可先尝试去掉 HC 中的 residual mixing：固定门控
  mixing 或纯 learned read/write gating 已接近 mHC，能省参数与计算。

  - 重复读取 expanded residual state 是 HC 训练开销主因；SimpleHC 的 shared group-entry state +
  batched reads/deferred writes + scalar correction 可直接迁移到任何 gated residual/memory
  模块，降低 HBM 访问。

  - 训练不稳定时不必只调优化器：简化残差连接、共享门控输入可带来更平滑梯度，适合大规模 MoE 训练。

  - 若需要用 15B–30B MoE 底座做 LLM4Rec 或 Agent 训练，SimpleHC 仅比 vanilla residual 多 2.4% 端到端时间，是可落地的降本方案。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Hyper-Connections 已被前沿语言模型采用，但其组件理解不足，且训练开销不可忽略。论文系统研究 HC 架构，目标是在保持性能的同时简化设计、提升训练效率。

**方法关键点**：研究发现 learned read/write gating 不混合、以及固定门控的非受限 mixing，分别足以达到与 mHC 相近的效果。进一步定位到 expanded residual state 的重复访问是训练开销主要来源，即使没有 mixing 也如此。据此提出 SimpleHC：移除 residual mixing，利用可加结构与共享门控输入实现 shared memory access；层特定门控共享 group-entry state，支持 batched reads 和 deferred writes；scalar corrections 精确保留前序 sublayer 输出贡献。

**关键结果**：在最大测试规模上，SimpleHC 相比 vanilla residual baseline 仅增加 2.4% 端到端训练时间；在 15B 到 30B MoE 模型上保持与 mHC 相当的性能；标准训练中梯度动态更平滑，压力测试下仍稳定。
