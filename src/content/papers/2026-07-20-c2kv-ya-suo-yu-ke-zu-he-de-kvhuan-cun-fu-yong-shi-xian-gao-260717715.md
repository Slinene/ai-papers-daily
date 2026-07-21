---
title: 'C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference'
title_zh: C²KV：压缩与可组合的KV缓存复用，实现高效长上下文LLM推理
authors:
- Chuheng Du
- Junyi Chen
- Hanlin Tang
- Kan Liu
- Tao Lan
- Lin Qu
- Chaoyue Niu
- Shengzhong Liu
- Guihai Chen
- Fan Wu
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
arxiv_id: '2607.17715'
url: https://arxiv.org/abs/2607.17715
pdf_url: https://arxiv.org/pdf/2607.17715
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: LLM推理加速 · KV缓存复用与压缩
tags:
- KV Cache
- Compression
- Reuse
- Long-Context
- LLM Serving
- Inference Acceleration
one_liner: 联合优化KV压缩与拼接，实现位置无关的可组合缓存，长上下文推理加速达17倍
practical_value: '- 在构建基于RAG的推荐或多文档搜索系统时，可直接复用C²KV的压缩与可组合缓存，避免每次请求重新编码海量上下文，大幅降低首token延迟和GPU内存占用。

  - 轻量侧车Extractor不修改基座模型，适合在已有生产LLM（如阿里通义、ChatGLM）上快速部署，无需重新训练或对齐，工程风险低。

  - 位置无关的模块化缓存设计，允许不同来源的文档片段独立压缩后动态拼接，特别适合电商搜索中多商品描述、多用户评价等异构上下文组合场景。

  - 压缩-拼接联合训练策略确保压缩后的表示可直接用于下游注意力计算，避免简单量化和重用带来的精度崩塌，为业务中长文本处理提供了可靠的效率-质量平衡。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：长上下文LLM推理（如RAG、多文档问答）存在严重的KV缓存存储和访问瓶颈，现有重用方法只关注计算节省，忽略存储成本；而直接组合压缩与非前缀重用会严重降低生成质量。

**方法**：提出C²KV，一个联合优化KV提取与推理时拼接的统一框架。核心是学习一个与位置无关、可组合的压缩KV缓存流形。引入轻量侧车Extractor（含可学习压缩token）与结构化注意力流，在不改变冻结基座模型的前提下，将任意文档片段压缩为模块化缓存。压缩-拼接联合训练确保提取时的表示与下游拼接重用行为对齐。

**结果**：在多个长上下文基准（LLaMA-3.1-8B-Instruct, Qwen2.5-7B-Instruct）上，C²KV在10K~128K token上下文下，存储与传输成本显著降低，推理速度最高提升17倍，且生成质量（ROUGE、BLEU等）基本无损，明显优于Naive压缩+重用基线。
