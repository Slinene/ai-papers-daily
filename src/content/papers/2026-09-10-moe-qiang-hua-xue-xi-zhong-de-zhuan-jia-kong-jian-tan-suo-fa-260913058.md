---
title: Expert-Space Exploration in MoE Reinforcement Learning
title_zh: MoE 强化学习中的专家空间探索方法 ESRL
authors:
- Hongyi He
- Zhenghao Lin
- Xiao Liu
- Peng Cheng
- Yan Lu
- Yeyun Gong
affiliations:
- Tsinghua University
- Microsoft Research
arxiv_id: '2609.13058'
url: https://arxiv.org/abs/2609.13058
pdf_url: https://arxiv.org/pdf/2609.13058
published: '2026-09-10'
collected: '2026-09-16'
category: Training
direction: MoE LLM 强化学习 · 专家路由空间探索
tags:
- MoE
- Reinforcement Learning
- GRPO
- Exploration
- Expert Routing
- Post-training
one_liner: 通过扰动专家路由、锚定高置信专家并重放路径，在 MoE LLM 的 RL 训练中实现安全的架构级探索，提升推理性能
practical_value: '- **MoE 生成式推荐/Agent 策略训练可迁移**：若用 MoE LLM 作为生成式推荐（如 Semantic ID 生成、query
  改写）或 Agent 策略网络，在 RL/在线学习阶段可将 expert routing 作为额外探索维度，通过扰动 router logits 提升轨迹多样性，缓解策略收敛后
  rollout 多样性下降、优势信号变弱的问题。

  - **锚定专家采样控制探索质量**：不要对全部专家加噪声，而是保留 top-K 中的高置信专家作为锚点，只从候选池中随机探索剩余专家；聚合权重仍使用原始 logits。这一
  trick 能防止随机路由到不合适的专家导致生成质量崩塌，对搜索/推荐场景中的生成质量稳定性尤其重要。

  - **路由重放（Rollout Routing Replay）保障 rollout 与训练一致**：在在线学习或 RL 训练中，记录 rollout 时实际激活的专家路径，优化阶段绕过
  Top-K 直接复用该路径，避免因重计算路由导致探索到的专家未参与梯度更新。该方法与业务中常见的 MoE 在线学习/增量训练场景直接兼容。

  - **自适应噪声强度**：根据 router 的归一化熵调整扰动幅度——低熵（分布尖锐）时加大噪声，高熵时减小噪声。相比固定噪声，能更平稳地探索，尤其适用于需要兼顾效果稳定性的电商/广告长尾
  query 或 item 生成任务。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

RL 已成为 LLM 后训练的核心，但 MoE 架构下的 RL 工作多聚焦优化稳定性与效率，将专家选择视为固定组件。传统 GRPO 依赖 token 级别采样提供 rollout 多样性，然而同一前缀下 MoE 的 Top-K 路由确定不变，导致可探索的计算子网络受限。随着训练推进策略趋于集中，rollout 多样性下降，组相对优势信号减弱。论文发现：直接对 router logits 加噪声能改变专家激活路径、重塑 next-token 分布，产生类似提高解码温度的多样性效果，但无约束扰动可能激活不合适的专家，严重降低 rollout 质量。这引出了核心问题：能否安全地利用专家路由空间作为 MoE LLM 强化学习的额外探索维度？

## 方法关键点

ESRL 在 rollout 阶段扰动 router logits，但采用三个组件控制质量：

- **自适应噪声调整**：根据归一化路由熵 H_t,ℓ 动态设置高斯噪声强度 σ_t,ℓ = σ_min + (σ_max - σ_min)(1 - H_t,ℓ)。路由分布尖锐时（低熵）加大扰动，分布弥散时减小扰动，避免过度破坏已有的不确定路由。
- **锚定专家采样**：将 K 个激活专家分为 K_anchor 个锚定专家和 K_explore 个探索专家。锚定专家直接由原始 Top-K 选出；探索专家从候选池（排除锚定专家后 top-M_explore）中加噪声后选取。激活后聚合权重仍使用原始 router logits，只改变离散计算路径，保留原始相对置信度。
- **Routing Replay**：记录每条 rollout 轨迹的完整专家激活路径 Z_i，优化阶段绕过 Top-K，强制使用记录路径计算 logits 和 MoE 输出，确保探索到的专家参与梯度更新，减少 rollout 与训练间的路由不匹配。

ESRL 保持 GRPO 目标函数不变，仅修改 rollout 阶段的专家选择机制，因此可与优化器/奖励层面的改进正交叠加。

## 关键实验与结果

在 Qwen3-30B-A3B（top-K，激活8/128）、Sigma-20B-A0.5B（top-1）、Moonlight-16B-A3B（共享专家）三种 MoE 骨架上，覆盖数学推理（OlympiadBench、AIME 2024、AMC、MinervaMath）与科学/代码任务（GPQA、MMLU-Pro、MMLU-Redux、LiveCodeBench）。对比 GRPO、GSPO、GRPO-R3、RO-GRPO、Aux-Loss、N-Sampling。

核心结果：Qwen3-30B-A3B 上平均 Pass@1 达 42.1%（较 GRPO 提升 3.2 个百分点），Pass@8 达 64.2%（提升 4.5 个百分点）；科学/代码平均 Pass@1 从 53.2 提升到 55.9，Pass@8 从 64.9 提升到 77.0。在 Instruct 模型上同样带来稳定增益。分析显示 ESRL 在低温度、小样本组下优势更明显，能维持更多“有信息量”的组（同时含正确与错误回答），并缓解训练过程中专家负载失衡。

## 最值得记住的一句话

专家路由空间是 MoE LLM 强化学习中除 token 采样以外的有效互补探索维度，通过锚定、候选池约束和路径重放，可以安全地利用这一架构特性提升 rollout 多样性与训练效率。
