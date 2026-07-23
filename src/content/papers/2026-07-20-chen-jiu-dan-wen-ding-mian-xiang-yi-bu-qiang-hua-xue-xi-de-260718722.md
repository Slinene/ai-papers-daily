---
title: 'Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous
  Reinforcement Learning'
title_zh: 陈旧但稳定：面向异步强化学习的陈旧自适应信任域
authors:
- Junyao Yang
- Yucheng Shi
- Zongxia Li
- Zhongzhi Li
- Ruhan Wang
- Xiangxin Zhou
- Kishan Panaganti
- Haitao Mi
- Leowei Liang
affiliations:
- Tencent Hy LLM Frontier
- National University of Singapore
- University of Maryland, College Park
- University of Georgia
- Indiana University
arxiv_id: '2607.18722'
url: https://arxiv.org/abs/2607.18722
pdf_url: https://arxiv.org/pdf/2607.18722
published: '2026-07-20'
collected: '2026-07-23'
category: Training
direction: 异步 RL 训练稳定性优化
tags:
- asynchronous RL
- trust region
- PPO
- staleness adaptive
- MoE routing
one_liner: 用 detached log-ratio 作为陈旧度代理，自适应收缩 PPO 区间端点，稳定异步 RL 训练
practical_value: '- 在电商/广告推荐系统的在线异步 RL 训练（如 PPO 策略梯度）中，可直接复用 **detached log-ratio
  作为 staleness 代理**，无需额外模型即可量化策略与行为策略的偏差，据此识别高风险更新样本。

  - 采用 **仅收缩 sign-selected 端点** 的区间约束，在保留大部分 token 原有 PPO 行为的同时，仅对高陈旧度导致的异常外向更新进行保守截断，实现细粒度稳定控制。

  - 针对推荐模型可能采用的 MoE 架构，**路由重放（routing replay）** 技巧可缓解异步陈旧带来的路由不一致问题，与裁剪配合形成互补稳定器，适合大规模稀疏激活的推荐模型训练。

  - 工程上，该方法在 SGLang 多推理引擎 + Megatron 异步训练框架下验证有效，可直接迁移到类似解耦架构的推荐 Agent 在线学习系统中，提升训练吞吐下的策略稳定性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：异步 RL 在提升吞吐的同时引入陈旧样本，落后策略、引擎延迟和 MoE 路由进一步放大陈旧度，PPO 的 clipping 仅是向外更新的采样代理，无法有效约束高陈旧更新。

**方法**：提出 **陈旧自适应信任域（SAT）**，用 **detached 采样 log-ratio 作为实用陈旧度代理**，通过 **基于陈旧度的高斯核缩放函数** 识别 batch 内高偏差尾部，并仅对 **PPO 原始区间的 sign-selected 端点** 施加有效收缩。此举在普通 token 上保持 PPO 行为，而对新截获的极端外向更新施加更保守的约束，从理论上证明了 **局部区间包含和逐点悲观性**。

**结果**：在 Qwen3-30B-A3B + SGLang + Megatron 的解耦异步 RL 设置中，**SAT-GSPO w/ R3** 在 lag1 达到 AIME24 avg@8 **35.83**，lag8 达到 **34.79**；SAT-GSPO 在 lag1 达到 34.17。自适应裁剪与路由重放互为补充，共同稳定异步训练。
