---
title: 'TPPO: Tracking-Value PPO For Language Model Reasoning'
title_zh: TPPO：用于语言模型推理的追踪价值 PPO
authors:
- Futing Wang
- Chenxi Li
- Jianhao Yan
- Yun Luo
- Zhi Wang
- Yizhuo Li
- Runzhe Zhan
- Yu Cheng
- Tao Lin
affiliations:
- Zhejiang University
- Westlake University
- Shanghai AI Laboratory
- The Hong Kong University of Science and Technology
- Nanjing University
arxiv_id: '2610.16794'
url: https://arxiv.org/abs/2610.16794
pdf_url: https://arxiv.org/pdf/2610.16794
published: '2026-10-11'
collected: '2026-10-14'
category: Training
direction: RLVR 中 PPO 价值函数参数化改进
tags:
- PPO
- RLVR
- Value Function
- Credit Assignment
- LLM
- Reasoning
one_liner: 将 PPO critic 改为逐 token logit 增量累加，在稀疏二元奖励下显著提升推理训练的 token 级信用分配与策略性能
practical_value: '- 若在 LLM 驱动的对话式推荐/搜索 Agent 中用 PPO 做 RL 训练，且奖励是终端转化/点击式的稀疏二元信号，可将
  critic 从独立预测 prefix value 改为累积 logit 参数化：每 token 输出一个 scalar，累加后 sigmoid 得到 prefix
  value，损失用 BCE；实现成本低，不需要 process reward。

  - 该方法直接改善 GAE 中相邻 token 的优势排序，减少噪声信用分配；对于需要区分多步推理中关键步骤（如商品筛选、需求澄清）的场景，能提升策略学习的稳定性，尤其适合长轨迹
  CoT。

  - 注意其假设是 γ=1、binary terminal reward；若业务奖励是 dense 或连续值（如 GMV、转化概率加权），需先做二值化或改造 logit
  分解，否则收益可能不成立。

  - 在评估 critic 质量时，可借鉴 SNR-conditioned sign accuracy 与 MC anchor 估计，用少量采样诊断训练中 critic
  是否在跟踪值演化，避免训练后期价值函数退化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
PPO 在 RLVR 中广泛用于提升 LLM 推理能力，但标准 critic 独立预测每个前缀的值，不显式建模值沿轨迹的演化 ΔV_t；而 ΔV_t 的符号直接决定 token 级优势排序，错误预测会反转信用分配。实证表明，PPO critic 对 ΔV 的符号准确率在训练中从 50.34% 降到 45.91%，接近随机，说明这是系统性问题。

## 方法关键点
- 在 binary terminal reward 且 γ=1 下，前缀价值等于 continuation 成功概率；连续前缀价值满足 Bayesian 更新，在 log-odds 空间具有可加增量：logit V(s_{t+1}) − logit V(s_t) = log-likelihood ratio。
- TPPO critic 将该结构参数化为累积 logit：bV_t = σ(Σ_{i=1}^t f_φ(s_i))，每个位置输出一个标量增量，求和后经 sigmoid 重构前缀价值。
- 使用终端 outcome 的 BCE 损失训练重构价值，无需额外 rollout 或 process-level 标注；bV_t 直接接入标准 GAE 和 PPO clipped objective。
- 相比标准 critic 的 MSE/BCE 独立预测，该累积参数化显式建模值演化，每个增量通过后缀聚合梯度学习。

## 关键结果
- Qwen3-4B-Base 和 Qwen3-8B-Base 数学推理平均分比 PPO 分别提升 7.0 和 8.4 个百分点，OOD 泛化也一致提升；n=1 下 Qwen3-4B 提升 10.1 个百分点。
- Countdown 任务提升 4.6/3.2 分；科学编程 Qwen3.5-9B LiveCodeBench Code Gen.v6 提升 15.5 分，平均提升 7.0 分。
- 值演化方向准确率显著高于 PPO，advantage sign accuracy 高 15.3–19.9 个百分点；消融显示增益主要来自累积参数化，BCE 提供额外收益。

最值得记住的一句话：在稀疏二元奖励下，显式建模值演化的 critic 参数化能显著改善 token 级信用分配，且几乎没有额外成本。
