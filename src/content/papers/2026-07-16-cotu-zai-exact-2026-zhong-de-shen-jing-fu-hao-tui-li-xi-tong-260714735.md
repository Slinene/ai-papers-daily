---
title: 'CoTu at EXACT 2026: Neuro-Symbolic Reasoning for Transparent Educational QA'
title_zh: CoTu 在 EXACT 2026 中的神经符号推理系统：透明教育问答
authors:
- Quoc-Khang Tran
- Minh-Thien Nguyen
- Phu-An Thai
- Xuan-Tung Bui
- Truong-Thanh Ma
- Nguyen-Khang Pham
affiliations:
- Can Tho University
- Tay Do University
arxiv_id: '2607.14735'
url: https://arxiv.org/abs/2607.14735
pdf_url: https://arxiv.org/pdf/2607.14735
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 神经符号推理 · 程序化思维
tags:
- neuro-symbolic
- Program-of-Thought
- Z3 solver
- small language model
- speculative decoding
- educational QA
one_liner: 4B 模型将推理外化为 Z3/Python 程序，物理满分、总技术分最高
practical_value: '- 在 Agent 或推荐系统中，将 LLM 的推理步骤输出为可执行的 Python/Z3 代码，交由外部求解器，可大幅提升数值计算和逻辑推导的可靠性，避免幻觉。

  - Program-of-Thought 范式可结合自我纠正循环：执行代码后若失败则自动回溯修正，适合多步任务（如自动生成广告竞价策略、动态定价脚本）。

  - 任务路由设计：用一个轻量分类器选择“逻辑推理”或“数值计算”分支，此思路可直接用于电商搜索中的意图分发（如判别为“比较查询”或“政策查询”后走不同处理链）。

  - 延迟敏感场景下，SGLang 框架 + 推测解码可保障 60s 内完成复杂多步推理，对推荐系统的实时生成式排序或 Agent 交互有工程参考价值。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：EXACT 2026 竞赛要求用 ≤8B 参数的开源模型实现可解释的教育问答，包含大学规章制度逻辑推理与多步物理题。团队需要在极小模型尺寸下保证答案正确性与推理透明度。

**方法**：构建神经符号程序化思维（Program-of-Thought）流水线。核心是用一个 4B 骨干模型将问题转化为程序而非直接回答：对规章制度查询生成 Z3 约束编码，由 Z3 求解器判定的蕴涵结果作为推理基础；对物理题生成数值 Python 代码并执行。两条路径共享一个自我纠正循环（执行失败后根据报错修正程序）和统一的 JSON 解释输出格式。引入任务类型路由、基于蒸馏的微调，以及采用 SGLang+推测解码的部署栈，确保每查询延迟在 60 秒内。

**结果**：在物理任务上两轮自动评估均获满分；最终轮技术分 13.44/15，为所有队伍最高，综合排名第三。证明在 4B 规模下，将答案根基扎在符号求解器中能得到正确且可验证的推理，剩余难点在于前提选择而非演绎本身。
