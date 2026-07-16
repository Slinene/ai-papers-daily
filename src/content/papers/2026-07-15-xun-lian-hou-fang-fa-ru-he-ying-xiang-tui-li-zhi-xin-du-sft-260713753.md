---
title: 'Post-Training Shifts Confidence: A Three-Stage Analysis of How SFT, RL, and
  OPD Shape Pre-, Intra-, and Post-CoT Calibration'
title_zh: 训练后方法如何影响推理置信度：SFT、RL、OPD三阶段校准分析
authors:
- Shuhao Li
- Guodong Du
- Anhao Zhao
- Wanyu Lin
- Tianyu Yuan
- Xiaoyu Shen
affiliations:
- Eastern Institute of Technology, Ningbo
- The Hong Kong Polytechnic University
arxiv_id: '2607.13753'
url: https://arxiv.org/abs/2607.13753
pdf_url: https://arxiv.org/pdf/2607.13753
published: '2026-07-15'
collected: '2026-07-16'
category: LLM
direction: LLM推理校准与后训练方法相互作用
tags:
- confidence calibration
- chain-of-thought
- reinforcement learning
- supervised fine-tuning
- on-policy distillation
- position-aware confidence
one_liner: 揭示SFT、RL、OPD在推理前/中/后校准特性迥异，并提出位置感知置信度PosConf大幅提升聚合与早停性能。
practical_value: '- **多路径推理置信度投票**：在Agent或RAG系统生成多个推理路径时，可借鉴RL模型的trace-level置信度进行加权投票，并仅在“路径承诺”后的可靠位置提取置信度，避免前期噪声，提升最终答案聚合准确率。

  - **推理早停控制**：对强延迟约束的在线推荐场景，可利用SFT模型的在线置信度信号做early stopping，动态终止低可能性生成，节省token消耗；OPD模型的早期置信度可用于难度预估，直接放弃高难度请求，进一步降低成本。

  - **位置感知置信度使用**：通用原则——不从推理全程提取置信度，而是针对不同训练策略识别可靠区间（如OPD仅用前段，RL用后段），可提升置信度的校准性和决策有效性，适用于生成式推荐的理由生成、对话Agent的多轮规划等。

  - **后训练方式选择依据**：若业务侧重推理前难度预估（如请求过滤），优先OPD；若需在线中断低质生成，优先SFT；若需高可靠的多路聚合，优先RL。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM通过SFT、RL、OPD等后训练方法显著提升推理能力，但评估多停留在最终答案正确率，这些方法如何影响推理过程中的置信度校准尚不清晰。用户信任、推理中断、多路聚合等均依赖可靠的置信度信号，因此需要系统分析不同训练方式对校准的影响。

**方法**：提出三阶段校准框架——推理前（pre-CoT）置信度用于难度估计，推理中（intra-CoT）用于early stopping，推理后（post-CoT）用于答案聚合。在数学推理基准上，控制比较SFT、RL、OPD三种模型在各阶段的表现，并进一步分析置信度随推理token位置的变化规律。基于发现的位置依赖特性，提出PosConf策略：仅从每个方法的可靠相对位置区间（如RL的后段、OPD的前段）提取置信度。

**结果**：OPD在推理前校准最好，SFT在推理中在线信号最有用，RL在trace-level聚合最可靠。PosConf将RL答案聚合在多数投票基础上提升6.1个点，OPD早停在严格token预算下最多提升4.3个点，且避免了OPD后期的逆校准区间。
