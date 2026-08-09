---
title: 'F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading'
title_zh: 多模态交易智能体的金融融合：F²Agent
authors:
- Changshuo Liu
- Yanzheng Jin
- Shangfeng Cai
- Peng Fang
- Xiaokui Xiao
- Beng Chin Ooi
affiliations:
- National University of Singapore
- Huazhong University of Science and Technology
- Zhejiang University
arxiv_id: '2608.05668'
url: https://arxiv.org/abs/2608.05668
pdf_url: https://arxiv.org/pdf/2608.05668
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: 多模态金融交易Agent框架
tags:
- Multimodal Trading
- Agentic Intelligence
- Financial Fusion
- Noise-Robust Regularization
- Modality-Aware Fusion
- LLM-based Agents
one_liner: 提出层次化多模态Agent架构，通过自适应融合与噪声鲁棒正则化，实现金融交易年化收益平均提升超20%
practical_value: '- **层次化多模态Agent分工**：在电商推荐或广告投放中，可借鉴将文本、图像、用户行为等多模态数据交由不同专用Agent分别处理，再融合预测，提升信号提取的精细度。

  - **模态感知自适应融合**：设计动态权重调节机制，根据上下文自动学习不同模态的重要性，可应用于商品主图+描述+评论的多模态排序场景，避免静态融合带来的信息折损。

  - **噪声鲁棒一致性正则**：金融数据的噪声问题在搜索/推荐系统中同样存在（如异常点击、刷单），该正则化方法可迁移到点击率预估或Agent决策的在线学习，提升模型对噪声样本的稳定性。

  - **Agent化交易决策流程**：虽然面向金融，但其“感知-融合-决策”的Agent链式架构可复用到广告智能出价或动态定价Agent，实现多源信息驱动的自适应策略。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：金融交易依赖多模态数据（价格序列、文本新闻等），但现有LLM Agent对跨模态依赖建模不足，且易受市场噪声干扰，导致决策不稳。

**方法关键点**：
- **层次化专用Agent**：部署多个子Agent分别处理不同模态（如价格趋势、新闻情感），提取模态专属信号。
- **模态感知自适应融合**：引入可学习的动态权重，自动捕捉细粒度跨模态交互，避免简单拼接。
- **噪声鲁棒一致性正则**：通过对输入施加扰动并强制输出一致性，增强模型对噪声的抵抗能力。

**关键结果**：在GOOG、TSLA等6个股票及加密货币上，相对16个基线，平均年化收益提升超过20%，GOOG和TSLA分别实现120.48%和148.41%的收益率，验证了其在动态市场中的有效性和鲁棒性。
