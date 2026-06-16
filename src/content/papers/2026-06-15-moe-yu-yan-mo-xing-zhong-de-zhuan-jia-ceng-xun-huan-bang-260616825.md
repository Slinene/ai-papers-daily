---
title: Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models
title_zh: MoE 语言模型中的专家层循环绑定
authors:
- Martin Jaggi
affiliations:
- EPFL
arxiv_id: '2606.16825'
url: https://arxiv.org/abs/2606.16825
pdf_url: https://arxiv.org/pdf/2606.16825
published: '2026-06-15'
collected: '2026-06-16'
category: Training
direction: MoE 参数共享与内存优化
tags:
- Mixture-of-Experts
- Expert Tying
- Parameter Sharing
- Efficient Training
- LLM Scaling
one_liner: 跨层共享专家参数，保持独立路由，几乎无损失地将 MoE 内存占用减半
practical_value: '- **大型推荐模型的内存压缩**：若采用 MoE 做多任务或用户分群建模，跨层共享专家 FFN 可近乎砍半参数内存，同时保持独立路由，适合搜索/推荐等需低延迟服务的场景。

  - **Agent 模型的低成本扩展**：构建多专家 Agent 系统时，可通过层间专家复用减少冗余，维持不同层路由独立以保留推理多样性，平衡能力与资源。

  - **工程实现注意**：复用需保证每层 router 和 attention 独立；可直接应用于 OLMoE/Qwen3/DeepSeek 等主流 MoE 结构，现有模型微调或蒸馏时可尝试专家合并。

  - **与 LoRA/量化结合**：专家共享后为稀疏模块再留出容量加 LoRA 或小块微调，可在内存受限设备上部署更大型的生成式推荐模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：Mixture-of-Experts（MoE）虽每 token 仅激活少数专家，但所有专家参数必须完整驻留在训练和推理内存中，当激活率极低（如 DeepSeek-V3 仅 5.5%）时，内存几乎全被闲置参数占据，这与追求参数效率的趋势相悖。

**方法关键**：提出 **Expert Tying**，将连续若干层中的专家 FFN 权重共享，而每层仍保留独立的路由器和注意力模块。共享组大小可调，通过循环复用同一组专家参数，大幅减少总参数量。在主流 MoE 架构（OLMoE、Qwen3、DeepSeek-style）上验证该方案。

**关键结果**：预训练实验表明，专家绑定可将内存占用降低接近 2 倍，同时困惑度与下游任务指标几乎无退化，有效实现了计算与内存间的有利权衡。
