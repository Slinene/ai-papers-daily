---
title: Improved Large Language Diffusion Models
title_zh: 改进的大语言扩散模型
authors:
- Shen Nie
- Qiyang Min
- Shaoxuan Xu
- Zihao Huang
- Yuxuan Song
- Yong Shan
- Yankai Lin
- Wayne Xin Zhao
- Chongxuan Li
- Ji-Rong Wen
affiliations:
- Renmin University of China
- Beijing Key Laboratory of Research on Large Models and Intelligent Governance
- Engineering Research Center of Next-Generation Intelligent Search and Recommendation,
  MOE
- ByteDance Seed
arxiv_id: '2606.25331'
url: https://arxiv.org/abs/2606.25331
pdf_url: https://arxiv.org/pdf/2606.25331
published: '2026-06-23'
collected: '2026-06-25'
category: LLM
direction: 大语言模型扩散训练与推理优化
tags:
- Diffusion Language Model
- Masked Diffusion
- Bidirectional Attention
- Pretraining
- Instruction Tuning
- Variable-length Generation
one_liner: 8B 全双向掩码扩散语言模型从零预训练 12T tokens，大幅超越 LLaDA 并与自回归模型竞争
practical_value: '- 生成式推荐场景可尝试用扩散模型替代自回归生成，尤其适合需要高吞吐、非自回归解码的物品标题、描述或语义 ID 生成。

  - 全双向注意力在用户序列建模、查询改写等需要全局上下文的推荐任务中可能提升效果。

  - 掩码扩散训练与变长生成技术可应用于对话式推荐响应生成，平衡效率与多样性。

  - 置信度评分为推荐候选集排序提供新思路，如计算 item 置信度辅助精排。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前大语言模型普遍采用自回归范式，扩散语言模型虽有全双向注意力等优势，但性能仍落后较多。LLaDA 已初步证明非自回归模型的 LLM 能力，本文进一步探索如何显著缩小与自回归模型的差距。

**方法**：提出 iLLaDA，一个 8B 参数的掩码扩散语言模型，从零开始使用全双向注意力预训练 12T tokens，并在 25B tokens 指令数据上持续用掩码扩散目标微调 12 个 epoch。为提升生成效率，引入变长生成策略；针对多项选择评估，设计基于置信度的打分方法。

**结果**：iLLaDA 在通用、数学和代码基准上全面超越 LLaDA：BBH 提升 21.6 点，ARC-Challenge 提升 14.9 点，MATH 提升 14.5 点，HumanEval 提升 16.5 点。在部分任务上能比肩 Qwen2.5 7B，证明全双向扩散训练可构建强语言模型，为 LLM 提供一条有竞争力的非自回归路径。
