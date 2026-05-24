---
title: 'Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State
  Reformulation'
title_zh: 均匀扩散模型再审视：留一法去噪与吸收态重构
authors:
- Samson Gourevitch
- Yazid Janati
- Dario Shariatian
- Umut Simsekli
- Eric Moulines
- Eric P. Xing
- Alain Durmus
affiliations:
- CMAP, Ecole polytechnique
- Institute of Foundation Models
- Inria, PSL Research University
- MBZUAI
- EPITA, LRE
arxiv_id: '2605.22765'
url: https://arxiv.org/abs/2605.22765
pdf_url: https://arxiv.org/pdf/2605.22765
published: '2026-05-21'
collected: '2026-05-24'
category: LLM
direction: 离散扩散模型优化 · 均匀扩散重参数化
tags:
- Discrete Diffusion
- Uniform Diffusion
- Leave-One-Out
- Masked Diffusion
- Text Generation
one_liner: 揭示了均匀扩散中标准参数化与训练目标的不匹配，提出留一去噪和吸收态重构改进生成质量
practical_value: " - 在离散扩散生成任务（如商品标题生成、评论生成）中，若使用均匀扩散，可直接换用 leave-one-out 参数化训练，无需模型改动即可提升生成质量。\n\
  \ - 吸收态重构将均匀扩散的采样过程分解为掩码扩散式操作，简化了推理实现，同时保留了联合分布，可降低工程复杂度并支持 remasking 策略。\n - 提出的\
  \ predictor-corrector 采样器和改进的温度采样技巧，无需额外训练，可用于控制生成多样性和质量，适合电商场景下需调控生成结果风格或创造性的应用。\n\
  \ - 结论表明扩散模型性能差距主要来自参数化和采样设计，而非边缘分布选择，这提示在推荐系统的扩散模型（如生成式推荐）中，应更多关注参数化策略而非生硬选择扩散类型。"
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：均匀扩散模型（UDM）在离散扩散生成中与掩码扩散模型（MDM）存在经验性能差距，但原因不明。作者发现标准 UDM 使用的桥接参数化并非由常规去噪后验优化，而是由一个“留一去噪后验”优化，该后验在预测每个干净 token 时不使用自身的噪声观测，导致 ELBO 与交叉熵训练目标不匹配。

**方法关键点**：
1. 严格刻画留一去噪后验，并推导出 denoiser、留一后验、score 之间的精确转换公式，允许灵活解耦参数化与训练目标。
2. 基于留一预测器，提出无需额外训练的 informed predictor-corrector 采样器和改进的温度采样，提升推理质量。
3. 提出吸收态重构：将均匀扩散的联合分布等价转换为吸收态过程，分解为类似掩码扩散的采样步骤，简化去噪后验，并自然支持 carry-over unmasking 和 remasking。

**关键结果**：在语言建模任务上，留一参数化一致提升 UDM 生成质量；吸收态重构匹配甚至超越掩码扩散模型。这表明 UDM 与 MDM 的差距主要由参数化和采样设计决定，而非扩散过程本身。
