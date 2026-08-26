---
title: 'Beyond the Stability-Exploration Dilemma: Environmental Regularization for
  LLM Policy Optimization'
title_zh: 环境正则化策略优化：用 Query-KL 解耦 LLM 训练的稳定与探索
authors:
- Xianlei Zhou
- Xiangdi Meng
- Yu He
- Tianyu Qi
- Shuyan Guan
- Xianli Zhang
- Jian Zhang
- Xin Li
- Qika Lin
- Jun Liu
affiliations:
- AMAP, Alibaba Group
- Xi’an Jiaotong University
- JD.com
- Beijing Normal University
- National University of Singapore
arxiv_id: '2608.23311'
url: https://arxiv.org/abs/2608.23311
pdf_url: https://arxiv.org/pdf/2608.23311
published: '2026-08-23'
collected: '2026-08-26'
category: Training
direction: LLM 强化学习训练稳定性优化
tags:
- ERPO
- Query-KL
- Policy Optimization
- RLVR
- GRPO
- Exploration-Stability
one_liner: 提出 ERPO，将 KL 正则从输出侧移到输入 query 分布侧，在保持探索的同时控制训练环境漂移
practical_value: '- 在生成式推荐/query 改写等 LLM RL 训练中，可尝试用 Query-KL 替代或补充 Policy-KL：约束模型对输入
  prompt 的似然漂移，而不是限制输出分布，从而保留输出空间探索，缓解长程训练崩溃。

  - 工程实现低成本：用 pre-RL 参考模型预计算并缓存训练集中每个 query 的 log-likelihood，训练时直接复用当前 policy 的前向结果计算
  Query-KL；无需额外 forward pass，可直接插入现有 GRPO/PPO/RLOO 框架。

  - 对每个 query 按参考模型下的似然做加权（低概率 query 降权），可降低梯度方差、减少对长尾/低质 prompt 的过拟合，适合电商/搜索中 user
  query 分布不均的场景。

  - 用多温度采样（如 0.1~1.5）评估 RL 训练后的模型稳定性，能暴露高温解码下的性能退化，比单一温度更全面；可作为生成式模型上线前的稳定性测试手段。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM 策略优化（RLVR）长期面临稳定性与探索的两难：主流做法在动作侧加 Policy-KL 正则，但会限制响应分布、消耗探索预算；同时训练中模型对 query 的似然会随参数更新持续漂移，导致环境非平稳和梯度方差增大，长程训练容易出现高温解码崩溃或 reward hacking。

## 方法关键点
- **Query-KL 正则**：将正则化从输出分布移到输入 query 分布。定义 policy-induced query distribution ρθ(q)=Pθ(q)，即模型对 prompt 的自回归序列似然。惩罚 KL(ρθ||ρθ0)，其中 ρθ0 为 pre-RL 参考模型。
- **结构化解耦**：Query-KL 的梯度只流经 query log-likelihood ∇θℓθ(q)，不包含 response score function ∇θ logπθ(o|q)，因此不对输出分布施加直接梯度压力，保留探索。
- **Query 重加权**：用参考模型派生的每个 query 权重 w(q)∝ℓθ0(q)，对 advantage 做 query 级加权，偏向参考分布下典型的 query，降低梯度方差，提升高温采样鲁棒性。
- **零额外开销**：参考 ℓθ0 训练前一次性计算并缓存，当前 ℓθ 直接复用 PG 前向结果，无需额外 forward pass；可插入 GRPO/PPO/REINFORCE 等估计器。

## 关键实验
- 训练数据：MATH Level 3-5 约 8.5K 数学题；模型：Qwen2.5-Math-7B 和 32B；baseline：GRPO。
- 评估：AIME24/25、AMC、MATH500、Minerva、OlympiadBench 六个基准，多温度采样 0.1~1.5。
- 主要结果：ERPO 的平均 Avg@32 为 0.336，较 GRPO 的 0.274 提升 6.2%；Pass@32 提升 3.64%，Pass@1 提升 5.69%。在 MATH500 上，仅替换 Query-KL 就带来 15.9% 的平均提升。长程训练 1K steps 下，GRPO 在 400 步后高温性能显著退化，而 ERPO 保持稳定；Train-Eval gap 从 6.47% 缩小到 3.14%，降幅约 51%。

> 最值得记住的一句话：把 KL 正则从输出分布挪到输入 query 分布，以极低的工程成本实现稳定性与探索的结构化解耦。
