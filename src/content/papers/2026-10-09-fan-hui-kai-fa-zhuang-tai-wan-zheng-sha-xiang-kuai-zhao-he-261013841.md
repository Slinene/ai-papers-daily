---
title: 'Returning to Development States: When Full Sandbox Snapshots Help Coding Agents'
title_zh: 返回开发状态：完整沙箱快照何时帮助编码智能体
authors:
- Daniel Thi Graviet
- Tanmay Shah
affiliations:
- Daytona
- University of Waterloo
arxiv_id: '2610.13841'
url: https://arxiv.org/abs/2610.13841
pdf_url: https://arxiv.org/pdf/2610.13841
published: '2026-10-09'
collected: '2026-10-13'
category: Agent
direction: 编码 Agent 的失败恢复与状态搜索
tags:
- Go-Explore
- coding agents
- sandbox snapshots
- test-time scaling
- failure recovery
- runtime state
one_liner: 在编码智能体失败恢复中，以完整沙箱快照为可搜索状态做 Go-Explore 式分支，发现收益主要来自仓库外运行时状态
practical_value: '- 多阶段 Agent 工作流（如推荐系统实验环境搭建、数据管道调试、线上服务配置迭代）中，失败恢复不要只保存代码 diff 或文本总结，可在关键中间步骤保存完整沙箱/容器快照（包括数据库、缓存、依赖、运行的服务），允许从中间状态分支重试，减少重复搭建成本。

  - 根据结论判断是否值得引入快照：如果任务涉及多个服务且状态无法从单个 git diff 重建（例如特征平台数据、模型服务配置、A/B 实验中间产物），快照收益最大；简单单仓库代码修复则不必增加复杂度。

  - 可借鉴 Go-Explore 的“记录有希望状态并回访”思想：在 Agent 测试时扩展中，除了采样轨迹，还可以维护一个状态池，按照进度指标（如任务完成度、关键里程碑）筛选值得分支的中间环境，提高长
  horizon 任务解决率。

  - 工程实现上，使用 Docker/容器快照或轻量级 VM 快照作为状态保存手段，成本可控；可设定快照触发条件（例如阶段成功、关键外部状态变更后），避免每一步都保存。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：编码智能体在失败后从零重试会丢失执行过程中积累的机器状态，如安装的依赖、启动的数据库和服务、生成的中间产物等。现有测试时扩展方法通常只保留文本记忆或源码级状态，无法恢复完整运行时环境。

**方法关键点**：将 Go-Explore 的搜索思想应用于编码智能体失败恢复。把完整的 Daytona 沙箱快照作为可搜索状态，冻结整个执行环境，使新的智能体实例可以从中间状态恢复并继续探索，而不是从初始仓库重新开始。搜索过程会记录有希望的中间快照，允许回访和分支。

**关键结果**：更高的解决率和更高效的搜索主要来自仓库之外的运行时状态（数据库、服务等）。完整快照搜索在长周期、跨多个服务、状态无法由单一 diff 重建的编码任务中最有效。对于简单单仓库修复任务，收益有限。
