---
title: 'Learning to Use Tools: Reinforcement Learning for Tool-Integrated Mathematical
  Reasoning'
title_zh: 用强化学习训练工具集成数学推理
authors:
- Minghui Xu
- Zi Wang
affiliations:
- Department of Energy Science and Engineering, Stanford University
arxiv_id: '2608.28447'
url: https://arxiv.org/abs/2608.28447
pdf_url: https://arxiv.org/pdf/2608.28447
published: '2026-08-28'
collected: '2026-08-31'
category: Reasoning
direction: RL 训练工具调用数学推理
tags:
- Tool Use
- RLVR
- DAPO
- Mathematical Reasoning
- GRPO
one_liner: 在 Countdown 任务上证明工具调用与 RLVR 互补，Tool-DAPO 把 pass@1 从 35.8% 提升到 66.0%
practical_value: '- 在需要精确数值计算的 Agent 链路（优惠计算、折扣叠加、预算控制、运费）中引入计算器工具，用 `<tool>expression</tool>`
  调用并注入 `<obs>` 环境观测，可显著减少算术/验证错误；RL 更新时只对模型生成 token 计算 loss，工具输出不参与梯度传播。

  - 自动构造带工具调用的 SFT 数据：先定位推理链中的错误算术步，在该步前插入 calculator call，再由参考模型继续生成正确后续推理，能低成本生成
  tool-use 训练样本，类似思路可迁移到需要计算校验的 query 理解或搜索词生成。

  - 做 RLVR 训练时，若 GRPO 出现训练不稳定，可借鉴 DAPO 的动态采样过滤掉全对/全错 prompt group，或改用 RLOO++ 的 batch-level
  advantage 归一化，避免零方差 group 带来的噪声更新；本论文中 Tool-DAPO 过滤了 60.7% 的 group，训练效率明显更高。

  - 评估 pass@k 时小测试集置信区间很宽，容易误判；建议构造大规模无重叠 held-out set，并用 bootstrap CI 比较不同策略，业务离线评测同理。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
LLM 在数学推理中仍会犯算术和逻辑错误，即使生成中间推理步骤，tokenization + autoregressive 缺少可靠计算和验证机制。Countdown 任务需要组合给定数字通过四则运算达到目标值，最终答案可自动验证，天然适合研究 RL 与工具调用结合能否提升推理可靠性。

## 方法关键点
- **工具格式**：模型可调用计算器，格式为 `<tool>表达式</tool>`，环境执行后返回 `<obs>=结果</obs>`；工具观测作为环境输出，不计入模型 token，policy loss 只作用于模型生成部分。
- **Tool-SFT 数据构造**：基于已有 SFT 数据，先定位错误算术步或错误最终答案，在错误前构造 prefix 并插入 calculator call，再由参考模型继续生成正确后续推理，得到带工具调用的训练语料。
- **RL 方法对比**：RLOO 用 leave-one-out baseline；RLOO++ 做 batch-level advantage normalization 并 rescale 到 target std 0.3；GRPO 用 group-normalized advantage，但在该任务中不稳定；DAPO 使用动态采样过滤全对/全错 group，并用不对称 clipping `[0.8,1.28]`。
- **评估**：构造 1,024 道无训练重叠的 held-out Countdown 测试集，用 pass@k 和 95% bootstrap CI 对比。

## 关键结果
- 工具集成一致提升：Tool-SFT pass@1 35.8% vs SFT 26.4%；Tool-RLOO pass@1 56.6% vs RLOO 50.6%，约 10 个百分点增益。
- Tool-DAPO 最强：pass@1 66.0%，比 Tool-SFT 提升 30.2pp，比 Tool-RLOO 提升 9.3pp；pass@16 也达到 76.6%。DAPO 动态采样过滤 60.7% prompt group，100 步训练 6.29 小时优于 200 步 Tool-RLOO 16.15 小时。
- RL 主要提高低 k 表现：Tool-RLOO++ pass@1 56.8% 与 Tool-RLOO 接近，但 pass@16 70.8% 略低，说明 RL 主要重分配已有正确轨迹的概率，而非扩展推理覆盖。
- 分析显示，RL 训练后平均 tool call 次数从不足 1 次提升到约 1 次，说明 RL 不仅保留 SFT 的工具使用行为，还会进一步鼓励有效工具调用。

## 最值得记住的一句话
最终答案可验证的 RL 主要把概率质量重新分配给模型已经能采样到的正确轨迹；工具调用减少算术/验证错误，DAPO 的动态采样过滤无信息 group 能显著提升训练效率。
