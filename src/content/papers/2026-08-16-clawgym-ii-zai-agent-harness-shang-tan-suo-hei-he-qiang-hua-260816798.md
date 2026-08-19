---
title: 'ClawGym II: Exploring Black-Box RL on Agent Harness'
title_zh: ClawGym II：在 Agent Harness 上探索黑盒强化学习
authors:
- Huatong Song
- Fei Bai
- Ming Yang
- Renyuan Li
- Jia Deng
- Jujie He
- Zhange Zhang
- Daixuan Cheng
- Yan Xing
- Qi Yun
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- IQuest Research
arxiv_id: '2608.16798'
url: https://arxiv.org/abs/2608.16798
pdf_url: https://arxiv.org/pdf/2608.16798
published: '2026-08-16'
collected: '2026-08-19'
category: Agent
direction: Agent 黑盒 RL 训练
tags:
- Black-box RL
- Agent Harness
- PPO
- GRPO
- Prefix Tree
- Training-Infrastructure
one_liner: 提出统一黑盒 RL 框架，通过不透明 harness 稳定规模化优化通用 Agent，并支持混合 harness 联合训练
practical_value: '- **把生产 harness 直接当 rollout engine，而不是重写 agent loop**：电商/广告/搜索推荐中的
  Agent 常运行在复杂编排系统里，重写会丢失上下文管理、重试、工具调度等关键行为。可以在模型服务边界加 proxy 拦截所有模型调用，以 token-in-token-out
  记录真实推理轨迹，再拿去做 RL 训练，避免训练-推理不一致。

  - **用 prefix tree 恢复分叉、去重的多轮轨迹**：同一 rollout 可能因 compaction、subagent、重试产生大量共享历史。组织成前缀树后，只优化
  main trajectories，过滤 dead leaves 和过分支 rollout，能显著降低噪声、提升训练效率；推荐/搜索 Agent 的多轮交互同理适用于这种树结构消重。

  - **引入 token-level importance sampling 校正 rollout 与训练引擎概率差异**：训练和推理引擎即使同一模型也可能因数值精度、并行方式产生
  log-prob 偏差，直接优化会带 off-policy 噪声。加一个截断的 token 级 IS ratio 是低成本、易迁移的稳定性 trick。

  - **mix-harness 训练可提升跨执行系统泛化**：如果业务中同一策略会跑在不同工具接口、不同上下文管理或不同编排系统上，可把同一 task 与多个
  harness 配对，按 task-harness pair 做分组 advantage 归一化，再联合梯度更新，避免策略过度绑定单一系统。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现代 Agent 能力高度依赖 harness（如 Claude Code、OpenClaw），它们内部包含系统提示、工具编排、上下文管理、重试恢复等复杂逻辑。直接在这些不透明 harness 上做 RL，很难获取完整轨迹，且大规模 rollout 会面临环境状态污染、执行失败和训练不稳定。已有 RL 多在简单白盒 agent loop 上做，无法覆盖生产 harness 的复杂行为。

**方法关键点**  
- **sandbox 隔离执行**：每个 task 环境和 harness 放入临时 sandbox，按需创建、结束后销毁，保证并发 rollout 状态隔离；外部能力通过 MCP server 提供。  
- **serving proxy 捕获模型调用**：在模型服务边界记录每轮请求/响应 token、log-prob，不与 harness 内部逻辑耦合。  
- **prefix tree 轨迹恢复**：将捕获的模型调用按共享前缀组织成 rollout 级前缀树，恢复多轮交互结构；过滤 dead leaves、过分支 rollout 和 auxiliary（subagent/compaction）轨迹，只保留 main trajectory 参与优化。  
- **PPO/GRPO 适配树结构**：GRPO 按 rollout 奖励做组内归一化；PPO 对同一 rollout 内多轨迹独立做优势估计，保持 rollout 级奖励语义。  
- **一致性保障**：token-in-token-out 保证训练 token 序列与推理生成完全一致；token-level importance sampling 校正训练与推理引擎概率差异。  
- **mix-harness training**：将同一 task 与多个 harness 配对，按 task-harness pair 分组计算优势，混合更新共享策略。

**关键结果**  
在 Qwen3-30A3B 上，黑盒 RL 通过 OpenClaw 和 Claude Code 分别将 ClawGym-Bench Pass@1 提升 9.98 和 14.81 点，PinchBench 提升 11.71 和 17.28 点，训练在 200–400 步内保持稳定；扩展至 JobBench 和 OfficeQA 后指标同样持续上升。与白盒 AgentLoop 对比，白盒同环境训练成绩更高，但跨 harness 迁移时黑盒训练明显更好。

**最值得记住的一句话**  
把不透明 harness 当作 rollout 引擎，在模型边界捕获轨迹并用前缀树重建训练数据，是让 Agent RL 稳定接入复杂生产执行系统的关键。
