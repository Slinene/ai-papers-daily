---
title: 'Harness^2: Recursive Agent Harnessing for an Open World'
title_zh: Harness²：开放世界中的递归 Agent 驾驭框架
authors:
- Ruiyao Xu
- Yanfei Chen
- Zhongying CuiZhu
- Bhavana Dalvi Mishra
- Yifei Ming
- Han Yu
- Rujun Han
- Chen-Yu Lee
- Tomas Pfister
affiliations:
- Northwestern University
- Google Cloud AI Research
arxiv_id: '2610.14224'
url: https://arxiv.org/abs/2610.14224
pdf_url: https://arxiv.org/pdf/2610.14224
published: '2026-10-08'
collected: '2026-10-14'
category: Agent
direction: Agent harness 递归自改进
tags:
- recursive self-improvement
- agent harness
- open-world tasks
- harness optimization
- test-time adaptation
- LLM agent
one_liner: 提出 Harness²，通过对比性 Propose-Probe-Compose 与经验库更新，在无 ground-truth 的开放世界中持续改进
  agent harness。
practical_value: '- 将推荐/搜索 agent 的运行时组件（prompt、工具说明、技能、子代理、中间件）显式文件化，支持在线编辑和版本管理，比黑盒
  prompt 更容易自动优化。

  - 在没有 ground-truth 的在线场景（如 query 推荐、文案生成质量难以标注），采用 Propose-Probe-Compose 的行为对比方法：让候选
  harness 与当前 harness 执行同一任务，对比轨迹和输出差异作为编辑证据，避免依赖不可靠的奖励模型。

  - 建立跨任务的经验库（harness improvement library），存储成功的 harness 组件和适用条件，支持新任务时按需检索和复用，避免每次从零调优；类似电商场景中不同品类/活动下的
  agent 配置可以复用。

  - 将 harness 优化与模型解耦，冻结模型权重，只优化外围组件，降低成本并便于快速迭代；弱模型配合优化后的 harness 可以超过强模型默认 harness。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM agent 的表现不仅取决于模型权重，更取决于其 harness（提示、记忆、技能、工具、编排）。手工设计 harness 难以应对开放世界中不断变化的任务需求；递归自改进（RSI）提供自动演化 harness 的可能，但开放世界任务在测试时没有 ground-truth 验证器，且任务特定的改进难以泛化到新场景。

## 方法关键点
Harness² 将 harness 分解为 8 个可编辑组件（系统提示、护栏、记忆、技能、工具指导、脚本、子代理、中间件插件），并通过两层递归实现改进：
- **任务级递归**：对当前任务，采用对比性 Propose–Probe–Compose 步骤。Propose 生成两类候选 harness：一类针对跨域通用缺陷（invariant），一类针对当前领域知识（domain-specific）；Probe 在相同条件下执行候选并与参考执行对比，获得行为对比证据；Compose 根据对比结果选择、合并或拒绝改动。支持并行递归（同时探索多个候选并聚合）和顺序递归（迭代细化）。整个过程不需要 ground-truth 标签。
- **驾驭级递归**：任务完成后，反思改进过程，提取可复用的 harness 和教训（EXPERIENCE.md），更新改进 harness 中的库，指导未来任务的提案与组合，使改进能力本身也持续提升。

## 关键结果
在 WorkBuddy-Bench、JobBench、LAB 三个专业基准上，使用 Gemini 3.5 Flash 和 GLM-5 作为冻结执行器，在 OpenCode 和 Codex 两个初始 harness 下评估。单步改进（k=1）在所有配置上均提升：WorkBuddy-Bench 上 GLM-5 在 OpenCode 下提升 11.5 点，JobBench 提升 4.5 点，LAB Partial 提升 11.8 个百分点。并行递归（k=5）进一步增加增益（WorkBuddy +2.9~3.9，JobBench +3.0~4.2，LAB +2.6~6.7）。计算-性能 Pareto 前沿上，Harness² 以更少计算获得更高增益。消融显示 library、scoping、composition 各贡献 1.6~3.7 点。跨基准迁移（JobBench→WorkBuddy）带来 0.5~2.9 点提升。同一模型兼任执行器和编辑器也能改进（GLM-5 在 LAB 上 +13.7 点）。

**最值得记住的一句话**：在没有 ground-truth 的开放世界中，通过行为对比（Propose–Probe–Compose）与跨任务经验库的递归更新，可以将任务特定的 harness 改进转化为可复用的在线适应能力。
