---
title: 'Xetrieval: Mechanistically Explaining Dense Retrieval'
title_zh: Xetrieval：机械式解释密集检索决策
authors:
- Zhixin Cai
- Jun Bai
- Yang Liu
- Jiaqi Li
- Yichi Zhang
- Taichuan Li
- Zhuofan Chen
- Zixia Jia
- Zilong Zheng
- Wenge Rong
affiliations:
- Beihang University
- BIGAI
arxiv_id: '2605.29507'
url: https://arxiv.org/abs/2605.29507
pdf_url: https://arxiv.org/pdf/2605.29507
published: '2026-05-27'
collected: '2026-05-31'
category: RAG
direction: 密集检索可解释性 · 嵌入空间
tags:
- dense retrieval
- explainability
- embedding space
- mechanistic interpretation
- sparse features
- chain-of-thought internalization
one_liner: 提出嵌入空间内推理内部化与稀疏特征分解框架，首次实现密集检索个体决策的机械式可解释性
practical_value: '- **检索模型透明度提升**：借鉴推理内部化思想，可在推荐双塔模型的嵌入层注入轻量级推理路径，使查询-物品相似度计算附带可追溯的推理痕迹，便于线上调试与审计。

  - **特征级归因与干预**：利用稀疏可解释特征重叠解释单个配对决策，可迁移至电商搜索或推荐系统的归因分析，定位具体特征对匹配结果的贡献，并通过特征引导调整检索偏好（如强调品牌匹配或价格敏感度）。

  - **在线系统友好设计**：推理内部化避免自回归生成，仅需额外单次前向传播，适合对延迟敏感的在线检索与推荐服务，可直接在现有双塔模型基础上微调部署。

  - **任务级特征操控**：在电商多域场景中，可对检索模型进行特征级方向控制，快速适配不同业务目标（如新品冷启动时侧重“新颖性”特征），无需重新训练。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：密集检索通过高维嵌入计算相关性，决策过程完全不透明，现有解释方法仅停留在词法匹配、token对齐或事后文本理由等表层信号，无法揭示嵌入层面的内在因素。
**方法**：提出Xetrieval框架，包含两步：1）推理内部化器——将思维链推理过程近似映射到嵌入空间，通过单次前向传播为句子嵌入注入推理信息，避免昂贵的自回归生成；2）稀疏特征分解——将推理增强后的嵌入分解为一组稀疏且人类可解释的特征，每个特征关联自然语言描述。对文档侧构建多个视图，聚合查询与文档在稀疏特征空间的重叠，从而在特征粒度上解释单个检索决策。
**结果**：在多种检索器（E5、BGE等）和多个基准上，Xetrieval成功提取出连贯可解释特征，成对干预实验表明其解释比基线更忠实，且能在任务层面通过特征引导改变检索行为。
