---
title: 'NMKFR: A Robust Framework for Time-Aware Cold-Start Recommendation'
title_zh: NMKFR：时间感知冷启动推荐的鲁棒框架
authors:
- Chengzhi Liu
- Ning Zeng
- Zehui Qu
affiliations:
- Southwest University
arxiv_id: '2607.26429'
url: https://arxiv.org/abs/2607.26429
pdf_url: https://arxiv.org/pdf/2607.26429
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 时间感知冷启动 · 卡尔曼融合
tags:
- Cold-Start
- Time-Aware
- Kalman Filter
- Memory-Augmented
- Uncertainty Calibration
one_liner: 提出神经记忆卡尔曼融合推荐器，利用后验协方差校准语义-时间融合以应对冷启动
practical_value: '- 使用卡尔曼滤波器建模物品生命周期中的不规则时间间隔，可迁移至电商新品冷启动的状态跟踪，融合交互时间衰减。

  - 后验协方差作为不确定性信号自适应平衡语义与时序分支，为多模态融合提供置信度加权思路，避免简单拼接。

  - 基于Titans的记忆增强语义编码器能更有效地从物品文本中抽取长期依赖，适用于电商商品的标题、描述等文本侧信息。

  - 框架的鲁棒性分析和有界不确定性行为为线上部署提供安全性保证，可作为推荐系统的置信度输出。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：新物品冷启动面临交互稀疏和推荐环境动态变化的双重挑战。静态内容、早期反馈和时序状态证据的可靠性随物品生命周期波动，现有方法难以自适应地融合这些异质信息。

**方法**：提出神经记忆卡尔曼融合推荐器（NMKFR），包含两条分支：
- 语义分支：基于Titans的记忆增强编码器，从物品文本中提取记忆增强的观测表征，捕获长期语义依赖。
- 时序分支：利用卡尔曼滤波器在非规则交互间隔下估计物品的隐状态，获得时序演化表征。
核心创新在于使用后验协方差作为不确定性信号，动态校准语义记忆检索强度，并自适应融合语义与时序分支，从而在交互稀疏时侧重内容，交互增多时依赖时序信号。

**结果**：在Amazon Video Games和MovieLens-32M数据集上，按时间感知和物品冷启动协议采样候选排序，NMKFR在所有对比方法中取得了最优的保留指标。消融实验证实了后验协方差引导融合的有效性，诊断实验显示不确定性内部行为有界，验证了模型在离线评估下的鲁棒性。
