---
title: 'SweepANN: A GPU-Accelerated Large-K Approximate Vector Search for Drug Discovery'
title_zh: SweepANN：面向药物发现的 GPU 加速大 K 近似向量搜索
authors:
- Zhenyu Zhang
- Qi Lin
- Nan Zhang
- Zhichao Cao
affiliations:
- Arizona State University
- Independent Researcher
arxiv_id: '2610.27306'
url: https://arxiv.org/abs/2610.27306
pdf_url: https://arxiv.org/pdf/2610.27306
published: '2026-10-19'
collected: '2026-10-22'
category: RecSys
direction: 大规模向量检索 GPU 加速 · 高召回大 K
tags:
- Approximate Vector Search
- GPU
- Large-K
- High Recall
- Drug Discovery
- Compressed Scanning
one_liner: GPU 分区扫描与窗口阈值过滤实现大 K 高召回向量检索，在药物筛选中达 99.6% 召回且比现有方案快 8-24x
practical_value: '- **批量矩阵乘法评分**：将向量分区常驻 GPU，一个块只读一次，用一次 GEMM 对整批 query 打分。在召回/匹配系统中，当
  query 批量较大时，可显著减少显存带宽压力，尤其适合双塔模型的批量召回打分。

  - **窗口计划（window plan）**：先用采样块估算每个 query 的 top-K 分数下界，之后仅处理高于阈值的行。该策略可在保证高召回的同时大幅降低计算和内存，适用于需要大
  K 候选（如广告召回数千候选）且对召回率要求极高的场景。

  - **压缩向量 + 溢出重算**：用压缩向量快速扫描筛选，对可能进入 top-K 的候选做精确重算，兼顾精度与效率。可借鉴到量化召回场景，用低精度预筛 + 高精度重排的方式平衡成本。

  - **自适应计划选择**：根据 K 和库大小选择不同执行计划（grouped vs window），自动平衡内存与速度。工程上可以设计类似的调度器，根据请求规模动态切换召回策略。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：DrugCLIP 将小分子和蛋白质口袋嵌入同一空间，一次筛选固定 26,562 个口袋，查询 500M 分子库，每个口袋返回 K=500K 候选，要求相对精确搜索的均值召回达到 99%。传统 ANN（IVF、图搜索）在大 K 下成本随 K 增长，失去相对暴力扫描的优势。

**方法关键点**：SweepANN 将压缩向量分区常驻 GPU，扫描每个分区；单个块用一次矩阵乘法对整批 query 评分，每块只读一次。设计了多种执行计划完成 K 相关的选择与合并，均返回压缩评分下的精确 top-K。其中窗口计划先采样部分块保留每个 query 的最佳 K 作为种子，交换种子最小分数作为全局阈值，仅将高于阈值的行写入固定容量缓冲，溢出时触发精确重算，并用 CUDA Graphs 重放扫描。

**结果**：4 块 RTX PRO 6000 上完成全部 26,562 个口袋约 61 秒（不含库加载），召回 99.6%；DrugCLIP 原方案用 8 块 A100 约需 24 小时。在 500M 行上，窗口计划比同内存的分组计划快 1.41x；25M-500M 行、K=10K-500K 时，所有达标的 GPU IVF 配置慢 8.2-24x。DEEP1B 10 亿向量 8 GPU 上，窗口计划比精确全分扫描快 5.4x（K=100K）和 3.2x（K=500K），每 GPU 峰值内存降低 6.0x 和 5.3x，召回损失仅 1.0 和 0.7 个点。
