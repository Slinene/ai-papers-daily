---
title: 'Doc-to-Atom: Learning to Compile and Compose Memory Atoms'
title_zh: 'Doc-to-Atom: 学习编译和组合记忆原子'
authors:
- Xingjian Diao
- Wenbo Li
- Yashas Malur Saidutta
- Avinash Amballa
- Lazar Valkov
- Srinivas Chappidi
affiliations:
- AI Center-Mountain View, Samsung Electronics
- Dartmouth College
arxiv_id: '2606.12400'
url: https://arxiv.org/abs/2606.12400
pdf_url: https://arxiv.org/pdf/2606.12400
published: '2026-06-10'
collected: '2026-06-11'
category: LLM
direction: 文档参数记忆 · 原子化知识组装
tags:
- parametric memory
- context distillation
- LoRA
- atom decomposition
- query routing
- long-document reasoning
one_liner: 将文档分解为语义类型原子并编译为 micro-LoRA，查询时动态路由组合相关原子，减少干扰并提升长文档推理性能。
practical_value: '- **长文档的知识原子化存储**：对电商商品详情、政策法规等长文本，可预分解为独立语义原子（事实、属性、事件等），每个原子生成微型
  LoRA 适配器，降低在线推理时的内存占用（文中内存减少 44-85%）。

  - **查询相关性驱动的动态适配器组装**：借鉴两阶段路由机制（近似索引 + 交叉编码器重排），只挑选与当前 query 最相关的 top-K 原子微调器组合，避免单一适配器对所有查询造成干扰，同时自然实现无关查询拒答（拒绝率可超
  85%）。

  - **稀疏门控与知识保护**：利用稀疏掩码限制每个原子只写入部分层/模块，结合 L2 或 null-space 约束防止覆盖基础模型能力，这对在多任务环境下避免灾难性遗忘特别有用。

  - **多目标训练与课程调度**：同时优化蒸馏、路由、无关抑制、组合一致性等损失，并通过分阶段课程增加检索原子数，可稳定训练复杂参数记忆系统，相关损失设计可直接复用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
长文档推理受限于 Transformer 的二次注意力复杂度，上下文蒸馏可将知识压缩到模型参数中，但现有方法（如 Doc-to-LoRA）为每个文档生成一个单一 LoRA，导致三方面问题：(1) 无关查询干扰——即使 query 不相关，适配器仍会修改隐藏状态；(2) 有限的组合召回——扁平低秩适配器难以选择性提取众多异构事实；(3) 长文档扩展性差——固定容量的适配器压缩全部内容会稀释关键信息。

**方法**
Doc2Atom 把文档分解为语义类型的**知识原子**，每个原子作为最小的可检索和可写入单元，包含类型、内容、检索文本、答案承载标志等元数据。离线阶段，共享文本编码器（复用基座前几层）提取原子嵌入，再通过记忆编译器生成每个原子的**溯源键**、**微 LoRA 因子**、可选微 KV 原型以及**稀疏掩码**。在线阶段，查询编码后经两阶段路由（余弦最大内积搜索 + 可选交叉编码器重排）选出 top‑K 原子，其微 LoRA 因子按路由权重加权求和，并点乘稀疏掩码，组装成查询专属适配器注入冻结基座。
训练采用教师‑学生范式：教师使用完整文档+查询，学生仅用查询加组装适配器，通过多目标损失联合优化（语言建模、KL 蒸馏、路由二元交叉熵、无关查询范数惩罚、知识保护 L2 约束、稀疏正则化、组合一致性对称 KL 等），并采用课程调度逐步增加检索原子数与损失权重。

**关键结果**
在 Gemma‑2‑2B 和 Qwen3‑4B 两个基座上，于 SQuAD、DROP、ROPES、2WikiMultihopQA、QASPER 及 LongBench 八个子集上评估。Doc2Atom 整体 F1 在 Gemma 上达到 37.99（对比最佳单适配器变体 D2Latom 的 29.41），在 Qwen3 上达到 35.72（vs 29.30），且在 LongBench 上零样本 F1 最高提升 6 倍。无关查询拒绝 F1 普遍超过 85%，远超基线（常低于 40%）。同时，内部化时额外 GPU 内存减少 44‑85%，但编译延迟稍高（2.1s vs 0.31s）。

**核心贡献一句话**
将文档内部化从单一适配器升级为可组合的原子记忆库，按查询需求选择性组装，显著提升了参数化记忆的精准度、抗干扰能力和长文本扩展性。
