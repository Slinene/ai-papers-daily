---
title: 'Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon
  Reasoning'
title_zh: 迈向技能原生LLM：用技能熵衡量与训练长程跨技能推理
authors:
- Yinghui He
- Ling Yang
- Jiarui Liu
- Yongjin Yang
- Lechen Zhang
- Yingcheng Wu
- Zhenfei Yin
- Mengdi Wang
- Sanjeev Arora
affiliations:
- Princeton University
- Carnegie Mellon University
- University of Toronto
- University of Illinois Urbana-Champaign
- Stanford University
arxiv_id: '2608.05139'
url: https://arxiv.org/abs/2608.05139
pdf_url: https://arxiv.org/pdf/2608.05139
published: '2026-08-04'
collected: '2026-08-06'
category: Reasoning
direction: 长程多技能推理评估与强化学习训练
tags:
- Skill Entropy
- Long-Horizon Reasoning
- Skill-Switching
- Benchmark
- RL
- LLM Evaluation
one_liner: 提出技能熵量化技能切换难度，构建Skill^2-Bench基准并设计Skill-Entropy RL训练框架，显著提升LLM长程跨技能推理性能
practical_value: '- **Agent 任务难度评估**：在电商 Agent 或对话式推荐系统中，多条技能链（意图识别→商品检索→价格计算→个性化推荐→原因解释）可借助技能熵量化任务复杂度，发现模型在哪类技能切换上频繁失败，定向优化。

  - **RL 训练技巧迁移**：Skill-Entropy RL 框架可直接套用到推荐 Agent 的训练，奖励模型不仅输出正确结果，还要正确选择每步使用的技能类型，以此强化长程规划的技能切换能力，避免步骤遗漏或逻辑跳跃。

  - **复用训练信号**：论文证明技能熵信号可跨数据集复用（如 OpenR1-Math），电商团队可构建内部多技能长链任务数据，用同样方法对自有模型做 RL 微调，无需改动业务模型架构。

  - **基准设计思路**：可以参照 Skill^2-Bench 构建技能切换的评测集，将不同推荐环节抽象为独立skill，自动检测模型是否按预期顺序调用技能，用于评价
  LLM 驱动的推荐系统中的多步推理鲁棒性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 长程推理任务往往要求模型在一条推理链中切换多种技能（如先数学计算，再根据结果做规划），但当前基准只能孤立评估单一技能，缺少对技能切换能力的系统度量。

**方法**：
- 定义**技能熵（Skill Entropy）**，基于技能间转移概率量化切换难度；
- 构建 **Skill^2-Bench**，含 558 个技能覆盖 9 个领域的长程跨技能任务，每条任务标注技能熵并分低/中/高难度；
- 提出 **Skill-Entropy RL**，模型需同时预测每步答案和所用技能，奖励函数融合步骤正确性与技能序列对齐度（技能熵奖励）；

**关键结果**：
- 在 12 个模型上验证，技能熵越高的任务准确率越低，揭示“技能切换缺口”；
- 基于 Qwen3-4B 和 1.7B，Skill-Entropy RL 将 Skill^2-Bench 得分从 34.4% 提至 68.4%、14.6% 提至 40.1%，显著优于多基线；
- 技能熵训练信号可迁移至其他数据（如 OpenR1-Math），表明其通用性。
