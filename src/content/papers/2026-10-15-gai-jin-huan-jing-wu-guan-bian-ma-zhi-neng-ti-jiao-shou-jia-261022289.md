---
title: 'Improving Environment-Agnostic Coding Agents: The Role of Scaffolding'
title_zh: 改进环境无关编码智能体：脚手架的作用
authors:
- Sergey Rodionov
affiliations:
- SingularityNET
arxiv_id: '2610.22289'
url: https://arxiv.org/abs/2610.22289
pdf_url: https://arxiv.org/pdf/2610.22289
published: '2026-10-15'
collected: '2026-10-17'
category: Agent
direction: Agent 脚手架与自主控制权衡
tags:
- Scaffolding
- LLM Agent
- Code Generation
- Environment-Agnostic
- Control Flow
- ARC-AGI
one_liner: 仅改变指令鼓励报告困难并自动继续，环境无关编码智能体在 ARC-AGI-3 和 AGI Maze 上得分提升，但专用脚手架仍有优势
practical_value: '- **环境无关脚手架与专用控制器解耦**：将通用工具（shell、文件系统、上下文管理）与领域特定控制逻辑分离，便于在电商推荐
  Agent 中复用通用层，只替换业务控制层，降低跨场景工程成本。

  - **引入“报告困难 + 自动继续”机制**：在购物助手或搜索 Agent 中，可要求模型在不确定时主动返回控制权，由外部脚本决定重试、换策略或退出，减少死循环和无效调用，提升任务完成率。

  - **把重置/重试等关键决策固化到控制器**：实验显示脚本化 controller 遵循已有约定能恢复部分专用 agent 优势；在推荐流程中，可将“重置会话、切换召回策略、回退规则”等决策从模型手中剥离，保证行为可预测。

  - **警惕教程/Few-shot 过度设计**：额外教程经验可能降低性能，提示在构造推荐 Agent 的示例或指令时需做严格消融，避免冗余示范干扰模型。

  - **关注 token 成本与性能的权衡**：性能提升伴随更高 token 开销，业务中采用此类自主控制机制前应对比推理成本与收益。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：更强的语言模型可能自行构造有用流程，削弱开发者提供的脚手架优势，但实际中专用脚手架仍然重要；需要弄清为什么环境无关 agent 仍落后于专用 agent，以及能否不依赖环境特定工程改进。

方法关键点：
- 在 ARC-AGI-3、AGI Maze、Terminal-Bench 三个环境中评估基于 Codex 的 agent，保持代码、prompt、通用工具完全不变，只让环境特定信息作为输入。
- 对比两个几乎相同的 prompt 变体：一个仅增加了“鼓励报告困难并返回控制权以便自动继续”的指令。
- 进一步将 reset 决策转移到脚本化控制器，该控制器遵循已经提供给 agent 的约定，不做环境特定优化。
- 在 AGI Maze 上测试额外教程经验的影响。

关键结果：
- 仅改变指令使 ARC-AGI-3 和 AGI Maze 的平均得分提升，Terminal-Bench 表现小且混合变化。
- 即便如此，通用 agent 仍低于 ARC-AGI-3 专用参考（包括使用 GPT-5.6-sol 时），参考方案主要是规定组织和控制，而不是提供新规则或答案。
- 将 reset 决策转移到脚本化控制器后，恢复了专用 agent 的部分优势。
- AGI Maze 中额外教程经验反而降低性能。
- 性能提升伴随更高 token 成本，且实验未完全分离信息/流程利用与额外或不同推理分配的影响。
