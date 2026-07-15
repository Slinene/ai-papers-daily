---
title: Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation
  Models
title_zh: 功能感知中间填充训练提升编码智能体基座模型
authors:
- Yubo Wang
- Jiarong Liang
- Yuxuan Zhang
- Xuye Liu
- Cong Wei
- Yuyu Zhang
- Ping Nie
- Wenhu Chen
arxiv_id: '2607.12463'
url: https://arxiv.org/abs/2607.12463
pdf_url: https://arxiv.org/pdf/2607.12463
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: 编码智能体训练 · 函数感知填充
tags:
- Fill-in-the-Middle
- Mid-Training
- Coding Agent
- Function Call
- Self-Supervised
one_liner: 用函数调用结构的自监督中间训练增强编码智能体，在复杂任务上提升超3%并缓解能力侵蚀
practical_value: '- 主要是学术贡献，业务可借鉴点有限。

  - 利用程序依赖图选择关键片段进行掩码训练的思想，可迁移到序列推荐中——针对高偏置交互或语义关键 token 进行掩码，强化模型对长程依赖的建模。

  - 在对话式推荐 Agent 的训练中，可设计类似的中间训练阶段，注入“查询-结果-使用”的循环偏置，提升模型对工具返回结果的利用效率。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

**动机**：编码智能体需要将外部工具返回融入持续推理，但标准左到右预训练仅单向暴露这种结构。观察到智能体的动作-观察-延续循环与代码中函数调用（传入参数、返回计算结果、下游消费）同构，且该结构在代码语料中天然存在。

**方法**：提出功能感知的填充中间（FIM）中期训练——一种自监督目标。通过程序依赖图分析和复杂度-可推理性双重标准选择函数进行掩码，迫使模型根据上下文还原被掩码的函数体。在 968 个 GitHub 仓库的 2.6B token 去污染语料上对 Qwen2.5-Coder-Instruct 和 Qwen3-8B 进行中期训练，随后接入现有智能体后训练流程。

**关键结果**：在 SWE-Bench-Verified 上，7B/14B 模型分别提升 +2.8/+3.0，Qwen3-8B 提升 +3.2；SWE-Bench-Lite 增益达 +3.7/+4.0/+5.4。增益跨后训练管线（R2E-Gym、SWE-Smith）和基座模型（含非 Qwen2.5 的 Qwen3-8B）保持稳定。此外，中期训练有效缓解智能体后训练对非智能体编码（如 LiveCodeBench）和非编码工具使用（tau-bench、BFCL）能力的侵蚀，尽管训练语料仅含 Python 代码，函数调用的归纳偏置仍存活于后训练中并带来一致增益。
