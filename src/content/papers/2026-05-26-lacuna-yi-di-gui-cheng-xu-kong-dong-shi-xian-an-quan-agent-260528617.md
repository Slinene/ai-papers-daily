---
title: 'LACUNA: Safe Agents as Recursive Program Holes'
title_zh: LACUNA：以递归程序孔洞实现安全 Agent
authors:
- Yaoyu Zhao
- Yichen Xu
- Oliver Bračevac
- Cao Nguyen Pham
- Frank Zhengqing Wu
- Martin Odersky
affiliations:
- EPFL
arxiv_id: '2605.28617'
url: https://arxiv.org/abs/2605.28617
pdf_url: https://arxiv.org/pdf/2605.28617
published: '2026-05-26'
collected: '2026-05-29'
category: Agent
direction: Agent 编程模型与安全执行
tags:
- agent
- programming model
- type safety
- code-as-action
- prompt injection
one_liner: 提出一种 Agent 编程模型，将动作封装为类型化调用，LLM 填充代码并执行前类型检查，兼顾表达力与安全
practical_value: '- **工具调用的类型约束**：在电商多 Agent 系统中，可为搜索、推荐、广告等工具定义输入输出类型，Agent 生成调用代码时进行静态检查，防止越权或错误调用，尤其适合
  prompt 注入风险高的场景。

  - **原子执行与状态回滚**：借鉴 all-or-nothing 语义，当 Agent 执行多步推荐逻辑（如更新用户画像、调用推荐 API、写入缓存）时，若某一步失败则整体回滚，避免残留脏状态，保障推荐链路一致性。

  - **编译诊断驱动的重试机制**：LLM 生成的动作代码若类型不匹配，可将编译器错误信息反馈给模型进行针对性重试，比盲目重试更高效，可直接用于现有 Agent
  框架的容错改造。

  - **将高级 Agent 模式融入控制流**：ReAct、子 Agent、技能组合、并行分解等模式被表达为普通程序结构，开发者可直接用编程语言描述复杂工作流，LACUNA
  原语作为安全嵌入点，降低实现复杂度并保证安全。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前 LLM Agent 采用代码作为行为，但运行时与模型生成的代码存在割裂——运行时控制循环、上下文和流程，模型无法改变。若让模型代码塑造运行时，虽能提升表达力，但会放大 prompt 注入、错误工具调用、部分失败留下不一致状态等安全问题。

**方法**：LACUNA 是一种 Agent 编程模型，将每个 Agent 动作建模为类型化调用 `agent[T](task)`。执行到达该调用时，LLM 被要求填充代码，随后填入的代码需通过周围程序的类型检查，确保动作整体被接受或拒绝，拒绝时环境不受影响，编译器诊断用于驱动重试。类型检查同时限制了动作可用的工具和数据流。该原语可将 ReAct 循环、子 Agent、技能、并行分解和多模型规划等表达为普通控制流。

**结果**：在 BrowseComp-Plus 上，8.6% 的生成在执行前被拒绝，平均每查询 0.7 次重试，准确率 27.1%；在 τ²-bench 的 4 个领域 392 个任务中，LACUNA 用强模型解决 76.0%，与普通基线持平，同时提供了安全保证。
