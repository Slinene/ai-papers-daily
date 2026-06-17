---
title: Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer
  is Key to Unification
title_zh: 统一多模态自回归建模：共享上下文视觉分词器是关键
authors:
- Wujian Peng
- Lingchen Meng
- Yuxuan Cai
- Xianwei Zhuang
- Yuhuan Yang
- Rongyao Fang
- Chenfei Wu
- Junyang Lin
- Zuxuan Wu
- Shuai Bai
affiliations:
- Institute of Trustworthy Embodied AI, Fudan University
- Shanghai Innovation Institute
- Qwen Team, Alibaba Inc.
arxiv_id: '2606.18249'
url: https://arxiv.org/abs/2606.18249
pdf_url: https://arxiv.org/pdf/2606.18249
published: '2026-06-15'
collected: '2026-06-17'
category: Multimodal
direction: 统一多模态自回归架构
tags:
- Unified Multimodal
- Autoregressive
- Discrete Visual Tokenizer
- Lookup-Free Quantization
- Diffusion Decoder
- Image Generation
one_liner: 用单一离散视觉分词器统一多模态理解与生成，实现自回归模型直接解读自身生成视觉token
practical_value: '- 统一视觉分词器设计可借鉴至电商商品多模态表征：单一离散token同时支持识别和生成任务，减少多套编码器的维护成本，对商品图搜索、审核、生成等场景具有统一表征潜力。

  - Lookup-free比特量化（bitwise quantization）扩展视觉词汇量的同时保持低开销，类似Semantic ID的思想可用于商品视觉ID构建，将图像转为紧凑离散码，便于在大规模召回或生成式推荐中作为条件。

  - 并行比特预测（parallel bitwise prediction）大幅缩短视觉序列长度，加速图像生成推理，对实时性要求高的商品图生成或虚拟试穿等场景有实用价值。

  - 若业务中需构建统一的多模态对话/导购助手，共享context的架构能避免重复编码生成结果，降低延迟，值得在Agent设计时参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有统一多模态模型在视觉理解与生成任务上各自使用独立的视觉分词器，导致表征空间割裂，难以真正共享上下文——即模型无法直接解读自己生成的视觉内容，需额外重编码。

**方法**：提出UniAR自回归框架，核心是用单个离散视觉分词器充当理解与生成的桥梁。该分词器基于预训练视觉编码器，引入多层级特征融合和无查找表的比特量化（lookup-free bitwise quantization），在几乎不增加开销的前提下扩展有效词汇量，同时保留高层语义和底层细节。自回归模型通过**并行比特预测**联合生成空间分组的多层级视觉码，显著缩短视觉序列长度，提升生成速度。最终由扩散解码器将离散token重建为高保真图像。训练策略包括大规模预训练、有监督微调和强化学习。

**结果**：在图像生成和图像编辑任务上达到SOTA，同时在多模态理解基准上保持竞争力，证明单一离散分词器能有效支撑视觉理解与生成的双向能力。
