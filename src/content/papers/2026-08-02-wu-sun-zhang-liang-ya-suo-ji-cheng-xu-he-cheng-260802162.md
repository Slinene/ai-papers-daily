---
title: Lossless Tensor Compression as Program Synthesis
title_zh: 无损张量压缩即程序合成
authors:
- Jieke Shi
- Junda He
- Wenjia Jiang
- Weifeng Sun
- Shidong Pan
- Zhensu Sun
- Chengran Yang
- Peixin Zhang
- Yifan Jia
- Zhou Yang
affiliations:
- Singapore Management University
- CSIRO
- AIDX TECH PTE LTD
- University of Alberta & Alberta Machine Intelligence Institute
arxiv_id: '2608.02162'
url: https://arxiv.org/abs/2608.02162
pdf_url: https://arxiv.org/pdf/2608.02162
published: '2026-08-02'
collected: '2026-08-08'
category: Other
direction: 模型检查点张量压缩 · 程序合成
tags:
- lossless compression
- program synthesis
- tensor compression
- checkpoint compression
- DSL
one_liner: 将无损张量压缩形式化为程序合成，合成紧凑DSL程序实现位精确重建，存储节省33.93%
practical_value: '- 电商/推荐模型（如深度CTR模型、LLM-agent）的检查点存储和传输成本高，可借鉴DSL+搜索的压缩范式，设计针对Embedding表、Transformer参数的特定压缩算子（如重复区域、浮点模式）。

  - 无损压缩保持模型精度不下降，适合对精度敏感的在线推理场景（如价格排序、广告匹配），避免有损压缩带来的预估偏差。

  - 可复用的工程trick：用少量代表性张量学习“产生式先验”来偏置搜索，提升压缩效率；将压缩过程抽象为可逆操作序列，解压时直接执行，无需额外依赖。

  - 吞吐量3.60 GB/s压缩、6.61 GB/s解压，远高于通用压缩器，适合实时模型部署和快速回滚场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：模型检查点数量与体积剧增（Hugging Face已存储超15PB），归档、传输和部署成本高昂。通用压缩器（如zstd、gzip）忽略张量内部结构，现有张量专用压缩器依赖固定管道，无法自适应多样化的模型结构与数据分布。

**方法**：提出Brevis，将无损张量压缩重新定义为程序合成。设计了一种带类型的领域特定语言（DSL），通过一组可逆算子（如重复区域、浮点字段模式）捕捉张量中的规律性结构。对给定张量，Brevis合成一个自包含的DSL程序，该程序能位精确地重建原始张量。利用从少量代表性张量样本中学习到的“检查点特定产生式先验”，引导有界A*搜索高效合成紧凑程序；解压时直接执行该程序即可。

**结果**：在语言、音频、图像生成等10个公开检查点上，将2.13 TB数据压缩至1.41 TB，存储减少33.93%；相比zstd、gzip等4种通用压缩器，档案大小最高减小30.87%，同时优于专用压缩器ZipNN和DFloat11。在实用并发配置下，压缩速度3.60 GB/s，解压速度6.61 GB/s，且保真每一源字节。
