---
title: Agent Explorative Policy Optimization for Multimodal Agentic Reasoning
title_zh: AXPO：通过思考-行动间隙探索优化多模态 Agent 推理
authors:
- Minki Kang
- Shizhe Diao
- Ryo Hachiuma
- Sung Ju Hwang
- Pavlo Molchanov
- Yu-Chiang Frank Wang
- Byung-Kwan Lee
affiliations:
- NVIDIA
- KAIST
arxiv_id: '2605.28774'
url: https://arxiv.org/abs/2605.28774
pdf_url: https://arxiv.org/pdf/2605.28774
published: '2026-05-26'
collected: '2026-05-28'
category: Agent
direction: Agent 探索策略优化 · 工具使用 RL
tags:
- GRPO
- tool-call resampling
- policy optimization
- multimodal agent
- thinking-acting gap
one_liner: 针对多模态 Agent 中工具调用利用不足与失败率高的问题，提出工具调用重采样以提升强化学习训练信号
practical_value: '- **工具调用探索优化**：当业务中 Agent 面临工具使用频率低、调用时全体失败的情况，可借鉴 `tool-call resampling`：固定思考前缀，在工具调用位置重采样，集中探索于动作本身，低成本恢复正样本，避免全量重采样的浪费。

  - **不确定性驱动的重采样选择**：对触发重采样的前缀按工具调用 token 的平均概率排序，只重采样最低置信度的前缀，节省额外预算。该 trick 可用于电商
  Agent 中对外部工具（搜索、计算、图像分析）的 RL 训练，优先在最不确定的调用点加固信号。

  - **分区分组优势计算**：将重采样产生的 continuation 构成独立优势组，并用二进制恢复奖励更新源前缀，避免同一前缀在成功和失败轨迹中的梯度冲突。在推荐场景中，若
  Agent 通过工具获取实时特征，可用类似方式解耦“意图”与“动作执行”的优化。

  - **计算预算分配**：仅用 +25% 的重采样预算，便超越直接加倍 rollout 的 GRPO，表明算力应投向最易失效的决策点。对于成本敏感的业务系统，可优先在工具调用处做局部探索而非全局扩增采样。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多模态 VLM 在推理时需自主决定何时继续思考、何时调用外部工具（如搜索、Python 解释器、图像缩放），但现有 RL 方法（如 GRPO）存在“思考-行动间隙”：工具调用仅占 30% 左右的 rollout，且一旦调用，约 40% 场景中整个工具使用子组全部失败，导致工具调用 token 无法获得正梯度信号，训练停滞。

**方法关键点**
- **诊断**：量化工具调用率低、全体失败率过高及思考前缀不决定具体工具调用（重采样多样性 2.9-3.4 语义簇），揭示工具调用是真实的分歧点。
- **核心思想**：提出 AXPO，对“全部错误的工具使用子组”，固定思考前缀，从工具调用边界重新采样 `K` 个动作及其后续轨迹，将探索集中在高变异的行为上。
- **可行性选择**：仅对全体错误的工具子组触发，按前缀不确定性（工具调用 token 的平均概率）排序，优先重采样最低置信前缀。
- **优势解耦**：重采样 continuation 构成独立 GRPO 组计算优势，源前缀则用二进制恢复奖励（是否存在任一正确 continuation）更新，避免梯度冲突。

**关键实验**
在 Qwen3-VL-Thinking 2B/4B/8B 上，使用 64K SFT 数据后 RL，覆盖 9 个多模态基准（数学推理、视觉感知、搜索）。SFT+AXPO 在 8B 模型上平均 Pass@1 提升 +1.8pp（相对 GRPO），Pass@4 提升 +1.8pp；8B 模型 Pass@4 超越 32B base 模型（75.8 vs 75.1），仅用 1/4 参数。训练动态：工具调用率上升 28pp，全体失败率下降 17pp。额外 25% 重采样预算效果优于将 GRPO rollout 预算加倍的方案。

**最值得记住的一句话**
AXPO 不改变奖励，仅通过重采样来扩大工具调用的覆盖，以极小的额外计算成本将学习信号精准注入协同中最脆弱的决策点。
