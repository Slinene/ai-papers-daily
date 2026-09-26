---
title: 'Your Transformer Can Hold Two Thoughts at Once: Evidence of Linear Superposition
  in LLMs'
title_zh: Transformer 能同时持有两种思想：LLM 线性叠加的证据
authors:
- Pavel Tikhonov
- Anton Korznikov
- Matvey Mikhalchuk
- Nikita Dragunov
- Temurbek Rahmatullaev
- Polina Druzhinina
- Anton Razzhigaev
- Ivan Oseledets
- Elena Tutubalina
arxiv_id: '2609.29845'
url: https://arxiv.org/abs/2609.29845
pdf_url: https://arxiv.org/pdf/2609.29845
published: '2026-09-23'
collected: '2026-09-26'
category: LLM
direction: Transformer 可解释性与推理加速
tags:
- linear superposition
- guided decoding
- Transformer interpretability
- parallel decoding
- LLM inference
one_liner: 证明 LLM 输入端线性组合会产生输出分布叠加，并提出引导解码实现单次前向生成两条连贯续写
practical_value: '- 推理加速：借鉴引导解码同时解耦叠加输出，可在一次前向中生成多个候选 query/文案，用于搜索推荐场景的多路召回或 A/B
  文案测试，降低 GPU 成本。

  - 多意图融合：若模型经轻量微调恢复叠加线性，可混合多个意图 prompt embedding（如“品牌词+品类词”），再用解码约束得到多条符合不同意图的结果，适合电商搜索
  query 推荐。

  - 可落地微调：叠加线性随预训练减弱但能通过轻量微调恢复，业务模型可以用少量数据进行微调，使多流输入并行处理成为可能，从而支持 Agent 同时处理多个子任务。

  - 注意边界：该线性性质与训练程度相关，实际部署前需在自有模型上验证；建议在微调阶段加入保持叠加线性的正则项或混合训练数据。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Transformer 由注意力、MLP 等非线性组件构成，通常被视作单一语义流处理。近期工作显示残差流层间存在强线性结构，于是追问：模型端到端输入输出是否也足够线性，使得输入线性组合对应的输出近似于各自输出的组合？

**方法关键点**：提出 Superposition Linearity Hypothesis——将两条 token 流的 embedding 线性组合（如逐元素平均）输入模型，输出 next-token 分布应是各自单独输入时分布的叠加。作者证明该性质主要源于 Transformer 架构本身，而非预训练后涌现；实际上随预训练进行线性叠加程度下降。进一步通过轻量微调可显著恢复叠加线性，降低预测分布与单独分布平均之间的散度。最后提出 guided decoding 过程，从叠加输出中解耦出两条连贯的续写。

**关键结果**：轻量微调后，叠加输出与个体输出平均的 divergence 显著下降；引导解码可在单次前向中同时生成两个独立且连贯的 continuation，验证了 LLM 端到端线性叠加的可行性。
