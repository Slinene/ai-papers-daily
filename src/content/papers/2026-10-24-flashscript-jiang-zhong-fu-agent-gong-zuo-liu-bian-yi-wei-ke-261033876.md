---
title: 'FlashScript: Compiling Recurring Agent Workflows into Reusable Neuro-Symbolic
  Programs'
title_zh: FlashScript：将重复 Agent 工作流编译为可复用神经符号程序
authors:
- Sadra Sabouri
- Hosein Hasanbeig
- Adam Sage
- Shreya Sinha
- Cale Darling
- Ashish Tiwari
- Katie Garms
- Souti Chattopadhyay
- Sumit Gulwani
affiliations:
- University of Southern California
- Microsoft
arxiv_id: '2610.33876'
url: https://arxiv.org/abs/2610.33876
pdf_url: https://arxiv.org/pdf/2610.33876
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: Agent 轨迹编译为可复用神经符号程序
tags:
- Neuro-Symbolic Programs
- Agent Workflows
- Program Synthesis
- Consistency
- Recurring Tasks
- LLM Calls
one_liner: 把成功 Agent 轨迹固化为代码加局部 LLM 调用的神经符号程序，实现一致、可泛化且低成本复用
practical_value: '- 高频运营/数据工作流（周报、选品监控、广告复盘、搜索 query 改写评估）可以先跑通一次，再用 FlashScript 思路固化：工具操作写死为代码，只有模糊判断（如“是否作弊”“是否敏感词”“是否价格异常”）保留为
  `llm<T>` 调用；后续执行一致，token 成本大幅下降。

  - 三层划分可直接迁移到推荐/Agent pipeline：输入层做非结构化请求到结构化参数的映射，计算层把阈值/规则判断写成代码，输出层只做文案渲染；这能显著减少
  LLM 调用次数，适合构建低延迟线上服务。

  - 三个降本技巧可直接复用：caching 观测值 + guard（已知类目 ID 直接用缓存，新类目才问 LLM）；codifying 把可规则化的审核/过滤写成正则或阈值；clubbing
  把多个独立判断合并成一个 LLM 请求或并行调用，适合批量处理商品/内容理解。

  - 如果业务里要让 Agent 重复执行某类任务，优先要求它生成可执行的 NSP，而不是 skill 提示；NSP 的可测试性更强，能把 symbolic shell
  与 neural calls 分开做单元/回归测试，便于上线和运维。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
Agent 在重复任务中每次从自然语言请求重建过程，导致轨迹、输出不稳定，且消耗大量 token 和时间。已有 skill 或经验指引仍让模型重新解释指导，无法保证一致；编程演示方法又泛化差。需要一种能把成功过程固化为可复用、可测试、低成本且可泛化的程序表示。

### 方法关键点
FlashScript 将完成后的 agent trajectory 编译为 neuro-symbolic program（NSP）。核心做法：
- 动作与数据变换变成 Python 代码；实例相关值参数化；需要模型判断的决策变成类型化 `llm<T>` 调用，返回类型 T 并在固定代码位置执行。
- 按信息流划分三层：input 层（非结构化词到类型化值，如 “L.A.” 映射到 sheet name）、computation 层（规则难表达的语义判断，如是否 scam）、output 层（把代码结果转自然语言）。
- 三种降本技术：caching 保存观测值并由 guard 决定复用或回退 LLM；codifying 把可重复判断写成正则/阈值规则；clubbing 合并独立问题为一次或并行调用。
- 非确定性没有被删除，而是被局部化，使确定性 shell 与 neural calls 可分开测试和维护。

### 关键实验
在 WorkBench 120 个 analytics 任务、Claude Haiku 4.5 上对比 vanilla agent 和 skill-guided agent。NSP 正确率 1.00，三次运行 tool calls 完全一致，输入 token 约从 21,986 降到 21（约 70 倍），runtime 约从 4.3-4.4s 降到 1.5s。组合任务中 skill-guided agent 正确率降到 23%，NSP 仍 100%；108 个未见实例 NSP 全部正确。生成时用模板+参考运行（R+T）效果最好，仅用轨迹会在组合任务掉到 0.53。

### 最值得记住的一句话
把成功 agent run 固化成“代码 + 受控 LLM 调用”的程序，是重复工作流实现一致性、泛化和低成本复用的关键。
