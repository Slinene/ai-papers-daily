---
title: Adaptive Loss Balancing for Noise-Robust GRPO in Generative Recommendation
title_zh: 面向生成式推荐的噪声鲁棒自适应损失平衡 GRPO
authors:
- Kewei Xu
- Junbo Qi
- Yanyan Zou
- Pengfei Zhang
- Xingzhi Yao
- Shengjie Li
affiliations:
- JD.com
- Waseda University
- University of Electronic Science and Technology of China
arxiv_id: '2606.08480'
url: https://arxiv.org/abs/2606.08480
pdf_url: https://arxiv.org/pdf/2606.08480
published: '2026-06-07'
collected: '2026-06-09'
category: GenRec
direction: 生成式推荐 · RL后训练
tags:
- Generative Recommendation
- GRPO
- Reward Noise
- Adaptive Clipping
- E-commerce
one_liner: 通过样本级门控让 GRPO 只在策略不确定且奖励可靠时才更新，解决奖励模型噪声问题。
practical_value: '- 在生成式商品推荐（如 Semantic ID 召回）的 RL 后训练中，不要均匀信任奖励模型：对每个样本分别计算策略侧难度（ground
  truth 是否落在策略 top-τ 之外）和奖励侧判别力（RM 是否把正确项排在头部且彻底压制无关负例），仅当两者同时满足时才施加 GRPO 更新，其余样本仅用监督
  NLL 损失。这种选择性更新可避免重复奖励模型噪声。

  - 保留监督 NLL 作为稳定锚点，GRPO 作为附加项，通过一个二值 clip 系数 gating。超参数只需要两个比例 τ、ρ（阈值比例），基于排名确定，不受绝对分值影响，易于迁移和调参。

  - 奖励判别力诊断中，使用来自同一 batch 其他 query 的生成负例作为“跨样本扰动项”，无需额外模型即可检验 RM 的局部校准程度，计算成本极低，是实用技巧。

  - 经过离线（HR 提升与低幻觉）和线上 A/B（有效 IPV、UCTR、停留时长显著增长，类目多样性未降）验证，方法在真实电商场景中可安全、稳定地提升 RL
  训练效果，避免 reward hacking 引起的多样性坍塌。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐（如 Semantic ID 解码）结合 RL 后训练能超越监督模仿，但严重依赖奖励模型的可靠度。产业界常用的多目标排序模型在曝光有偏日志上训练，对长尾和未曝光商品评分不准确。分析发现，平均而言 RM 对训练样本的排名修正接近零，甚至有害；然而，当策略不确定（ground truth 不在 rollout 前排）且 RM 能清晰区分正负例时，RM 的单点影响可提升数倍。因此，统一施加奖励信号不安全，需要选择性信任。

**方法关键点**：
- 提出 AdaGRPO，以监督 NLL 为锚点，对 GRPO 损失引入**样本级二值门控**。
- 门控由两个基于 rollout 的诊断构成：**策略侧难度**（ground truth 是否在策略 top-τ 比例之外）和**奖励侧判别力**（ground truth 在 RM 排名 top-τ 内，且从同一 batch 其它 query 随机采样的负例全部落在 bottom-ρ 之外）。只有两者同为真，α=1 激活 GRPO 更新；否则 α=0，退化为纯监督。
- 诊断复用 GRPO 已有的 rollout 和奖励分数，无额外采样成本，超参数仅 τ、ρ，以 rollout 数 K 为基准，免于绝对阈值调参。
- 可视为 PPO 裁剪从 token 级到 sample 级的推广：定义信任区域基于哪些样本值得被 RL 更新，而非每个 token 更新的幅度。

**关键结果**：
- 实验基于大规模电商日志（约 17.5 万序列），基模型为 SFT 的 decoder-only LLM，物品用分层 Semantic ID，奖励模型为曝光偏差下的 CTR 排序器。
- 离线：最佳中间 checkpoint 将 HR@10 从基线的 11.01% 提升至 12.18%，幻觉率 ≤0.22%；最终 checkpoint 仍保持 HR@10=11.63%、幻觉率 0.27%，优于固定混合 NLL+GRPO。在难度分位数分析中，增益集中在中等难度样本，符合门控设计意图。
- 在线 A/B：有效 IPV 提升 0.43%（显著），UCTR 提升 0.27%，停留时长提升 0.23%，且曝光和点击类目数增加，未损害多样性。
- 核心启示：“在生成式推荐中应用 RL 的核心挑战不是设计更强的奖励，而是判断何时可以信任它们。”
