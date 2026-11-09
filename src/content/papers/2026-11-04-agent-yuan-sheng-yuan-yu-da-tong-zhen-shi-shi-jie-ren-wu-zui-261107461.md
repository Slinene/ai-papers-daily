---
title: 'The Last Mile to the Real World: Agent-Native Primitives as Reusable Building
  Blocks for Solving Real-World Tasks'
title_zh: Agent 原生原语：打通真实世界任务最后一公里
authors:
- Haibo Jin
- Peng Kuang
- Xiaopeng Yuan
- Lucheng Fu
- Jerry Wang
- Xucheng Yu
- Yaoning Yu
- Dehao Wu
- Runguo Li
- Colin Su
affiliations:
- University of Illinois Urbana-Champaign
- Georgia Institute of Technology
- heelo.dev
arxiv_id: '2611.07461'
url: https://arxiv.org/abs/2611.07461
pdf_url: https://arxiv.org/pdf/2611.07461
published: '2026-11-04'
collected: '2026-11-09'
category: Agent
direction: Agent-Native Primitives 与 Harness 工程
tags:
- Agent-Native Primitives
- Harness Engineering
- LLM Agents
- Tool Use
- Multi-Agent Systems
one_liner: 提出 Agent-Native Primitives 与 HEELO 框架，让资源自带应用能力，在 26 项对比和 46 个真实任务上大幅超越
  Codex/Claude Code
practical_value: '- 把业务中高频工具/API（商品查询、订单接口、投放接口）封装成 Agent-Native Primitive：资源自带 resident
  LLM，负责 schema 绑定与参数接地，调用方只传自然语言意图；这样能大幅减少主 agent 的上下文压力和工具调用错误。

  - 用按需组成的 task graph 替代固定 agent harness：每个请求只激活相关 primitives，成本随任务需求而非库规模增长，适合电商多工具、多系统场景下降低
  token 与延迟。

  - 借鉴 evidence-based revision：所有关键步骤结果都要有可验证证据（API 返回校验、测试、编译等），失败时自动定位到 implicated
  primitives 并在有限轮内局部修订，避免整体重跑。

  - 建立独立的 validation/publishing 路径：新的 primitive 或改进必须通过测试/回归才允许入库，让营销执行、订单处理、内容生成等能力沉淀为可复用资产时质量可控。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM agents 在真实任务上仍明显不足：在 Terminal-Bench 4.0 最大推理强度下，GPT-5.6 Sol + Codex 只解决 37.3% 任务，Claude Opus 5 + Claude Code 为 51.8%。核心瓶颈不是“资源不可达”，而是“最后一公里”——资源已找到但无法正确应用：工具调用要接地参数、代码要适配目标、证明方法要匹配条件、答案要忠于来源。现有做法把资源留给调用者，让每个 harness 反复重建“如何应用资源”的能力。

**方法关键点**  
- 定义 Agent-Native Primitive：每个 primitive 由可复用资源 + 常驻 LLM + 对外接口 + 消息机制组成。常驻 LLM 让资源自身具备自然语言接口、上下文应用能力，并能与其他 primitive 通信。资源可以是工具 schema-function 对、代码组件、证明方法、知识源模型、多智能体模式、控制操作等。
- 提出 HEELO 框架，包含三个机制：
  1. **库选择与组合**：通过接口检索或 primitive 自评估，按任务动态组合成 task-specific graph，只激活需要的 primitives；
  2. **基于证据执行与改进**：执行后由测试/编译/环境证据验证结果，失败时自动定位 implicated primitives，并仅修订受影响部分；
  3. **验证与发布**：新的或改进的 primitive 必须通过独立验证路径（测试、编译、开发任务等）才能入库。
- 用八个 primitive families 实例化：Tool、Code、Math、Knowledge、Agent、Dev、Navigation、Harness，覆盖工具使用、代码构建、定理证明、知识任务、多智能体、软件工程、大信息空间和 harness 工程。

**关键实验**  
- 在 26 项公开基准对比中，HEELO 全部领先各自 baseline。
- Dev-Primitives 在 Terminal-Bench 4.0 上把 Codex 的 37.3% 提升到 55.5%；Harness Primitives 在 100 个 SWE-bench Verified 任务上 Pass@1 从 73.0% 提升到 80.5%，超过 Codex 的 79.0%。
- Tool Primitives 在 ToolBench 通过率从 55.8% 提升到 75.1%；Agent Primitives 在八个 math/code/QA 基准上的平均准确率从单 agent 的 58.8% 提升到 75.3%；Math Primitives 在 Putnam hit@5 上达到 95.0%，超过最强 reranker 的 84.2%。
- 在 heelo.dev 的 46 个真实任务上，Claude Code 和 Codex 各自仅完成 9 个，接入 HEELO 后分别完成 39 和 35 个，耗时降低 1.9×/2.3×，单任务成本降低 1.55×。

**最值得记住的一句话**  
把“如何使用资源的能力”封装进资源本身，而不是让调用方每次重新学习。
