---
title: 'PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas'
title_zh: PersonaCUABench：多样化用户人设下的计算机使用智能体评测基准
authors:
- Haoming Li
- Defu Cao
- Xu Hu
- Yingtao Luo
- Yiyang Wang
- Xianghe Xu
- Jiashu He
- Wanting Jiang
- Yifan Zhang
- Yunhan Zhao
affiliations:
- The University of Texas at Dallas
- University of Southern California
- Carnegie Mellon University
- Georgia Institute of Technology
- University of California, Los Angeles
arxiv_id: '2610.22990'
url: https://arxiv.org/abs/2610.22990
pdf_url: https://arxiv.org/pdf/2610.22990
published: '2026-10-15'
collected: '2026-10-31'
category: Eval
direction: Agent 评测 · 用户多样性
tags:
- Computer-Use Agents
- Persona
- Benchmark
- Evaluation
- User Simulation
one_liner: 固定任务、仅变化用户人设，发现 CUA 任务完成率平均下降 36%
practical_value: '- 对话式推荐/购物 Agent 评测可借鉴「固定任务、仅变化用户 persona」的设计，分离任务难度与用户表达差异，避免只测固定指令。

  - 用户 simulation 中让 persona agent 用自己的话改写请求、回答追问，能暴露模型对含混需求、额外约束、批准流程的理解能力。

  - 评估指标需同时看任务完成与用户满意度/约束遵循：论文中任务完成但用户最高满意度仅 62.7%，提醒业务中不能只优化结果正确。

  - 错误分析维度「理解错需求导致失败」vs「用户要求停止但被判定失败」可帮助定位是语义理解问题还是策略/安全机制问题。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有计算机使用智能体（CUA）评测大多采用固定任务说明，但真实用户可能省略需求、添加约束、要求在关键动作前获得批准。完成任务不等于服务好用户。

**方法关键点**：PersonaCUABench 保持 74 个任务、11 个领域不变，仅改变“谁在提问”。一个 persona agent 扮演 44 个人设之一（分四组），用该用户自己的话改写指令并回答 CUA 的追问；CUA 只看到对话，看不到人设档案或原始指令。在 9 个 backbone 上共进行 3,330 次运行。

**关键结果**：相对原始请求，平均任务完成率下降 36%。丢分单元中，59.9% 是 agent 按照用户要求做了但仍做错，11.2% 是用户要求停止但评分器判为失败。即使 persona 请求被完全完成，用户给出最高满意度评分的比例仅为 62.7%，而原始请求为 84.1%。这说明 CUA 应同时评估任务完成与用户表达的约束和需求是否被满足。
