---
title: 'hLLM: Single Pass Decoding for Generative Reranking'
title_zh: hLLM：单次前向解码生成式重排
authors:
- Emil Laftchiev
- Prachi Agrawal
- Moe Kayali
- Bixing Yan
- Qi Xu
- Zijie Lei
- Chen Qiu
- Zhi Hua
- Ke Li
- Luke Simon
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2609.01807'
url: https://arxiv.org/abs/2609.01807
pdf_url: https://arxiv.org/pdf/2609.01807
published: '2026-09-01'
collected: '2026-09-03'
category: RecSys
direction: 生成式重排 · 匈牙利解码
tags:
- Generative Reranking
- Hungarian Algorithm
- LoRA
- Knowledge Distillation
- Sinkhorn
- LLM Inference
one_liner: 用匈牙利算法从 LLM 隐状态矩阵直接解出排序序数，以 O(1) 次前向替代逐 token 自回归解码，实现 28ms 近无损重排
practical_value: '- 重排场景可将 LLM 输出从「逐 token 生成序数」改为「prefill 隐状态 → N×K 分数矩阵 → 匈牙利/LAPJV
  求解」，推理从 O(N·T) 降为 1 次前向；N≤50 时 solver 在 CPU 约 0.008ms，适合广告/电商候选集实时重排。

  - 训练用离线 teacher 蒸馏：大模型对每个 slate 生成完整排列，学生用 Sinkhorn 交叉熵拟合；无需在线 rollout，避免 exposure
  bias，蒸馏工程成本低。

  - 自注意力 scoring head 表现最好：candidate 表示过 2 层 self-attention 再投影到 K 个位置，优于线性 probe
  和 slot-query；LoRA 适配 backbone 后优势更明显。

  - 去除 teacher 的 reasoning trace 对排序质量几乎无损失，可直接输出序数，省去大量解码 token；LoRA 是吸收排列蒸馏信号的关键。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
自回归 LLM 做生成式重排时，每个候选序号都要串行解码，推理耗时主要由 decode 阶段决定：实验中带 reasoning 的 teacher 为 1807ms，其中 prefill 仅 28ms，而排序输出只是 N 个序数，格式高度受限。

**方法关键点**
- 只做一次 prefill，取每个候选 description 末 token 的隐状态 h_i。
- 轻量自注意力 head（2 层 Transformer encoder）对 h_i 做 item 间比较，输出 N×K 的 item–position 分数矩阵 M。
- 用 Hungarian 算法从 M 解最大权二分匹配，直接得到合法排列；解码为 O(1) 次前向，不依赖 N。
- 训练使用离线 teacher 排列蒸馏：teacher 提前生成完整排列，学生用 Sinkhorn 交叉熵做可微代理；backbone 用 LoRA r=64 适配。

**关键结果**
内部数据集上，HLLM 端到端 28ms，比带 reasoning 的 teacher 快 64.5×，比无 reasoning 的 teacher 快 3.1×；NDCG@1 0.1791、R@1 0.1652、AUC 0.5907，与 teacher 基本持平。Amazon Beauty 上同样达到 113ms 与 44.9× 加速。消融显示 self-attention head 最优，组合求解器开销不足总延迟 0.03%。

**一句话记忆**
排序只需输出序数，与其自回归生成，不如从 prefill 隐状态用 Hungarian 算法一次解码。
