---
title: Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents
title_zh: 工具智能体的轨迹级推测与语义验证
authors:
- Zilin Wang
- Yinhong Liu
- Chao Chen
- Qun Liu
- Zhijiang Guo
affiliations:
- LARK, HKUST (GZ)
- Yinwang
- University of Cambridge
- HKUST
arxiv_id: '2610.21463'
url: https://arxiv.org/abs/2610.21463
pdf_url: https://arxiv.org/pdf/2610.21463
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 弱-强模型协作与推测执行
tags:
- speculative execution
- tool-using agents
- weak-strong collaboration
- semantic verification
- prefill
- latency reduction
one_liner: 让弱模型草稿执行只读工具调用，强模型在不可逆动作前一次性 prefill 验证并修复，用验证替代逐步解码
practical_value: '- 在电商客服/订单处理 Agent 中，把工具调用分为只读查询和状态变更：订单查询、库存查询、读用户记录等只读步骤可以由 4B
  小模型草稿并立即执行；退款、改单、发 push 等写操作由大模型在提交前一次性验证，大幅降低大模型调用次数。

  - 验证时用语义接受而非 exact match：不要求小模型步骤与大模型自己生成的一致，只判断该步骤是否朝任务目标有效推进。推荐/搜索 Agent 中，query
  改写、工具参数选择可以有多种有效路径，这样能保留小模型的有效进展，避免无谓重生成。

  - 工程上把验证 prompt 设计成只输出短 verdict：接受前缀长度 + 替换动作 + 理由，让大模型只解码少量 token 而不是逐步生成动作；融合
  replacement action 能减少额外修复调用。

  - 适合 memory-bandwidth-bound 的线上 serving：节省主要来自用一次 prefill 读取整段草稿替代逐个 token 解码，HBM-read
  和 wall time 下降 40-50%；在云-端部署中可显著降低云端 output tokens 和 API 成本。注意如果小模型太弱、acceptance
  rate 过低，repair 次数会上升，节省消失，上线前需离线评估 weak-only 能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

LLM Agent 完成任务需要几十到上百轮工具调用，主流设计让一个强模型生成每一步，服务成本随轨迹长度线性增长，且大模型逐步解码是 memory-bound 的。但很多步骤是例行的只读操作，小模型也能胜任。现有弱-强协作方法要么让强模型仍然逐步生成，要么做 exact match 或 step-level critic，要求草稿与强模型自己的动作一致，太严格，会丢弃有效但不同的推进路径。

## 方法关键点

- **职责反转**：弱模型 Weak 作为 drafter，强模型 Strong 作为 reviewer，从逐步作者变为审阅者。
- **只读即执行、写操作 hold**：Weak 草稿时，只读工具调用立即执行并拿到真实 observation，在第一个状态变更动作（如改库、提交答案）前停止并 hold，保证不可逆操作前必须验证。
- **语义前缀验证**：Strong 读历史 + 草稿段做一次 prefill，输出最长可接受前缀长度 j、拒绝原因 r、可选替换动作 ~a；如果整段接受则执行 held action，否则提交前缀并执行融合的 replacement 或 fallback 修复。
- **不是 exact match**：验证器判断步骤是否朝任务目标有效推进，而非是否与 Strong 自己的选择一致。
- **成本模型**：节省来自用 prefill 替代 decoding，Strong 解码比例 R_u = (1-p)/(1-p^n) * v/d + ρ(1-p)；FLOPs 会上升，但 HBM-read 和 wall time 下降。

## 关键结果

- τ2-Bench Airline：Pass@1 86.0 vs Strong-only 86.0，HBM-read 降到 43-45%，wall time 41%；Retail：87.7 vs 88.6，恢复 89% 质量差，HBM-read 53-57%，wall time 54%。
- AutomationBench 恢复 44% 弱-强质量差，VitaBench 恢复 75%，两者 HBM-read 和 wall time 均低于 Strong-only。
- MCP-Atlas 云-端部署：三种云端强模型恢复 53-75% gap，云端 output tokens 只有 Strong-only 的 36-50%，API 成本降到 59-81%。
- FLOPs 上升 30-87%，说明节省的是 memory traffic/latency 而非 compute。

最值得记住的一句话：强模型不必逐步生成每个动作；作为审阅者，一次 prefill 验证弱模型整段草稿并只修复首个被拒步骤，能保留大部分质量，同时大幅降低内存流量和时延。
