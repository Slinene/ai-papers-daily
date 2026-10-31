---
title: 'Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI
  Interfaces for Language Agents'
title_zh: 匹配能力、不同行为：语言智能体MCP与CLI接口受控研究
authors:
- Zhenning Shi
- Liang Pang
- Yongqi Li
affiliations:
- The Hong Kong Polytechnic University
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2610.34298'
url: https://arxiv.org/abs/2610.34298
pdf_url: https://arxiv.org/pdf/2610.34298
published: '2026-10-24'
collected: '2026-10-31'
category: Agent
direction: Agent 接口表示与工具调用行为分析
tags:
- MCP
- CLI
- Language Agents
- Tool Use
- Interface Representation
- DART
one_liner: 在可执行能力固定时，MCP与CLI的接口表示差异显著改变智能体动作选择、失败恢复与成本，DART可修复实现层失败
practical_value: '- 工具接口设计应作为决策环境的一部分：在构建商品搜索Agent、客服Agent或推荐解释Agent时，同一组底层API用MCP
  schema还是CLI命令呈现，可能改变动作分布和任务成功率。建议针对具体模型做接口A/B测试，不要默认MCP一定优于CLI或反之。

  - 借鉴DART解耦“语义决策”与“接口表达”：当工具调用失败时，先验证语义动作是否有效，若有效则只修复参数格式化或调用语法，不重新选择动作。这种commitment-preserving修复可在不增加推理步数的情况下提升恢复率，并显著降低token消耗（最高每任务省27.1k
  token）。

  - 组件级消融定位接口敏感点：将接口分解为presentation、realization、feedback，在相同决策上下文下做因子实验，可快速定位是schema描述、解码协议还是错误反馈导致行为漂移，指导工程化接口优化。

  - 交互轨迹的早期分歧会传播：在线Agent系统中，早期接口诱发的细微动作差异可能通过历史状态放大，最终导致任务失败或成本剧增。可通过配对轨迹分析识别高风险决策点，设置针对性干预或缓存策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有工具使用研究多关注工具集或scaffolding差异，未在能力匹配下隔离接口表示的影响。MCP和CLI是两种主流工具接口，但系统级比较混杂多个变量。该工作用受控比较回答：执行能力固定时，模型面对的表示如何改变策略。

**方法关键点**
- 引入MICA框架，从共享语义动作契约渲染MCP和CLI，共享验证、编译、执行运行时。
- 接口分解为presentation Φ、realization R、feedback Ψ，在匹配决策上下文做2×2×2因子实验，估计主效应和交互效应。
- 配对自然轨迹分析，定义首个consequential divergence t*，追踪早期分歧如何传播到后续历史和状态。
- 提出DART，将语义动作选择与接口特定实现解耦，失败时保持已提交语义动作，仅修复表达式。

**关键结果数字**
- 在ALFWorld、WebShop、ScienceWorld三个环境，六个模型（Qwen3系列、DeepSeek-v4-Flash、Gemini-2.5-Flash）上，匹配能力下MCP与CLI仍有显著性能差异：Qwen3-14B在ALFWorld上MCP比CLI低36.6分，但WebShop上高4.9分；token成本相应反向变化。
- 94.3%的配对轨迹（2004对中1889对）出现结构化分歧，且多发生在早期。
- 局部敏感分析：realization组件效应最大，如ALFWorld/Qwen3-32B上realization失败率变化达84.4个百分点；三阶交互可改变admission rate 37.8点。
- DART在六个基准-接口设置全部提升分数（+0.8到+9.0分），MCP下token成本降低最多27.1k/任务。

**最值得记住的一句话**：接口表示是智能体闭环决策环境的一部分，"怎么呈现能力"与"能做什么"同样塑造策略。
