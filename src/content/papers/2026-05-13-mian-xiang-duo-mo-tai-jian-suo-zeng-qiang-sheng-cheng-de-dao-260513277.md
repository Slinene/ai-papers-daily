---
title: Utility-Oriented Visual Evidence Selection for Multimodal Retrieval-Augmented
  Generation
title_zh: 面向多模态检索增强生成的效用导向视觉证据选择
authors:
- Weiqing Luo
- Zongye Hu
- Xiao Wang
- Zhiyuan Yu
- Haofeng Zhang
- Ziyi Huang
affiliations:
- Arizona State University
- Texas A&M University
- Morgan Stanley
arxiv_id: '2605.13277'
url: https://arxiv.org/abs/2605.13277
pdf_url: https://arxiv.org/pdf/2605.13277
published: '2026-05-13'
collected: '2026-05-16'
category: Multimodal
tags:
- Multimodal RAG
- Evidence Selection
- Information Gain
- Surrogate Model
- Discriminative Utility Estimation
one_liner: 通过信息增益与潜在有用性变量重新定义证据选择，并用轻量替身模型高效估计效用，无需训练即可超越基线
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有多模态 RAG 的证据选择依赖语义相似度或 CLIP 风格的相关性评分，常常选出视觉上相似但对回答问题无用的图像。这种“相关性≠生成效用”的错配严重限制了多模态检索增强的潜力，亟需一种直接衡量证据对模型输出影响的效用导向选择策略。

**方法关键点**  
- 从信息论出发，将证据效用定义为条件证据于输出分布的信息增益（IG），即 `D_KL(P(Y|C=c,q) || P(Y|q))`。  
- 由于答案空间 IG 难以直接优化，引入潜在的二元**有用性变量 Z**，并理论证明在温和假设下，按 Z 的 IG 排序等价于答案空间排序，从而将高维输出分布的比较简化为估计 `P(Z=1|C=c,q)`。  
- 构建**辅助判别任务**：向模型询问“该图像对回答问题是否有帮助？”，从最终层 logit 中获取“True”的 logit 作为有用性得分。  
- 提出**替身加速流水线**：使用轻量多模态模型（如 Qwen3-VL-2B）对所有候选证据并行计算有用性得分，选取 Top-K 后仅调用一次大型主模型生成最终答案，大幅降低计算开销。整个流程无需训练，仅依赖推理。

**关键实验**  
- 在两个基准 MRAG-Bench 和 Visual-RAG 上测试，涵盖 Qwen3-VL、MiniCPM‑V4.5、Gemma‑3‑12B、Ovis2.5、InternVL3.5 等 5 个模型族。  
- 与多种基线对比：CLIP/SigLIP 等嵌入方法、MLLM 重排序器（GME、UniME‑V2、LamRA‑Rank 等）以及答案空间不确定性方法。  
- 我们的方法在多数设定下取得最优，尤其 Visual‑RAG 上最高提升 **+16.18**（Ovis2.5‑9B, K=1）；轻量替身（2B）性能与 8B+ 主模型高度一致，Top‑1 平均差距仅 0.38（MRAG‑Bench）和 0.18（Visual‑RAG）。  
- 计算成本上，2B 替身的预填充 FLOPs 不足 8B 主模型的 25%，且判别式估计的解码 FLOPs 仅为答案空间方法的 **1/20 以下**。

**最值得记住的一句话**  
将证据选择从“检索相关性”转向“模型有用性”，并用轻量替身完成效用排序，是多模态 RAG 高效、稳定提升的可行路径。
