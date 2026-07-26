---
title: 'Progressive Cramming: Reliable Token Compression and What It Reveals'
title_zh: 渐进式填塞：可靠Token压缩及其揭示的局限
authors:
- Dmitrii Tarasov
- Timofei Lashukov
- Elizaveta Goncharova
- Andrey Kuznetsov
affiliations:
- FusionBrain Lab
- HSE University
- Innopolis University
arxiv_id: '2607.21231'
url: https://arxiv.org/abs/2607.21231
pdf_url: https://arxiv.org/pdf/2607.21231
published: '2026-07-23'
collected: '2026-07-26'
category: LLM
direction: LLM token压缩与表示容量研究
tags:
- token compression
- progressive cramming
- transformer capacity
- attention knockout
- reconstruction
one_liner: 逐token扩展压缩目标直至重建失败，定位可靠压缩边界，并揭示早期层交互致下游崩溃
practical_value: '- 在推荐/搜索系统中将用户行为序列压缩为少量 token 时，即使自回归重建准确率高，也可能严重削弱 LLM 的推理与生成能力，评估应以下游任务为准，不能只看重建误差。

  - 渐进式 cramming 提供了一种确定序列压缩极限的方法，可用于测试不同长度用户序列能被无损编码的边界，指导压缩程度的选择。

  - 因果注意力 knockout 表明压缩嵌入主要通过模型早期层引入干扰，尝试在早期层后插入压缩表示或进行针对性微调可能缓解能力退化。

  - 对 Agent 长程记忆压缩的场景，该工作提示“完美重建”并不等同于保留可转移的语义，需关注压缩对代理决策的实际影响。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：现有 token cramming 用固定预算和 99% 重建准确率阈值，无法区分残差是优化失败还是根本限制。
方法：提出渐进式 cramming，从单个 token 开始逐 token 扩展目标前缀，直至在固定优化预算内无法实现完美重建，精准定位可靠压缩的极限。训练轨迹在嵌入空间呈现低维结构。
关键发现：在压缩嵌入前加原始前缀进行多选基准测试时，仍导致中等但一致的准确率下降；在生成评估下能力完全崩溃。因果注意力 knockout 实验将退化定位到嵌入与模型早期层的交互。
结论：完美重建（通过脆弱引导而非可转移语义实现）不足以构成有意义的压缩。渐进式 cramming 可作为研究压缩介限的工具。
