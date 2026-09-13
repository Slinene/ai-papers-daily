---
title: 'From Parameters to Answers: How LLMs Retrieve and Use Their Internal Knowledge'
title_zh: 从参数到答案：LLM 如何检索并使用其内部知识
authors:
- Wenkang Wei
- Yuan Fang
- Renhe Jiang
- Hong Cheng
- Xingtong Yu
affiliations:
- University of Science and Technology of China
- Singapore Management University
- The University of Tokyo
- The Chinese University of Hong Kong
arxiv_id: '2609.11859'
url: https://arxiv.org/abs/2609.11859
pdf_url: https://arxiv.org/pdf/2609.11859
published: '2026-09-10'
collected: '2026-09-13'
category: LLM
direction: LLM 内部知识检索机制与可解释性
tags:
- mechanistic interpretability
- layerwise intervention
- internal knowledge retrieval
- causal probing
- request routing
- hidden states
one_liner: 通过层间干预分离LLM问答中的请求路由信息与目标知识依赖，揭示层间交接模式并跨模型比较
practical_value: '- 层间干预方法可迁移到生成式推荐/商品文案场景：在 LLM 的 hidden states 上分别拟合『请求方向』和『内容知识』probe，定位模型哪几层完成用户意图路由、哪几层提取事实性知识，帮助诊断
  query 理解偏差或事实错误。

  - 跨模型实验表明路由-内容交接模式并不统一（如 Llama 无持续路由效应窗口），因此在多模型集成、蒸馏或对隐藏状态做干预时，不能假设同一中间层都适合注入知识或引导；需要按模型分别标定有效窗口。

  - 对 RAG/Agent 检索增强推荐有借鉴：论文显示问题结束时已存在可读的路由和内容表示，后续层才发生交接，可在路由已稳定但内容依赖尚在形成的层注入检索到的商品知识或候选，减少外部知识与内部参数知识的冲突。

  - 局限：主要是机制解释性贡献，业务收益需要自行验证，但可作为 LLM4Rec 内部行为分析和故障定位工具。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 在预训练中储存大量知识，但问答过程中模型如何在层间逐步访问内部知识并生成答案仍不清楚。以往工作多定位知识存储位置，未明确分离『查询路由信息』和『目标知识内容』的依赖变化。

**方法**：在 Qwen、Llama、Gemma 上，对问题结束位置的隐藏状态做层间干预。使用 country-continent 问答（答案类型为名词、形容词、代码）构建不同测量：pair-conditioned 请求方向描述自然单国问题中查询哪个国家；global 请求方向区分成对问题中的第一/第二国请求；另有选择候选测量隐藏状态中已存在内容上的控制能力。

**关键结果**：对冻结 Qwen 状态的诊断重分析显示，pair-conditioned 方向在干预开始改变后期知识前已增强，其因果窗口打开时答案支持内容仍在形成。三模型轨迹不统一：Gemma 呈现部分重叠的中层路由-内容 profile，Llama 在同样门控下没有持续路由效应窗口。配对协议中，对 global 请求方向的依赖从早期层到后期层下降，而对 fitted 内容的依赖持续。匹配的 Qwen 比较中，pair-conditioned 方向保留后期效应，说明操作交接只涉及 global fitted 方向而非所有请求信息。结果分离了早期可读性、自然强度、因果引导与后期内容依赖。
