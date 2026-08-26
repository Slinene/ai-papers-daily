---
title: 'MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks'
title_zh: MobilePA-Bench：复杂真实任务中移动规划代理的基准测试
authors:
- Yi Zhu
- Xiongwei Wu
- Qiyi Wang
- Tingyu Qu
- Jiajun Liu
- Sihan Cao
- Long Chen
- Weigao Sun
- Feida Zhu
- Yiran Zhong
affiliations:
- MAI Team
- Alibaba Token Hub
- Alibaba Group
arxiv_id: '2608.23035'
url: https://arxiv.org/abs/2608.23035
pdf_url: https://arxiv.org/pdf/2608.23035
published: '2026-08-23'
collected: '2026-08-26'
category: Eval
direction: 移动 Agent 规划评估 · 工具调用基准
tags:
- Mobile Agent
- Tool Calling
- Benchmark
- Memory
- Sub-agent
- Skill Usage
one_liner: 提出有状态、工具中心的移动规划代理基准，覆盖工具调用、子代理协作、记忆与技能四维能力
practical_value: '- 评估 Agent 工具调用时，用 **stateful sandbox** 执行真实工具并返回动态反馈，比静态字符串匹配更能暴露运行时错误（如权限拒绝、依赖顺序）。电商场景可模拟库存、订单、用户画像等实时状态，让
  Agent 在真实约束下做决策。

  - 验证阶段按证据类型分桶（**Tool Call / State Change / Agent Behavior**），不同任务用不同 checker，避免单一指标过严或过松。可迁移到电商
  Agent 评估：下单类任务看最终订单状态，推荐类任务看是否调用正确检索工具并合理追问。

  - **Memory Usage** 维度要求 Agent 必须先显式调用 `search_user_memory` 检索用户偏好/历史，再规划动作，否则 gate
  直接判失败。这启示电商个性化 Agent 应强制显式记忆检索，而不是依赖模型隐式猜测。

  - **Skill Usage** 用预打包复合技能替代原子工具逐步规划，能显著降低长程任务错误累积（Skill 分数普遍高于 Memory）。在电商中，可将“下单+优惠券+支付”“退款+库存回补+通知”等流程封装成
  skill，提升整体成功率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
当前移动端 LLM Agent 评估存在两极分化：GUI-centric 基准只测屏幕点击与像素感知，忽略后台结构化 API 调用和长程规划；静态 function-calling 基准离线匹配 API 签名，脱离真实运行时状态与异常。然而真实移动任务（如多日旅行规划）需要统一调度记忆检索、复合技能、子代理路由和工具调用，现有基准无法诊断这种复合能力。

**方法关键点**
- 构建 **MobilePA-Bench**：交互式、有状态、工具中心基准，包含 1,705 个任务、13 个功能域、212 个移动工具，运行在可执行沙箱上，维护 live application databases 并返回结构化反馈。
- 评估四个能力维度：**Basic Tool Use**（参数接地、依赖顺序、边界检测与错误恢复）、**Sub-agent Collaboration**（任务分解与上下文交接）、**Memory Usage**（检索持久化用户画像/偏好以消解隐式请求）、**Skill Usage**（调用预打包复合技能而非逐步规划）。
- 验证采用三个证据对齐的 query buckets：**Tool Call**（精确序列匹配）、**State Change**（数据库终态差异）、**Agent Behavior**（子代理路由与追问合理性），并根据任务语义固定分配。
- 动作空间统一为 function schema，候选工具使用 top-N recall（N=15），每次调用返回动态 feedback，最大步数 15，多轮函数调用执行。

**关键实验**
在 13 个前沿海量模型上评估。最佳总体分数仅 **75.52%**（Claude-Opus-5），7/13 个模型低于 70%。分维度看：Basic Tool Use 最高 83.85%（Claude-Opus-5），Memory Usage 最高 64.63%（Qwen-3.8-Max），Sub-agent Collaboration 最高 77.53%（Gemini-3.1-Pro），Skill Usage 最高 78.00%（Claude-Opus-5）。没有模型在所有维度同时领先，错误跨能力边界级联。

**最值得记住的一句话**
真实移动工作流要求记忆、技能、子代理与工具调用的复合可靠性，但当前最强模型整体成功率仅 75.52%，且各维度最强分散在不同模型——部署级可靠性仍远未达到。
