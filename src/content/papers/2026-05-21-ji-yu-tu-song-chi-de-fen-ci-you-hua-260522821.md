---
title: Tokenisation via Convex Relaxations
title_zh: 基于凸松弛的分词优化
authors:
- Jan Tempus
- Philip Whittington
- Craig W. Schmidt
- Dennis Komm
- Tiago Pimentel
affiliations:
- ETH Zurich
- Kensho Technologies
arxiv_id: '2605.22821'
url: https://arxiv.org/abs/2605.22821
pdf_url: https://arxiv.org/pdf/2605.22821
published: '2026-05-21'
collected: '2026-05-24'
category: Training
direction: 分词优化·凸松弛
tags:
- tokenisation
- convex optimization
- linear programming
- BPE
- language model
- compression
one_liner: 将分词器构建转化为线性规划，用凸优化求解全局最优词表，压缩率和语言模型性能超越贪心算法
practical_value: '- 可将分词目标显式建模为最小化编码成本，利用凸优化求解全局词表，获得更优压缩率，减少电商商品描述等文本的 token 序列长度，降低
  LLM 推理成本。

  - 提供严格的最优性下界，用于定量评估现有分词器（如 BPE）的优化差距，指导词汇量设置。

  - 方法可作为 BPE 的离线替代，训练时直接使用 ConvexTok 词表，无需改动下游模型架构。

  - 注意：目标函数设计依赖具体语料，在生成式推荐中可考虑引入业务指标（如文本编码后的推荐效果）作为优化目标，但需定制化实现。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：当前主流分词算法如 BPE 和 Unigram 均为贪心算法，只做局部最优合并，忽略词汇表整体的全局最优性，导致压缩效率受限，且向下游语言模型传递次优表示。直接求解最优分词器是 NP 难的，因此需高效的近似方法。

**方法**：作者将分词器构建形式化为一个线性规划问题，目标是最小化语料在给定词汇表下的总编码长度（或等价比特数）。通过对合并操作连续松弛，利用凸优化工具高效求解，得到词表分配，新算法命名为 ConvexTok。该方法还给出最优目标值的下界，可量化所得解的优化程度。

**结果**：在多语言文本上，ConvexTok 在字符编码效率、词汇利用率等内禀指标上一致超越 BPE 和 Unigram；语言模型以同样的架构训练后，bits-per-byte (BpB) 平均降低 0.02-0.05；下游任务 GLUE/XGLUE 得分有提升但一致性较弱。在常见词汇量（32k-128k）下，ConvexTok 的解被证明在最优目标的 1% 以内，接近全局最优。
