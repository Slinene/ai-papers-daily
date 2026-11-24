---
title: A Pipeline-Parallel System for Depth-Recurrent Models
title_zh: 面向深度循环模型的流水线并行训练系统
authors:
- Yunjia Xi
- Jiarui Qin
- Di Yin
- Xing Sun
affiliations:
- Tencent Youtu Lab
arxiv_id: '2611.30581'
url: https://arxiv.org/abs/2611.30581
pdf_url: https://arxiv.org/pdf/2611.30581
published: '2026-11-22'
collected: '2026-11-24'
category: Training
direction: 循环模型训练 · Pipeline Parallelism
tags:
- Pipeline Parallelism
- Depth-Recurrent Models
- 1F1B
- MoE
- Communication Overlap
one_liner: 为循环依赖的深度模型重建流水线调度与通信，显存最高降32.8%、吞吐升12.7%
practical_value: '- 若业务中要训练或微调采用 shared block 循环的 Transformer / MoE（如 reasoning 模型、test-time
  scaling 架构），在跨卡流水线并行时可直接参考 Loop-PP 的调度：把同一 stage 的多次循环访问当作独立 slot 显式排序，避免原生 1F1B
  的死锁和乱序。

  - 其“静态指令流 + send/wait 解耦”的工程实现可迁移到推荐系统的大规模流水线训练或在线推理服务：预先编排通信原语，把发送和等待拆开，使通信与计算
  kernel 重叠，降低尾部延迟。

  - 对显存敏感的大模型训练：循环模型结合 MoE 时，Loop-PP 可降峰值显存约 33%，有助于在有限 GPU 数量下扩大模型宽度或序列长度，适合电商搜索/推荐大模型的参数扩展。

  - 如果当前业务不是 Looped 架构而是标准前馈模型，则收益有限；但若探索生成式推荐中的循环解码或多轮 Agent 推理，可借鉴其 bit-identical
  保证与训练/推理对齐方法。'
score: 7
source: huggingface-daily
depth: abstract
---

深度循环（Looped）模型通过复用同一组 block 提升有效深度，能增加容量而不增加参数，但扩展到多设备时，现有流水线并行（PP）假设 stage graph 无环、每个 micro-batch 只进入每个 stage 一次；而循环模型跨 stage 后会重复访问同一 stage 并形成反向依赖，原生 interleaved 1F1B 没有调度额外访问的位置，且仅有邻居通信无法处理回边，导致停滞或乱序。

Loop-PP 将同一 stage 的不同迭代分离调度，把 1F1B 骨架特化为覆盖循环访问的全局一致顺序；为每个 rank 生成静态指令流，将发送（post）与等待（wait）分离，让通信与本地计算重叠，并保证结果与单 stage 参考逐位一致。实验在 8B-60B MoE 模型上，峰值显存最多降低 32.8%，固定算力下最佳吞吐提升 12.7%。
