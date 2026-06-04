---
title: 'RePercENT: Scaling Disentangled Representation Learning Beyond Two Modalities'
title_zh: RePercENT：将解耦表示学习扩展到超越双模态的可扩展框架
authors:
- Vasiliki Rizou
- Pascal Frossard
- Dorina Thanou
affiliations:
- EPFL
arxiv_id: '2606.05109'
url: https://arxiv.org/abs/2606.05109
pdf_url: https://arxiv.org/pdf/2606.05109
published: '2026-06-03'
collected: '2026-06-04'
category: Multimodal
direction: 可扩展多模态解耦表示学习
tags:
- Disentangled Representation
- Multimodal Learning
- Self-Supervised
- Scalable
- Pre-extracted Embeddings
one_liner: 提出自监督框架 RePercENT，从预提取的多模态嵌入中联合解耦共享与独特成分，突破两模态限制，大幅降低计算成本
practical_value: '- **多模态商品理解**：直接使用商品图像、标题、描述等预提取特征（如 CLIP/bert 嵌入），解耦出共享语义与模态特有属性（如视觉风格、文本细节），改善多模态检索与推荐中的跨模态匹配。

  - **低成本即插即用**：无需昂贵的多模态联合预训练，可利用现有各模态基础模型的嵌入进行快速实验与部署，适合电商场景中多模态数据快速接入。

  - **可扩展至多模态**：业务中常涉及图像、文本、用户行为、音频等多源数据，该框架天然支持超过两种模态的解耦，为多模态融合提供更细粒度的可控性。

  - **理论保证下的稳定解耦**：联合优化目标与理论分析确保了共享/独特成分的可辨识性，避免解耦崩溃，可借鉴其损失设计思路，提升推荐系统中多模态特征的解耦质量。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多模态学习通常依赖对齐与融合，忽略模态间共享与特有因素的显式建模，而解耦表示学习受限于两模态扩展性瓶颈。
**方法**：提出自监督框架 RePercENT，直接操作预提取的多模态嵌入，设计联合优化目标同时推导共享和独特成分，并给出解最优性的理论保证。框架呈“即插即用”式，不依赖底层模型或联合预训练，可自然扩展到超过两种模态。
**结果**：在图像、音频、文本等多种模态组合上，成功恢复出有意义的解耦表示，在下游任务中取得竞争力性能，且计算复杂度较现有方法显著降低。
