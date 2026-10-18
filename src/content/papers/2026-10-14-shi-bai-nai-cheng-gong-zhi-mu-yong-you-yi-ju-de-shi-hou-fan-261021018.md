---
title: 'Failure Is the Mother of Success: Recovering Supervision with Grounding Hindsight'
title_zh: 失败乃成功之母：用有依据的事后反思重放恢复 GRPO 监督
authors:
- Sheldon Yu
- Tong Yu
- Nikki Lijing Kuang
- Zhendong Chu
- Zhenwei Tang
- Sungchul Kim
- Lina Yao
- Julian McAuley
- Junda Wu
affiliations:
- University of California, San Diego
- Adobe Research
- University of Virginia
- University of Toronto
- University of New South Wales
arxiv_id: '2610.21018'
url: https://arxiv.org/abs/2610.21018
pdf_url: https://arxiv.org/pdf/2610.21018
published: '2026-10-14'
collected: '2026-10-18'
category: Training
direction: 强化学习训练 · 失败恢复监督
tags:
- GRPO
- Hindsight Distillation
- Reasoning Exploration
- RLVR
- On-Policy Distillation
- LLM
one_liner: 提出 RSHD：从失败 rollout 写纠正笔记，经重放效果筛选和防泄漏后蒸馏回 plain-prompt，在 GRPO 全失败组上恢复监督信号
practical_value: '- 如果你在业务中用 GRPO/RLVR 微调 Agent 或 LLM（如对话式购物 Agent、query 改写、推荐文案生成），当一组
  rollout 全部失败时 GRPO advantage 为零，这些 hardest cases 完全被浪费。可借鉴 RSHD：对失败轨迹写不超过 80 词 corrective
  note，但不看参考答案；用原组 no-note 成功率作为 baseline，只保留 replay 成功率高于 baseline 的 note；再把带 note
  的成功续写蒸馏回 plain-prompt，推理时零额外开销。

  - 工程实现上，note 搜索可直接在 TRL GRPOTrainer 上加两个 hook，复用现有 vLLM server；训练 token 约翻倍但只在训练期。对业务中失败率高的长尾难题尤其有效：论文按
  base 模型 0/8 成功率分层，RSHD 较 GRPO 的收益几乎全部落在“从不成功”的样本上，简单样本基本不退化。

  - 安全与防泄漏不可省：论文观察到约 9% 的 note 直接写出参考答案，约 60% 未通过 replay 测试。复用时要保留“字符串匹配检测答案 + replay
  效果筛选”，而不是直接信任 note 文本做蒸馏，否则会引入泄漏或强化错误诊断。

  - 训练细节可复用：蒸馏权重用带 note 与不带 note 的 log-prob 正 lift 并 clip 到 [0,2]，只更新 plain-prompt
  student，teacher stop-gradient；当没有 note 被保留时该步完全退化为 GRPO，避免噪音。这个机制对业务中 RL 微调 Agent
  的稀疏奖励场景很实用。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机

GRPO 训练推理模型时依赖同一问题组内的 reward 差异：当一组 rollout 全部失败，所有 group-relative advantage 为零，该组对任务奖励没有梯度。论文统计 MATH 最难级别约一半的组没有任何学习信号。失败轨迹其实包含可识别的错误和策略信息，但已有做法要么在重试时泄露参考答案，要么不经验证就信任自我反馈，要么只重打分而不重采样，导致无法把失败转化为有效监督。

## 方法关键点

- **失败条件探索**：对每个失败的 rollout，同一 policy 在不看参考答案或正确解的情况下写一段 ≤80 词 corrective note，说明核心错误和下一步该怎么做。
- **答案泄漏检测**：先做字符串匹配，直接写出参考答案的 note 直接丢弃。
- **重放效果筛选**：用 note 重新采样 k=2 个 complete replays；仅当 replay 成功率 > 原组 no-note 成功率时保留该 note；失败可修订一次。
- **蒸馏回 plain-prompt**：从保留 note 的 replays 中均匀采样一个，用带 note 的 teacher 与 plain-prompt student 的 per-token log-prob 正 lift（clip 到 [0,2]）加权，加入 GRPO loss；原始 GRPO advantages 不变，没有 note 保留时完全退化为 GRPO。
- **推理无额外开销**：note 只出现在训练 teacher 上下文，部署仍用 plain prompt。

## 关键实验

Qwen3-1.7B/4B/8B 上，两个训练域：MATH 7498 题和 MMLU-Pro 数值题 2141 题。150 步训练，8 rollouts/问题。

- MATH-500：Qwen3-4B GRPO 76.9 → RSHD 84.5；Qwen3-8B 75.3 → 80.6。
- 科学域 held-out：Qwen3-4B GRPO 48.7 → RSHD 61.2；Qwen3-8B 45.1 → 60.7。
- 域外泛化：GPQA-Diamond matched 9.6 → 27.0，TheoremQA 40.1 → 56.5。
- 难度分层：MATH Level 5 上提升 +10.8 点；按 base 模型 0/8 成功率分层，66 个从不成功的问题上 RSHD 15.0 vs GRPO 6.4。
- 行为变化：平均输出 1979 vs 2545 tokens，超预算率 13.2% vs 26.2%，无 boxed 答案率 8.9% vs 18.2%。训练成本约 2 倍 token，仅训练期。

**最值得记住的一句话**：失败 rollout 不是浪费的样本；只要用“重放效果测试 + 防泄漏”筛出有用的纠正笔记，并把带 note 的成功续写蒸馏回 plain-prompt，就能在 GRPO 全失败/困难问题上恢复监督，提升推理且不增加推理成本。
