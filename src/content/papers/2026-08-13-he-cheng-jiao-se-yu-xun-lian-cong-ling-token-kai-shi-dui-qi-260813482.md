---
title: 'Synthetic Persona Pretraining: Alignment from Token Zero'
title_zh: 合成角色预训练：从零 token 开始对齐
authors:
- Julian Minder
- Viktor Moskvoretskii
- Raghav Singhal
- Difan Jiao
- Andy Arditi
- Shaobo Cui
- Yiderigun Borjigin
- Kartik Bali
- Stefan Krsteski
- Harsh Raj
affiliations:
- EPFL
- MATS
- University of Toronto
- Northeastern University
- SJTU
arxiv_id: '2608.13482'
url: https://arxiv.org/abs/2608.13482
pdf_url: https://arxiv.org/pdf/2608.13482
published: '2026-08-13'
collected: '2026-08-15'
category: Training
direction: LLM 对齐 · 预训练阶段 persona 注入
tags:
- Synthetic Persona Pretraining
- Alignment
- Pretraining
- Persona Binding
- Jailbreak Robustness
- Constitution Following
one_liner: 在预训练阶段注入合成角色反思，从 token zero 安装助手人格，提升对齐与鲁棒性
practical_value: '- 若业务中有基于 LLM 的导购助手或 Agent，可在领域继续预训练阶段混入带品牌语调/平台规范的第一人称反思数据，让模型早期建立期望
  persona，减少后期 RLHF/SFT 对齐成本。

  - 借鉴 persona binding 思路：在通用预训练后，用少量用户-助手对话数据将预训练安装的 persona 绑定到特定助手身份，可能提升业务场景下响应一致性。

  - 实验结果提示早期干预优于后期微调，且优势随预训练数据量增加而扩大；若预算允许，应尽早注入领域价值观而非仅靠后训练微调。

  - 注意该方法主要针对通用对齐，电商搜索推荐中的直接迁移价值有限，需自行构造领域反射数据并验证对推荐指标无损害。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：当前 LLM 的 assistant identity 和价值观通常在预训练后引入，行为先验已固化，对齐只是薄层覆盖，容易引发后续失对齐。

**方法关键点**：
- 用规范性价值宪法生成第一人称反思，注释预训练文档；
- 在标准预训练中混合原始文档与这些反思，以交叉熵损失训练，从 token zero 安装期望 persona；
- 后训练在用户-助手对话数据上进行 persona binding，将预训练安装的 persona 绑定到 assistant identity。

**关键结果数字**：在最多 3B 参数、500B tokens 的模型上，SPP 提升 constitution following 和 jailbreak 鲁棒性，降低 OOD 道德困境中的 misalignment rate，同时保持能力。与仅在预训练末尾引入 SPP 相比，从 token zero 开始优势明显，且该优势依赖 persona binding，随预训练预算增加而扩大。
