---
title: 'ARE-bench: Benchmarking Agents'' Research Ability in Real-World Researcher
  Sessions and Workspaces'
title_zh: ARE-bench：真实研究者会话与工作区中的智能体研究能力基准
authors:
- Jiahang Lin
- Wanying Ren
- Wanghan Xu
- Huayu Sha
- Yang Shu
- Zhonghang Lu
- Chengjun Pan
- Yi Dong
- Shichun Liu
- Yuyang Hu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Fudan University
- East China Normal University
- Shanghai Jiao Tong University
- Renmin University of China
arxiv_id: '2611.14364'
url: https://arxiv.org/abs/2611.14364
pdf_url: https://arxiv.org/pdf/2611.14364
published: '2026-11-10'
collected: '2026-11-11'
category: Eval
direction: 真实科研环境下的研究Agent评测
tags:
- Research Agents
- Benchmark
- Real-world Workspace
- Long-horizon
- Contextual Evaluation
- LLM
one_liner: 构建基于真实科研项目会话与未清理工作区的基准，揭示只评估交付结果会高估研究智能体能力
practical_value: '- 评估业务中的 Agent 时，不能只看最终交付结果，需把历史会话依赖、工作区残留文件、旧版本、失败尝试等上下文纳入检查项，否则会大幅高估模型真实可用性。

  - 借鉴其“真实会话+未清理工作区回放”的思路，为搜索推荐 Agent 构建连续工作流回归测试，让评测更贴近线上真实多轮协作场景。

  - 使用二进制 checklist 与 intent-aligned rubric 打分，允许任何有效解决方案，可提升 Agent 评测的客观性和可复现性。

  - 按不同阶段（如方案设计、执行）统计通过率，快速定位 Agent 在复杂需求上的短板，便于针对性优化 prompt 或工具链。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有研究 Agent 基准多关注独立任务和干净工作区，但真实科研中用户请求往往只是持续项目的一步，依赖之前会话决策，工作区包含未完成文件、旧版本和失败尝试。为更真实地评估 Agent 推进项目的能力，提出 ARE-bench。

**方法关键点**：ARE-bench 基于招募研究者的真实科研项目会话与完整工作区，包含 75 个任务，覆盖 7 个研究阶段、33 项需求、150 个子需求，共 1173 个二进制 checklist 项。每个任务锚定一个真实用户请求，保留其需求，并将仍在生效的前序请求总结为背景；工作区完整回放到该节点，不做清理，保留早期产物。checklist 从 intent-aligned rubric 编译，认可任何有效解决方案。

**关键结果**：在七个前沿模型上，最强模型仅在 66.2% 的任务上通过所有 checklist 项，Design 和 Execution 是所有模型最难的阶段。三个模型在仅检查交付合约与通用规范时通过约 69% 的任务，但加入历史、材料或工作区要求后仅剩 28.4%~40.0%。说明忽略上下文要求会高估研究 Agent 并掩盖模型差异。
