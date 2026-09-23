---
title: 'Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable
  Specialist Agents'
title_zh: 让 harness 成长而非上下文：从无策略脚手架到可复用专家智能体
authors:
- Laizhen Li
- Jiarui Li
- Juanjuan Zhao
- Kejiang Ye
- Ye Li
- Cheng-zhong Xu
- Xitong Gao
affiliations:
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Shenzhen University of Advanced Technology
- University of Macau
arxiv_id: '2609.26760'
url: https://arxiv.org/abs/2609.26760
pdf_url: https://arxiv.org/pdf/2609.26760
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent harness 自动增长优化
tags:
- Agent Harness
- Failure-Guided Learning
- Context Efficiency
- Program Synthesis
- LLM Agents
- Cost Reduction
one_liner: 通过任务反馈把重复控制固化为可执行代码，LLM仅做语义推理，实现低成本高成功率Agent
practical_value: '- 把高频控制路径（query 改写、结果校验、状态机流转、停止条件、重试策略）从 prompt/上下文固化到代码，LLM 只负责语义比较和最终生成；对电商搜索
  Agent、客服 Agent 等高频请求场景，可显著降低单次 token 与成本。

  - 建立 function-level trace 和失败窗口：线上失败日志关联到具体函数，优化器只修改被 trace 覆盖的有限代码面，避免全量重写；这能形成可维护的“局部重训练”工程闭环。

  - 引入 held-out gate 与 checkpoint 回滚：每个修复候选必须在固定验证集上不降低成功率才接受，防止修复当前 case 导致历史能力退化；持续优化推荐策略或
  Agent 逻辑时尤其关键。

  - 小模型部署友好：将可复用控制移到代码后，4B 模型在 WebArena-Verified 上成功率达到 45.3%，而 Tool-Calling 只有 6.7%；端侧或低成本电商/搜索
  Agent 可优先采用代码 harness 而非依赖大模型在线规划。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
LLM Agent 反复处理同一任务族时，每次都在上下文里重新构建相同的控制决策：query 精炼、观察过滤、进度校验、错误恢复、停止判断等。这带来大量重复推理调用、上下文膨胀，并让小模型在线规划能力成为瓶颈。如果能把可复用控制固化为可执行代码，让 LLM 只做任务相关的语义推理，就能显著降低推理成本并提升小模型可用性。

**方法关键点**
- 从 **strategy-free scaffold** 起步：只暴露固定 LLM 和工具接口，不预设 ReAct 等控制器。
- **失败驱动训练**：维护失败窗口（大小 K），执行当前 harness 并记录 function-level execution DAG trace，将任务失败定位到参与函数。
- **trace-local 编辑**：离线优化器只能在失败 trace 覆盖的函数范围内修改或新增 helper，编辑预算 L 限制改动函数数量；确定性、可复用逻辑写进代码，保留 LLM 调用给语义解读、模糊比较和答案生成。
- **候选评估与 gate rollback**：候选在失败窗口上重执行，要求修复至少 Q 个失败；再用 held-out gate 集检验，若 gate 成功率下降则整段回滚到最近 checkpoint，防止修复当前 case 导致历史能力退化。
- 接受编辑累积在共享 harness 中，控制结构随任务反馈逐步涌现。

**关键实验**
在 BrowseComp-Plus 和 WebArena-Verified 两个基准上，用 200 训练任务、50 gate 任务、50 最终测试任务，部署模型为 gpt-oss-120b、gpt-oss-20b、Qwen3.5-4B。对比 Tool-Calling、Self-Ask、IRCoT、WebDreamer、AgentOccam。结果：6 个 benchmark-model setting 中 5 个取得最高平均成功率，另一个距最高仅差 0.7 pp；相对 Tool-Calling，LLM 调用减少 76.0–91.8%，在线成本降低 74.4–98.6%。WebArena-Verified 上，4B 小模型成功率保持在 44.7–45.3%，而 Tool-Calling 掉到 6.7%。消融：去掉 function-level guidance 成功率从 36% 降到 18%；去掉 gate validation 出现明显回归；去掉 failure-window 降低 8 pp。

**最值得记住的一句话**：在固定任务族中，把可复用控制逻辑从模型上下文迁移到可执行代码，比反复让 LLM 重新推理更高效，并且能让小模型部署保持竞争力。
