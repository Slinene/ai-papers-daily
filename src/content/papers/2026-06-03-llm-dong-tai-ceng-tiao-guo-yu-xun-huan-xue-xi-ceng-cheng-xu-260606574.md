---
title: Skip a Layer or Loop It? Learning Program-of-Layers in LLMs
title_zh: LLM 动态层跳过与循环：学习「层程序」提升推理效率与准确率
authors:
- Ziyue Li
- Yang Li
- Tianyi Zhou
affiliations:
- University of Maryland, College Park, MD, USA
- MBZUAI, Abu Dhabi, UAE
arxiv_id: '2606.06574'
url: https://arxiv.org/abs/2606.06574
pdf_url: https://arxiv.org/pdf/2606.06574
published: '2026-06-03'
collected: '2026-06-15'
category: LLM
direction: 动态层执行优化 · 自适应计算
tags:
- dynamic-inference
- layer-skipping
- layer-looping
- adaptive-computation
- LLM-reasoning
one_liner: 提出 PoLar，让 LLM 为每个输入动态决定跳过或循环哪些层，用更少层达到同等或更高准确率。
practical_value: '- **低成本 LLM 推理加速**：在电商推荐、对话 Agent 等需要高吞吐的场景，可借鉴 PoLar 的「层跳过」与「层循环」思想，根据输入复杂度动态分配计算量，减少不必要的层计算，降低时延与成本。

  - **纠错与能力自修复**：PoLar 发现错误预测可通过更少的层组合纠正，这启示我们在推荐生成或多 Agent 交互中，当 LLM 输出不可靠时，可尝试用剪枝或路径重排的方式生成备选输出，而无需完整重跑模型。

  - **轻量级路由网络设计**：PoLar 提出的轻量预测网络（如基于隐藏状态的 LSTM）能以极小开销学习层执行程序，这种路由机制可直接迁移到 MoE 推荐模型或生成式推荐中，为不同样本选择不同的专家或计算路径。

  - **模型能力挖掘**：论文表明固定深度推理仅捕获了 LLM 潜能的一个子集，这提示我们在使用生成式推荐模型（如语义 ID 生成）时，可探索冻结主干下的动态解码路径，用更少步骤生成更优推荐。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 对所有输入均执行固定深度的全层前向计算，忽视了问题复杂度差异。作者发现，对许多输入，跳过或重复部分预训练层形成的动态“层程序”（PoLar）可用更少层达到相同或更高准确率，甚至能纠正原始全层预测的错误。这说明固定深度推理只挖掘了 LLM 潜在计算能力的一小部分。

**方法**：将预训练 LLM 的每一层视为基本函数，允许推理时跳过（skip）或循环（loop）若干层，为每个输入样例定制计算路径。为高效搜索最佳路径，训练一个轻量级 PoLar 预测网络（例如基于门控循环单元的序列模型），它根据早期层输出的隐藏状态来动态决定每个位置是跳过还是循环某层。训练时使用少量标注样本，以任务损失和路径长度正则作为目标。

**关键结果**：在数学推理基准（如 GSM8K、MATH）上，PoLar 在平均执行层数少于标准推理和先前动态深度方法（如深度自适应 Transformer）的情况下，一致提升准确率（例如在 7B 模型上，层数减少 30% 仍提升约 1-2 个百分点）。性能增益在分布外评估中也保持稳定。
