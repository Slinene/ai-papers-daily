---
title: 'What Gets Hacked in a Collaborative Reward for LLM Recommenders: The Part
  That Does Not Depend on the User'
title_zh: LLM 推荐中协同过滤奖励的漏洞：与用户无关的 item 均值分量
authors:
- Zhuangsheng Li
- Liang Dong
- Yu Wu
- Dailin Li
- Yu Xia
- Yunhan C. Zhang
- Rui Cai
- Yi Wu
- Julian McAuley
affiliations:
- University of California, San Diego
- Google Inc.
- University of Virginia
- University of Melbourne
- University of California, Davis
arxiv_id: '2611.07588'
url: https://arxiv.org/abs/2611.07588
pdf_url: https://arxiv.org/pdf/2611.07588
published: '2026-11-05'
collected: '2026-11-06'
category: GenRec
direction: 生成式推荐 · RL 奖励修正
tags:
- LLM4Rec
- RL reward
- exposure collapse
- popularity bias
- GRPO
- Semantic ID
one_liner: 识别 CF 奖励中的 item-mean 分量导致曝光坍缩，per-item centering/standardization 将 top-1
  多样性提升最高 9.8 倍且精度基本不降
practical_value: '- 在用 CF/双塔等 scorer 作为 LLM 策略的 RL 奖励前，先做 per-item centering：离线抽样几千条用户历史对
  catalog 打分，训练时 reward = r - m̂(i)，只需维护 item bias lookup table，不动 CF 模型和 GRPO 就能显著缓解曝光坍缩。

  - 需要更均匀长尾曝光时，再除以 item 历史得分 std（z-score），并设 std floor（如 10th 分位），避免低方差 item 被过度放大；该方法在
  SASRec/GRU4Rec/two-tower/CTR head 上均成立，可推广到不同 scorer。

  - 调试 reward hacking 时，把奖励拆成 item 全局均值 + user residual 两项分别训练：若 item-mean 单项导致 top-1
  骤降，就能定位是全局 bias，而不是个性化信息丢失。

  - 线上评估不要只看 HR/NDCG：CF reward 训练中 HR@10 几乎不变但 top-1 品种数腰斩，建议监控 distinct top-1 items、coverage@10
  和 exposure Gini，保护中小商家曝光。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 推荐直接用 CF 模型分数作为 RL 奖励，虽然能提供细粒度个性化反馈，却会导致曝光坍缩：推荐集中在少量 item 上，即使 CF 模型直接排序仍保留用户差异。例：Beauty + Semantic IDs 下 HR@10 仅从 0.0851 变为 0.0843，但 distinct top-1 从 1317 跌到 837；Sports 从 840 跌到 169。

**方法关键点**
- 将 CF 分数分解为 `r(u,i)=m(i)+ε(u,i)`，其中 `m(i)=E_u[r(u,i)]` 是 item 全局均值分量，`ε` 是 user-specific 残差。
- 控制干预：只训练 `m̂(i)` 时 top-1 仅剩 32 个，而只训练残差得到 1830 个，定位 item-mean 是曝光坍缩来源。
- Per-item centering：RL 前采样 4000 条历史，对 catalog 打分求 `m̂(i)`，奖励改为 `r - m̂(i)`。
- Per-item standardization：进一步 `(r - m̂(i)) / max(σ̂(i), s0)`，s0 取 σ̂ 的 10th 分位，抑制低方差 item 被过度放大。统计量预计算一次并冻结。

**关键实验**
Amazon Beauty / Sports & Outdoors，Semantic/Atomic IDs，Qwen2.5-0.5B + GRPO。对比 CF reward、random/rule reward、popularity penalty、HiLaR、Dr. GRPO 等。
- Per-item standardization 的 distinct top-1 是 CF reward 的 1.6–9.8 倍；Sports Semantic IDs 从 169 增至 1652，centering 增至 699。
- HR@10 基本持平或小幅波动，mid-tier HR@10 提升 1.3–2.8 倍；16 组 CF 架构组合和两种额外 LLM backbone 均有效。

**一句话**
用 CF 分数做 RL 奖励前，先减去每个 item 的跨用户均值，再视需要除以其标准差，别直接喂 raw logits。
