---
title: 'Hierarchical Muon: Tiled Newton-Schulz Updates for Efficient Muon Optimization'
title_zh: 分层Muon：高效训练的分块Newton-Schulz更新
authors:
- Ziyuan Tang
- Tianshi Xu
- Yousef Saad
- Yuanzhe Xi
arxiv_id: '2606.27216'
url: https://arxiv.org/abs/2606.27216
pdf_url: https://arxiv.org/pdf/2606.27216
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 高效训练优化器 · 分块Newton-Schulz
tags:
- Muon optimizer
- Newton-Schulz
- hierarchical matrix
- GPU kernel
- LLM training
one_liner: 通过将动量梯度矩阵分块独立应用Newton-Schulz，大幅降低Muon优化器计算量并实现高效GPU并行
practical_value: '- 在训练含有大型密集矩阵参数的推荐或广告模型时，可将 Muon 优化器的 Newton-Schulz 步改为分块方案，直接降低从
  O(r²s) 到 O(HWT) 的单步计算量，同时保持接近全矩阵更新的训练效果。

  - 利用独立小方块计算的特性，可以设计 tile-size 相关的 GPU kernel，配合跨层批处理（cross-layer batching），将不同层的同尺寸块合并批量矩阵乘法，显著提升
  GPU 吞吐。

  - 采用内存受限分块（memory-bounded chunking）和运行时动态调整块尺寸的策略，能灵活适配不同硬件显存限制，避免 OOM 且不牺牲收敛。

  - 该方法将矩阵谱交互限定在块内，可作为工程上折衷效果与效率的通用抽象，类似思路可迁移至其他需要 per‑parameter 矩阵变换的优化场景（如 Shampoo
  类优化器的分块近似）。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：全矩阵 Muon 优化器在大型参数上应用 Newton-Schulz 迭代时，计算复杂度为 O(r² s K)（r = min(H,W), s = max(H,W)），需反复计算 Gram 矩阵，耦合所有行列，导致高开销与扩展瓶颈。

**方法**：提出分层 Muon（HiMuon），将动量梯度矩阵分割成 T×T 的块，对每个块独立执行相同的有限步 Newton-Schulz 映射，再拼回原矩阵。谱相互作用被局限在块内，忽略块间耦合，使前导计算量降至 O(H W T K)，且分解为完全独立的稠密小矩阵运算。该结构允许：按块尺寸定制 GPU kernel、跨矩阵尺寸相同的块组成批量、根据显存自动分块、运行时动态选择块大小。

**结果**：在 Transformer 训练与受控矩阵函数诊断中，HiMuon 在测试范围内保持与全矩阵 Muon 接近的 loss 曲线与矩阵更新方向，同时显著降低单步优化时间，提高 GPU 利用率和可扩展性。
