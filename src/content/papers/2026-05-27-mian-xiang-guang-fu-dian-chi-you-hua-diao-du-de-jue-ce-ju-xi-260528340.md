---
title: Decision-focused learning for optimal PV-Battery scheduling
title_zh: 面向光伏电池优化调度的决策聚焦学习
authors:
- Joris Depoortere
- Hussain Kazmi
- Johan Driesen
affiliations:
- KU Leuven
arxiv_id: '2605.28340'
url: https://arxiv.org/abs/2605.28340
pdf_url: https://arxiv.org/pdf/2605.28340
published: '2026-05-27'
collected: '2026-05-28'
category: Other
direction: 决策聚焦学习 · 预测与优化协同
tags:
- decision-focused learning
- PV forecasting
- battery scheduling
- LSTM
- convex optimization
- warm start
one_liner: 将预测与优化任务联合训练，通过 warm-start 方式在 20 栋住宅上降低平均电费 7.8%
practical_value: '- **业务目标对齐训练**：推荐系统中常以 CTR、CVR 为中间指标，可以借鉴 DFL 将最终收益（如 GMV）直接作为损失指导召回或排序模型训练，避免统计精度与业务目标的脱节。

  - **Warm‑start 策略**：先用传统损失预训练，再用任务相关损失微调，能兼顾预测稳定性与下游收益，适合从已有高精度模型迁移到新业务目标。

  - **凸优化层嵌入**：若线上决策问题可建模为凸优化（如动态定价、资源分配），可用 cvxpylayers 等工具将其可微化，端到端训练前向预测模型，直接优化决策质量。

  - **注意其他不确定参数的影响**：系统中若存在多个不确定输入（如推荐里的用户意图），DFL 会受其噪声影响，warm‑start 可缓解这种脆弱性，值得在
  Agent 多智体协同中参考。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
家庭光伏-电池系统的经济性高度依赖准确的日前光伏功率预测，但传统预测模型以 RMSE 等统计指标为目标，并未考虑下游的电池调度成本。当预测存在不可避免的偏差时，最小化 RMSE 不保证最小化电费。决策聚焦学习（DFL）将预测与优化联合训练，让预测器直接为调度任务服务。

**方法关键点**  
- 数据：荷兰 20 栋住宅 2018‑2021 年负荷与光伏数据，模拟电池及动态电价。PV 预测输入为历史 PV、含噪声的 DNI 预报、时间变量，负荷预报也加入噪声以模拟实际。
- 模型：LSTM 为预测器，cvxpylayers 嵌入凸优化层（日电费最小化，含电池 SOC、充放电功率等约束）。DFL 损失为“后悔值”：用预测 PV 得到的调度成本与用真实 PV 的最优成本之差。训练时需做两次优化前向传播以计算后悔。
- 策略：对比四种模型——朴素季节模型、标准 LSTM（MSE 训练）、冷启动 DFL、warm‑start DFL‑WS（先用 MSE 预训练，再用后悔值微调）。

**关键结果**  
- 20 栋建筑 14 个月测试期内，DFL 比 LSTM 平均相对成本降低 3.6%（从 43.6% 降至 40.0%，相对于无优化与完美预报之间的差距）。DFL‑WS 进一步降到 35.4%，即额外降低约 8%。
- RMSE 方面：LSTM S‑RMSE 8.2%，DFL 19.9%，DFL‑WS 13.7%，说明 DFL 牺牲了统计精度但换来了更高经济效益。
- 显著性：DFL‑WS 在所有建筑上均成本更低，Diebold‑Mariano 检验 p＜0.001。
- 负荷预报噪声影响：当负荷预报质量恶化时，DFL‑WS 仍保持优势，冷启动 DFL 则在极高噪声下表现最差。

**值得记住的一句话**  
“用下游任务损失训练的预报器以更高的统计误差换回了实打实的电费节省，warm‑start 是平衡预测稳定性与决策质量的关键一招。”
