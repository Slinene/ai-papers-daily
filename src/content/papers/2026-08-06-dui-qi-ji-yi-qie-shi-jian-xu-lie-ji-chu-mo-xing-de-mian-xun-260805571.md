---
title: 'Align-RAG: Alignment Is All You Need for TSFM In-Context Learning'
title_zh: 对齐即一切：时间序列基础模型的免训练检索增强预测
authors:
- Mohammad Asadi
- Soheil Hor
- Bardiya Akhbari
- Jack W. O'Sullivan
- Tahoura Nedaee
- Layne C. Price
- Raviteja Anantha
- Euan Ashley
- Ehsan Adeli
affiliations:
- Stanford University
- Amazon
arxiv_id: '2608.05571'
url: https://arxiv.org/abs/2608.05571
pdf_url: https://arxiv.org/pdf/2608.05571
published: '2026-08-06'
collected: '2026-08-08'
category: RAG
direction: 检索增强预测 · 免训练时序对齐
tags:
- Time Series Forecasting
- Retrieval-Augmented Generation
- In-Context Learning
- Foundation Models
- Alignment
- Training-Free
one_liner: 提出免训练的时序对齐方法Align-RAG，证明冻结模型自身即可动态利用检索上下文，无需训练适配器
practical_value: '- 在电商销量/广告点击预测中，可直接使用“幅度缩放+相位平移”的对齐方法，将检索到的相似时间序列与当前序列对齐后输入冻结预测模型，无需训练任何适配器，降低工程复杂度。

  - 用户行为序列预测（如下次购买时间、点击路径）可借鉴此思路：对检索到的历史行为窗口进行均值和方差归一化，并基于互相关计算最佳滞后，再作为冻结基座模型的上下文，有望提升零样本泛化能力。

  - 对推荐系统的RAG设计启示：冻结大模型本身已具备动态利用检索上下文的能力，应优先采用无参数的输入对齐基线，避免过早引入可学习的融合模块，减少训练成本和过拟合风险。

  - 工程实现简单高效：对齐仅需计算均值和方差（幅度缩放）及整数滞后（相位对齐），易于集成至现有检索增强推理流水线，可作为时序预测任务的默认基线。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：检索增强预测通常依赖可训练的融合模块，基于“冻结时序基座模型无法自行利用检索上下文”的假设。本工作指出这一假设并非必要。

**方法关键点**：Align-RAG是一种免训练方法，对每一个检索到的过去-未来窗口，在输入冻结基座模型前，先与当前查询窗口进行闭式对齐。对齐分为两步：
- 幅度重缩放（amplitude rescaling）：将检索窗口的均值和方差调整到与查询窗口一致；
- 相位平移（phase shift）：在-7到+7的整数滞后范围内搜索使互相关最大的滞后，并对检索序列进行相应平移。
对齐后的窗口替代原始检索序列作为模型上下文，无需任何可学习参数。

**关键结果**：
- 在标准基准的7个数据集上，Align-RAG在冻结的Chronos-Bolt上平均MSE降低3.75%，全面超越需要训练的最先进检索适配器。
- 在4种不同架构的额外冻结时序基座模型上，零样本MSE改善幅度为2.5%～13.7%，且无需针对各基座模型调参。
- 分析表明，对齐后的演示能为冻结模型引入与闭式岭预测器高度一致的预测偏移，证实冻结模型本身已具备动态上下文学习能力，闭合形式对齐应作为检索增强预测的默认基线。
