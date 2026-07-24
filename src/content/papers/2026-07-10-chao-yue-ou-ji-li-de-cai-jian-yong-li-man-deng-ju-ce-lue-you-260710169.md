---
title: 'Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian
  Isometric Policy Optimization'
title_zh: 超越欧几里得裁剪：用黎曼等距策略优化克服 LLM RL 探索崩塌
authors:
- Zhicheng Cai
- Xinyuan Guo
- Hanlin Wu
- Mingxuan Wang
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
affiliations:
- Tsinghua University (AIR)
- ByteDance Seed
arxiv_id: '2607.10169'
url: https://arxiv.org/abs/2607.10169
pdf_url: https://arxiv.org/pdf/2607.10169
published: '2026-07-10'
collected: '2026-07-24'
category: Training
direction: RL 训练方法 · 几何优化
tags:
- RL
- PPO
- exploration_collapse
- Riemannian_manifold
- policy_optimization
- LLM
one_liner: 发现 PPO-Clip 的欧氏度量与策略黎曼流形不匹配是探索崩塌的根本原因，提出 RIPO 实现等距更新以平衡探索与利用，大幅提升推理 RL
  性能
practical_value: '- 在推荐/搜索的 policy gradient 训练（如 PPO 排序策略、对话策略）中，直接用 `epsilon = sqrt(delta
  / pi_old)` 动态裁剪重要性比，让低概率动作（冷门 item / 新动作）获得更大更新空间，避免过早收敛到高频动作，保持策略多样性。

  - 工程实现时，将信任域半径 δ 设为 0.02~0.05 即可稳定工作，无需复杂调参；可对用户行为序列中不同位置的 token 或动作单独计算裁剪边界，兼容现有
  GRPO/PPO 框架。

  - 对于多臂赌博机 / 上下文 bandit 在线学习，几何等距裁剪能缓解热门臂的过度利用问题，思路可迁移至 EE 场景的策略更新规则。

  - 在 LLM Agent 的 RL 训练中（工具调用、查询改写），RIPO 可防止 Agent 重复使用少数高频工具而忽略潜在有效的探索路径，提升长程任务成功率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
PPO-Clip 在 LLM 强化学习训练中频繁出现探索崩塌：策略快速集中到少数高概率 token，稀有但信息量大的动作几乎不被更新，严重损害长程推理性能。现有改进（如 DAPO 提高裁剪上限）只是启发性修补，未触及本质。本文揭示根本原因是几何失配：PPO-Clip 用欧氏距离 `(r-1)^2` 度量策略变化，而策略分布的真实几何是由 KL 散度诱导的黎曼流形，其距离正比于 `π_old·(r-1)^2`。这导致高概率动作更新过激，低概率动作更新极度保守，最终探索崩塌。

**方法关键点**  
- 从 Fisher 信息与 KL 的二阶展开导出策略流形上的几何距离，指出应令每次更新的几何距离相等，即约束 `½π_old(r-1)^2 ≤ δ`。  
- 提出 Riemannian Isometric Clip (RIC)：裁剪阈值设为 `ε = √(δ/π_old)`，使低概率 token 获得更大 `ε`，高概率 token `ε` 更小，实现等距更新。  
- 结合 GRPO 组内相对优势，形成 RIPO 算法；理论上几何等距使重要性采样方差趋近同方差，带来更好的偏差‑方差权衡。  
- 该方法可直接嵌入 PPO 目标，具有通用性。

**关键实验**  
- 训练数据：DAPO-Math-17k（17,917 道数学题）；测试：AIME24/25、AMC23、HMMT25 等 7 个竞赛级基准。  
- 模型：Qwen3-1.7B/4B/8B-Base，Llama3.2-3B-Instruct；对照 GRPO、DAPO、GSPO、GMPO、DCPO 等。  
- 结果：Qwen3-8B 上 RIPO 平均分 38.5，较 GRPO 提升 35.1%，较最佳变体 DCPO 提高 4 个百分点；AIME24 上相对 GRPO 提升最高 60%（1.7B 模型）。  
- 训练动态：熵保持在适中水平，梯度范数平稳，裁剪比例均衡；Pass@128 分析显示 RIPO 突破基座能力边界（AIME25 从 GRPO 的 53.3% 提升至 60.0%）。  
- 消融：δ 在 0.02–0.08 内性能稳健；PPO 目标下同样优于其他裁剪（GSM8K，Qwen2.5-1.5B 提升 2.4%）。  

**值得记住的一句话**  
用 `ε = √(δ/π_old)` 代替固定裁剪，让策略更新尊重概率流形的几何结构，从根本上解决探索崩塌。
