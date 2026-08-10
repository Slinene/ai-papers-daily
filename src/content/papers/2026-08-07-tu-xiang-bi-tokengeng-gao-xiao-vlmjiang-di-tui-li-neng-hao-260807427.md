---
title: 'A Picture is Worth a Thousand Tokens: How Vision Language Models Cut AI Energy
  Costs While Improving Accuracy'
title_zh: 图像比Token更高效：VLM降低推理能耗同时提升时序异常检测精度
authors:
- Bhavika Jalli
- Nikhil Korati Prasanna
- Jayanta Choudhury
affiliations:
- Ericsson
arxiv_id: '2608.07427'
url: https://arxiv.org/abs/2608.07427
pdf_url: https://arxiv.org/pdf/2608.07427
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: VLM用于数值时序的Token高效推理
tags:
- Vision-Language Models
- Token Efficiency
- Energy Efficiency
- Time-Series Anomaly Detection
- Multimodal AI
- Telecom Analytics
one_liner: 将时间序列转为2D图表输入VLM，减少3.6-10.4倍输入Token，推理能耗降1.8-2.5倍且精度大幅提高
practical_value: '- 电商/广告系统的实时监控指标（如QPS、转化率时序）可转为图表输入VLM做异常检测或根因分析，避免原始数值Token爆炸，显著降低成本。

  - 在多模态Agent架构中，可将结构化数据（如分日报表、A/B测试指标序列）先渲染为图像，再交给VLM做语义推理，突破纯文本上下文窗口限制。

  - 该思路可推广至需要处理大量连续数值特征的推荐/搜索模型辅助分析场景（如Embedding漂移监控），用VLM替代纯文本LLM实现能耗和可扩展性平衡。

  - 微调VLM时，图表+自然语言指令的混合提示设计值得借鉴：保留时间趋势的视觉先验，让语言模型聚焦语义判断，可能迁移到广告素材效果分析或用户行为序列理解。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：LLM推理能耗占AI总能耗90%以上，且输入Token数直接决定成本。在电信网络监控中，多变量KPI时间序列窗口（24个以上指标）展开成浮点数文本后，Token量常超过128K上下文限制，同时导致推理能耗过高。

关键方法：将时间序列绘制为2D折线图，使用VLM（Llama-3.2-90B-Vision、Qwen2.5-VL-72B、Pixtral-12B）直接对图像进行异常检测，从而避免序列化数值Token。通过微调实现视觉模态与语言指令的联合推理。

关键结果：相比纯文本LLM，VLM输入Token减少3.6~10.4倍，实测推理能耗降低1.8~2.5倍，在监测200个基站的边缘部署中每日可节约约7.2 MJ。微调后的Llama-3.2-90B-Vision在电信异常检测上精度比文本版高220.7%，比LSTM/ARIMA基线高144%以上。在公开基准上，Pixtral-12B的J/F1分数提升20.6倍，平均F1达0.82。当KPI数量达到24个时，文本表示超出多数产品LLM的上下文窗口，而视觉输入仍保持在标准限制内。
