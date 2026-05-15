---
title: 'Nexus : An Agentic Framework for Time Series Forecasting'
title_zh: Nexus：多智能体时间序列预测框架
authors:
- Sarkar Snigdha Sarathi Das
- Palash Goyal
- Mihir Parmar
- Nanyun Peng
- Vishy Tirumalashetty
- Chun-Liang Li
- Rui Zhang
- Jinsung Yoon
- Tomas Pfister
affiliations:
- Google
- Pennsylvania State University
arxiv_id: '2605.14389'
url: https://arxiv.org/abs/2605.14389
pdf_url: https://arxiv.org/pdf/2605.14389
published: '2026-05-13'
collected: '2026-05-15'
category: Agent
tags:
- LLM
- Agent
- Time Series Forecasting
- Multimodal
- Calibration
one_liner: 通过宏微观双分辨率预测与动态校准，Nexus 多智能体框架在零样本预测中超越专业时序模型，并输出可解释推理。
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
专业时序基础模型（TSFM，如 TimesFM-2.5）善于捕捉数值模式，却无法利用新闻、事件等非结构化上下文，对结构性突变脆弱；而 LLM 虽能理解文本，但在纯数值预测上表现不稳，且缺乏对时间序列内在规律的把握。单纯靠单一模型同时处理数值与文本容易导致认知过载或推理偏差，因此需要一种能分解任务、融合多模态信号的新型预测范式。

## 方法关键点
- **三阶分解**：Nexus 将预测拆分为 **Contextualization**（历史上下文清洗与结构化）、**Dual-Resolution Outlook Generation**（宏/微观双分辨率前景生成）、**Forecast Synthesis & Calibration**（合成与校准）三大阶段。
- **宏微观代理**：Macro-Reasoning Agent 从全局趋势推演粗粒度走向；Micro-Reasoning Agent 逐步评估短期催化与波动，二者互补。
- **校准代理**：通过历史回测拆分多折，生成通用审查指南，并经验证集过滤，防止过拟合与泄露。
- **零知识泄露设计**：选用知识截止2025年1月的 Gemini-3.1-Pro 和 Claude-4.5-Sonnet，在严格后于截止日期的 Zillow 房地产（15城周度库存）与 Stock Market（7只股票周度收盘价）数据集上评估。

## 关键结果
- **多模态上下文**：Nexus 显著优于 Chain-of-Thought 基线。Gemini 上 NEXUS 在 Zillow 数据集平均 MAPE 降低 14.7%，RMSE 降低 15.3%；Claude 上更分别降低 86.6% 与 88.6%。
- **纯数值场景**：Nexus 在 Zillow 上 MAPE 降至 0.0378（Gemini），低于 TimesFM-2.5 的 0.0387；在 Stock 上 MAPE 0.1238，优于 CoT 基线 0.1334，与 TSFM 相当。
- **推理质量**：交叉评判下，Nexus 在领域相关性、事件合理性、逻辑-数字一致性及分析深度上均大幅领先，总体偏好率达 79.8%～97.1%。

Nexus 证明，通过分解宏微观预测与动态校准，LLM 驱动的多智能体框架不仅能匹配甚至超越专门时序模型，还能提供驱动预测的透明推理链，将实时预测重新定义为一个智能体推理问题。
