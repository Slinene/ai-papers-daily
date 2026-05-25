---
title: Training-Free Looped Transformers
title_zh: 无需训练的循环 Transformer：冻结模型推理时循环层块提升性能
authors:
- Lizhang Chen
- Jonathan Li
- Chen Liang
- Ni Lao
- Qiang Liu
arxiv_id: '2605.23872'
url: https://arxiv.org/abs/2605.23872
pdf_url: https://arxiv.org/pdf/2605.23872
published: '2026-05-22'
collected: '2026-05-25'
category: LLM
direction: 推理时循环复用层块
tags:
- Training-Free
- Looped Transformers
- Inference-Time Recurrence
- ODE
- Damped Sub-steps
- LLM
one_liner: 在冻结的预训练模型上，通过阻尼子步骤循环中间层块，无需微调或架构改动即可显著提升推理性能
practical_value: '- 可直接对现网 LLM（如 Qwen、DeepSeek 等）在推理时套用循环包装器，无需重新训练或微调，适合快速上线和成本敏感场景。

  - 循环中间若干层并除以迭代次数的阻尼策略，可作为一种轻量级「深度增强」手段，在低延时约束下提升模型推理质量，例如用于电商 Agent 的多步推理、复杂指令遵循等。

  - 该方法不修改模型权重和架构，可配合现有推理优化（KV cache、量化等），可在已有工程框架中低成本实现。

  - 提供的层选择策略（中间层块）和迭代次数阻尼关系，可作为超参直接迁移到其他模型上，用于微调受限环境下的性能补强。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有循环 Transformer 需要从训练阶段就引入循环结构，无法应用于已发布的冻结模型。本文探索是否能在推理时直接对一个冻结的、现成的 Transformer 应用循环，而不做任何训练或架构修改。

**方法**：将预归一化 Transformer 块看作常微分方程的前向欧拉步，循环该块相当于将原本的一大步更新分解为多个阻尼子步骤。具体做法：从冻结模型中选取连续的中间层块（如 4-8 层），在推理时将该块的输出重新输入自身多次，每次将残差分支除以迭代次数以保持幅值一致。通过这种阻尼循环，可缓解直接重复块导致的退化。

**结果**：在 7 个涵盖密集、稀疏 MoE、MLA+MoE 的模型家族上验证，无需训练即可提升推理性能。例如，Qwen3-4B-Instruct 在 MMLU-Pro 上提升 2.64 个百分点，Qwen3-30B-A3B-Instruct 在 CommonsenseQA 上提升 1.14 个百分点，Moonlight-16B-A3B-Instruct 在 OpenBookQA 上提升 1.20 个百分点。消融实验表明，阻尼策略和层块选择位置对效果至关重要。
