---
title: 'Working Around the Compute Ceiling: Byte-Exact Memory in Galahad Makes LLM
  Reading a One-Time Cost LLM Reading a One-Time Cost'
title_zh: 绕过计算上限：Galahad 字节精确记忆使 LLM 阅读成为一次性成本
authors:
- Sietse Schelpe
affiliations:
- Corbenic AI
arxiv_id: '2609.39358'
url: https://arxiv.org/abs/2609.39358
pdf_url: https://arxiv.org/pdf/2609.39358
published: '2026-09-30'
collected: '2026-10-04'
category: LLM
direction: LLM 推理优化 · KV cache 复用
tags:
- KV cache
- LLM serving
- stateful inference
- memory layer
- exact match
- long context
one_liner: Galahad 为 vLLM/SGLang/llama.cpp 提供字节精确 KV 记忆层，将重复文档阅读变成一次性成本
practical_value: '- 搜广推场景中大量 prompt 前缀重复（商品描述、用户历史、知识库、广告素材），可对固定上下文离线预计算 KV 并持久化，在线按需加载，避免每次重算；字节精确匹配
  + fail-closed 机制保证缓存不会改变答案，适合线上一致性要求高的场景。

  - 对长上下文任务（如用户长期行为序列、商品详情问答），可结合检索式片段注入：Blaise 只把必要片段送入模型，比全量投喂或纯 RAG 更省 token、更准；实验里
  100/100 vs 调优 RAGFlow 的 77/100。

  - 工程实现上，分段缓存与恢复要校验 bit-identical，避免因缓存错误影响线上 A/B 或模型输出；如果加载校验不过则回退重算，可作为推理网关的通用设计。

  - 成本收益可量化：缓存构建的能耗在少量请求后即可收回，适合高频重复查询的电商知识库、活动规则问答、客服机器人等场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM 服务通常无状态，同一文档被多次提问时，每次都要从第一个 token 重新计算注意力状态。论文统计七个真实数据集，98.7% 的 prompt token 是模型已读过的文本，大量计算被浪费。

方法：提出 Galahad，为 vLLM、SGLang、llama.cpp 增加记忆层。Taliesin 按字节块保存文本对应的 KV 状态，下次请求中出现相同字节时直接加载，不再重算；Blaise 保存文档本身，只把问题所需片段传给模型。恢复状态要求 bit-identical，加载不通过则自动回退重算。

结果：在 97,000 token 语料中隐藏 100 个事实的召回测试上，Gemma 4 31B 单独用 Taliesin 在 llama.cpp 上答对 98/100，耗时 3.0s、能耗 572J；对比无 Galahad 只能保留最后 12,000 token，答对 10/100，耗时 9.3s、能耗 2,754J。加上 Blaise 后，每问只读约 668 token，三个运行时均答对 100/100，耗时 0.59-0.64s、能耗 200-213J；调优 RAGFlow 答对 77/100。存储语料一次性成本约 100s、28kJ，13 个问题后收回。恢复后所有 262,144 个输出 logits 完全一致。
