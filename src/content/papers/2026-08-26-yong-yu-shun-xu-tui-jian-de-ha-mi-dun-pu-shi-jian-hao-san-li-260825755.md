---
title: Hamiltonian Spectral-Temporal Dissipative Dynamics for Sequential Recommendation
title_zh: 用于顺序推荐的哈密顿谱-时间耗散动力学
authors:
- Shuiying Liao
- P. Y. Mok
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2608.25755'
url: https://arxiv.org/abs/2608.25755
pdf_url: https://arxiv.org/pdf/2608.25755
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 序列推荐 · 二阶动力学与频域建模
tags:
- Sequential Recommendation
- Hamiltonian Dynamics
- Frequency Domain
- Momentum Extrapolation
- State Space
one_liner: 将用户偏好演化建模为耗散哈密顿系统，用频域谱传播与动量外推提升序列推荐
practical_value: '- 可借鉴「位置+动量」的二阶状态设计：在电商会话或广告点击流中，用户兴趣常出现惯性回摆（看了一圈商品后回到原品类）和短期热点偏离，传统一阶
  RNN/Transformer 只更新当前隐状态，难以表达这类动态。可以在现有序列模型里增加一个动量通道，并用阻尼项衰减短期冲动，物理先验能提升稀疏行为建模。

  - 频域传播用 RFFT/IRFFT 将长序列演化降到 O(T log T)，且参数量少。工程上可直接用 GPU 上的批量 FFT 替代标准 self-attention
  的长程依赖建模，在用户行为序列很长时能显著降低延迟和显存；但需注意 FFT 分支不适合超短序列，需配合局部卷积。

  - 局部脉冲分支（DWConv1D + 门控融合）专门处理突发点击和噪声，与全局平滑轨迹互补。电商推荐里常有大促、直播带货等短期爆点，可以在主模型旁路加一个轻量局部卷积分支，用
  sigmoid 门控融合到最终表示，提升对热点的响应速度。

  - One-step phase-space extrapolation 用当前动量外推下一步状态，而不是只取最终位置。这种「预测用户去向而非现在在哪」的思想适用于
  next-item、next-query 或 push 消息生成，可以在推理时把趋势方向作为额外打分信号。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐普遍假设偏好演化是一阶过程：下一状态只依赖当前隐状态。但真实用户行为常常包含惯性、周期性和突然偏移：例如用户看了几部动作片，短暂被科幻预告吸引后又回到动作片，这本质上是二阶动力学中的惯性、临时偏差和阻尼恢复。论文据此将偏好演化重铸为**耗散哈密顿系统**，在相空间同时建模位置（稳定偏好）和动量（短期倾向），以更完整地刻画用户兴趣动态。

### 方法关键点
- **二阶动力学建模**：每个隐维度服从阻尼驱动谐振子方程 \(m_i \ddot{q}_i + c_i \dot{q}_i + \kappa_i q_i = f_i\)，其中质量 \(m_i\)（惯性）、阻尼 \(c_i\)（遗忘速率）、刚度 \(\kappa_i\)（偏好稳定性）均为可学习参数。
- **频域谱传播**：利用傅里叶变换将 ODE 转为代数方程，定义谱传播子 \(G(\omega)=1/(\kappa - m\omega^2 + ic\omega)\)，分母由物理方程固定，分子是可学习复数。通过 RFFT/IRFFT 在 \(O(T\log T)\) 内完成全局长程演化，避免 time-domain 模拟。
- **局部脉冲分支**：并行使用深度可分离时序卷积（DWConv1D）建模突发点击或短期好奇，再经门控融合到全局轨迹中，处理稀疏日志中的尖锐波动。
- **末端相空间恢复与动量外推**：对最终隐藏序列重新做 RFFT 求导恢复动量，保证位置与动量同源；预测时执行一步 Euler 外推 \(\hat{q}_u = q_T + \Delta t M^{-1} p_T\)，用动量预测下一步兴趣，而非仅用最终位置。

### 关键结果
在 Amazon-Beauty、Amazon-Video-Games、MovieLens-1M 上，HSR 在 Hit@10/NDCG@10/MRR@10 上总体超过 Transformer、HSTU、DIFF、Mamba4Rec 等基线。稀疏数据上优势明显：Amazon-Beauty NDCG@10 0.0566 vs DIFF 0.0527（+7.4%），MRR +10.34%；Amazon-Video-Games NDCG +10.57%，MRR +17.42%。参数量仅 4.74M，比 Mamba4Rec 少 21.91%，训练时间减半，推理吞吐 60k QPS。消融显示 Hamilton 结构、短时脉冲、相空间外推均有效，模型对噪声注入也更鲁棒。

**最值得记住的一句话**：二阶动力学 + 频域传播 + 动量外推为序列偏好建模提供了物理启发、可解释且高效的归纳偏置。
