---
title: 'Meta^n: Recursive Self-Improvement through Emergent Depth'
title_zh: Meta^n：通过涌现深度实现递归自我改进
authors:
- Zae Myung Kim
- Young-Jun Lee
- Seungyeon Jwa
- Dongyeop Kang
affiliations:
- University of Minnesota
- Seoul National University
arxiv_id: '2608.24735'
url: https://arxiv.org/abs/2608.24735
pdf_url: https://arxiv.org/pdf/2608.24735
published: '2026-08-24'
collected: '2026-08-26'
category: Agent
direction: 递归元认知 Agent 自我改进
tags:
- LLM Agent
- Self-Improvement
- Meta-Reasoning
- Recursive
- ARC-AGI
- Evolutionary Search
one_liner: 固定元操作 Ω 并递归应用于输入，实现可收敛深度的 LLM 自我改进，在 ARC-AGI-2 唯一得正分
practical_value: '- 可将固定元操作递归应用到多阶段推荐/搜索流水线：每层读取下层 trace 与代码，输出下一层的预处理策略和可复用 helper
  库，把隐式流程知识显式化为工具和策略，便于在 query 改写、召回排序等环节复用。

  - 深度由收敛决定而非预先固定，可在 Agent 规划或 query 改写中引入自评收敛，减少无效迭代；结合进化 archive 搜索层链，可迁移为对多策略组合的进化选择，适用于搜索广告出价、文案生成等场景。

  - 层间 conditioning 是主要收益：把上一层的完整推理 trace 和生成代码作为下一层上下文，比仅传最终答案更有效，建议在 LLM 推理管道中传递过程性知识而非仅结果。

  - 主要是通用推理 Agent 贡献，业务落地需谨慎：任务为 ARC-AGI 等通用推理，与电商推荐数据分布差异大，但固定操作+递归输入的设计可借鉴到多智能体系统的自我改进循环，避免自编辑导致的不稳定。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有自我改进 LLM agent 只优化答案，不优化产生答案的过程；增加 meta 层会固定层级，自我编辑则必须保留部分编辑机制以维持稳定，导致实际元深度上限约为 2。

方法：Meta^n 保持元操作 Ω 不变，将其递归应用到输入上。Ω 每次读取下层 solver stack 的推理 trace 及其生成代码，然后写出下一层，包括一个策略性预处理步骤和一个可调用 helper 库。因为 Ω 不变，系统不易失稳；因为输入持续增长，每层有更高视角。深度不预先固定，由收敛决定，并通过进化 archive 搜索不同的层链。

结果：在两个 backbone 上，Meta^n 在全部 8 个 benchmark family 上超过已有自我改进 agent；在特意抵抗技能记忆的 ARC-AGI-2 上，是唯一得分高于零的方法。消融显示递归的大部分收益来自层间传递的 conditioning；深度增加时，在未提示的情况下出现了不同的层角色。
