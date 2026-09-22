---
title: MLLMs Hallucinate when Information Distribution Drifts in Synergy Heads
title_zh: 多模态大模型幻觉源于协同头信息分布漂移
authors:
- Meng&#39;en Qin
- Junye Chen
- Jucheng Liu
- Youlu Xing
- Song Wang
- Ruize Han
affiliations:
- Shenzhen University of Advanced Technology
arxiv_id: '2609.09206'
url: https://arxiv.org/abs/2609.09206
pdf_url: https://arxiv.org/pdf/2609.09206
published: '2026-09-04'
collected: '2026-09-22'
category: Multimodal
direction: 多模态大模型幻觉归因与校准
tags:
- Hallucination
- MLLM
- Attention Heads
- Causal Intervention
- Calibration
- Interpretability
one_liner: 提出 HEAL，通过头部级信息解耦与校准识别并缓解多模态大模型幻觉
practical_value: '- 多模态 LLM 在电商商品描述生成、图文推荐、广告创意生成等场景中容易出现幻觉，可借鉴头部级解耦与校准思路：定位并校准跨模态协同注意力头，无需全模型微调，降低落地成本。

  - 因果噪声干预筛选冗余头的方法可用于分析现有多模态推荐模型的注意力机制，识别对跨模态对齐贡献不大的头，进行剪枝或优化，提升推理效率。

  - 动态注入校准因子到 value vectors 的机制可迁移到多模态特征融合模块，作为轻量级即插即用组件，增强图像和文本特征的一致性。

  - 结论“幻觉与模态特定头数量/强度无关，而与协同头信息分布漂移相关”提示在多模态推荐/搜索中应关注跨模态交互的质量而非单模态表示的强度，可指导模型调试和特征工程。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
多模态大模型（MLLMs）在医疗影像等高精度场景中常产生幻觉，生成与视觉上下文不一致的内容，严重阻碍可靠落地。现有基于注意力的缓解方法依赖注意力权重等间接信号，无法准确反映幻觉背后的真实信息偏移。

**方法关键点**  
提出 HEAL（Head-lEvel information disentAnglement and caLibration）。首先对多头输出施加因果噪声干预，过滤因果冗余头；随后利用反事实双重差分（Difference-in-Differences）解耦剩余头的信息分布，将头划分为四类。分析发现：幻觉发生在协同头（synergy heads）的信息分布偏离健康均衡时，与模态特定头的数量或强度无强相关。基于此，HEAL 向协同头的 value vectors 注入动态信息校准因子，主动调节视觉-语言依赖，将输出分布引导至事实证据。

**关键结果**  
在多个 MLLM 上的大量实验表明 HEAL 能有效降低幻觉，提供了一条简单、可解释的提升模型可信度的路径。
