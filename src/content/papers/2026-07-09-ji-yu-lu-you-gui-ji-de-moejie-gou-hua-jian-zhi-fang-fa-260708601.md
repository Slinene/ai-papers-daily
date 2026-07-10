---
title: It Takes a MAESTRO To Prune Bad Experts
title_zh: 基于路由轨迹的MoE结构化剪枝方法MAESTRO
authors:
- Palaash Goel
- Ayush Maheshwari
- Tanmoy Chakraborty
affiliations:
- Indian Institute of Technology Delhi
- NVIDIA
arxiv_id: '2607.08601'
url: https://arxiv.org/abs/2607.08601
pdf_url: https://arxiv.org/pdf/2607.08601
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: MoE模型压缩 · 全局重要性评估
tags:
- MoE
- Structured Pruning
- Markov Chain
- Routing
- Model Compression
- LLM
one_liner: 将专家激活轨迹建模为马尔可夫链，利用稳态分布评估全局重要性，实现MoE模型的高效剪枝
practical_value: '- 对于部署MoE大模型的场景（如DeepSeek、Mixtral），可直接采用MAESTRO在保持性能的同时压缩50%参数，显存占用和部署成本大幅下降，适合资源受限的在线推理环境。

  - 该方法通过建模专家激活的跨层转移依赖，计算全局重要性，可借鉴到推荐系统的多专家网络或多任务模型中，用于识别并裁剪冗余模块，提升模型效率。

  - 剪枝过程保持路由一致性（routing-congruent），减少剪切前后路由分布漂移，这一思想可迁移到推荐模型的召回/排序链路中，在模型压缩时保留原始决策逻辑。

  - 评估覆盖安全、偏见、伦理等领域，剪枝后模型跨任务方差更低，说明该方法产出更鲁棒的通才模型，适合需要兼顾多业务目标的平台（如电商搜索推荐同时需保证公平性与安全性）。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：稀疏激活的MoE语言模型推理效率高，但全部专家均需驻留内存，严重阻碍大模型部署。现有结构化剪枝方法多针对稠密Transformer，基于局部启发式评估专家重要性，忽视MoE路由跨层相互依赖的特性，导致剪枝性能不稳定。

**方法**：提出MAESTRO框架，将自回归生成过程中各层被激活的专家序列视为一条轨迹，建模为遍历马尔可夫链。通过计算该链的稳态分布，编码层间转移依赖，得到每个专家的全局重要性分数。剪枝时基于该分数，并引入路由一致性约束，确保剪枝后的路由行为与原始模型对齐，最终移除低分专家。

**结果**：在涵盖安全、偏见、伦理等五个领域的数据上评估，50%压缩率下，MAESTRO平均性能保持率比最强基线（如梯度、权重范数剪枝）高出10.61%，且跨任务性能方差显著更低，表明全局路由感知剪枝能获得更一致的泛化能力。
