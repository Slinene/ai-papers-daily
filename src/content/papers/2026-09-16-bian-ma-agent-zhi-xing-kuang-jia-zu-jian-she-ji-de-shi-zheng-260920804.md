---
title: An Empirical Study of Harness Design for Coding Agents
title_zh: 编码 Agent 执行框架组件设计的实证研究
authors:
- Run-Ze Fan
- Zihao Zhang
- Simin Ma
- Yebowen Hu
- Shouju Wang
- Kaiqiang Song
- Fei Liu
- Hamed Zamani
- Xiaoyang Wang
affiliations:
- UMass Amherst
- Emory University
- UNC Charlotte
- Zoom
arxiv_id: '2609.20804'
url: https://arxiv.org/abs/2609.20804
pdf_url: https://arxiv.org/pdf/2609.20804
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent 执行框架组件消融与设计
tags:
- coding agent
- harness design
- context management
- planning
- action space
- ablation study
one_liner: 系统性消融编码 Agent 的上下文管理、规划与动作空间，揭示模型与预算相关的组件设计规律
practical_value: '- 上下文管理策略可直接借鉴：先用规则过滤冗余内容，再按需用 LLM 摘要，能有效控制 token 成本；避免实现“可恢复的删减”机制，因为模型几乎不会去调用，徒增工程复杂度。

  - 动态规划开关：强模型上规划主要降低 token 消耗而非提升精度，弱模型上才是精度支撑。可在推荐/搜索 Agent 中按模型能力决定是否启用规划步骤，平衡效果与成本。

  - 动作空间设计遵循“够用即可”：对工具使用能力较弱的模型提供结构化预定义工具，对 bash 能力强的模型只给命令行接口，既提升成功率又降低成本，尤其适合命令密集型任务。

  - 组件解耦的消融框架值得复用：固定执行循环，独立替换上下文、规划、动作模块，可快速定位系统瓶颈，适合在电商 Agent 中进行模块化调优。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：编码 Agent 的执行框架（harness）将模型能力转化为长程软件工程表现，但现有工作通常将整框架作为黑盒评估，组件各自贡献不清。该研究通过固定执行循环、单独变动规划、动作空间和上下文管理三个组件，实现组件级对比。

**方法**：在 SWE-Bench Verified 和 Terminal-Bench 2.1 上，用四个模型评估 176 个配对设置，覆盖五种上下文管理策略、四种上下文窗口预算，并对规划和动作空间做靶向消融。

**关键结果**：
- 上下文管理在窗口预算紧张时价值提升，主要收益来自防止上下文溢出失败。
- 先用规则删除再 LLM 摘要的策略整体效率最强；可恢复被删内容的机制模型很少使用，未带来精度提升。
- 规划从弱模型的精度支架转变为强模型的成本节省器，精度变化不大。
- 对 bash 能力弱的模型，预定义工具提升性能；对 bash 能力强的模型，仅用 bash 接口即可有效且成本大幅降低，尤其在命令行中心任务上。
轨迹分析表明：上下文管理延长执行轨迹但不显著改变行为，规划改变轨迹停止位置，动作空间改变代码编写粒度。结论为模型与预算感知的框架设计提供依据。
