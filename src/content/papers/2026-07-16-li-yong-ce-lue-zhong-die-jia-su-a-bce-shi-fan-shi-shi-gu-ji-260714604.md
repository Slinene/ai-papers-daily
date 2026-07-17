---
title: 'Accelerating A/B-Tests with Counterfactual Estimation: Reducing Variance through
  Policy Overlap'
title_zh: 利用策略重叠加速A/B测试：反事实估计视角
authors:
- Olivier Jeunen
affiliations:
- Independent Researcher
- aampe
arxiv_id: '2607.14604'
url: https://arxiv.org/abs/2607.14604
pdf_url: https://arxiv.org/pdf/2607.14604
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 反事实估计 · A/B测试加速
tags:
- A-B Testing
- Off-Policy Evaluation
- Variance Reduction
- Doubly Robust
- Ranking
- Causal Inference
one_liner: 将随机流量分配视为元策略，用Δ-OPE利用策略重叠达成严格方差缩减，并提供最优流量与排名扩展
practical_value: '- **免费方差缩减**：在线上A/B测试中直接使用Δ-IPS或Δ-DR代替标准DiM，仅需记录两个策略的动作分布，当新旧模型存在重叠时即可自动获得更低方差，无需改变流量分配或延迟实验。

  - **非平衡流量设计**：放弃固定的50/50分流，利用历史日志估计策略分歧度，计算方差最优分流比p*（例如对探索性策略倾斜流量），可额外减小18%以上的方差（模拟显示）。

  - **聚焦模型训练**：Δ-MRDR loss对样本加权 wΔ²，让奖励模型集中拟合策略分歧区域，在推荐场景异构用户分布下，可比标准Δ-DR再降约8%的ATE估计方差。

  - **排名实验加速**：对推荐/搜索排序，用Δ-DCG并加入位置最优基线（Δβ*⊥⊥-DCG），可抵消策略分歧增大时的方差膨胀，始终优于传统均值差，可直接用于多臂A/B测试中的曝光指标评估。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
A/B测试是推荐系统在线评估的金标准，但用户指标（点击率、观看时长等）噪声大，检出微小效果需要长时间实验。当实验组与对照组策略对同一用户做出相同动作时，该样本不贡献ATE信号反而增加噪声，标准DiM估计器不加区分地赋予同等权重，导致统计功效被稀释。实际中的模型更新大多是增量式的，策略重叠度高，这一结构性信息远未被利用。

**方法关键点**
- **Δ-OPE视角**：将随机流量分配视为元策略 π0= pπ + (1-p)π′，直接使用策略感知的重要性权重 wΔ=(π(a|x)-π′(a|x))/π0(a|x)，代入Δ-IPS或Δ-DR得到无偏ATE估计。
- **严格方差优势**：证明当策略存在重叠且残差方差非零时，Var(Δβ★ᴵᴾˢ) ≤ Var(DiM)，且降幅正比于策略分歧。该优势自动继承到回归调整版本（RADiM vs Δ-DR）。
- **最优分流设计**：推导方差关于流量比p的凸目标函数J(p)，可基于实验前数据求解p★，仿真中p★≈0.81较50/50额外降低18%方差。
- **Δ-MRDR**：加权最小二乘损失 L=∑ wΔ² (y - fθ(x,a))²，让reward model容量集中在策略分歧大的区域，进一步压低ATE方差。
- **排名扩展Δ-DCG**：在位置点击模型下，用曝光倾向替换动作倾向，并引入每个位置的最优基线β*⊥⊥，得到方差可控的排名ATE估计器。

**关键实验结果**
模拟环境验证：Δ-IPS在动作空间从10到5000的扩展中，MSE始终低于DiM，策略高重叠时方差趋近零；在异构场景中，Δ-MRDR使ATE方差比Δ-IPS降低75%、比Δ-DR再降8%；排名实验中，Δβ*⊥⊥-DCG在策略分歧从0到1的全区间方差都低于传统DiM。

**最值得记住的一句话**
“只要新旧策略存在共同动作且该重叠区域有残差方差，以Δ-OPE方式重写A/B测试估计器就能自动获得严格方差缩减，几乎零工程开销。”
