---
title: 'Pay for the Fault, Not the Flow: Label-Free In-Flow Multi-Agent Workflow Optimization'
title_zh: 无标签流内多智能体工作流优化：按故障而非全流程付费
authors:
- Xuehang Guo
- Haoyu Wang
- Shengyu Chen
- Zach Chen
- Wei Cheng
- Qingyun Wang
- Haifeng Chen
affiliations:
- William & Mary
- NEC Corporation of America
arxiv_id: '2610.01017'
url: https://arxiv.org/abs/2610.01017
pdf_url: https://arxiv.org/pdf/2610.01017
published: '2026-09-30'
collected: '2026-10-02'
category: MultiAgent
direction: 无标签多Agent工作流优化
tags:
- Multi-Agent
- Workflow Optimization
- Label-Free
- In-Flow
- Agent Creation
- Fault Attribution
one_liner: 提出 INFLOWOP，用统一无标签成本驱动多Agent工作流构建与流内局部修复，在 BRAID 上最高较单Agent提升11.97%
practical_value: '- 在推荐/广告多 Agent 编排中引入成本矩阵对手头模型/工具做适配评分；当子任务（如召回、精排、文案生成）没有合适专家时，触发新
  specialist 创建而非强行复用，避免不匹配导致的性能损失。

  - 为每个子任务定义输入/输出契约（例如召回需满足相关性、精排输出需符合业务格式），运行时用 semantic matching 检测契约破坏，无需标注即可定位故障属于
  assignment 还是 decomposition，适合在线无监督场景。

  - 局部修复与缓存复用：某一步失败只暂停该步并重跑下游依赖，保留其他成功结果，避免整套 pipeline 重跑；在广告/搜索工作流中能显著降低推理延迟和计算成本。

  - 借鉴 Agent card + self-evolving empirical profile：为每个专家模型维护声明能力与历史成功案例画像，仅用成功样本更新画像，用于后续成本估计和路由决策，比仅靠声明能力带来稳定提升。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：多 Agent 工作流将复杂任务分解并分配给专家，但分解粒度、agent 选择、何时创建新 agent 通常由固定模板或监督信号决定；一旦流程失败，定位故障依赖参考答案或重跑整个流程，优化代价高。缺少统一、无监督的成本函数来同时指导构建与运行。

**方法关键点**：
- 提出 INFLOWOP 两阶段框架：构建阶段 COALESCE 先 top-down 将任务分解到最细原子，再 bottom-up 根据成本矩阵合并，成本 = 可靠性成本 + β×延迟成本 + γ×创建成本。
- 成本矩阵通过 rubric semantic estimator 匹配子任务需求与 agent card（声明能力 + 自我演化经验画像），无需标签。
- 每个子任务带有输入/输出条件契约，运行时用同一 matching 函数检测契约破坏，判断故障属于 assignment（换 agent）还是 decomposition（局部重分解）。
- 优化采用成本有序阶梯：先 RE-ASSIGN，再 RE-DECOMPOSE；只重跑受影响子任务闭包，保留其他结果。
- 提出 BRAID 基准，任务要求多 Agent 协调且单 Agent 难以完成，覆盖 8 领域 19 个 evaluation arms。

**关键实验**：
- 在 BRAID 上跨 6 个 backbone，INFLOWOP 相对单 Agent 基线提升 +7.15% 到 +11.97%，最强 backbone GPT-5.6-luna 从 41.99% 提升至 49.37%。
- 消融显示：COALESCE 相对 greedy-search 提升 +6.72%，in-flow 再加 +1.59%，profile 更新再 +1.33%；动态 cost matrix 和动态 agent pool 分别带来约 +2.5~4.5% 提升；全局定位反而降准确率。

**最值得记住的一句话**：用统一的无标签成本同时指导工作流构建与运行优化，只修复故障点而非重跑整个流程。
