---
title: 'Symmetry-Compatible Principle for Optimizer Design: Embeddings, LM Heads,
  SwiGLU MLPs, and MoE Routers'
title_zh: 对称性兼容原则指导优化器设计：嵌入、LM头、SwiGLU MLP和MoE路由
authors:
- Tim Tsz-Kit Lau
- Weijie Su
arxiv_id: '2605.18106'
url: https://arxiv.org/abs/2605.18106
pdf_url: https://arxiv.org/pdf/2605.18106
published: '2026-05-17'
collected: '2026-05-20'
category: Training
direction: 优化器设计 · 等变更新 · 预训练
tags:
- optimizer
- symmetry
- equivariance
- SwiGLU
- MoE
- LLM pretraining
one_liner: 提出基于参数块对称群的等变优化器设计原则，为不同层定制更新规则，在LLM预训中超越AdamW
practical_value: '- **嵌入层与投影层优化**：推荐模型的实体/用户嵌入矩阵和最终的投影层可尝试行归一化（row-norm）或单边谱更新，利用左置换等变性，可能提升大规模嵌入训练稳定性。

  - **SwiGLU MLP 的定制更新**：若模型采用 SwiGLU 激活，其权重块的中间神经元置换对称性可指导设计 row-aware 或 column-aware
  更新，提升梯度信号对齐，加速收敛。

  - **MoE 路由器优化**：在多领域或多专家推荐中，MoE 路由矩阵可利用专家置换和偏移不变性，采用中心化行归一化或左谱更新，可能改善负载均衡和路由精度。

  - **系统化分块优化器设计**：整体思想可迁移——先分析模型各参数块的对称群，再选配等变更新规则，而非统一使用 Adam，尤其适用于推荐系统中多种异质参数（Embedding、Attention、MoE
  等）的混合架构。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前主流优化器（如 Adam/AdamW）逐坐标更新，破坏了神经网络参数空间固有的对称与等变性。不同参数块（嵌入矩阵、LM 头、SwiGLU MLP、MoE 路由器）分别服从不同的对称群，优化器的更新应与之等变，但缺乏统一的指导思想。

**方法**：提出对称兼容原则：对于每个权重块，梯度更新规则在其对称群作用下应为等变映射。首先统一了一般矩阵层的双正交等变更新（如 Muon、Scion、谱梯度等）。进而针对特定参数块推导新优化器：对嵌入和 LM 头，利用左置换与右正交等变性，得到单边谱、行范数、混合行范数/谱更新；对 SwiGLU MLP 的投影矩阵，中间神经元置换对称性导出 row-aware 与 column-aware 变体；对 MoE 路由器，专家置换和共享 logit 偏移不变性催生中心化行范数和左谱更新。所有规则组合成端到端的层定制优化器堆栈。

**关键结果**：在稠密及稀疏 MoE 语言模型预训练（Qwen3-0.6B、Gemma 3 1B、OLMoE-1B-7B、缩小版 gpt-oss）中，对称兼容更新在验证损失上全面优于对应 AdamW，并在多组实验中提升了训练稳定性。验证了按参数块对称性定制优化的有效性。
