---
title: 'WattGPU: Predicting Inference Power and Latency on Unseen GPUs and LLMs'
title_zh: WattGPU：预测未见GPU和LLM的推理功耗与延迟
authors:
- Mauricio Fadel Argerich
- Jonathan Fürst
- Marta Patiño-Martínez
affiliations:
- Universidad Politécnica de Madrid
- Zurich University of Applied Sciences
arxiv_id: '2607.02391'
url: https://arxiv.org/abs/2607.02391
pdf_url: https://arxiv.org/pdf/2607.02391
published: '2026-07-02'
collected: '2026-07-03'
category: Other
direction: 推理能耗预测 · 机器学习系统
tags:
- inference power prediction
- LLM deployment
- GPU efficiency
- sustainable AI
- regression model
one_liner: 仅用公开元数据与规格，无需硬件即可预测LLM在未见GPU上的推理功耗和延迟，泛化良好。
practical_value: '- 在引入新GPU或新LLM时，可快速预估推理功耗与延迟，替代昂贵的手工profiling，辅助部署前硬件选型。

  - 模型仅依赖公开的LLM参数表和GPU规格（如内存带宽、TDP），无需购置或租用设备，能大幅降低评估成本。

  - 给出的中位绝对百分比误差在离线场景约3.4%，服务器场景约13.5%，虽非生产级精度，但GPU排序相关性高（Kendall τ≥0.76），适合做粗筛，识别表现突出的GPU型号。

  - 仓库开源，可将自有的LLM与硬件数据加入扩展，为广告/推荐系统中Agent、查询改写等LLM服务做容量规划和性价比对比。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM推理正成为数据中心能耗增长最快的部分，为每个模型选择最省电的GPU需要大量实测，现有预测工具依赖profiling数据且对未见硬件泛化差。为此需要一种仅依赖公开信息、无需硬件访问的预测方法。

**方法关键点**：WattGPU包含两个独立模型——平均GPU功率预测与Token间延迟（ITL）预测。输入仅为LLM参数量、层数、Hidden Size等元数据，以及GPU的Memory Bandwidth、TDP等规格，不需要任何profiling。特征工程结合物理公式（Roofline模型、TDP缩放），模型本身采用线性/轻量回归结构，保证可解释性与泛化性。

**结果**：在42个开源LLM（0.1B–27B参数）和8款NVIDIA服务器GPU上，留一GPU未见泛化测试：离线场景功耗中位绝对百分比误差≤3.4%，服务器场景≤13.5%；延迟误差≤8.5%；GPU排序的Kendall τ≥0.76。相比传统的TDP缩放功耗和Roofline延迟基线，误差降低约2–4倍。
