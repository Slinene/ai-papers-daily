---
title: 'On-Demand Attention: Language Models Know When to Recall'
title_zh: 按需注意力：语言模型知道何时回忆
authors:
- Haibo Feng
- Ruiqi Liang
- Hanyang Peng
- Shiqi Yu
affiliations:
- Southern University of Science and Technology
- Peking University
- Peng Cheng Laboratory
arxiv_id: '2609.20734'
url: https://arxiv.org/abs/2609.20734
pdf_url: https://arxiv.org/pdf/2609.20734
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: 长上下文高效推理 · 按需注意力
tags:
- On-Demand Attention
- long-context inference
- KV cache
- local attention
- vLLM
- efficient decoding
one_liner: 训练轻量 recall head 基于解码状态动态触发全局注意力，在保持性能的同时大幅减少长上下文全局读取
practical_value: '- 在电商多轮 Agent / 长会话推荐场景，可采用 local-first + 轻量 recall head 的思路：先用局部注意力生成，仅在预测到当前步需要全局信息时触发全局注意力，降低长上下文推理成本。

  - 借鉴「只训练 recall head、冻结基座权重」的做法：在不改动线上 LLM 主干的前提下，通过一个极小的辅助头提升注意力分配效率，易于迭代和上线。

  - 工程实现上参考其 vLLM 的 GPU 端条件执行：把是否执行全局注意力的分支放在 GPU kernel 内，避免 CPU-GPU 同步，才能真正把减少的全局读取转化为实际解码加速。

  - 若业务使用 hybrid-attention 或长历史序列建模（如用户长期行为、商品描述），该方法可迁移为对重要 step 的按需全局召回，降低推理耗时同时保持大部分效果。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：长上下文推理中 full attention 每步都读取完整 KV cache，成本随上下文长度线性增长；但并非每个生成步骤都需要全局信息，远程信息的需求在步骤间差异很大。

**方法关键点**：发现预训练模型的解码状态本身已经包含「当前步是否受益于全局注意力」的预测信息。基于此提出 On-Demand Attention (ODA)：默认执行局部注意力（local attention），用一个轻量 recall head 根据解码状态预测全局注意力的收益变化，当收益增加时选择性触发全局注意力。ODA 只训练 recall head，保持预训练权重不变，并保留完整历史 KV cache 供未来召回。还在 vLLM 中实现了 GPU 端条件执行，把减少的全局读取转化为实际解码加速。

**关键结果**：在 Qwen 和 Gemma 系列模型（包括 hybrid-attention 骨干）上，ODA 的选择性召回恢复了局部注意力造成的大部分性能损失，同时显著减少了全局读取次数；在长上下文长度下相比 full attention 获得实际解码加速。
