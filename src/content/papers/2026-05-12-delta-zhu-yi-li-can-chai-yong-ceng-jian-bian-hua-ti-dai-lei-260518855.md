---
title: Delta Attention Residuals
title_zh: Delta 注意力残差：用层间变化替代累积状态提升路由选择性
authors:
- Cheng Luo
- Zefan Cai
- Junjie Hu
affiliations:
- Independent Researcher
- University of Wisconsin–Madison
arxiv_id: '2605.18855'
url: https://arxiv.org/abs/2605.18855
pdf_url: https://arxiv.org/pdf/2605.18855
published: '2026-05-12'
collected: '2026-05-20'
category: LLM
direction: Delta 注意力残差路由
tags:
- Delta Attention
- Residual Connections
- Selective Routing
- Transformer Architecture
- Training Stability
one_liner: 用子层输出的变化量（delta）替代累积隐藏状态进行注意力路由，缓解深层冗余与路由塌缩
practical_value: '- 推荐模型中的跨层特征融合：借鉴 delta 残差机制，在深度兴趣网络等模型中，将各层输出的变动量作为注意力汇聚的对象，避免相邻层特征高度冗余，提升高阶交互的区分度。

  - 多智能体通信路由优化：当多个 Agent 间传递信息时，不直接传递当前状态，而传递相对于上一轮的变化量（delta），可使路由注意力更聚焦于新颖信息，降低通信带宽并提升协作效率。

  - 预训练模型微调策略：可将现有 Transformer 模型的固定残差连接替换为 Delta 注意力残差后，仅通过少量微调就能继承预训练知识并获得困惑度收益，适合业务场景中低成本架构升级。

  - 大规模模型训练稳定性：Delta 残差天然具有更高对比度的注意力分布，能缓解深层网络中的路由塌缩，在训练 recommender 的深层 Transformer
  时可直接采用该连接方式以提升训练稳定性和最终效果。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：标准 Attention Residuals 使用 softmax 注意力对前层累积隐藏状态进行加权路由，但累积状态在深层高度冗余，导致注意力分布趋于均匀（最大权重仅约 0.2），形成“路由塌缩”，削弱了跨层选择性融合的能力。

**方法**：提出 Delta Attention Residuals，将路由目标从累积隐藏状态改为子层输出的变化量（delta：v_i = h_{i+1} - h_i）。由于各子层引入的变化量在结构上更具多样性，计算得到的注意力权重对比度大幅提升（最大权重约 0.6），使模型能更有选择性地聚合前层信息。该方法可灵活应用于子层或块级粒度，且只需将原残差中的状态向量替换为 delta 向量，无需改变网络其他结构。

**结果**：在 220M 至 7.6B 参数规模的模型上，Delta Attention Residuals 相比标准残差和 Attention Residuals，验证集困惑度降低 1.7%–8.2%，并在不同规模上一致有效。同时，预训练模型可通过标准微调转换为 Delta 版本，实现即插即用。代码已开源。
