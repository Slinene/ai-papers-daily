---
title: Measured Coupling for Parallel Decoding in Diffusion Language Models
title_zh: 扩散语言模型中用于并行解码的实测耦合
authors:
- Tal Oved
- Lior Wolf
affiliations:
- Tel Aviv University
arxiv_id: '2611.08307'
url: https://arxiv.org/abs/2611.08307
pdf_url: https://arxiv.org/pdf/2611.08307
published: '2026-11-05'
collected: '2026-11-08'
category: LLM
direction: 扩散语言模型并行解码优化
tags:
- Diffusion Language Models
- Parallel Decoding
- Mean-field
- Coupling Measurement
- Inference Acceleration
one_liner: 用主前向传播内的廉价探针测量 token 间耦合，替代相似性惩罚，大幅减少扩散语言模型解码步骤
practical_value: '- 对于生成式推荐中的序列生成（如 Semantic ID 序列、商品标题或描述），若采用扩散模型，可借鉴此方法：在主前向中测量位置间实际耦合，替代基于分布相似性的惩罚，从而更准确地选择可并行生成的
  token，减少推理步骤、降低延迟。

  - 该方法训练无关、无需额外模型，可直接嵌入现有扩散推理流程，适合电商场景快速验证；支持 KV cache，对长序列生成友好。

  - 核心结论——“真实耦合比相似性代理更有效”——可迁移到其他并行解码场景（如多 token 预测、并行 agent 动作规划）：依赖关系应直接测量而非用启发式代理。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散语言模型可并行生成多个 token，但需决定哪些 token 可一起 commit。独立预测可能产生错误组合，现有 mean-field 解码用预测分布相似性作为惩罚，但这是间接代理。  
**方法**：本文直接测量耦合本身——即 commit 一个 token 对另一位置模型置信度的影响。在主前向传播内使用廉价探针计算，无需训练或额外模型，并集成到同一 mean-field 规则中。  
**结果**：在三个模型和四个基准上，所需解码步骤远少于 mean-field 解码，大多数设置下推理更快（包括使用 KV cache），平均准确率仅下降 1.1 点。随机打乱耦合或替换为统一奖励会失去该增益，验证了耦合测量的有效性。
