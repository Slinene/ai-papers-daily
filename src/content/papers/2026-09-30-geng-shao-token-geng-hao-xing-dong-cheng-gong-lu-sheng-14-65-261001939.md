---
title: 'Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success
  Rate but 65% Fewer Tokens'
title_zh: 更少 Token 更好行动：成功率升 14%、Token 省 65% 的机器人 Agent
authors:
- Ruiyang Si
- Jianxin Bi
- Shunyu Yang
- Rui Ni
- Wenbo Huang
- Qiang Wang
- Shulong Jiang
- Duomin Wang
- Xiuyu Li
- Haiwen Feng
affiliations:
- Peking University
- National University of Singapore
- NVIDIA
- Impossible Research
arxiv_id: '2610.01939'
url: https://arxiv.org/abs/2610.01939
pdf_url: https://arxiv.org/pdf/2610.01939
published: '2026-09-30'
collected: '2026-10-03'
category: Agent
direction: VLM Agent 代码执行与选择性观察
tags:
- VLM Agent
- Code Execution
- Selective Observation
- Token Efficiency
- Tool Calling
one_liner: PyRUA-Lean 用代码执行+选择性观察，同等调用预算下成功率 63.1%→71.7%，Token 省 65%
practical_value: '- 用 Python 代码块代替多轮 tool-calling：将多个工具调用组合成可执行 cell，包含条件判断和局部重试，减少
  LLM 往返；在电商 Agent 中可把「查询商品→筛选→比价→生成文案」编码为模板化代码，LLM 只填参数。

  - 选择性观察：不让 Agent 每次接收完整环境状态/全部候选商品，而是显式请求所需字段（价格、库存、历史行为），降低输入 token；类似 RAG 按需取上下文。

  - 局部重试机制：在代码块内处理可预见失败（API 超时、无搜索结果、价格变动）而不回传 LLM，只在需要重新规划时才调用 LLM，可显著降低调用次数。

  - 同等调用预算下提升成功率：省下的 token 可用于更多次 LLM 调用或更复杂规划，在固定成本内提升推荐/搜索效果。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：VLM 机器人 Agent 需要反复调用模型并接收冗余观察，token 开销大且成功率受限。

**方法**：PyRUA-Lean 采用交互式代码执行框架，将经典机器人原语与学习到的 VLA 策略组合成 Python cell；cell 内可执行条件检查和局部重试，只返回显式请求的图像和状态反馈用于重新规划，从而减少无效观察和不必要调用。

**结果**：在 LIBERO-PRO、RoboTwin 2.0、RoboCasa365 共 700 个仿真任务上，与使用相同 GPT-6 Astra planner 和底层原语的 tool-calling baseline 相比，在同等 LLM 调用预算下整体成功率从 63.1% 提升至 71.7%；在两者都解决的任务上，LLM 调用次数减少 49%，输入 token 减少 65%，平均成本降低 2.2 倍；长时程/多步任务提升更明显（+36.0 pp 和 +40.0 pp）。
