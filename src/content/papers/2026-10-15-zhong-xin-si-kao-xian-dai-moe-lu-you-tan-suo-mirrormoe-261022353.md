---
title: Rethinking Routing Exploration in Modern Mixture-of-Experts
title_zh: 重新思考现代 MoE 路由探索：MirrorMoE
authors:
- Bingcong Li
- Hao Ma
- Michael Muehlebach
- Niao He
- Yi Ma
affiliations:
- ETH Zurich
- The University of Hong Kong
- Max Planck Institute for Intelligent Systems
- WU Vienna
arxiv_id: '2610.22353'
url: https://arxiv.org/abs/2610.22353
pdf_url: https://arxiv.org/pdf/2610.22353
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: MoE 预训练路由探索优化
tags:
- MoE
- routing exploration
- shared experts
- pretraining
- load balancing
one_liner: MirrorMoE 通过 token 自适应抑制低概率路由专家缩小探索空间，解决细粒度共享专家 MoE 的探索困境并稳定涨点
practical_value: '- 若服务链路使用 DeepSeek/Qwen3 等 MoE 基座做 embedding、生成式推荐或 Agent 策略，当启用或调大
  fine-grained top-k 时，不要假设 shared experts 一定带来收益；可先做单 expert 消融或随机路由诊断，确认 shared
  experts 是否主导输出并压制路由探索。

  - 训练阶段可采用 MirrorMoE 式“选择分布与聚合分布分离”：用镜像 logits 选专家，用原始 logits 权重聚合，再把 rho 从 0.4 cosine
  退火到 0；工程实现只需额外一次 softmax 和符号翻转，训练成本几乎不增。

  - 负载均衡 loss 应加在实际贡献概率 xi 上，而不是选择概率 p 上；当低权重专家被激活但几乎不贡献时，这种设计能避免均衡目标误导路由，可迁移到多兴趣/多任务
  MoE 推荐模型。

  - 若模型不含 shared experts，MirrorMoE 提升有限；不要盲目上该 trick，应优先用于 shared-expert + 较大 K 的配置，并在增大
  K 时重点观察是否出现“K 涨指标不涨甚至下降”的探索困境。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机

现代 MoE 越来越普遍地同时采用两种设计：细粒度专家切割（更大 E 和 K，路由空间组合数爆炸）和共享专家（对所有 token 激活）。论文识别出一个探索困境：共享专家在训练中会主导 token 表示，使 routed experts 对输出的影响变小，从而让不同路由选择产生的表示差异很小，削弱路由探索；与此同时，细粒度切割又需要更大的探索空间。结果是共享专家的收益随 K 增大而消失，甚至 K 增大反而掉点。

## 方法关键点

- 提出 MirrorMoE，不鼓励探索，而是通过 token 自适应抑制不必要专家来缩小探索空间。
- **Mirror routing**：路由概率由原始 softmax 分布 xi 和符号翻转 softmax 分布 zeta 凸组合得到，使选择偏向 logits 两端，用这个分布做 top-(K-S) 选择。
- **Mirror aggregation**：聚合时使用原始 logits 对应的概率 xi，而不是镜像选择概率 p；因此被选中的低 logit 专家得到极小聚合权重，功能上被抑制，有效专家数 Keff 下降。
- **训练调度**：rho 从 0.4 按 cosine 退火到 0，逐步恢复完整路由空间；负载均衡 loss 作用在原始贡献概率 xi 上，而不是镜像选择概率 p 上。

## 关键实验

在 DCLM 数据集、Megatron-LM 框架上训练 100M 到 2.4B 参数共享专家 MoE，配置 R=64/128、S=2、K=6-10。

- 预训练 PPL：100M 从 54.78 降到 51.77；498M 从 28.31 降到 27.36；625M 从 28.46 降到 27.84；2.4B 从 21.17 降到 20.50。
- 2.4B 模型下游 6 个常识推理任务平均提升 1.64 点。
- 在 K=6/8/10 下，MirrorMoE 均让 shared-expert MoE 超过无 shared experts 版本，并恢复 K 增大带来的收益。
- 消融：cosine 调度 + rho0=0.4 最优；非自适应调 K 的 baseline 不如 MirrorMoE；无 shared experts 时 MirrorMoE 提升有限。

## 最值得记住的一句话

共享专家会压制路由探索；用镜像 logits 选择专家、原始 logits 聚合，并将 rho cosine 退火，可以在几乎不增加训练成本下恢复 K 增大带来的表达力。
