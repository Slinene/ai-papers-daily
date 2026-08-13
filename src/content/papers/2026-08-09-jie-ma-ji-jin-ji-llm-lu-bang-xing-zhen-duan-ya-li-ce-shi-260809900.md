---
title: 'Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness'
title_zh: 解码级禁忌：LLM 鲁棒性诊断压力测试
authors:
- Tadanobu Chuyo Kamijo
- Ori Rottenstreich
- Javier Conde
- Gonzalo Martínez
- Pedro Reviriego
affiliations:
- University of the Ryukyus
- Technion
- Information Processing and Telecommunications Center (IPTC), Universidad Politécnica
  de Madrid
arxiv_id: '2608.09900'
url: https://arxiv.org/abs/2608.09900
pdf_url: https://arxiv.org/pdf/2608.09900
published: '2026-08-09'
collected: '2026-08-13'
category: Eval
direction: LLM 鲁棒性 · 解码级压力测试
tags:
- LLM robustness
- stress testing
- logit masking
- circumlocution
- evaluation
- instruction alignment
one_liner: 在 logit 空间动态屏蔽词边界主候选 token，强迫模型迂回表达，揭示离路径鲁棒性受规模与指令对齐影响
practical_value: '- 在电商文案生成、push 选词等场景，常需施加负面约束（如禁用竞品词、敏感词）。可用类似 logit 层动态 mask 的方式做上线前压力测试，提前暴露哪些约束会导致生成质量骤降或模型崩坏。

  - 对于要求严格结构化输出（如 JSON schema、工具调用参数）的 Agent 或生成式推荐链路，可借鉴 Taboo 在解码时强制屏蔽违规 token，评估模型在受限条件下的规划与生成鲁棒性，避免线上因约束过强而失效。

  - 结论提示：更大参数规模与指令后训练对齐显著改善离路径鲁棒性。选型或微调 LLM 用于推荐/Agent 时，可优先考虑对齐质量好的模型，并针对业务约束做专门指令微调。

  - 将 Taboo 作为数据增强原语：通过屏蔽高频 token 迫使模型生成同义改写或替代表达，可批量构造多样化的 query 改写、商品描述、推荐理由等合成数据。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：标准 LLM 评估集中在名义条件下的最优解码路径，掩盖了模型在真实部署中面对复杂系统提示、安全护栏、结构化约束时的鲁棒性不足。模型可能在 benchmark 上表现优异，但一旦被迫偏离熟悉的高频 token 序列就会失效。

**方法关键点**：提出 Decoding-Level Taboo，一种零提示诊断压力测试。与修改 prompt 不同，该方法在运行时直接干预 logit 空间，动态屏蔽词边界上的主要候选 token，迫使模型进行机器式迂回（circumlocution）。通过这种解码层级的“禁忌”约束，能有效探测模型是否具备可迁移的内部推理能力，而非依赖记忆化轨迹。

**关键结果**：在多个 open-weight 模型家族上评估发现，离路径鲁棒性受参数规模和指令后训练对齐双重影响：模型越大、对齐越好，鲁棒性越强。此外，Taboo 可作为生成多样化合成数据、压力测试运行时安全护栏、审计模型部署前可靠性的通用原语。
