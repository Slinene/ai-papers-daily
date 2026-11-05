---
title: 'ServerBench: How can your coding agents design specialized LLM serving systems?'
title_zh: ServerBench：编码智能体设计专用 LLM 服务系统基准
authors:
- Xinrui Zhong
- Zhiming Wang
- Yongqi Liu
- Zhaohui Wang
- Shanglin Yang
- Zikun Li
- Zhuoming Chen
- Beidi Chen
affiliations:
- Carnegie Mellon University
- University of Southern California
arxiv_id: '2611.06841'
url: https://arxiv.org/abs/2611.06841
pdf_url: https://arxiv.org/pdf/2611.06841
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: Agent 自动设计 LLM 服务系统评测
tags:
- LLM serving
- coding agents
- benchmark
- stateful replay
- cost efficiency
- verification
one_liner: 提出 ServerBench 基准，让编码智能体以每 GPU 美元时延合格 token 价值为目标，自动设计并验证专用 LLM 服务系统
practical_value: '- 可借鉴“单一经济指标 + 实验反馈 + 独立验证”的闭环：将推荐/广告在线服务优化（动态 batching、KV cache、模型路由）交由
  coding agent 迭代，把业务目标形式化为“每 GPU 美元的有效 token/曝光价值”，快速探索设计空间。

  - Stateful replay 思想：服务评测中构造带 session 依赖的请求序列，比无状态压测更能暴露延迟、缓存与调度问题；推荐系统做流量回放或在线仿真时，加入用户行为序列依赖可更真实评估收益。

  - 验证 agent 生成的代码/策略必须覆盖优化引入的新执行路径（如 speculative decoding、选择性负载丢弃），防止局部指标好但正确性受损；对应推荐
  Agent 产出策略代码后需加独立验证模块。

  - 让 agent 针对 workload-relevant 实验（如电商大促突发流量）解读反馈，可引导其协调容量提升与负载选择，产出高价值服务设计。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM coding agents 能通过反复实验开发软件，但设计支撑其自身运行的 LLM serving 系统需同时满足 session 依赖、延迟约束与正确性；现有评估缺乏统一目标。

**方法关键点**：ServerBench 设定统一目标“dollars per dollar”——每美元 GPU 成本获得的时延合格 token 价值。它通过 stateful replay 保留会话依赖，并用 independent verification 独立验证提交系统。Agent 需完成实现与运行决策，而非仅生成代码。

**关键结果**：在 11 个 coding-agent 模型、3 种部署上，Claude Sonnet 5.5 在 Gemma E4B 上达到 2.97 dollars per dollar，是 vLLM 参考的 4.87 倍；33 次运行中 22 次产出可验证系统，13 次超过最强基线。分析发现：高价值设计会协调容量提升与负载选择；agent 通过 workload-relevant 实验解读反馈；可靠交付需要验证优化引入的执行路径。
