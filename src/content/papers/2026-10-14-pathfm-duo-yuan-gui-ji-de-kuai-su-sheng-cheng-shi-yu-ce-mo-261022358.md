---
title: 'PathFM: Fast Generative Forecasting of Multivariate Trajectories'
title_zh: PathFM：多元轨迹的快速生成式预测模型
authors:
- Jiachen Yao
- Xiyuan Zhang
- Annan Yu
- Boran Han
- Abdul Fatir Ansari
- Shuai Zhang
- Michael Bohlke-Schneider
- Bernie Wang
affiliations:
- California Institute of Technology
- Amazon
arxiv_id: '2610.22358'
url: https://arxiv.org/abs/2610.22358
pdf_url: https://arxiv.org/pdf/2610.22358
published: '2026-10-14'
collected: '2026-10-18'
category: Other
direction: 生成式时间序列预测 · Flow Matching
tags:
- Flow Matching
- Time Series
- Foundation Model
- Trajectory Forecasting
- Distillation
- Probabilistic Forecasting
one_liner: PathFM 用 flow matching 生成完整多元轨迹，通过蒸馏与共享 KV cache 实现近单次查询速度，并取得最优路径分数
practical_value: '- 需求/流量预测：电商大促、广告库存等场景需要累积需求、峰值、到达时间等轨迹级指标，用 flow matching 替代纯分位数模型可同时保留多步依赖与不确定性，适合
  downstream 优化。

  - 工程加速：多轨迹采样通过蒸馏到 1-2 步 + 共享 history attention cache 显著降低在线推理成本；类似思路可迁移到生成式推荐或 Agent
  场景中需要对同一上下文做多次采样的模块。

  - 校准损失直接优化：蒸馏后采样器支持端到端校准目标，比事后校准更稳定；在电商不确定预测（如缺货概率、风险控制）中可借鉴。

  - 评估指标：引入 energy score / variogram score 评估路径依赖，比单纯 CRPS 更能反映序列依赖结构，可用于多步推荐收益预测、广告投放轨迹评估。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有时间序列基础模型（TSFM）多预测边际分位数，缺失未来轨迹间的依赖结构。但累积需求、峰值负载、事件时间等下游指标依赖整条路径，点预测与边际概率评分无法反映。需要能生成完整未来路径且保持依赖结构的模型。

**方法关键点**：PathFM 基于 flow matching 生成完整多元轨迹。为提升推理速度，蒸馏采样器至 1-2 步，并在多次采样间共享历史 attention cache，使多条路径采样耗时约等于一次分位数模型查询。蒸馏后的采样器还可直接优化校准损失。评估方面引入 fps-bench，在 fev-bench 任务上增加 energy score、variogram score 及下游指标。

**关键结果**：在 fev-bench 和 TIME 上边际精度有竞争力；在 fps-bench 上聚合路径分数高于所有外部基线；混沌系统实验中长期变异性保持，而强基线迅速坍缩。整体实现生成式时间序列预测的实用化。
