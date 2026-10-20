---
title: 'Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards'
title_zh: Lean4AgenticRL：可验证多层级过程奖励推进 Agentic RL
authors:
- Ruida Wang
- Gerald Friedland
- Tong Zhang
- Chris Kong
affiliations:
- Amazon Web Services
- University of Illinois Urbana-Champaign
arxiv_id: '2610.22448'
url: https://arxiv.org/abs/2610.22448
pdf_url: https://arxiv.org/pdf/2610.22448
published: '2026-10-14'
collected: '2026-10-20'
category: Agent
direction: Agentic RL 多层级可验证过程奖励
tags:
- Agentic RL
- Process Reward
- Lean4
- GRPO
- Formal Verification
- Workflow Normalization
one_liner: 用 Lean4 统一多层级可验证过程奖励，配合 workflow-stage-normalized GRPO 稳定提升 Agentic RL
  训练效果
practical_value: '- 把导购/搜索 Agent 的复杂任务拆成可验证的工作流 stage（如需求澄清、商品召回、排序、话术生成），为每个 stage
  定义 post-condition 并用规则/轻量 LLM judge 给中间奖励，使 RL 训练信号更密。

  - 对 agent 的工具调用设置 penalty-only 的低层奖励（-1/0），专门惩罚重复查询、空操作、固定占位命令等 reward hacking；不给正奖励，避免策略利用，工程上容易实现。

  - 在 GRPO 中将 advantage 按工作流 stage 而不是整条 rollout 归一化，使不同轨迹中相同语义步骤可比，改善长 horizon 信用分配，适用于多轮对话推荐和搜索
  agent。

  - PSWF plan-then-execute 可作为轻量级 prompt 策略单独使用：先让模型探索环境生成定制化计划，再按计划执行，即使不重新训练也能小幅提升
  agent 成功率，便于快速验证业务收益。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
当前大模型 Agent 在复杂软件工程和终端任务上主要依赖高层 outcome reward 做 agentic RL，但单靠最终成功/失败信号无法区分长轨迹中的有效和冗余中间步骤，训练效率低；而现有的过程奖励多聚焦低层 toolcall 结果，忽略工作流层面的进展，且容易被策略通过重复命令等方式 hack。Lean4AgenticRL 将高、中、低三层奖励统一到 Lean4 可验证框架中，以提升训练稳定性和最终性能。

**方法关键点**
- 构建 problem-specific workflow (PSWF) agent system：采用 plan-then-execute，规划阶段探索环境并生成针对具体问题的自然语言工作流，执行阶段按此工作流行动，平衡固定工作流的可控性和 ReAct 的灵活性。
- 将 Lean4Agent 验证从固定工作流推广到通用 harness：用 LLM 将 PSWF 形式化为 Lean4 中的 stage 及 pre/post-condition；再按局部窗口将执行轨迹切分到工作流阶段，支持超长轨迹。
- 定义多层级奖励：α 为最终 outcome reward（-1/1）；β 为 workflow-stage reward，验证每个 stage 是否满足 post-condition，可由 Lean/Python 直接判定或 LLM judge 语义判断；γ 为 toolcall-level penalty-only reward（-1/0），惩罚重复、noop、const shell 等 reward-hacking 行为。
- 训练采用 workflow-stage-normalized GRPO：在同一 general workflow stage 内归一化 advantage，解决跨轨迹步骤对齐；β 奖励权重最多 0.5，且仅在 group pass rate 为 0% 或 ≥75% 时应用；γ 只罚不奖；规划阶段 token 仅用 α 训练。

**关键实验**
在 SWE-Bench-Verified、TerminalBench-2.0/2.1 上评估。LAR-9B 相对 base Qwen-3.5-9B 分别提升 20.2、13.5、13.4 个百分点；LAR-27B 达到 84.2%、68.2%、77.3%，平均优于 base 9.89%、优于同尺寸第二 5.07%。对比纯 outcome-reward GRPO，训练曲线更平稳，更早达到并超过最佳点；消融显示去掉 γ 后 SWE 性能从 56.0% 降至 49.4%，重复命令增加 66.8%；去掉 PSWF 从 44.0% 降至 42.4%。在 Qwen-3.6-27B 和 DeepSeek-V4-Flash-0731-304B 上进一步验证，分别提升 4.0/8.0 和 5.6 个百分点。

**最值得记住的一句话**：用 Lean4 形式化工作流统一多层级过程奖励，配合 workflow-stage-normalized GRPO 和 penalty-only toolcall reward，可在不扩大模型规模的情况下稳定提高 Agentic RL 训练效果。
