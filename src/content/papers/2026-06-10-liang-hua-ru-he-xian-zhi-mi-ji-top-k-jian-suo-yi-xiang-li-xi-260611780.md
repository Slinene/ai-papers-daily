---
title: What Limits Does Quantization Place on Dense Top-$k$ Retrieval? A Theoretical
  Study
title_zh: 量化如何限制密集 top-k 检索？一项理论分析
authors:
- Koki Okajima
- Tsukasa Yoshida
affiliations:
- NTT, Inc.
arxiv_id: '2606.11780'
url: https://arxiv.org/abs/2606.11780
pdf_url: https://arxiv.org/pdf/2606.11780
published: '2026-06-10'
collected: '2026-06-14'
category: RecSys
direction: 密集检索 · 向量量化理论
tags:
- Dense Retrieval
- Top-k Retrieval
- Quantization
- Embedding Dimension
- Information Theory
one_liner: 证明在量化精度下，嵌入维度必须随语料库规模对数增长，打破了无限精度下维度与 N 无关的结论。
practical_value: '- 在电商推荐的大规模向量检索中，若采用标量量化或乘积量化压缩向量，随着商品库增长，需同步提升嵌入维度或量化精度，否则 top-k
  检索的完备性会下降。

  - 可根据理论关系 $Bd = \Omega(k\ln N)$ 评估当前系统的量化配置是否安全：给定 $N$、$k$ 和每个坐标的比特数 $B$，反推所需最小维度
  $d$，作为系统扩展的参考。

  - 在 Agent 或 RAG 场景中，若使用向量数据库存储外部记忆或工具描述，量化压缩策略需考虑检索任务复杂度（$k$ 的大小）与记忆条目数 $N$ 的乘积效应，避免精度不足导致的检索失败。

  - 提示工程或检索增强流程中，若融合多个量化向量索引（如多级 PQ），推荐根据总比特预算 $Bd$ 分配资源，而非孤立压缩，以维持检索表达力。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：近期理论工作表明，在无限精度下，只需嵌入维度 $d=O(k)$ 即可将任意 $k$ 子集的 top-k 检索关系嵌入到 $d$ 维球面，与语料库大小 $N$ 无关。但实际向量检索系统广泛使用量化节省内存，量化精度是否会限制这种理论上的维度无关性？本文从信息论角度给出答案。

**方法**：首先建立一般量化模型，假设每条嵌入的每个坐标用 $B$ 比特表示，证明完美实现所有 $k$-子集 top-k 检索所需的总体比特数必须满足 $Bd = \Omega(k\ln N)$，即对于固定精度 $B$，维度 $d$ 必须随 $N$ 至少对数增长，打破了无限精度下的 $O(k)$ 上界。接着专门针对 $\ell_2$ 归一化向量的 $B$ 比特均匀标量量化，推导出精度阈值 $B^* = O(\ln\ln N)$：当 $B < B^*$ 时，无论维度多大都无法满足需求；在 $B$ 高于阈值后，可行性区域由 $d$ 和 $B$ 共同决定，并给出了上下界。

**关键结果**：（1）总比特下界 $Bd = \Omega(k\ln N)$，说明量化后维度必须随 $N$ 增长；（2）对于标量均匀量化，存在临界精度 $B^* = O(\ln\ln N)$，低于此值检索能力崩溃；（3）在可行区内，维度与精度存在权衡，呈现在 $B$-$d$ 平面上的三个可行/不可行区域。这意味着实际向量数据库和密集检索系统在采用量化时，嵌入维度和精度必须随语料库规模同步提升，否则无法保持完备的 top-k 检索能力。
