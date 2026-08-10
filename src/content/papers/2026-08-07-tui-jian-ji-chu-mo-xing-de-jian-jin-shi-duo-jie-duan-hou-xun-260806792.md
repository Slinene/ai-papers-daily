---
title: Progressive Alignment of Recommender Foundation Model through Multi-Phase Post-Training
title_zh: 推荐基础模型的渐进式多阶段后训练与业务对齐
authors:
- Oseong Choi
- Hoeinn Kim
- Jihoon Lee
- Byungsoo Kang
- Taeyeong Jang
affiliations:
- NAVER WEBTOON
arxiv_id: '2608.06792'
url: https://arxiv.org/abs/2608.06792
pdf_url: https://arxiv.org/pdf/2608.06792
published: '2026-08-07'
collected: '2026-08-10'
category: RecSys
direction: 推荐基础模型的渐进后训练与奖励对齐
tags:
- Foundation Model
- Progressive Fine-Tuning
- Reinforcement Fine-Tuning
- Reward Modeling
- GRPO
- Online A-B Test
one_liner: 通过三阶段渐进后训练（LP→FFT→RFT）分离适配与对齐，用奖励模型引导策略优化，显著提升深度业务指标
practical_value: '- 当基础模型适配下游任务时，先做线性探测（LP）冻结骨干训练 Task Head，再做全参数微调（FFT），并使用差异化学习率（骨干学习率
  1/10），可有效缓解灾难性遗忘，稳定适配过程。

  - 不要直接将面向业务指标的奖励模型作为排序策略部署；将其作为 RFT 的对齐信号，对基于密集隐式反馈（如点击）训练的排序策略进行 fine-tune，既能提升深层业务指标，又保持强排序能力。

  - 奖励模型训练时，利用倾向得分（IPS）加权矫正曝光偏差，并用序数回归（Ordinal Regression）将多级漏斗转化为连续奖励分数，可作为电商推荐中多阶段转化（浏览→加购→下单→支付）等长周期目标的通用建模方式。

  - 在线上系统上线新模型时，可采用 GRPO 做奖励对齐，其在深度参与指标上优于 DPO；若偏好信号密集且可靠（如基于实际漏斗阶段），DPO 也可作为轻量替代，尤其适合提升即时点击行为。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业界常用单个预训练基础模型（FM）通过 SFT 适配多个推荐场景，但 SFT 优化的点击、阅读等短期目标与长期业务指标（如深度转化、留存）存在差距。直接对稀疏且延迟的业务标签做监督训练，策略泛化能力差。需要将对业务指标的建模与排名策略分离，用奖励信号对齐排序模型。

**方法关键点**：
- 三阶段渐进式后训练：线性探测（LP）→全参数微调（FFT）→强化微调（RFT）。
- LP 阶段冻结 FM 骨干，仅训练新增下游编码器与任务头，在稳定的表示空间中预热随机初始化组件。
- FFT 阶段解冻所有参数，对 FM 骨干施加更小学习率（如 1e-5，下游 1e-4），在保留预训练知识的同时进行下游特化。
- 奖励模型：用六阶段内容消费漏斗（曝光→点击→免费完成→付费进入→付费完成）作为监督信号，采取序数回归输出连续性奖励分，并用裁剪的逆倾向得分（IPS）进行自归一化加权，矫正曝光偏差。
- RFT 阶段：参考策略冻结，策略联合更新策略头与 FM 骨干，通过 GRPO（Group Relative Policy Optimization）或 DPO 利用奖励模型信号进行对齐，添加 KL 散度正则化防止策略偏离。候选组内 top-32 候选进行优势归一化。

**关键结果**：
- 离线：2 阶段 SFT（LP→FFT）较 1 阶段 SFT 显著提升，Rank NDCG +0.008，Funnel NDCG +0.005；在此基础上，GRPO with RM 进一步提升 Rank NDCG 至 0.463（+0.026），Funnel NDCG 至 0.637（+0.012）。直接使用奖励模型排序的 Rank NDCG 仅 0.394，验证了将奖励作为对齐信号而非直接服务的有效性。
- 线上 A/B 测试（千万级用户，一月周期）：所有 FM 变体均优于非基础模型的 CTR*CVR 基准。GRPO w/ RM 在深度参与指标（Engaged/Imp, LastFree/Imp）上提升最大；DPO w/o RM 在点击率上表现最佳。增益在初期后趋于稳定且统计显著（p<0.001）。
