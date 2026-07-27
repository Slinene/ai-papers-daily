---
title: 'PinEqualizer: Full Funnel Content Exploration and Debiasing System at Pinterest'
title_zh: Pinterest全漏斗内容冷启动探索与去偏系统PinEqualizer
authors:
- Olafur Gudmundsson
- Bo Zhao
- Huayi Liao
- Anna Kiyantseva
- Sai Xiao
- Heath Vinicombe
- Mostafa Keikha
- Luke DeLuccia
- Zihao Chen
- Junpeng Hou
affiliations:
- Pinterest, Inc.
arxiv_id: '2607.22518'
url: https://arxiv.org/abs/2607.22518
pdf_url: https://arxiv.org/pdf/2607.22518
published: '2026-07-24'
collected: '2026-07-27'
category: RecSys
direction: 全漏斗冷启动探索与去偏
tags:
- cold-start
- exploration
- debiasing
- full-funnel
- recommender systems
- industrial-scale
one_liner: 提出覆盖语料、召回、排序的全漏斗冷启动解决方案，通过去偏与探索结合高效测量框架显著提升新鲜内容分发与用户参与
practical_value: '- **特征工程去偏**：使用内容唯一依赖的Embedding（VLM/CLIP）避免图Embedding对新鲜内容的偏倚；对历史互动特征做Individual
  Dropout，迫使模型更依赖内容信号；通过DCNv2交叉内容年龄、内容特征与互动特征，让模型动态调整偏好。

  - **低成本的探索策略**：在效用层加入基于实时印象数的简单UCB奖励（`UCB = α / sqrt(1+β·impressions)`），无需方差估计即可有效提升未探索内容分发；Neural
  Linear UCB精度更高但可解释性差，适合在最终精排中使用。

  - **快速实验与测量**：使用“未探索内容互动量”作为用户A/B实验的代理指标，与长期留存强相关且无内容泄露问题，可大幅加速迭代；长期新鲜内容Holdout实验测量增量价值，证明探索的长期收益大于短期成本。

  - **全漏斗瓶颈分析**：对各阶段新鲜内容的输入占比与输出存活率进行分析，识别瓶颈（如召回不足或排序打压），从而优先投入ROI最高的环节；为搜索表面单独提升相关性权重，保证探索不牺牲语义相关性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
Pinterest面临严重的内容冷启动问题：大量新Pin缺乏与用户图（board graph）的连接，导致曝光困难，富者愈富效应损害内容生态健康。传统方法偏重协同过滤或图信号，无法应对快速变化的内容来源，亟需一套全漏斗、支持搜索与推荐的多表面解决方案。

**方法关键点**  
- **三层测量框架**：长期新鲜内容Holdout实验作为北极星指标；中间代理指标“内容毕业”（content graduation）衡量积累足够互动的新内容量；用户A/B实验中使用“未探索内容互动量”作为快速迭代指标，可克服传统用户-内容同域实验的内容泄露与成本问题。  
- **全漏斗优化**：
  - **语料选择**：利用Thompson Sampling或模型先验筛选高潜新鲜内容组成探索语料，动态退役已毕业或低质内容。
  - **检索**：构建专用探索倒排索引和图随机游走加权（提高未探索Pin的边权重）；统一双塔模型中通过特征去偏（如分离内容与互动特征再融合）减少对旧内容的偏倚。
  - **排序与效用**：特征层面加入纯内容Embedding（如PinCLIP、Unified Visual Embedding）、语义ID，对缺失Embedding进行维度级正态插补，对互动特征做Individual Dropout，并用DCNv2交叉内容年龄与内容/互动特征；校准层按内容类型校准；效用层引入基于印象数的UCB奖励，或Neural Linear UCB，搜索表面还结合相关性分数对探索项加权，确保低质内容不获得过多探索优势。  

**关键实验**  
系统上线后，新鲜内容总印象提升350%。YoY对比，北美整体成功会话提升24%，国际提升49%；购物会话北美提升63%，国际提升29%；28天内毕业的内容量增长41%；成功内容提供者数量增长99%。组件消融显示，加入探索语料和排序特征改善对未探索内容互动量提升最明显（分别+16.92%和+18.52%），Neural Linear UCB相比简单UCB有+5.32%的增量，但简单方案因易解释而被广泛采用。

**核心一句话**  
“全漏斗去偏与探索必须协同改进，并用灵敏的短期代理指标加速迭代，才能将内容冷启动的长期成本转化为用户留存的净增益。”
