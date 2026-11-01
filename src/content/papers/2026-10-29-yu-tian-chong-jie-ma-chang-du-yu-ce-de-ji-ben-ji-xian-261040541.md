---
title: On the Fundamental Limits of Prefill-Based Decoding Length Prediction
title_zh: 预填充解码长度预测的基本极限
authors:
- Haowen Shi
- Xuzhe Yan
- Fahao Chen
- Peng Li
affiliations:
- Xi'an Jiaotong University
- Shandong University
arxiv_id: '2610.40541'
url: https://arxiv.org/abs/2610.40541
pdf_url: https://arxiv.org/pdf/2610.40541
published: '2026-10-29'
collected: '2026-11-01'
category: LLM
direction: LLM推理调度与基准协议
tags:
- Decoding Length Prediction
- LLM Inference
- Prefill
- Stochastic Process
- Benchmarking
- Central Limit Theorem
one_liner: 揭示解码长度预测中的系统误差主导性，推导出所有基于预填充的方法必须遵守的统计界限
practical_value: '- 在 LLM 生成式推荐或 Agent 对话系统中，解码长度预测可用于响应时间预估、超时设置与批量调度；可直接借鉴论文中的正态/CLT
  模型对长度分布建模，用均值和方差快速估算尾部风险，无需部署复杂预测器。

  - 评估任何解码长度预测模型时，必须固定模型版本、数据分布、采样参数（temperature/top-p/top-k），否则预测精度数字不可比；应同时报告相对误差指标，避免被绝对
  MAE 误导。

  - 若要在业务中优化推理资源或做容量规划，先训练一个简单 MLP 逼近理论界限，作为系统误差基线；若复杂模型（FiLM、MoE 等）无法显著超过该基线，则不需要引入额外复杂度，节省工程成本。

  - 方差律 σ=αμ+b 可直接用于线上 SLA 估算：只需统计平均解码长度即可估算方差区间，辅助确定告警阈值、超时上限以及 GPU 并发调度策略。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 推理调度需要仅凭 prefill 隐藏状态预测解码 token 数，但现有基准在不同模型、数据集或采样配置下精度剧烈波动，根源被忽略。

**方法关键点**：将解码视为停止随机过程；每步停止概率并非恒定，而是在数百步内逐渐上升，因此解码长度由大量局部终止决策共同决定，满足中心极限定理。推导出 per-prompt 正态分布及显式误差项，并得到仿射方差律 σ=αμ+b，斜率 α 等于响应段数的变异系数。

**关键结果数字**：正态律复现 per-prompt MAE 和长度分布中心质量，误差在几个百分点内；轻微右偏和过量峰度与采样噪声修正预测一致。在固定模型、数据、采样条件下，MLP、EGTP、FiLM、soft-label、MoE 变体等广泛预测器性能收敛至接近理论界限，表明系统误差主导模型误差。建议基准协议固定模型、数据、采样参数，并报告相对误差与绝对误差。
