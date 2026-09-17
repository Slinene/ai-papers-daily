---
title: 'ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement'
title_zh: 模块化递归执行框架自改进：可泛化的对比式 Harness 进化
authors:
- Siwei Wu
- Jincheng Ren
- Yizhi Li
- Haau-Sing Li
- Chengran Yang
- Yuxuan Zhang
- Weicheng Gu
- Jian Yang
- Riza Batista-Navarro
- Chuanyi Zhang
affiliations:
- Beihang University
- University of Manchester
- IQuest Research
- M-A-P
- Langboat
arxiv_id: '2609.14857'
url: https://arxiv.org/abs/2609.14857
pdf_url: https://arxiv.org/pdf/2609.14857
published: '2026-09-13'
collected: '2026-09-17'
category: Agent
direction: Agent harness 自进化 · 模块化归因
tags:
- Agent
- Harness Self-Improvement
- Recursive Self-Improvement
- Modular Evolution
- Contrastive Trajectory
- Benchmark-Disjoint
one_liner: 对比同类轨迹并按五个功能模块独立进化 harness，在基准隔离数据上实现跨任务/跨模型可泛化自改进
practical_value: '- 将推荐/搜索 Agent 的执行 harness 拆成 Agent Loop / Tool Use / Observation
  Management / Context Management / Task Completion Detection 五个模块，每次只改一个模块并限制 diff
  范围；这比整体改写 prompt 或流程更可控，适合线上 Agent 的灰度、回滚与归因。

  - 采集同一任务的多次 rollout，区分 positive / contrastive / negative 组，用成功-失败轨迹对比定位“哪个机制该改”，并用跨任务投票聚合证据，避免把单条失败轨迹的
  case-specific 修复写进全局；可迁移到商品推荐、query 改写、客服 Agent 的失败归因。

  - 建立与评估集隔离的进化任务池（benchmark-disjoint），每个改动必须通过 AST/静态检查、import/protocol 校验、以及“是否过拟合当前实例”的
  diff review 后才保留，否则自动回滚；这能防止自改进只在测试集刷分，适合离线自进化流水线。

  - 维护 Evolution History 和 Trajectory Memory，对函数库做 Function Merge + Task-Aware Function
  Composition，避免多轮自改进后函数膨胀和振荡；适合把 self-improvement 用于线上持续优化但需要控制风险。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Agent 能力越来越依赖执行框架（harness）的循环控制、工具调用、上下文管理与终止检测。用任务级成功/失败信号做 harness 自改进，面临三个问题：进化数据常来自下游评测基准，难区分可泛化机制与刷分适配；单条轨迹混淆系统缺陷和实例特定解法；整体改写 harness 无法把缺陷归因到具体组件。

**方法关键点**：
- 把 Terminus-2 harness 拆成五个功能模块：Agent Loop、Tool Use、Observation Management、Context Management、Task Completion Detection，各自独立进化，限制修改范围。
- 对每个任务多次 rollout，划分 positive / contrastive / negative 三组；用成功-失败轨迹对比产生结构化诊断，再跨任务聚合相似诊断并投票排序，筛出反复出现的机制缺陷。
- 修改后经过三层 Validation Gates：AST/import/protocol 静态检查、Diff Review 过滤 task-specific 修改、实际执行验证，失败则基于 diff 回滚。
- 通过 Trajectory Memory 复用历史成功轨迹，Evolution History 防止重复/冲突修改；最后做 Cross-Module Integration 合并五个模块，再用 Function Merge 去重和 Task-Aware Function Composer 按任务激活函数。
- 进化协议使用 2,000 个外部构造的可执行任务，完全与下游 TerminalBench 2.0 / SWE-Bench Verified 隔离。

**关键结果**：
- 在 TB-related 数据上进化的 harness，TerminalBench 2.0 准确率从 47.57→52.43，Pass3 从 30.34→35.96；在 SWE-Bench Verified 上从 73.40→76.45。
- 跨域迁移：TB 进化集提升 SWE-Bench Verified 到 75.80；SWE 进化集提升 TerminalBench 2.0 到 49.40。
- 跨模型迁移：冻结核心主模型 DeepSeek-V4-Flash 进化出的 harness，在 GLM-5.2、MiniMax-2.5 上均有提升。
- 消融显示非模块化进化降到 46.44，联合所有模块进化降到 44.19，而先独立再集成到 52.43；单模块中 Agent Loop 提升最大，Observation Management 显著降低步数。
- 与 AHE、Meta-Harness 在统一 benchmark-disjoint 协议下对比，AHE/Meta-Harness 仅提升约 1 个点，ModularRSI 提升 5+ 个点。

**最值得记住的一句话**：可泛化的 harness 自改进必须同时解决数据隔离、轨迹归因和机制 credit assignment，模块化 + 对比轨迹 + 验证门是一种可复用方案。
