---
title: 'DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees'
title_zh: DARTree：基于自回归草稿树的推测性扩散解码
authors:
- Tianyi Li
- Yaxin Luo
- Xinyi Shang
- Zhiqiang Shen
affiliations:
- VILA Lab, MBZUAI
arxiv_id: '2608.13524'
url: https://arxiv.org/abs/2608.13524
pdf_url: https://arxiv.org/pdf/2608.13524
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: LLM 推理加速 · 推测解码
tags:
- Speculative Decoding
- Diffusion Drafter
- Autoregressive Tree
- Lossless Speedup
- LLM Inference
one_liner: 将扩散块草稿与树形自回归校正结合，训练无关地提升推测解码接受长度与加速比
practical_value: '- 对线上部署 LLM 做生成式推荐（商品文案、推荐解释、对话式导购、搜索 query 改写）的团队，可直接把 DARTree
  作为即插即用的推理加速层：训练无关，只需预训练 AR 校正头，无需额外训练成本，且保持无损输出分布。

  - 借鉴其“固定宽度候选树 + 批量扩展评分”的工程 trick：把树节点扩展和 AR 校正头推理合并为单个 batch，避免逐节点堆排序的串行开销，适合在 GPU
  上高并发执行，有利于降低在线服务延迟。

  - 扩散草稿器做块级并行预测时，其边际分布需通过树形 AR 校正来恢复因果条件，这对其他使用扩散/非自回归草稿的加速方案有参考意义：不要只用单一链式校正，树形候选能显著提高接受长度。

  - 注意该方法主要针对通用 LLM 解码，对传统推荐模型的排序、召回无直接帮助；但其加速比（最高 9.73x）在 LLM 参与的推荐链路里能有效缓解推理瓶颈。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：推理加速是 LLM 实际部署的关键瓶颈。推测解码用轻量草稿器并行验证多个 token，但自回归草稿仍序列生成；扩散草稿器虽可并行预测整块 token，其位置分布是边际而非沿草稿路径的条件分布，导致接受的 token 质量受限。现有循环校正只在单一链上引入因果信息，扩散树构造扩大了候选覆盖但缺少分支级校正。

**方法关键点**：DARTree 将预训练的自回归校正头从链式扩展到树形，且无需训练。首先构造固定宽度候选树，在每个深度批量扩展并评分所有节点，随后仅用最佳优先剪枝选出验证树，把 AR 头推理与顺序堆操作解耦成批量计算。这使得校正头可以高效处理多个候选分支，同时保持与目标模型输出分布的一致性。

**关键结果**：在 7 个数学、代码和对话基准上，DARTree 在四种模型-温度配置下均取得最高平均接受长度与加速比：单轮验证最多接受 12.97 个 token，同一设置下比 DFlash 高 98.6%，比 Domino 高 27.9%；相对本地自回归解码实现最高 9.73 倍无损加速。
