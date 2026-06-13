---
title: 'Flash-GMM: A Memory-Efficient Kernel for Scalable Soft Clustering'
title_zh: Flash-GMM：用于可扩展软聚类的内存高效 GPU 内核
authors:
- Gal Bloch
- Ariel Gera
- Matan Orbach
- Ohad Eytan
- Assaf Toledo
affiliations:
- IBM Research
arxiv_id: '2606.10896'
url: https://arxiv.org/abs/2606.10896
pdf_url: https://arxiv.org/pdf/2606.10896
published: '2026-06-08'
collected: '2026-06-13'
category: RecSys
direction: 大规模 GPU GMM 聚类加速
tags:
- GMM
- Triton
- GPU
- IVF
- ANN
one_liner: 提岀 Flash-GMM，通过 Triton 内核融合避免显存实现完整责任矩阵，实现 20 倍加速，支持单卡训练百倍更大数据集。
practical_value: '- **用 GMM 软聚类替代 k-means 做 IVF 粗量化**：利用 GMM 的责任度将边界向量分配给多个簇，相比 k-means
  硬分配，在相同召回下可减少最高 1.7× 的距离计算量，或同等计算预算下提升 recall@10 2~12 个点，适合召回阶段的向量检索优化。

  - **单卡训练超大规模聚类模型**：Flash-GMM 避免了显存中 N×K 责任矩阵的实例化，能在单块 A100 (80GB) 上直接训练多达 1 亿向量、1024
  个簇的 GMM，为十亿级物品库的索引构建提供可能。

  - **融合核与工程实现**：整个 EM 迭代在一个 Triton kernel 中完成，无需存储中间矩阵，可作为即插即用的模块集成到现有 GPU 向量检索管线，显著降低内存压力并提升训练吞吐。

  - **扩展软分配思想**：在多模态 / 语义 ID 场景，可借鉴 GMM 的责任度作为软标签，为物品生成多个语义簇归属，替代独热分配，提升生成式推荐的聚类表达能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：GMM 训练需在显存中维持 N×K 的责任矩阵，当数据量或簇数增大时，显存迅速耗尽，限制 GMM 在大规模聚类（如向量检索的粗量化）中的应用。现有 GPU GMM 实现因显存瓶颈无法处理千万级以上数据。

**方法**：提出 Flash-GMM，一个高度融合的 Triton kernel，将 GMM 的 E 步（责任度计算）和 M 步（参数更新）合并为单次 GPU pass，不再显式存储完整责任矩阵。通过在线统计量累积和直接在寄存器中完成加权更新，消除了对全局内存的大量读写，使得 N 和 K 可以远超显存容量。

**结果**：在 A100 (80GB) 上，Flash-GMM 相比基于 PyTorch 的 GPU 实现（TorchGMM）获得 20× 以上的速度提升；可稳定训练 1 亿向量、D=128、K=1024 的模型，而对比方法在百万级即出现 OOM。集成到 IVF 近似最近邻搜索中，用 GMM 软聚类替换 k-means 粗量化：通过将边界向量依据责任度分配给多个簇，在达到相同 recall@10 目标时最多减少 1.7× 的距离计算，或在匹配成本下带来 2~12 个点的 recall@10 提升。代码已开源。
