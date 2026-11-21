---
title: 'dLoop: Looped Diffusion Language Models via Recurrent Latent Refinement'
title_zh: dLoop：循环潜在精炼的扩散语言模型
authors:
- Handa Li
- Pengxiang Li
- Mingyu Cao
- Xilu Wang
- Li Shen
- Da Li
- Lu Yin
affiliations:
- University of Surrey
- The Hong Kong Polytechnic University
- Sun Yat-sen University
- University of York
- Shenzhen University of Advanced Technology
arxiv_id: '2611.26275'
url: https://arxiv.org/abs/2611.26275
pdf_url: https://arxiv.org/pdf/2611.26275
published: '2026-11-19'
collected: '2026-11-21'
category: LLM
direction: 扩散语言模型循环精修加速
tags:
- Diffusion Language Models
- Recurrent Refinement
- Inference Acceleration
- Latent Computation
- Parallel Decoding
one_liner: 通过Prelude-Loop-Coda结构对同一掩码状态循环共享参数中间块，提升扩散语言模型推理准确率与效率
practical_value: '- 生成式推荐中生成 Semantic ID 或 query 时，可借鉴“先预填后循环精修”：对同一部分掩码状态重复共享参数的中间块，让未确定位置充分交互后再提交，提升生成质量而不增加额外参数或大量去噪步。

  - 面向电商文案、广告标题等对准确率敏感的场景，可将推理计算从“增加采样步数或更长 CoT”转为“对低置信输出施加可选循环精修”，在固定延迟预算下提高可靠 token
  比例。

  - Agent 任务规划或工具选择生成可循环更新未确定槽位，而非一次性生成完整计划，参数共享可减少额外训练成本，且对慢/不稳定轨迹有针对性增益。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：扩散语言模型支持并行生成，但需大量去噪步，因为每步只有少量 token 足够可靠可提交。现有加速方法集中于优化置信学习或提交策略，却只在单次前向输出上操作，提示、已提交 token 与未提交位置的信息未充分整合，仅改提交策略无法改善底层表征。

**方法**：将预训练扩散语言模型重构为 Prelude-Loop-Coda 架构，对同一部分掩码状态循环应用参数共享中间块。每个额外循环不推进去噪过程，而是提供更多潜在计算，使未提交位置的信息持续交互，提交前表征更充分整合。

**结果**：在 GSM8K、MATH、MBPP、HumanEval 上达到最高或并列最高准确率。按循环计算调整 TPF 后，在全部四个基准上准确率和 TPF 均超 Fast-dLLM，在三个基准上超 dParallel，准确率均超 d3LLM（但 d3LLM TPF 更高）。机制分析显示额外循环主要帮助慢/不稳定轨迹，未提交位置的更新驱动 token 决策变化，表明提交前潜在计算是 DLM 加速的一条独立路径。
