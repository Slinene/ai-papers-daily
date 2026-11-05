---
title: Where Should a KV-Cache Repair Budget Go? Distractor Structure and Contextual
  Compatibility in Non-Prefix Reuse
title_zh: 非前缀 KV 缓存复用中修复预算应分配到哪里？干扰结构与上下文兼容性
authors:
- Yuxing Peng
- Zhiqing Tang
- Weijia Jia
affiliations:
- Beijing Normal University, Zhuhai
- Institute of Artificial Intelligence and Future Networks, Beijing Normal University
- Guangdong Key Lab of AI and Multi-Modal Data Processing, Beijing Normal-Hong Kong
  Baptist University
arxiv_id: '2611.06397'
url: https://arxiv.org/abs/2611.06397
pdf_url: https://arxiv.org/pdf/2611.06397
published: '2026-11-04'
collected: '2026-11-05'
category: RAG
direction: 非前缀 KV-cache 复用 · 修复预算分配
tags:
- KV cache
- non-prefix reuse
- RAG
- context compatibility
- budget allocation
- LLM inference
one_liner: 发现非前缀 KV-cache 复用中修复预算应集中于答案承载块，且重新计算目标块优于插入完整预填充 KV。
practical_value: '- 在电商 RAG/工具检索场景（如商品知识库问答、API 文档助手）采用非前缀 KV-cache 复用时，若修复预算有限（如仅能重算5%
  token），应优先重算包含答案的目标块，而非分散修复多个干扰块；因为可恢复损害分散在其它块，恢复少数收效甚微。

  - 警惕检索块类型同质性：当上下文中多个文档块类型相似（如全是商品描述或全是 API 文档）时，非前缀复用性能损失更大，可考虑对不同类型块采用差异化缓存策略或额外校验。

  - 重算目标块时，直接基于复用后的上下文缓存进行重算（上下文兼容）比插入其完整预填充 KV 更有效且成本更低，说明位置与上下文调整比完全重算更重要；工程实现中可优先调整位置而非重算整个块。

  - 块选择策略上，检索器（如相似度）比问题注意力更可靠；选中后将该块移动到问题旁边再重算，能在同样预算下显著优于 InfoFlow 式重排序（开放域 QA/API
  文档场景 6/9 胜出）。对对话记忆场景，简单块级重算未必优于 token 级选择器，需考虑更细粒度修复。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：非前缀 KV-cache 复用可节省每个请求重新编码的成本，但独立编码和拼接缓存可能损害上下文依赖问题的性能。需要确定有限修复预算应花在哪些块上。

**方法关键点**：在三个 7B-8B 模型、四个数据集（对话记忆、开放域 QA、API 文档）上，通过变化目标块周围的干扰块，分析重用性能损失。比较了不同预算分配策略：重新计算目标块、插入完整预填充 KV、问题注意力选块、检索器选块并移动位置、InfoFlow 重排序、token 级选择器。

**关键结果**：重用丢失 19-100% 的上下文相关问题；当干扰块与目标块同类型时损失更大。可恢复损害分散在其它块，恢复少数块无效，预算应集中在目标块。重新计算目标块（上下文兼容）在所有七个设置中优于插入完整预填充 KV。问题注意力选择目标块比例≤18.8%；检索器更有效，其顶部块移动至问题旁后重新计算，在 6/9 开放域 QA 和 API 文档设置中优于 InfoFlow 重排序（5% 预算）。对话记忆上，块级重算未显著优于 token 级选择器。
