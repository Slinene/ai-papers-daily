---
title: 'FLASH-MAXSIM: IO-Aware Fused Kernels for Late-Interaction Scoring'
title_zh: FLASH-MAXSIM：面向晚交互评分的 IO 感知融合核
authors:
- Roi Pony
- Adi Raz Goldfarb
- Idan Friedman
- Daniel Ezer
- Udi Barzelay
affiliations:
- IBM Research Israel
arxiv_id: '2605.29517'
url: https://arxiv.org/abs/2605.29517
pdf_url: https://arxiv.org/pdf/2605.29517
published: '2026-05-28'
collected: '2026-05-31'
category: RecSys
direction: ColBERT/MaxSim 的 IO 感知核优化
tags:
- Late-Interaction
- MaxSim
- GPU Kernel
- ColBERT
- IO-Aware
one_liner: 通过流式融合核避免物化完整相似度张量，大幅降低内存并加速 MaxSim 计算，保持精确排序
practical_value: '- 线上服务直接替换 PyTorch 实现：在 ColBERT/ColPali 的检索或推荐召回中，用 Flash-MaxSim
  计算 MaxSim，无需改变模型即可获得 3.9–4.7 倍加速与 16 倍推理内存节省，支持更大 batch 和文档量，降低线上延迟。

  - 训练时反向传播优化：训练晚交互模型可使用其原子操作无关的梯度聚合，节省约 28 倍训练内存，允许在有限 GPU 资源下增大 batch size 或序列长度，稳定训练过程。

  - INT8 量化推理：提供的 INT8×INT8 量化核可进一步压缩内存与带宽，适合对延迟敏感的电商搜索或推荐服务，且在 top-20 排序上完全精确。

  - 融合归约设计思路可迁移：业务中涉及“点积→行/列最大→求和”类操作（如 attention 变体、多向量匹配），可借鉴其分块流式、在片上归约的策略，避免中间张量膨胀。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：晚交互检索（ColBERT、ColPali）使用 MaxSim 计算 query-document 得分，标准 PyTorch 实现通过 einsum 物化完整的 query×document 相似度张量（例如 ColPali 处理 10K 文档时 FP16 张量达 21 GB），仅用于归约后丢弃，严重蚕食 GPU 显存，限制了推理和训练的 batch size。

**方法**：Flash-MaxSim 提出 IO 感知的融合 GPU kernel，将 query 和 document 分块流式加载到 SRAM，并在同一趟遍历中直接完成行最大与求和归约，完全不物化中间张量。反向传播进一步利用前向 argmax 构造 CSR 稀疏归约，避免原子操作。同时支持 INT8 量化和变长（无填充）序列，在所有变体中保持 IO 最优。

**结果**：在 A100 上比朴素 PyTorch 快 3.9 倍（H100 上 4.7 倍），推理内存占用降低 16 倍，训练内存降低约 28 倍，可处理原本显存无法支撑的语料和 batch 规模，且与 FP32 参考结果在 top-20 排名上 100% 一致。
