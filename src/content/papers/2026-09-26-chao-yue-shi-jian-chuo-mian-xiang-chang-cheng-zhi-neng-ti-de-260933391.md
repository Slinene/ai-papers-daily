---
title: 'Beyond Timestamps: Decision-Aligned On-Policy Distillation for Long-Horizon
  Agents'
title_zh: 超越时间戳：面向长程智能体的决策对齐在线策略蒸馏
authors:
- Mingju Chen
- Can Lv
- Jinrong Liu
- Huan Zhang
- Heng Chang
- Shiji Zhou
affiliations:
- Beihang University
- Tsinghua University
arxiv_id: '2609.33391'
url: https://arxiv.org/abs/2609.33391
pdf_url: https://arxiv.org/pdf/2609.33391
published: '2026-09-26'
collected: '2026-09-29'
category: Agent
direction: 长程 Agent 决策对齐的在线自蒸馏
tags:
- OPSD
- Credit Assignment
- RLVR
- Long-Horizon Agents
- Self-Distillation
- Decision Alignment
one_liner: 提出 ALIGNOPSD，用跨 rollout 决策对齐修正特权监督并用可变决策片段分配 credit，长程 Agent RL 提升 5.5–8.7%
practical_value: '- 在电商导购/搜索式推荐 Agent 的 RLVR 训练中，若用带特权信息的 teacher policy 做 dense 监督，不要按
  turn index 对齐 teacher/student；用 thinking trace 的 frozen embedding 余弦做跨 rollout soft
  matching，再 teacher-force 同一 response，可避免时间戳错配污染 credit。

  - 把一次输出作为 credit 最小单位太粗、token 太细；用相邻 turn 的 correspondence profile 的 JSD 变化自动切分决策片段，再在
  span 内按证据分配 advantage，更适合“同一个决策跨多轮”的场景（如搜索→点商品→比价→加购中“比价”持续多轮）。

  - 优势分配时用 stop-gradient 的权重乘到 group-normalized advantage，不引入额外 distillation loss；KL
  正则约束 span/turn 分配不偏离均匀 token measure，训练更稳定。

  - 超参默认值：credit temperature T=0.5 跨任务和模型尺度较稳定；thinking similarity threshold 0.7–0.8
  较稳；top-K 需按任务调，长轨迹可稍大，短轨迹需更小。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：RLVR 只有稀疏 terminal reward，GRPO 把 trajectory-level advantage 广播到所有 token，无法区分有效决策与偶然行为；OPSD 用 privileged teacher 提供 dense 监督，但其 timestamp-local 信号存在 Decision–Timestamp Mismatch：跨 rollout 同一时间步可能对应不同决策，对应决策也可能发生在不同时间步；轨迹内一个功能决策常跨多个 turn，固定窗口或逐 turn 分配都会割裂或混入错误 credit。

**方法关键点**：
- **Decision-Aligned Supervision Rectification**：将 student 与 privileged teacher 的 thinking trace 用 frozen encoder 编码，构建跨 rollout 余弦相似度矩阵 H；经过相似度阈值、top-K、动作一致性过滤后，每个 target turn 最多选 K 个 source。用 teacher 在 matched source history 下 teacher-force 同一 student response，计算 aligned log-prob，并与 local gap 按 correspondence confidence α 混合，得到 rectified gap。
- **Semi-Markov Hierarchical Credit Assignment**：把 H 的 dense profile 在相邻 turn 间的 JSD 变化作为边界，切出可变长度决策 span；将 group-normalized trajectory advantage 视为 credit budget，先在 span 层按 outcome-oriented evidence 分配，再在 span 内按 turn evidence 分配。权重 stop-gradient 乘到 token advantage，不新增辅助 distillation loss。
- 只在训练时使用 privileged info，inference 仍用普通 history。

**关键结果**：Qwen2.5-3B/7B 在 ALFWorld、Search-QA、WebShop 上，八个 backbone–metric 组合中六项第一、两项第二；比 GRPO 提升 5.5–8.7%，比 StepOPSD 全胜。WebShop 7B 消融：去掉 rectification 后 Score 从 87.9 降到 84.2、Acc 从 78.9 降到 71.9；替换为 token/turn/random allocation 分别得到 Score 81.6/86.3/78.9、Acc 71.1/77.3/69.5。诊断显示 WebShop 中约 80% 的 matched actions 发生在不同 turn，中位位移 4 轮；训练中 off-turn matching weight 在 ALFWorld/WebShop/Search-QA 上分别为 96.70%/83.63%/22.71%。

**最值得记住的一句话**：把“功能决策”而不是时间戳作为 credit assignment 的单位，并先跨 rollout 对齐监督上下文，再用该对齐变化切分决策片段。
