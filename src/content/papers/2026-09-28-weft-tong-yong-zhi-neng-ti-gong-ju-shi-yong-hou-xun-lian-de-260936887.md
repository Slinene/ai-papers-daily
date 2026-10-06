---
title: 'WEFT: Scaling Tool-Use Post-Training for General-Purpose Agents'
title_zh: WEFT：通用智能体工具使用后训练的全系统扩展框架
authors:
- Bo Mao
- Hang He
- Linting Wang
- Lizhi Lin
- Maosen Zhou
- Guanming Liu
- Jinxiu Liu
- Tianyu Huai
- Chaoyun Zhang
- Bingxuan Li
affiliations:
- East China Normal University
- Fudan University
- Shanghai Innovation Institute
- Renmin University of China
- Shanghai Qiji Zhifeng Co., Ltd
arxiv_id: '2609.36887'
url: https://arxiv.org/abs/2609.36887
pdf_url: https://arxiv.org/pdf/2609.36887
published: '2026-09-28'
collected: '2026-10-06'
category: Agent
direction: Agent 工具使用后训练 · 全系统扩展与自进化
tags:
- Tool-Use Post-Training
- Agent
- Execution-Driven Evolution
- RL Credit Assignment
- MCP
- SFT
one_liner: 构建可扩展交互系统、执行驱动自进化与稳定训练，WEFT 在多个工具使用基准上超过同规模环境扩展基线。
practical_value: '- 在构建电商工具调用训练环境时，不要只堆 API/MCP 数量；建立「执行证据→失败归因→修订环境/任务/校验器」的闭环。具体
  trick：用状态 diff 和工具返回来做 verifier，先修环境 bug 再训模型，减少“模型背锅”。

  - SFT 数据构造用 prefix-preserving rejection sampling：以原子任务（如“查商品→加购物车→下单”）为边界，失败只重采样当前原子任务的
  attempt，保留已验证前缀和状态快照，提高长链路训练轨迹利用率。

  - RL 中做 atomic-turn credit assignment：对每个原子任务组内做 group-relative 归一化，只对当前 turn 的
  policy token 施加 advantage，避免 trajectory-level reward 把无关前缀也更新；对检测到重复/格式错误/接口违规的成功段，mask
  正 credit。

  - 部署层面，可用类似 MegaMCP 的共享服务+私有状态隔离：MCP/工具服务共享 Python 进程，数据库 copy-on-write 克隆，workspace
  隔离，快照支持重试/候选采样，降低大规模 rollout 成本（upload 降 95%、内存降 77-95%）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具使用后训练大多只扩展可执行环境数量，但训练信号来自环境、任务、agent harness、evaluator 组成的完整交互系统。环境可用不代表任务可行、评估正确；失败可能由工具实现、任务不可行或 verifier 错误导致，直接归因于策略会引入误导性学习信号。因此需要在扩展环境的同时，持续改进整个交互系统，并用执行证据支撑策略学习与组件修订。

### 方法关键点
- **可扩展交互系统构建**：从工具文档合成 stateful MCP 环境（database/workspace 状态、execution-based validation）；生成经过验证的原子任务，按依赖关系组合成跨 MCP DAG，渐进式初始状态；同一任务通过 Agentic/SimUser 视图和 ReAct/OpenClaw/Hermes harness 产生多样性 rollout。
- **执行驱动自进化**：用状态 diff 和工具返回做 executable checks；失败归因到策略 vs 环境/任务/verifier；只修订负责组件，重跑构建检查，用 fresh rollouts 验证并进入下一轮。
- **稳定后训练**：SFT 使用 prefix-preserving rejection sampling，以原子任务为边界保留已验证前缀和状态快照；RL 先做任务与 verifier 一致性过滤，再用 atomic-turn group-relative credit assignment：对同一历史状态采 G 个候选段，按当前原子任务完成结果归一化 advantage，只更新当前 turn token，检测到重复/格式错误/接口违规时 mask 正 credit。
- **MegaMCP**：共享工具服务进程 + 每 rollout 私有数据库/workspace，copy-on-write 初始快照，支持重试和候选采样，降低部署与冷启动成本。

### 关键实验
构建 8,172 个 MCP、64,755 个工具、41,695 个认证原子任务、11,884 个组合任务；在 Qwen3-8B/14B 和 Qwen3.5-35B-A3B 上后训练。WEFT-8B/14B 在 BFCL V4、τ2-Bench、Claw-Eval 上超过所有同规模环境扩展基线；WEFT-14B 相对 Agent-World-14B 分别高 6.41/2.23/12.27 pp。固定任务和 rollout 预算下，三轮自进化将 tool-error rate 从 1.76% 降到 0.96%（相对 -45.5%），三个 benchmark 平均提升 3.65–5.25 pp。prefix-preserving sampling 在 Toolathlon-Verified / AutomationBench 分别 +1.85/+2.17 pp；atomic-turn GRPO 避免 trajectory-level GRPO 在 τ2-Bench 上的回退。MegaMCP 减少 sandbox upload 95.5%、内存 77.6%–95.7%、首个 tool call 中位延迟 54.1%。

### 最值得记住的一句话
用执行经验同时做策略学习数据和交互系统改进的证据，才能获得可靠学习信号；扩展工具使用后训练是系统问题，不是简单增加环境数量。
