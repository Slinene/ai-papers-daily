---
title: Group Entropy-Controlled Policy Optimization
title_zh: 分组熵控制的策略优化
authors:
- Guangran Cheng
- Chengqi Lyu
- Songyang Gao
- Wenwei Zhang
- Kai Chen
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2607.16850'
url: https://arxiv.org/abs/2607.16850
pdf_url: https://arxiv.org/pdf/2607.16850
published: '2026-07-17'
collected: '2026-07-21'
category: Training
direction: LLM强化学习训练 · 分组熵控制
tags:
- GRPO
- entropy control
- group entropy
- exploration-exploitation
- LLM alignment
- RL training
one_liner: 提出分组熵控制优势塑造方法，解决多任务 RL 训练中探索-利用失衡与优势不可比问题
practical_value: '面向电商/Agent从业者的可借鉴点：

  - 训练多任务推荐 Agent 时，不同任务（如商品推荐、对话引导）的探索需求不同，可引入分组熵控制，对低熵任务（已学好的模板）适度压制正优势以减少过度利用，对高熵任务（新品类）保留负优势以鼓励探索，避免全局熵调度的僵化。

  - 若在推荐对话 Agent 中采用 GRPO 类算法，GEPO 只需在已有分组样本上计算组熵并修正优势，改动微小，适合作为轻量级工程优化直接集成。

  - 自适应阈值的思路（用历史熵移动平均动态决定何时干预）可迁移到推荐系统的 Bandit/RL 策略中，实时调整探索系数，无需手动调参。

  - GEPO 不引入额外模型，仅利用现有采样组统计量，对线上推理无侵入，符合生产环境对低 overhead 的要求。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
在大语言模型对齐的强化学习（RL）中，GRPO 等算法通过组内归一化优势训练，但面对数学、代码、指令等异构任务混合时，不同任务的自然探索需求差异显著：低熵任务接近确定性，需抑制过度利用；高熵任务仍存在较大不确定性，需保留探索。而 GRPO 的组间优势因熵的差异变得不可比，导致全局或 token 级熵控制无法适应这种任务特定需求。  
**方法**  
提出 GEPO，一种轻量级 GRPO 扩展。利用每 prompt 已存在的采样组，计算**组熵**，据此对组内优势进行**非对称塑造**：低熵组中，缩放正优势以降低“利用”信号；高熵组中，缩放负优势以维持“探索”信号。阈值由历史熵统计的自适应规则确定（例如移动平均标准差法），无需额外超参数或模型，仅需改动优势计算部分。  
**结果**  
在 Qwen2.5-7B 和 LLaMA3-8B 两个基模、13 个基准（涵盖数学、物理、科学、代码生成、指令遵循）上，GEPO 一致超越 GRPO 及近期熵控制方法，取得跨任务的均衡提升，并且在整个训练过程中稳定维持任务特定的探索水平，消融实验验证了分组粒度和非对称塑造的必要性。
