---
title: Looped Language Models Improve Compositional Tool Calling
title_zh: 循环语言模型提升组合工具调用
authors:
- Andrei Cristian Popescu
- Haitz Sáez de Ocáriz Borde
- Pietro Liò
affiliations:
- Department of Computer Science and Technology, University of Cambridge, United Kingdom
arxiv_id: '2608.18171'
url: https://arxiv.org/abs/2608.18171
pdf_url: https://arxiv.org/pdf/2608.18171
published: '2026-08-16'
collected: '2026-08-21'
category: Agent
direction: 循环语言模型优化多步工具调用
tags:
- Looped LLM
- Tool Calling
- Compositional API
- Adaptive Inference
- Agent
one_liner: 循环计算在组合式工具调用中提升准确率，自适应推理深度提供更优算力-性能折中
practical_value: '- 多步 API 协调、状态依赖保持是 Agent 落地的核心难点，可尝试将 backbone 换成或改造为循环语言模型，替代复杂
  prompt 工程，提升组合工具调用稳定性。

  - 自适应推理深度在保证准确率的同时控制算力，适合线上 API 开销敏感场景；可以在推理时根据任务复杂度动态分配 recurrent depth。

  - 论文验证了 retrofitted 循环模型（对 Llama、OLMo 等现有模型插入循环层）与原生循环模型均有增益，意味着现有 SFT 流程可复用，作为生成式
  Agent 的候选架构成本较低。

  - 业务中若涉及复杂工具编排（如电商 Agent 串联商品查询、订单、物流接口），可重点评测多步依赖型任务的准确率，而非只关注单步 API 调用指标。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 被越来越多地用作执行工具调用的 Agent，但组合式工具调用需要协调多个 API、维护中间状态并保持依赖关系，现有模型在该场景下可靠性不足。循环语言模型在推理基准上表现良好，却很少被研究用于 agentic tool use。

**方法关键点**：
- 在 API-Bank、BFCL、NESTful 三个基准上评测原生循环模型（如 Ouro）和用循环层改造的标准模型（retrofitted looped Llama、OLMo）。
- 控制变量：匹配的 SFT 训练配方，比较 looped 与 non-looped 模型。
- 推理时改变 recurrent depth，并引入自适应推理，按需分配额外循环计算。

**关键结果数字**：
- 组合式及依赖感知工具调用中，循环计算带来一致收益；单步 API 调用收益较小且依赖具体模型。
- 多步工具调用准确率随 recurrent depth 增加总体提升，但自适应推理以更少计算实现更优的准确率-计算代价折中。
- 在 BFCL 多调用类别上，循环模型相对优势最大，表明其适合复杂 Agent 工作流。
