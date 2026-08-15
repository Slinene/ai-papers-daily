---
title: Simplex Relaxation for Discrete Diffusion
title_zh: 离散扩散模型的单纯形松弛方法
authors:
- Jinya Sakurai
- Patrick Pynadath
- Satoshi Hayakawa
- Jaehong Yoon
- Xulei Yang
- Nancy F. Chen
- Xun Xu
affiliations:
- NTU Singapore
- The University of Tokyo
- Purdue University
- Institute for Advanced Intelligence and Computing (IAIC), A*STAR
- Centre for Frontier AI Research (CFAR), A*STAR
arxiv_id: '2608.10615'
url: https://arxiv.org/abs/2608.10615
pdf_url: https://arxiv.org/pdf/2608.10615
published: '2026-08-10'
collected: '2026-08-15'
category: Other
direction: 离散扩散生成模型优化
tags:
- discrete diffusion
- Dirichlet augmentation
- Rao-Blackwellization
- categorical generation
- text generation
- Sudoku
one_liner: 通过 Dirichlet-categorical 增广保持均匀扩散边际不变，导出 Rao-Blackwell 反向桥目标与采样器
practical_value: '- 生成式推荐（如 Semantic ID 序列生成）中，离散扩散模型可借鉴 Simplax 的辅助连续变量增广：不改变离散 corruption
  过程，复用现有离散 token 的 embedding 和 denoiser 架构，同时用 Dirichlet 增广获得 Rao-Blackwell 化的目标，降低训练方差。

  - 若在 query 推荐/搜索词生成里使用离散扩散，可尝试保留 corrupted categorical state 作为网络输入，仅通过辅助 simplex
  变量改善反向桥估计，工程上无需重构输入管道。

  - 该方法的 open-source 思路适合需要更稳定离散扩散训练的场景，例如生成商品标题、push 文案等短文本，可参考其在 perplexity–entropy
  权衡上的改善。

  - 在数据稀疏、需要跨 clue 密度泛化的结构化生成任务（如补全属性、约束推荐解释）中，其 Sudoku 实验表明用高线索密度训练可泛化到最低可解密度，类似策略可用于可控性要求高的搜索推荐文本生成。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：离散扩散模型的 corruption kernel 决定中间状态空间和反向预测问题。均匀离散扩散虽然简单，但训练目标和反向转移可能不够丰富，限制了生成质量。

方法关键：引入 Simplax，一种精确的 Dirichlet-categorical 增广，将每个被破坏的 categorical 状态耦合一个 auxiliary simplex-valued 变量，同时保持原始均匀扩散过程作为 categorical marginal。该增广不改变 corruption 过程，也不改变 denoiser 的输入——仍然使用 corrupted categorical state。由此得到可处理的 Rao-Blackwellized reverse-bridge objective 和对应的 stochastic reverse sampler，用连续辅助变量改善反向桥估计。

结果：在 OpenWebText 无条件生成上，Simplax 改善 generative perplexity–entropy 权衡。在 Sudoku 任务中，仅在 30-clue 谜题上训练的模型，在所有评估的 clue 密度（包括最小唯一可解的 17-clue 区间）上达到对比方法中的最高准确率，并在无条件生成中取得最高有效性。
