---
title: Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling
title_zh: 面向延迟优化的 Web Agent 规划与调度的 Agent JIT 编译
authors:
- Caleb Winston
- Ron Yifeng Wang
- Azalia Mirhoseini
- Christos Kozyrakis
affiliations:
- Stanford University
arxiv_id: '2605.21470'
url: https://arxiv.org/abs/2605.21470
pdf_url: https://arxiv.org/pdf/2605.21470
published: '2026-05-20'
collected: '2026-05-21'
category: Agent
direction: Agent 规划调度优化
tags:
- Web Agent
- JIT Compilation
- Planning
- Scheduling
- Latency Optimization
- Tool Use
one_liner: 通过 JIT 编译、不变式强制工具协议和代价优化规划/调度，将 Web Agent 延迟降低 10.4 倍且准确率提升 28%。
practical_value: '- **工具协议的设计（pre/post conditions）**：在电商自动化操作中，可以为每个动作（如添加购物车、结算）定义前置页面状态与后置预期状态，编译时即做状态流校验，大幅减少点击错误元素等失误（实验中该类错误从
  59% 降至 25%）。

  - **代价优化的规划策略**：同时生成多个任务计划（代码形式），通过静态检查与代价模型（惩罚 LLM 调用和循环）选出最低成本计划。在电商场景可用来减少不必要的
  LLM 推理，将大量纯代码操作替代昂贵模型调用。

  - **自适应调度（串行/并行/对冲）**：根据历史延迟分布做蒙特卡洛估计，为每个任务选择最优策略。当电商操作中某些元素交互方差大（如查找特定商品按钮）时自动采用对冲（同时多路执行取最早成功），可有效控制尾延迟。

  - **缓存与工具代码复用**：将成功执行 trace 合成为可缓存工具，后续任务直接调用代码而非每步推理，显著降低延迟并将 LLM 调用次数降至接近零。类似做法可直接用于重复性电商流程（如批量比价、多店铺信息抓取）。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：现有 Computer-Use Agent 采用顺序截图-推理-执行循环，每一步都需要 LLM 调用，延迟高且错误率突出（如点击错误、顺序错乱）。静态的工具集（只有 click/type 等原语）、仅串行执行以及规划后的非确定性是延迟与准确率的主要瓶颈。

**方法**：提出 Agent JIT 编译器，将自然语言任务描述直接编译为可包含工具调用、LLM 调用以及并行化的可执行代码。核心为三个组件：
- **不变式强制工具协议**：每个工具声明前置/后置状态不变式（如 page_type: store），编译时可静态校验工具调用序列的状态流正确性，错误率大幅降低。
- **代价优化规划器**：并行生成多个代码候选，通过 CFG 同时做状态验证与代价估计（代价模型惩罚 LLM 调用和循环，给予较大权重），选出最小代价的有效计划。
- **代价感知调度器**：基于历史交互的延迟分布，利用 LLM 预测计划会涉及的页面元素，再用蒙特卡洛采样评估串行、并行、对冲三种 vCPU 分配策略的期望延迟，选择最优策略。

**关键结果**：在 Dashdish、Gitlab 等 5 个 Web 应用共 37 个任务上，JIT-Planner 相比 Browser-Use 平均加速 10.4×（122.1s → 11.7s），准确率绝对提升 28 个百分点（61% → 89%）。JIT-Scheduler 相比 OpenAI CUA 加速 2.4×（258.7s → 109.9s），准确率提升 9 个百分点。不变式协议将有效计划生成率从 77% 提高到 90.6%。代价估计有效，最小成本 vs 最大成本计划延迟差距达 1.8×。协议与并行候选生成结合进一步降低计划生成时间（Pass@t 在 5s 内可达 100%）。
