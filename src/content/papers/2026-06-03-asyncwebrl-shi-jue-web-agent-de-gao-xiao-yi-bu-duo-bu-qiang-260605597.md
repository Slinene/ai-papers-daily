---
title: 'AsyncWebRL: Efficient Multi-Step RL for Visual Web Agents'
title_zh: 'AsyncWebRL: 视觉 Web Agent 的高效异步多步强化学习'
authors:
- Hao Bai
- Rui Yang
- Chenlu Ye
- Spencer Whitehead
- Aviral Kumar
- Tong Zhang
affiliations:
- UIUC
- Microsoft
- CMU
arxiv_id: '2606.05597'
url: https://arxiv.org/abs/2606.05597
pdf_url: https://arxiv.org/pdf/2606.05597
published: '2026-06-03'
collected: '2026-06-10'
category: Agent
direction: 视觉 Web Agent 多步 RL 训练优化
tags:
- Async RL
- Multi-step RL
- GRPO
- Visual Web Agent
- Training Efficiency
- Off-policy Correction
one_liner: 异步系统 + 去除轨迹步数归一化，实现视觉 Web Agent 训练 2.9× 加速且 OOD 准确率新高
practical_value: '- **异步 RL 系统设计可照搬**：长存 rollout 池（Everlasting Rollout Pool）让浏览器会话跨迭代持续存活，消除每轮重建开销；轻量截图处理（Lightweight
  Screenshot Handling）把图片留在专用 Actor 中，仅传引用，避免 RPC 对象存储因高并发图片序列化而写盘，这对电商中的多步视觉 Agent（如商品详情页浏览）有直接参考价值。

  - **GRPO 的长度归一化陷阱**：多步 GRPO 中按轨迹步数归一化 `1/|τ_i|` 会使失败长轨迹的梯度衰减，策略倾向于生成冗长记忆填充，在电商 Agent
  训练中可能导致类似「记流水账」行为；改为常数 `1/k`（k 设为 Easy 难度 horizon）可恢复对失败样本的完整惩罚，压缩不必要的输出 token。

  - **解耦重要性采样（Decoupled PPO）**：将 `πθ/πbehave` 拆成 `πprox/πbehave`（无 clip）和 `πθ/πprox`（有
  clip），clip 率减半，训练奖励提升更快，适合任何异步 RL 训练中的 off-policy 校正。

  - **DAPO 式动态采样与 bandit-like 优势共享**：每个 task 采样 16 个 rollout，跳过全成功/全失败组，再用组内均值归一化轨迹优势，在稀疏奖励的电商任务中也能稳定获得对比信号。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：训练视觉 Web Agent 的多步 RL 有两个严重效率瓶颈：同步 RL 中 GPU 因等待最慢的 rollout 而产生大量气泡；标准多步 GRPO 按轨迹步数归一化 `1/|τ_i|`，因失败轨迹平均比成功轨迹长约 2.4 倍，导致失败 token 的梯度被衰减，策略学会用冗长记忆模式填充步数而非真正提升决策能力。

**方法关键点**：
- **系统层**：提出 AsyncWebRL，引入**长存 rollout 池**（worker 跨迭代不断开，参数更新即时广播）和**轻量截图处理**（图片张量仅存于专用 Actor，rollout 与 trainer 间只传引用），彻底消除 GPU 等待和数据序列化开销。
- **算法层**：
  1. **解耦重要性采样**：将重要性比拆分为 `πprox/πbehave`（无 clip）和 `πθ/πprox`（有 clip），clip 率降低约一半，训练收敛更快。
  2. **常数步数归一化**：将多步 GRPO 损失中的 `1/|τ_i|` 替换为常数 `1/k`（k=10），解除轨迹长度与梯度的耦合，使长失败轨迹获得完整惩罚，从而抑制冗长记忆、压缩轨迹。

**关键实验**：
- 在 WebGym OOD 测试集（1167 个任务，含未见网站）上，基于 Qwen3-VL-8B，AsyncWebRL 全量方案达到 45.4% 成功率（相对提升 +5.8%），Medium 和 Hard 子集分别提升 42% 和 48%。
- 系统吞吐从同步的 ≈1050–1300 轨迹/小时提升至 ≈3100 轨迹/小时，加速 2.4–2.9 倍。
- 去除长度归一化后，每步平均 token 数从约 240 降至 180，每步梯度更新时间收缩 11–19%。

**一句话**：多步 GRPO 的 `1/|τ_i|` 是鼓励冗长输出的隐形毒药，换成常数 `1/k` 就能同时提升效率与效果。
