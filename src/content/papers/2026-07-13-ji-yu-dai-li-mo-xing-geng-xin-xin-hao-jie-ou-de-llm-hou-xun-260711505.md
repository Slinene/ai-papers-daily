---
title: 'Proxy Exploration and Reusable Guidance: A Modular LLM Post-Training Paradigm
  via Proxy-Guided Update Signals'
title_zh: 基于代理模型更新信号解耦的 LLM 后训练模块化范式
authors:
- Daocheng Fu
- Rong Wu
- Yu Yang
- Xuemeng Yang
- Jianbiao Mei
- Licheng Wen
- Pinlong Cai
- Yong Liu
- Botian Shi
- Yu Qiao
affiliations:
- Shanghai AI Laboratory
- Fudan University
- Zhejiang University
- Shanghai Innovation Institute
- Shanghai Jiao Tong University
arxiv_id: '2607.11505'
url: https://arxiv.org/abs/2607.11505
pdf_url: https://arxiv.org/pdf/2607.11505
published: '2026-07-13'
collected: '2026-07-15'
category: Training
direction: LLM 后训练 · 代理探索 · 信号解耦
tags:
- Proxy Exploration
- Update Signal Transfer
- Post-Training
- Distribution Matching
- Weak-to-Strong Generalization
- LLM Alignment
one_liner: 用轻量代理模型探索相对改进信号并解耦式传输，实现异步、可复用的跨模型后训练
practical_value: '- **低成本探索与迁移**：在推荐模型或 Agent 策略训练中，可利用小模型（如蒸馏版或轻量级网络）作代理，探索用户反馈/奖励信号，将相对改进信号迁移到大模型，大幅降低采样与评估成本。

  - **异步信号缓存与复用**：解耦后，代理探索的更新方向可独立存储为分布差异对，一次探索、多模型复用，适合多场景（电商搜索、广告推荐）快速对齐不同版本主模型，无需重复完整RL
  pipeline。

  - **弱到强泛化迁移**：相对改进信号不依赖代理绝对能力，弱代理探索的信号可有效提升强主模型，适用于利用用户行为日志训练小模型提取偏好、再迁移至大规模生成式推荐模型。

  - **校准系数控制迁移强度**：借鉴λ的锚点校准机制，在迁移时根据主模型当前状态动态调整信号强度，避免过更新，可在电商/广告的强化学习训练中实现更稳定的策略迭代。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有LLM后训练方法（PPO/GRPO）将策略探索与分布对齐紧密耦合，探索成本高且难以跨模型复用优化信号；OPD等分布匹配虽加速对齐，但仍须依赖主模型自身去探索高奖励分布，限制了异步生成和信号迁移。因此需要解耦探索与对齐，实现高效、可复用的后训练。

**方法**：提出Proxy-guided Update Signal Transfer（PUST）框架，分为三阶段：
- **代理探索**：用轻量代理模型执行GRPO等奖励优化，得到优化前后策略对（πϕ 与 πϕ+），避免主模型直接在线采样。
- **更新信号提取**：计算代理模型在每个token状态的相对改进信号Δϕ(a|st) = log(πϕ+/πϕ)，捕捉奖励驱动的方向性变化，而非绝对分布。
- **信号传输**：将提取的信号通过带校准的目标函数传输给主模型πθ，目标为最小化Lproxy = -E[Σ πθ(·)(Δϕ - λ log(πθ/πref))]，其中λ>0为校准系数，防止过更新。整个流程中πϕ, πϕ+, πref冻结，仅更新πθ。

**关键结果**：
- 数学基准：Qwen3-4B代理信号传输至8B主模型，Average Mean@16达47.5（base 17.3），接近4B自身RL的46.5，且训练步数仅50步（GRPO需500步）。
- 代码基准：4B→8B在HumanEval+/MBPP+/LCB上Average 60.5（base 55.9）。
- 信号可复用：同一代理信号传输至1.7B/4B/8B均一致提升，50步内收敛。
- λ调优关键：过小（如0.5）导致性能崩溃，最优λ随代理-主模型差距增大而增大（4B→8B λ*=1.08；1.7B→8B λ*=1.57）。
- 探索质量：弱代理信号接近强主模型直接GRPO的效果，更多探索步数或数据可进一步缩小差距。
