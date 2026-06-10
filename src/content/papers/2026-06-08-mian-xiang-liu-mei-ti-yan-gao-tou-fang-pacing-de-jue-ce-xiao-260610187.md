---
title: Decision-Calibrated Conformal Uncertainty for Pacing Decisions in Streaming
  Advertising
title_zh: 面向流媒体广告投放 pacing 的决策校准 conformal 不确定性
authors:
- Prashant Shekhar
- Caroline Howard
affiliations:
- Embry-Riddle Aeronautical University
arxiv_id: '2606.10187'
url: https://arxiv.org/abs/2606.10187
pdf_url: https://arxiv.org/pdf/2606.10187
published: '2026-06-08'
collected: '2026-06-10'
category: RecSys
direction: 广告投放 pacing · 决策校准不确定性量化
tags:
- conformal prediction
- pacing
- advertising
- decision calibration
- dual-weighted score
- robust optimization
one_liner: 通过投影预测误差至策略价值/约束方向而非全库存空间，实现更紧凑的 pacing 鲁棒认证半径，避免过度保守。
practical_value: '- **决策无关方向的噪声不应当约束投放决策**：将库存预测误差投影到 pacing 策略目录的敏感方向（价值、配送、预算、体验负载）后再校准半径，可大幅缩小不确定性集，避免为无关维度预留松弛，直接用于实时竞价或预算分配的鲁棒控制。

  - **预测模型选型应依据“决策半径”而非 MAE**：实验表明，最低测试 MAE 的模型不一定给出最小 pacing 半径，季节性岭回归在 Criteo 上的半径（17.7）比
  Transformer（481.0 MAE 最小）更小，指导工程选型时需在验证集上计算决策相关的 conformal 分位数，而非只看预测损失。

  - **conformal 校准可嵌入现有的“预测-优化”管道**：文中 split-conformal 仅需历史校准块，无需修改预测器，可直接用于电商广告 budget
  pacing、个性化推荐曝光控制等场景，对已有 forecast 模块做轻量级包装，输出鲁棒策略或未解决短名单，提升决策可靠性。

  - **鲁棒优化与 conformal 半径结合可作为安全阀**：当 conformal 半径施加后，策略目录中无可行解时自动返回“未解决”状态，避免执行高违规风险策略，这种机制可以用于防止超投、超预算或用户体验恶化，适合有严格约束的广告系统。'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
流媒体广告平台需要提前为未来不确定的库存、需求、增量响应和用户体验负载做出 pacing 决策。传统方法校准预测残差时平等对待所有库存维度，导致不确定性集过大，为许多对当前策略目录无影响的“无关库存”预留了不必要的松弛，使得 pacing 决策过于保守。本文提出决策校准 conformal 框架，将预测误差投影到策略目录的敏感方向（价值、配送、预算、用户负载）上，生成更紧凑的鲁棒半径，仅在决策相关方向控制风险。

**方法关键点**  
- **双加权预测分数**：对每个部署策略 π，计算其灵敏度向量 w_π（拉格朗日对偶梯度），预测误差 e 的决策影响定义为 max_π |⟨w_π, e⟩|，即策略目录下最大拉格朗日变化。
- **几何最小性**：该分数等于所有 w_π 与 -w_π 的凸包（策略敏感集）的支持函数，且是覆盖整个目录的最小有效标量证书（定理 4.1）。
- **分量级校准**：为支持实际部署，对平台价值、交付不足、预算超支、用户负载四个分量分别计算灵敏度方向和 conformal 分位数半径，采用 Bonferroni 校正控制整体 α。
- **鲁棒选择器**：用点预测值减去价值半径、约束加半径，求解 max lower bound, s.t. upper bounds，得到认证策略；若无可行解则输出未解决短名单。
- **响应与体验不确定性融合**：将增量响应和用户经验的不确定区间进一步收紧价值下界和约束上界（如 doubly robust 估计 ±1.96se）。

**实验设置**  
使用 Criteo Uplift（随机对照广告效果）和 KuaiRand（序列推荐曝光）两个公开数据集，构建 120 个 流式块的仿真环境（60 训练、30 校准、30 测试），包含 12 个 pacing 策略的目录。比较三种方法：点预测基线、通用残差 conformal（全库存欧式半径）、决策校准 conformal。

**关键结果**  
- Criteo：通用残差半径高达 7236.7，决策校准半径降至 18.4；认证策略 pace_i3_q1 的违规率从点预测的 16.7% 降至 3.3%，预算和用户负载违规为零。
- KuaiRand：决策校准半径从 4629.4 降至 278.6，但因用户负载和交付不确定性仍无策略通过认证，输出未解决，符合设计预期。
- 预测器对比：Transformer 获得最低测试 MAE（481.0），但季节性岭回归获得最小决策半径（17.7），说明降低预测损失不等同于降低决策不确定性。
- 响应估计：使用 doubly robust 校正后，Criteo 的稳健响应输入 0.01094，仍认证同一策略，表明方法对合理响应不确定性不敏感。

**最值得记住的一句话**  
预测、响应和用户体验模型的价值应通过它们是否缩小 pacing 决策所使用的 uncertainty 来评判，而非单纯的预测精度。
