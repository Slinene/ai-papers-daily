---
title: 'Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge
  Internalization'
title_zh: 注入、对齐、恢复：面向无检索文档知识内化的分阶段后训练
authors:
- Qian Kou
- Xiaofeng Shi
- Xiaosong Qiu
- Hua Zhou
affiliations:
- Beijing Academy of Artificial Intelligence (BAAI)
arxiv_id: '2608.20281'
url: https://arxiv.org/abs/2608.20281
pdf_url: https://arxiv.org/pdf/2608.20281
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: LLM 后训练 · 文档知识内化
tags:
- LLM
- Post-Training
- Knowledge Internalization
- Retrieval-Free QA
- Model Merging
- Document QA
one_liner: 提出IAR三阶段后训练框架，将固定文档语料内化为LLM参数知识，兼顾领域QA与通用能力
practical_value: '- 在电商/客服场景需要将商品库、政策文档内化到LLM以支持无检索问答时，可将文档转为多种重构目标（续写、改写、指令条件重建）做注入，比单纯
  continued pretraining 更利于后续指令跟随。

  - 三阶段分离有效：先注入领域知识，再做答案监督的QA对齐，最后将领域模型与基座指令模型合并恢复通用能力——这种“领域适配+模型合并”模式可直接复用到导购Agent、店铺客服模型，避免灾难性遗忘。

  - 若算力受限，LoRA/FAPM 等参数高效方法在部分通用指标上可赢，但 IAR 在领域内化与通用能力平衡上更稳；业务中优先选择 IAR 式全量阶段或混合方案。

  - 评估时同时报告领域QA准确率和 IFEval/MMLU 等通用指标，避免只盯领域指标导致通用能力坍塌；业务中应建立类似的领域-通用双维度评测。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RAG 依赖检索，但不少部署场景（延迟、隐私）需要模型不检索就能回答关于固定文档集合的问题，即文档知识内化。现有 continued pretraining 或 SFT 容易顾此失彼，领域性能与通用能力难平衡。

**方法关键点**：IAR 分三阶段。Inject 阶段把源文档转成续写、改写和指令条件重建三种目标，让模型结构化吸收文档知识，而非简单继续预训练。Align 阶段用仅答案监督的 QA 数据调整注入后的模型，让模型学会在无证据时直接产出答案。Recover 阶段将领域适配模型与基座指令模型合并，恢复通用指令跟随、知识和推理能力。

**结果**：在 Common Corpus 和 CCI 两个数据集上，覆盖 Llama、Phi、Qwen、SmolLM 多个模型家族，IAR 在 8 个数据集-模型设置中有 7 个设置全部四项指标超过 Vanilla SFT，领域 QA 准确率平均提升 3.6 个百分点，IFEval、MMLU、MSBench 平均通用性能提升 12.1 个百分点。扩展基线中 LoRA 和 FAPM 可在个别通用指标上占优，但 IAR 在保持领先领域内化的同时通用能力最强之一。
