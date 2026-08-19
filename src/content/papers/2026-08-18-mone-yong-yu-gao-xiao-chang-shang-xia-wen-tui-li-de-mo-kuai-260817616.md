---
title: 'MoNe: Modular Neural Memory for Efficient Long Context Inference'
title_zh: MoNe：用于高效长上下文推理的模块化神经记忆
authors:
- Wonguk Cho
- Kyubyung Chae
- Tribhuvanesh Orekondy
- Sunghyun Park
- Hyoungwoo Park
- Jeongho Kim
- Arash Behboodi
- Kyuwoong Hwang
- Sungrack Yun
affiliations:
- Qualcomm AI Research
arxiv_id: '2608.17616'
url: https://arxiv.org/abs/2608.17616
pdf_url: https://arxiv.org/pdf/2608.17616
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: 长上下文推理 · 神经记忆
tags:
- Long context
- Neural memory
- Test-time learning
- Fast weights
- Efficient inference
- Transformer
one_liner: 提出轻量模块化神经记忆 MoNe，通过 test-time fast-weight 学习实现 O(N) 预处理、O(1) 查询的长上下文推理，无需重训练
practical_value: '- 在电商/Agent 场景处理超长用户会话或商品描述时，可借鉴 MoNe 的 test-time fast-weight memory：将长上下文分段压缩进轻量记忆参数，在线推理只从
  query 生成 KV，避免每次带全量上下文；特别适合在移动端/边缘设备控制峰值显存。

  - 该方法附加在冻结模型上，仅 6.4% 参数开销，业务上可作为 Plug-in 模块对已有 LLM 服务做增量改造，无需全量重训，风险可控。

  - 注意 test-time learning 需要对每个 context 做梯度更新，适合将用户长期历史、固定知识库等离线预处理并缓存 memory，在线摊销成本；高并发推荐/搜索
  query 侧可享 O(1) 查询。

  - 128K 长度下 compute 和峰值 GPU 内存降低约 80%，且在小模型长上下文提取信息不稳定时仍保持性能，可参考该量化结果作为成本收益评估。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：长上下文处理（个性化助手、文档QA、Agent 系统）越来越重要，但全上下文 ICL 的 FLOPs 随长度二次增长，移动端难以承受；小模型即使上下文窗够大也常无法可靠提取长 prompt 信息。

方法关键点：MoNe 是轻量模块化神经记忆，可附加到任意冻结预训练 Transformer，无需重训练。分两阶段：test-time 学习阶段，按固定大小分段读取上下文，用 fast-weight 神经记忆网络做层局部梯度更新，将上下文压缩进记忆参数；推理阶段，记忆仅用 query token 生成 keys/values，不重读上下文 token，使推理成本与上下文长度解耦。复杂度 O(N) 预处理、O(1) 查询，峰值 GPU 内存不随 N 增长。

关键结果：在 128K token 上，相比 ICL，MoNe 将计算和峰值 GPU 内存降低约 80%，仅增加 6.4% 参数开销。在 RULER 的 needle-in-a-haystack 和 word extraction 基准上，MoNe 可泛化到远超骨干模型原生窗口的长度，且 ICL 急剧退化时仍表现强劲。
