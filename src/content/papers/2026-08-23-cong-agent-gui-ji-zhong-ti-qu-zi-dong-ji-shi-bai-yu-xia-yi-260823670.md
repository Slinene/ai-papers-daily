---
title: 'Automata from Agent Traces: Failure and Next-Step Prediction'
title_zh: 从 Agent 轨迹中提取自动机：失败与下一步预测
authors:
- Seonglae Cho
- Franklin Cardenoso Fernandez
- Umar Mohammed
- Zekun Wu
- Kleyton Da Costa
- Ilham Wicaksono
- Adriano Koshiyama
affiliations:
- Holistic AI
- PUC-Rio
- University College London
arxiv_id: '2608.23670'
url: https://arxiv.org/abs/2608.23670
pdf_url: https://arxiv.org/pdf/2608.23670
published: '2026-08-23'
collected: '2026-08-27'
category: Agent
direction: Agent 行为 FSM 抽象与监控
tags:
- LLM agents
- finite state machine
- failure prediction
- next-step prediction
- runtime monitoring
- workflow memory
one_liner: 用紧凑确定性 FSM 统一 LLM Agent 的工作流记忆、下一步预测、失败预测与运行时监控
practical_value: '- 将电商客服/购物助手 Agent 的 tool-call/action 序列直接抽成 FSM（状态=最近 activity），即可获得紧凑行为拓扑，用于实时检测循环和异常状态，无需复杂
  ML 模型；活动抽取用默认 role-type 粒度即可，对结果鲁棒。

  - 把 FSM 状态作为 LLM 的轻量上下文：只给当前状态的转移概率 + top-15 后续 continuation，而不是完整 workflow 列表，能提升下一步动作预测（对
  AWM 平均 +12.9pp）。在推荐/搜索 Agent 中可将用户意图-工具调用序列压缩为状态，作为 prompt 背景。

  - 失败预测用 per-state 特征（访问频率、消息长度、错误率、时序）+ FSM cross-entropy 异常特征（trace CE、max surprise
  等），梯度提升树即可达到 AUROC 0.94；对安全标注均衡的数据集（如 ATBench）稳定。可用于电商推荐 Agent 的在线失败预警。

  - 在线监控用 cycle-rate（prefix revisits / step）阈值，简单高效；设置高精度操作点可实现 100% precision、零误报的提前终止，在客服流程中节省算力并避免糟糕体验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM-based agents 执行多步任务，但行为结构不透明：长非结构化轨迹难以支撑安全审计和运行时监控。现有方法要么逐轨迹分析、要么只看成功样本，丢失了跨运行拓扑，无法同时支持下一步预测和失败预测。论文从 inverse problem 角度，将整个 trace corpus 压缩成一个紧凑的有限状态机（FSM），作为 LLM agent 行为的结构基座。

**方法关键点**  
- 通过 activity extraction 将每条轨迹映射为活动序列（tool calls、action tags、command extraction），得到小字母表（6–42 个符号）。
- 构建 prefix tree，再按 last-activity right congruence 合并所有由同一活动到达的状态，得到 deterministic FSM，状态数 = |A|+1；过滤观察次数为 1 且非唯一后继的 rare transitions。
- 构建完全无超参数、线性时间、确定性（同一语料唯一 FSM）。
- 同一 FSM 支撑四类任务：① 下一步预测：FSM 状态条件转移概率；② 失败预测：per-state 行为特征 + cross-entropy 异常特征 + 梯度提升树；③ 作为 LLM 的 workflow memory：只提供当前状态转移概率和 top-15 continuations 的 minimal format；④ 在线监控：cycle-rate 阈值监测。

**关键结果**  
在 12 个公开数据集上，FSM 仅 7–43 states，测试 replay fitness ≥0.997，构建 1–110 ms，相比 RPNI 压缩 15–3,036×。下一步预测：FSM-state 条件比 Unigram 降低 62% CE（0.93 bits avg）；FSM-LR-K7 达 0.729 bits。FSM 作为 LLM 上下文在 8/8 数据集上击败 Agent Workflow Memory，held-out 平均 +13.1pp top-1。失败预测：per-state 特征 held-out AUROC 最高 0.94（tau2-telecom）；50% 完成度时保留 92% 最终 AUROC；在线监控在 SWE-agent 上 32% 完成度触发 early stopping，省 68% 计算，precision 85.9% / recall 95.5%。跨模型迁移：单 FSM 在 4 个 chat models 上 perfect fitness，failure features 平均 cross-AUROC 0.786。

**最值得记住的一句话**  
LLM agent 的行为拓扑主要由部署 harness（system prompt、tools、task distribution）决定，而非 LLM 本身；一个紧凑确定性 FSM 即可作为统一的结构基座，同时支持工作流记忆、下一步预测、失败预测与运行时监控。
