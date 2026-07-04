---
title: 'Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning'
title_zh: 对抗文本噪声与冗余的熵感知密集视觉令牌剪枝
authors:
- Xuehui Wang
- Xuankun Yang
- Wei Shen
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2607.02484'
url: https://arxiv.org/abs/2607.02484
pdf_url: https://arxiv.org/pdf/2607.02484
published: '2026-07-02'
collected: '2026-07-04'
category: Multimodal
direction: 多模态模型视觉令牌剪枝
tags:
- Visual Token Pruning
- Entropy-Aware
- Textual Noise
- Submodular Maximization
- Dense Instructions
- VLM Efficiency
one_liner: EADP 用熵过滤文本噪声并将令牌选择建模为带空间先验的次模最大化，在严格预算下保持细粒度视觉线索
practical_value: '- 在多模态推荐场景（如商品图像+用户查询）中，可借鉴熵过滤来抑制查询文本中的噪声词，提升跨模态打分鲁棒性，避免关键图像块被错误丢弃。

  - 采用次模最大化+空间先验替代 top-K 选取视觉令牌，能更全面地保留细粒度细节（如商品微小瑕疵、特定图案），适合高要求的商品理解任务。

  - 方法无训练、即插即用，可直接集成到现有多模态 VLM 推理管线中，在延迟敏感场景（如实时搜索推荐）降低视觉上下文成本而不过度损失精度。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：视觉令牌剪枝是加速 VLM 的关键手段，但在密集指令与细粒度查询（如多目标推理、小细节识别）时，现有方法易丢弃关键视觉线索。分析发现两个瓶颈：文本噪声广泛散布，污染了跨模态 token 打分；标准 top-K 选择导致特征碎片化，丢失整体上下文。  

**方法**：提出 Entropy-Aware Dense Pruning (EADP)。第一步，基于统计熵量化并滤除文本 token 中的噪声成分，生成更鲁棒的指令相关性分数；第二步，将视觉 token 选择建模为带空间平滑先验的次模最大化问题，显式鼓励选出整体信息量大且空间非冗余的 token 子集，而非逐 token 贪心 top-K。  

**结果**：在多个 VLM（如 LLaVA）与多模态基准上，EADP 在严格压缩比（保留极少量视觉 token）下显著提升准确率，例如在 MME、POPE 等任务上超越 SOTA 剪枝方法，同时将推理效率提高数倍，证明了在挑战性密集任务中保留细粒度线索的有效性。
