---
title: 'Mingbird: A Local-First Agent Harness Enabling Small Open Models to Complete
  Real Tasks'
title_zh: Mingbird：本地优先 Agent 框架让小型开源模型完成真实任务
authors:
- Hao Wang
- Ting Huang
affiliations:
- University of Science and Technology Beijing
- Honor Device Co., Ltd.
arxiv_id: '2610.02001'
url: https://arxiv.org/abs/2610.02001
pdf_url: https://arxiv.org/pdf/2610.02001
published: '2026-10-01'
collected: '2026-10-03'
category: Agent
direction: Agent harness 本地小模型任务执行优化
tags:
- Agent Harness
- Small Open Models
- Tool Use
- Loop Detection
- Prefill Budget
- Local-First
one_liner: Mingbird 通过十项机制补偿小模型故障，在 LRAB 与 τ²-bench 上显著超过 goose/opencode/agent-mini
practical_value: '- 小模型做工具调用时，优先治理 prefill 预算而非只靠模型截断：可把工具 schema 压缩到字节级配额，尤其适合端侧或低延迟搜索推荐
  Agent。

  - 在 Agent 完成提交前增加“重读任务/用户 query”的 finish gate，能减少静默放弃与提前结束；可用于多轮 query 改写、推荐解释生成等需可靠终止信号的场景。

  - 采用签名级 loop detection 监控工具调用序列（函数名+参数模式），而不是文本相似度，能更快终止无效循环，节省 token 与延迟。

  - 若业务有隐私或成本限制，可考虑 2-9B 本地模型 + 强 harness 做降级链路，通过工程补偿换取小模型可用的任务完成率，而非直接升级大模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：2-9B 开源模型在笔记本可运行，但在云规模 agent harness 下常因工具 prefill 撑爆上下文、自我纠错发散、工具演示循环、静默放弃任务而失败。对照实验和第三方基准显示，相当一部分失败源自 harness 而非模型本身。

**方法关键点**：Mingbird 是面向 Windows 和 Ollama 的本地优先 agent harness，含 10 个机制逐点补偿小模型故障。代表机制包括字节级 net-zero prefill budget——对工具预填充做净零字节预算；finish gate——接受完成前重读任务；签名级 loop detection——按工具签名检测循环调用。

**关键结果**：LRAB 受控比较固定机器、模型、预算和评分（4 harness × 4 开源模型 2B-35B × 18 真实任务），Mingbird 总分为 0.886，对照 goose 0.631、opencode 0.479、agent-mini 0.405，全部 288 个 cell 公开；τ²-bench 278 任务总分 0.856，对照 0.791 和 0.737；前沿模型探针同任务跨 harness 从 0.997 到 0.478。消融显示同夜复现波动最高 0.069，full stack 相比仅 text re-read 的完成守卫配对 +0.10。
