---
title: 'SkillOpt-Lite: Better and Faster Agent Self-evolution via One Line of Vibe'
title_zh: SkillOpt-Lite：一行代码实现更优更快的 Agent 技能自我进化
authors:
- Yifei Shen
- Bo Li
- Xinjie Zhang
affiliations:
- LMMs-Lab
- NTU MMLab
- Microsoft
arxiv_id: '2607.03451'
url: https://arxiv.org/abs/2607.03451
pdf_url: https://arxiv.org/pdf/2607.03451
published: '2026-07-02'
collected: '2026-07-08'
category: Agent
direction: 代理技能自进化 · 零阶优化
tags:
- Skill Optimization
- Zeroth-Order Optimization
- Agent Self-evolution
- Minimal Pipeline
- Vibe Coding
- Code Agent
one_liner: 用零阶优化与三项原则将 Agent 技能优化精简为一行代码，提速收敛并让纳米模型超越大模型
practical_value: '- 借鉴 SkillOpt-Lite 的最小管线思路，可把推荐系统的策略文档/提示工程当做可编辑代码，通过文件轨迹探索+共识挖掘自动化迭代，减少人工调参。

  - 独立验证门控（independent validation gating）能作为推荐系统在线实验的安全网，自动拦截效果退化。

  - 零阶优化对不可微的 LLM 推荐链路适用，可用于优化召回 query 生成或排序 prompt，无需访问模型内部梯度。

  - 一行 `vibe` 命令集成进 VSCode 的哲学，可启发构建面向业务分析师或运营的“一键调优推荐策略”工具，降低门槛。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 Agent 技能优化方法依赖复杂流水线，未明确最小可行组件。该工作从零阶优化视角形式化技能优化，借鉴经典数值扰动与信任域，发现技能轨迹作为可解释调试反馈优于盲扰动，旨在探索极简管线。

**方法**：基于 Claude Code 哲学与 PAC 学习理论，提出三项收敛与泛化原则：(1) 基于文件系统的轨迹探索（自动生成并存储轨迹作为调试信号）；(2) 共识属性挖掘（从成功轨迹中抽取共性模式）；(3) 独立验证门控（防止过拟合）。据此消除冗余，得到 SkillOpt-Lite 极简管线。管线将所有 Agent 组件视为标准可编辑代码，在一行 `vibe` 命令下完成技能进化，并自然泛化到完整脚手架优化（HarnessOpt）。

**关键结果**：SkillOpt-Lite 在 LiveMath 上对 GPT-5.5 提升 +8.8 分，对 GPT-5.4-nano 提升 +25.4 分，使 nano 模型超越 SkillOpt 优化的标准 GPT-5.4。在 SpreadsheetBench 上，HarnessOpt 驱动 GPT-5.4-nano 获 0.7758 准确率，超过 GPT-5.5 标准流水线的 0.7620。方法已集成至 VSCode Copilot，实现生产环境中一行代码进化 Agent 技能。
