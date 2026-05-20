---
title: Probability-Conserving Flow Guidance
title_zh: 概率守恒流形引导：自适应流形引导方法AdaMaG
authors:
- Parsa Esmati
- Junha Hyung
- Amirhossein Dadashzadeh
- Jaegul Choo
- Majid Mirmehdi
affiliations:
- University of Bristol
- KAIST
arxiv_id: '2605.20079'
url: https://arxiv.org/abs/2605.20079
pdf_url: https://arxiv.org/pdf/2605.20079
published: '2026-05-19'
collected: '2026-05-20'
category: Other
direction: 扩散模型引导 · 概率守恒
tags:
- CFG
- Diffusion Models
- Flow Matching
- Guidance
- Probability Conservation
- Image Generation
one_liner: 提出零推理成本的AdaMaG，通过散度与分数平行项衰减，在流扩散生成中保持概率守恒，解决CFG强引导下的饱和与伪影。
practical_value: '- **扩散生成式推荐/内容生成的引导优化**：若使用扩散模型生成电商文案或创意，强条件引导常导致失真，可直接用AdaMaG替换CFG组合公式，不增加推理耗时，保持生成质量与条件符合度。

  - **引导问题的理论分析框架**：基于连续性方程分解的散度项和分数平行项，可迁移分析文本扩散模型中引导过强的崩塌现象，帮助设计衰减策略。

  - **时间依赖调度即插即用**：AdaMaG的时间衰减调度是独立于模型的、无需重训练的启发式规则，可在现有流匹配/扩散管道中直接嵌入，适合快速落地验证。

  - **可控生成与真实度平衡**：强约束场景（如节日大促风格控制）下，可利用分数平行项衰减控制去饱和程度，稳定生成质量。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有扩散/流模型的Classifier-Free Guidance (CFG) 为线性速度/分数组合，忽略生成流形几何，强引导下破坏概率守恒，使采样轨迹偏离数据流形，导致过饱和与幻觉。

**方法**：通过连续性方程解析引导对概率流的影响，将引导效应分解为**散度项**和**分数平行项**，二者在参数化变换下不变。理论证明采样靠近数据流形时散度项结构发散，据此提出**自适应流形引导 (AdaMaG)**：引入**时间依赖的衰减调度**以压制散度项，同时**衰减分数平行项**防止偏离流形，计算零开销。推导表明多数减轻CFG饱和的启发式方法可统一为该分解下的对应操作。

**结果**：在图像生成基准上，AdaMaG显著提升高引导强度下的真实感，减少伪影与幻觉，实现可控的去饱和。
