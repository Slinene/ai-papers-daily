---
title: Rethinking Expressivity and Efficiency in Test-Time Training
title_zh: 重新思考 Test-Time Training 中的表达力与效率
authors:
- Zeyun Zhong
- Joya Chen
- Manuel Martin
- Frederik Diederichs
- Juergen Gall
- Juergen Beyerer
affiliations:
- Karlsruhe Institute of Technology (KIT)
- National University of Singapore
- Fraunhofer IOSB
- Lamarr Institute for Machine Learning and Artificial Intelligence
- University of Bonn
arxiv_id: '2608.21308'
url: https://arxiv.org/abs/2608.21308
pdf_url: https://arxiv.org/pdf/2608.21308
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 高效长上下文 Test-Time Training
tags:
- Test-Time Training
- Long-context
- Transformer
- Efficiency
- Expressivity
- Length Extrapolation
one_liner: 提出 E²-TTT，通过闭式状态转移并行化分块 TTT 训练，在保持每 token 更新时序结构的同时匹配分块方法吞吐
practical_value: '- 长序列用户行为建模：电商推荐中的用户长期历史、会话依赖往往超过常见上下文长度，E²-TTT 可作为替代或混合 attention
  的序列建模模块，尤其在需要长度外推时，其 8× 训练长度外推能力可减少重新训练成本。

  - Agent 长任务记忆：多步 Agent 需要持续从长 horizon 任务中学习，TTT 的权重更新机制比 KV cache 更紧凑，E²-TTT 的并行分块训练使在线学习用户偏好或任务适应在工程上更可行。

  - 工程实现参考：论文中的闭式状态转移 + 分块并行训练思路，可迁移到任何需要高效时序递归更新的模块，避免简单 chunk-wise 近似丢弃中间状态，同时保持吞吐。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Test-Time Training (TTT) 允许推理时更新权重，但 per-token 更新表达力强而硬件效率低；chunk-wise 近似高效却丢失时序结构。如何兼顾表达力与效率是瓶颈。

**方法关键点**：在标准梯度近似（在 chunk-start 权重处取梯度）下，推导出闭式状态转移，精确复现 per-token recurrence 在 chunk-end 的 fast-weight 与 momentum 状态。这使得 chunk-level 训练可完全并行化，同时保留此前 chunk-wise 方法丢弃的时序更新规则。

**关键结果**：从零训练 1.3B 参数模型，语言建模与之前 TTT 及 hybrid attention 基线持平，in-context retrieval 更优；在 Needle in a Haystack passkey 测试中，8× 训练上下文长度下保持 >90% 准确率；训练吞吐与高效 chunk-wise 方法相当。
