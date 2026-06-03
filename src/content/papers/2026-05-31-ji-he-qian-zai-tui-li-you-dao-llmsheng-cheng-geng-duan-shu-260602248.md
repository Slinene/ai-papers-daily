---
title: Geometric Latent Reasoning Induces Shorter Generations in LLMs
title_zh: 几何潜在推理诱导LLM生成更短输出
authors:
- Shashi Kumar
- Yacouba Kaloga
- Petr Motlicek
- Ina Kodrasi
- Andrea Cavallaro
affiliations:
- Idiap Research Institute
- EPFL
- BUT
arxiv_id: '2606.02248'
url: https://arxiv.org/abs/2606.02248
pdf_url: https://arxiv.org/pdf/2606.02248
published: '2026-05-31'
collected: '2026-06-03'
category: Reasoning
direction: 潜在推理 · 几何嵌入路径近似
tags:
- latent reasoning
- geometric embedding
- chain-of-thought
- length reduction
- emergent phenomenon
one_liner: 将潜在推理形式化为嵌入空间路径近似，出现压缩推理长度的涌现现象
practical_value: '- 在电商对话Agent或推荐解释生成中，可借鉴GLR在embedding空间连续推进的轻量设计，将早期推理步骤替换为潜在向量更新，显著缩短显式生成长度，降低API调用成本和延迟。

  - 对于多步Agent任务（如订单查询、售后协商），可训练一个小型transition head预测思维转向，实现紧凑的中间状态表征，既保留推理能力又减少tokens消耗，适合高并发场景。

  - GLR不修改主模型权重、仅添加可训练的过渡头，工程实现简单，可直接作为即插即用模块嵌入现有LLM服务，提升推理吞吐。

  - 涌现性的长度压缩现象提示：通过调整潜在步数（computation budget），可在不牺牲精度的前提下灵活控制输出冗长度，这对生成式推荐中控制解释文本长度具有启发意义。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM依靠显式思维链（CoT）推理解决复杂问题，但离散语言步骤导致生成长度膨胀、计算开销大，且每一步必须过早选定具体token。潜在推理虽用连续状态替换中间步骤，却缺乏有效的中间表征结构。

**方法**：将潜在推理定义为模型预训练token嵌入空间中的几何路径近似问题，提出**几何潜在推理（GLR）**。它在原有Transformer层间插入一个轻量**过渡头**，基于当前嵌入迭代预测方向更新，形成连续轨迹。以文本CoT轨迹为锚点进行蒸馏学习，使潜在路径能近似离散推理，同时允许适度偏离具体token嵌入。

**结果**：在数学推理基准（Qwen3模型）上，GLR展现出**涌现现象**——未施加长度目标，模型自发用早期潜在步骤替代大量显式推理，总生成步数大幅减少，答案正确性得以保持。这揭示了连续轨迹作为紧凑中间推理态的新权衡：调整潜在计算预算，可灵活控制输出长度与准确度。
