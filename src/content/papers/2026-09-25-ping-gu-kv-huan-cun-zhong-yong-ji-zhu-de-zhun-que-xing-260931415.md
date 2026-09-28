---
title: Evaluating the accuracy of KV cache reuse techniques
title_zh: 评估 KV 缓存重用技术的准确性
authors:
- Samuel Cestola
- Tianxiang Xia
- Pengfei Zheng
- Weiyan Zheng
- Bo Wang
- Yi Zhao
- Diego Didona
affiliations:
- Huawei Technologies Ltd.
- Department of Computer Science, ETH Zurich
arxiv_id: '2609.31415'
url: https://arxiv.org/abs/2609.31415
pdf_url: https://arxiv.org/pdf/2609.31415
published: '2026-09-25'
collected: '2026-09-28'
category: Eval
direction: LLM 推理评测与 KV cache 复用
tags:
- KV cache
- RAG
- evaluation
- LLM inference
- latency
one_liner: 指出当前 KV 缓存重用评测方法高估效果，提出无歧义精度损失评测法并推出 Boxoffice 生成挑战性数据集
practical_value: '- 若业务中用 RAG 为推荐/广告/搜索文案提供上下文，评估 KV cache 复用方案时必须把「复用带来的精度损失」与「检索质量/模型生成质量」分开测，否则会高估技术收益，建议设置隔离变量实验。

  - 位置无关 KV cache 复用比 prefix caching 更灵活，但跨 chunk attention 缺失是主要精度损失来源；落地前应重点验证恢复跨
  chunk attention 的 token 数量与位置对下游任务（如用户意图识别、商品描述生成）的实际影响。

  - 借鉴 Boxoffice 的程序化生成评测集思路：构造具有不同 chunk 重复频率、乱序、跨 chunk 依赖的查询，模拟真实 RAG 中重叠/交错上下文，提前暴露复用策略在长尾模式下的退化。

  - 若在 Agent 多步检索生成中启用 KV cache 复用降低 prefill 延迟，需要同时监控端到端业务指标（如点击率、转化率），因为微小的 token
  级精度损失可能在业务链路上被放大。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：RAG 系统通过插入检索文本块增强 LLM，但 prompt 变长导致 prefill 阶段 KV cache 计算成为延迟瓶颈。位置无关 KV cache 复用可让每个 chunk 的 KV cache 计算一次后在任意位置重用，比 prefix caching 更具普适性，但其精度损失评测存在缺陷。

方法关键点：论文指出当前评测依赖的测量方式无法忠实反映复用导致的精度损失，常夸大效果；同时现有数据集缺乏真正考验复用技术的重用动态。为此提出一种无歧义的精度损失评测方法，并开发 Boxoffice 工具，通过程序化生成具有挑战性 KV cache 重用模式的数据集，使评测更能暴露跨 chunk attention 缺失带来的问题。

关键结果：现有评测方法会人为抬高位置无关复用技术的有效性；新评测能更准确捕捉精度损失，Boxoffice 数据集能填补当前评测空白。
