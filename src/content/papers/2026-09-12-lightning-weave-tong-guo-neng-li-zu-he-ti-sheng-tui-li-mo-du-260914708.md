---
title: 'Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models
  through Capability Composition'
title_zh: Lightning Weave：通过能力组合提升推理模型精度-效率前沿
authors:
- Yecheng Wu
- Song Han
- Han Cai
affiliations:
- Massachusetts Institute of Technology
- NVIDIA
arxiv_id: '2609.14708'
url: https://arxiv.org/abs/2609.14708
pdf_url: https://arxiv.org/pdf/2609.14708
published: '2026-09-12'
collected: '2026-09-16'
category: Reasoning
direction: 推理模型 · 能力蒸馏与组合
tags:
- On-Policy Distillation
- Capability Composition
- Efficient Reasoning
- LLM Post-training
- Tilted-Target DOPD
one_liner: 提出 Lightning Weave，组合独立后训练模型的策略 log-ratio 并稳定离线蒸馏，同时提升推理准确率与 token 效率
practical_value: '- 使用 anchor pair 的 log-ratio 表示能力差异，可迁移到推荐模型蒸馏：从 base 到业务优化模型的策略偏移提取特定能力，避免直接匹配教师分布带来的风格冲突，实现对转化率、多样性等单一目标的精准迁移。

  - 多能力加权组合方式可借鉴到生成式推荐/Agent 策略优化：不联合训练冲突目标，而是独立训练不同目标的专家，再在共享状态上组合其 log-ratio 生成单一学生，后续通过权重调节在相关性、多样性、时延等指标间取得可控
  Pareto 前沿。

  - 离线缓存教师评分 + Tilted-Target DOPD 修正固定点，适合大规模线上蒸馏：让行为策略生成轨迹并一次性缓存多个 anchor 模型打分，训练时只跑学生模型，降低实时服务多教师成本；同时用显式
  tilted target 避免离线 KL 估计偏差，稳定收敛。

  - 权重扫描获得不同 accuracy-efficiency 档位，可直接用于电商响应质量 vs 成本权衡：按流量价值或场景动态调整组合权重，产出不同档位学生模型或行为模式。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
大型推理模型在复杂任务上表现强，但常生成冗长推理链，推理成本高。直接联合优化准确率和 token 效率可能冲突；而独立后训练模型已分别擅长准确率（如 Klear）或效率（如 DECS）。能否提取这些专家已学到的能力并组合到单一学生，同时改善精度和效率？

## 方法关键点
- **能力表示**：每个能力用 anchor pair 的 token 级 log-ratio 表示，即后训练前后策略的对数比 r_i(a|s)=log(π+_i(a|s)/π−_i(a|s))，隔离后训练阶段引入的行为变化。
- **状态对齐与组合**：在共享的学生生成 token 状态上，对多个 log-ratio 加权求和 r_w=Σw_i r_i，再用该组合偏移指数倾斜行为策略 π_b，得到显式联合目标 q_w∝π_b exp(r_w/α)。
- **Tilted-Target DOPD**：将缓存轨迹上的组合偏移转化为显式目标分布，训练最小化学生与 q_w 的 KL；该目标在 q_w 处梯度消失，修正朴素离线缓存 DOPD 因缓存动作导致的固定点漂移，稳定离线训练。
- **工程高效**：每个 anchor pair 只对缓存轨迹评分一次，后续训练仅需学生模型，无需实时服务多个 anchor 模型；权重 w 可调，产生可控的 accuracy-efficiency 权衡。

## 关键实验
在 Qwen3-1.7B/4B/4B-Thinking-2507/3.5-4B 和 OLMo-3-7B-Think 五个学生模型上，用 Klear 和 DECS 作为准确率/效率锚点，评估数学 AIME 2024/2025、HMMT 2025 和代码 LiveCodeBench v5/v6。与 base、单锚点及 SimpleSD、Art、PromptCoT 2.0、模型插值等基线对比。
- Qwen3-4B：平均准确率 +4.02 点，响应 token 减少 19.7%。
- Qwen3.5-4B：HMMT 2025 准确率 59.2%→64.0%，token 减少 10.7%；LCB v5 41.7%→54.2%，token 减少 9.6%。
- 权重扫描的非支配点构成经验 Pareto 前沿，优于单锚点和外部基线；三锚点组合（Klear+DECS+MiMo-RL）AES 达 0.42。

## 核心结论
将独立后训练模型的能力表示为策略 log-ratio，并在共享状态上加权组合后蒸馏，可同时提升推理准确率与 token 效率，权重调节提供可控的精度-效率 Pareto 前沿。
