---
title: 'Where Should a Document Live: Context, Representations, or Parameters?'
title_zh: 文档应该存在哪里：上下文、表示还是参数？
authors:
- Nathanaël Carraz Rakotonirina
- Momchil Hardalov
- Gonzalo Iglesias
- Adrià de Gispert
affiliations:
- Amazon AGI
arxiv_id: '2609.17346'
url: https://arxiv.org/abs/2609.17346
pdf_url: https://arxiv.org/pdf/2609.17346
published: '2026-09-15'
collected: '2026-09-16'
category: RAG
direction: 知识注入位置对比 · KV vs LoRA
tags:
- Knowledge Injection
- KV Cache
- LoRA
- RAG
- Adapter Composition
- Catastrophic Forgetting
one_liner: 系统对比知识注入三种位置，Cartridges(KV)在多文档检索中唯一匹配 ICL，但高压缩下有遗忘
practical_value: '- 电商/搜索的高频文档（商品详情、活动规则、广告素材）可以预计算成 KV-cache adapter（Cartridge）在线复用，避免每次查询重复
  prefill 原文；20× 压缩下加载 10 个 adapter 约 30–50ms，10× token 减少约带来 100× prefill FLOPs 下降，适合低延迟在线服务。

  - 多文档组合场景下，不要用「每个文档训一个 LoRA 再合并」替代检索，尤其信息密集任务；论文显示一个 distractor 就能让合并效果崩溃（FinQA
  k=3 时 34.5→4.9）。若必须用参数化方式，joint training 优于 adapter merging，但仍不如可拼接的 KV-cache。

  - 训练知识注入 adapter 时，用蒸馏目标（teacher = 原文 in context，student = adapter）比普通 next-token
  CE 平均高 4 个点，在数值推理/金融类任务上收益更大；可直接迁移到商品属性提取、活动规则问答等场景。

  - 上线前要评估通用能力退化：LoRA 低秩约束更稳，full FT 和大 MLP adapter 遗忘严重；如果使用 Cartridge，可考虑用 Compaction
  初始化 KV cache 来缓解 HumanEval 类代码能力下降（论文中下降了 16 点）。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM 面对新知识时通常有三种放置方式：上下文、参数、表示。此前对比多使用 Wikipedia 等预训练已见过的文档，测的是 recall 而非真正注入新知识。论文在五个知识密集基准上做受控比较，覆盖单文档 oracle 和多文档检索两种现实设置。

**方法关键点**
- 比较 7 种方法：No context、ICL、Cartridges（训练 KV cache 前缀）、Compaction（注意力匹配压缩 KV）、LoRA、MLP adapters、full fine-tuning。
- 训练数据用 Self-Study 合成 QA：GPT-OSS 120B 生成问题，目标模型作为 answer generator，每 chunk 生成 20 问。
- 目标函数采用蒸馏：teacher 是原文 in context 的模型，student 是无 context 的 adapter 模型，KL 匹配分布；比 next-token CE 平均高约 4 点。
- 多文档组合：表示方法拼接 KV cache，参数方法对权重做平均合并；检索 top-k chunks。

**关键实验结果**
- 单文档 2× 压缩：Compaction 平均 73.4 接近 ICL 的 73.6，Cartridges 70.6，LoRA 64.5，full FT 59.8。
- 跨压缩率：Cartridges 几乎不降（LongHealth 从 81.1 到 77.3 @100×），Compaction 高压缩急剧退化（FinQA 从 66.4@2× 跌到 19.3@20×），LoRA/MLP 在高存储匹配下平台化。
- 多文档检索：Cartridges 是唯一随 k 增大保持或提升的方法（LongHealth k=1→10：70.8→83.2）；Compaction 单调下降（TechQA 65.4→26.4）；LoRA 合并崩溃（QuALITY k=10 降到 44.2，FinQA k=3 仅 4.9）。
- 遗忘：Cartridges 平均降 6%，其中 HumanEval 降 16 点；Compaction 几乎无遗忘；LoRA 保持；full FT 遗忘严重。

**最值得记住的一句话**
多文档新知识注入场景优先选可拼接的 KV-cache Cartridges，而不是参数化 LoRA 合并；低秩约束和蒸馏目标是保持通用能力、提升注入效果的关键。
