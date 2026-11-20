---
title: 'GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers'
title_zh: GLiDE：从推理教师蒸馏的快速校准决策模型
authors:
- Sahibzada Allahyar
- Julia White
- Dhruv Atreja
- George Hurn-Maloney
- Urchade Zaratiana
affiliations:
- Fastino Labs
arxiv_id: '2611.26509'
url: https://arxiv.org/abs/2611.26509
pdf_url: https://arxiv.org/pdf/2611.26509
published: '2026-11-19'
collected: '2026-11-20'
category: Training
direction: 推理能力蒸馏到单前向决策模型
tags:
- decision model
- distillation
- reasoning teacher
- calibration
- single-forward pass
- recurrent depth
one_liner: 从推理教师蒸馏出无需生成推理的单前向决策模型，在速度、校准与精度上达到 Pareto 前沿
practical_value: '- 在推荐/广告精排或 Agent 决策点，可考虑用判别式打分模型替换生成式 LLM 推理：候选集一次前向得到分数，延迟从秒级降到百毫秒级；用推理大模型做软标签蒸馏，保留推理带来的排序质量。

  - 若基于 causal LLM 做打分，可尝试移除 full-attention 层的 causal mask，让 context、question、candidate
  双向交互，提升对候选答案的判别力，尤其适合排序/选择题式任务。

  - 其参数-free recurrent depth 思路值得借鉴：固定参数重复执行某些层/注意力计算，不生成 token 也能增加推理时计算量，类似 test-time
  compute 的廉价版，可用于精排阶段提升分数质量。

  - 校准误差 ECE 2.0% 是生产系统的关键指标：电商广告出价、推荐置信度阈值、Agent 决策放弃/人工兜底都需要可靠概率；蒸馏训练时可显式加入校准约束或选择校准友好的目标。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：推理能显著提升决策质量，但生成完整推理链带来高昂延迟。能否只保留推理的好处、又不付出生成成本？  

**方法关键点**：GLiDE 基于 Qwen hybrid 模型，移除 full-attention 层的 causal mask，使 context、question 和 candidate answer 之间双向交互，一次前向即可为候选答案打分。训练时结合多教师软标签蒸馏：其中一个教师是推理模型，将推理能力迁移到单步判别中；再用渐进式多任务后训练覆盖多种决策任务。引入 parameter-free recurrent depth，无需新增参数、不生成 token 即可增加推理时计算。  

**关键结果**：五种规模（0.4B–27B）均位于 Hugging Face Decision Index 性能-参数 Pareto 前沿。GLiDE V1.2 (27B) hidden-set 71.52，ECE 2.0%，单 GPU 中位延迟 92.9ms；加入 checkpoint averaging 和 recurrent depth 后达到 73.37，ECE 2.1%。
