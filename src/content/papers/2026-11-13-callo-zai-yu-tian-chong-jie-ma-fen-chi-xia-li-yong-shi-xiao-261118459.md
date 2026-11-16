---
title: 'Callo: Serving Cache-Miss Requests with Speculative Decoding on Invalidated
  KV under Prefill-Decode Disaggregation'
title_zh: Callo：在预填充-解码分离下利用失效 KV 推测解码服务缓存未命中请求
authors:
- Jianjun Ou
- Matthew Lentz
affiliations:
- Duke University
arxiv_id: '2611.18459'
url: https://arxiv.org/abs/2611.18459
pdf_url: https://arxiv.org/pdf/2611.18459
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM 推理服务·推测解码与 KV 缓存
tags:
- Speculative Decoding
- KV Cache
- Prefill-Decode Disaggregation
- Agent Serving
- Inference Optimization
- Prefix Caching
one_liner: Callo 利用失效 KV 作推测 draft，在 P/D 分离中隐藏 context edit 导致的 re-prefill 延迟，实测加速
  1.05-1.19x
practical_value: '- 在长会话 Agent（如购物助手、客服）中，频繁编辑历史/删除错误信息会导致 prefix cache 失效与 re-prefill
  延迟。可直接借鉴 Callo 思路：保留失效 KV 用于生成推测 draft，待重新 prefill 后的精确 KV 验证，隐藏关键路径延迟；工程上可在 vLLM/SGLang
  上实现类似机制，无需修改模型。

  - 调度上，将 speculative draft 计算安排在 decode 资源空闲时段（如低峰期或多路请求间隙），避免抢占正常 decode；并实现一个轻量级接受率预测器，在上下文变动剧烈、draft
  大概率不被接受时提前抢占（preempt），节省 GPU 资源。推荐系统的高并发在线服务也可以利用此思路，在闲时预计算候选，忙时验证。

  - 对推荐/搜索的 agent 化产品（如智能导购、RAG+工具调用），长会话中上下文编辑常见，此方法能显著降低 P/D 分离架构下 cache-miss 的尾部延迟；可结合集群级模拟评估，用真实轨迹验证性能收益。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Agent 长会话（如编码/购物助手）频繁编辑上下文，导致 KV cache 大面积失效。在 prefill-decode 分离架构中，缓存未命中请求必须先等待重新 prefill，再进入 decode，带来显著延迟和成本。

**方法关键点**：Callo 在重新 prefill 期间，复用已被编辑失效的旧 KV 生成推测 draft tokens；待精确 KV 重新计算完成后，用其验证 draft 的每个 token，验证通过才提交，从而将 re-prefill 延迟与 decode 重叠。此外，Callo 将 speculation 计算调度在 decode 资源利用率低谷时段，并基于接受率预测在 draft 可能被拒绝时抢占，避免浪费。

**关键结果数字**：在两 GPU 测试台上使用 SWE-agent 会话、覆盖三个模型家族，相对于 vLLM，在中等负载下 Callo 获得全请求 1.05–1.19× 加速；并基于真实轨迹的集群级模拟验证了规模化收益。
