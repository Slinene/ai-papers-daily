---
title: 'YANchor-4B: Effective Long-Horizon Reasoning in O(N) Time with O(1) Memory'
title_zh: YANchor-4B：O(N)时间与O(1)内存下的长时程推理
authors:
- Huishan Ji
- Hua Xu
- Weiming Zhang
- Qirui Ye
affiliations:
- Rocore Matrix
- Stonehill Tech
- Carnegie Mellon University
arxiv_id: '2610.10118'
url: https://arxiv.org/abs/2610.10118
pdf_url: https://arxiv.org/pdf/2610.10118
published: '2026-10-07'
collected: '2026-10-08'
category: Reasoning
direction: 长时程推理 · 线性复杂度架构
tags:
- Long-horizon reasoning
- Linear-time inference
- Memory anchors
- Recurrent architecture
- O(1) memory
- RLVR
one_liner: 用固定容量记忆锚点结合循环状态与局部注意力，在O(N)/O(1)下实现强长时程推理
practical_value: '- **高并发长序列在线推理**：如果你的 Agent 或推荐链路需要处理长会话/长用户历史，可考虑用固定状态 + 显式记忆的结构，避免
  KV cache 随长度膨胀，显著降低显存峰值，提升批量吞吐；适合电商大促高 QPS 场景。

  - **业务记忆选择**：论文中每个 KV group 独立保留 Top-K 高分记录，admission score 在写入时计算，类似信息重要性过滤器。推荐系统可借鉴此设计，对用户行为序列或搜索
  Session 做关键记忆选择，优先保存高价值交互（如加购、支付），而不只是最近 N 条。

  - **多路历史表示**：循环状态压缩全局、局部窗口保留近期、独立记忆保留远期关键记录，三者互补。在生成式推荐或对话式导购中，可以解耦用户长期偏好、近期意图和关键事件，分别建模后再融合。

  - **RLVR 可借鉴**：用可验证结果（如是否点击、是否成交）做 outcome-guided 强化学习，提升生成任务（query 推荐、文案）的准确率，而不只依赖监督数据。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
长时程推理需要持续访问早期信息，全历史 attention 的显存和计算随长度增长，循环压缩又容易丢失精确细节。YANchor-4B 希望在固定容量历史状态下保留关键信息，以 O(N) 时间、O(1) 内存完成复杂推理。

## 方法关键点
- **三路历史表示**：基于 Qwen3.5-4B 改造，32 层分为 8 组，每组 GDN×3 + SWA 1024 + Memory。Gated DeltaNet 压缩全局状态，局部窗口保留最近 1024 位置，独立记忆模块保存选定的远期记录。
- **记忆写入与准入**：残差 writer 生成 K/V，admission network 为每个 KV group 打分；每 256-token 块提交一次，每个 group 独立保留 Top-1024 记录，形成记忆锚点。
- **检索与集成**：16 个 query heads、4 个 KV groups、head dim 256，grouped-query attention 带 zero-logit neutral item；query-conditioned gate 调制记忆输出。
- **固定状态**：记忆 K/V 仅 40 MiB/序列，批量 512、64K context 时峰值显存 67.71 GiB，远低于 Transformer 基线。
- **训练四阶段**：M0 记忆适应 → R 联合适应 → S 监督后训练 → RLVR 结果引导策略精炼。

## 关键实验
- 竞赛数学：AIME 2024-2026 平均 pass@1 **82.93%**，HMMT Feb 2026 **63.64%**，大幅领先最强线性恒定状态基线 RWKV-7 G1j 13.3B 的 18.89% 和 12.12%；MATH-500 达 97.49%。
- 通用能力：24 个文本基准平均 **78.64**，领先最强 bounded-state baseline 22.35 分；与 Qwen3.5-4B 的 80.44 接近。
- 长记忆：启用记忆分支 query accuracy **94.14%**，禁用后仅 0.39%，证明记忆路径关键。
- 推理效率：单 H100 持续解码 213 token/s（128K 输入+128K 输出），吞吐是 Qwen3.5-4B 的 4.12-6.58 倍；长序列输出 token 消耗比 Qwen3.5-4B 少 43-47%。

## 最值得记住的一句话
用独立写入门控和分组 Top-K 记忆锚点，把固定容量记忆与循环压缩、局部窗口结合，可在 O(N) 时间和 O(1) 内存下实现强长时程推理。
