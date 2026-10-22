---
title: pplx-embed-v2-late Technical Report
title_zh: PPLX-Embed-V2-Late：0.6B/9B 多模态后期交互检索模型
authors:
- Markus Krimmel
- Louis Milliken
- Ekaterina Glazkova
- Maximilian Schall
- Antoine Chaffin
- Sedigheh Eslami
- Jonas Golde
- Denis Bykov
- Claire Beamer
- Jeremy Yang
affiliations:
- Perplexity AI
arxiv_id: '2610.29523'
url: https://arxiv.org/abs/2610.29523
pdf_url: https://arxiv.org/pdf/2610.29523
published: '2026-10-21'
collected: '2026-10-22'
category: RAG
direction: 多模态 late-interaction 检索蒸馏
tags:
- late-interaction
- representation distillation
- multimodal retrieval
- ColBERT
- embedding
- agentic search
one_liner: 用 18B 教师表征蒸馏出 0.6B/9B 多模态 late-interaction 模型，支持大模型离线建库、小模型在线查询的共享向量空间
practical_value: '- 非对称部署：用 9B 离线索引商品/文档/图片，0.6B 在线编码 query；报告显示 0.6B query + 9B doc
  比纯 0.6B 平均 nDCG@10 高 1.6pp，query 延迟不变，适合电商大规模商品库和低延迟搜索。

  - 表征蒸馏优于直接 contrastive：训练小 late-interaction 模型时，直接拟合 18B 教师的 token 级 L2 归一化表征，比单独对比学习更稳，尤其
  <1B 模型；业务里想压缩强检索模型可以优先考虑这种 pointwise distillation。

  - 128 维多向量是低成本选择：在视觉文档检索上，0.6B 128 维 multi-vector 超过同尺寸 0.8B 模型 3.3pp；相比 4096 维
  dense，存储和 ANN 成本显著降低，适合电商图片搜索、商品详情页截图检索。

  - 训练工程 trick：用 gradient caching + 自定义 Triton MaxSim kernel 支持 16,384 对比 batch；quasi-random
  golden-ratio Kronecker 采样保证多个子数据集比例稳定且均匀出现，可复用到多源商品/query 数据混合。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

检索系统需要在效率与 query-document 交互深度之间权衡。Dense embedding 内积计算快但交互弱，cross-encoder 交互强但每候选都要过一遍模型；late-interaction 处于两者之间，已在 OOD、长上下文、Agentic Search 和视觉文档检索中表现突出。因此需要把强 late-interaction 模型压缩到小尺寸，同时保持多模态、多语言能力。

## 方法关键点

- **18B 教师**：从 Qwen3.5-27B 剪掉最后 20 层初始化，融合 bidirectional full attention 与 Gated DeltaNet；两阶段对比训练，先 query-document pair，再 triplet hard negatives。LoRA rank 128，InfoNCE batch 16,384，margin 0.2 做 in-batch negative masking。
- **数据**：186M query-doc pairs，981 个子数据集，采样权重调整为 56.5% text-text / 30.9% text-image / 12.6% text-visual doc；用 golden-ratio Kronecker 序列做 quasi-random 采样，保证子数据集比例稳定且均匀出现。
- **蒸馏**：冻结 18B 教师，学生拟合 token 级 L2 归一化表征，query 与 doc 位置损失取平均。9B 学生用 Qwen3.5-9B，LoRA 容量不够，采用最后八层全参微调 + 剩余层 LoRA；0.6B 学生从 Qwen3.5-0.8B 剪枝得到 594M 参数，全参微调。所有模型输出 128 维 token embedding。
- **工程实现**：gradient caching 支持大对比 batch；自定义 Triton MaxSim kernel 避免物化 token 相似度矩阵。

## 关键结果

- 领域文本检索：9B 平均 81.3 nDCG@10，比最强 baseline 高 1.6pp；0.6B 平均 78.0，在 <1B 模型里全部领域第一。
- Q2D-Web agent 查询：Combined Recall@1000 上 9B 74.8%、0.6B 73.6%，最强 baseline 69.3%。
- ViDoRe-V3：text 版本 9B 64.7%，比 best baseline 高 4.1pp；image 版本 9B 65.2%，在 vision-language 模型里最高，0.6B 62.3% 高于同尺寸 topk-embed-v1-0.8b 3.3pp。
- BrowseComp+ Agentic Retrieval：9B 达到 64.0% accuracy，比最佳 dense 模型高 8.7pp，搜索次数更少。
- 交叉模型：0.6B query + 9B doc 比纯 0.6B 高 1.6pp，且 query 编码成本不变。

## 最值得记住的一句话

小 query encoder + 大 doc encoder 共享同一教师向量空间，是实现低延迟、高效果检索的实用部署范式。
