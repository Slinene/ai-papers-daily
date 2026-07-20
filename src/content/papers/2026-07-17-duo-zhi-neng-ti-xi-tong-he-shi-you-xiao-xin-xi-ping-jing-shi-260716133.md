---
title: When Do Multi-Agent Systems Help? An Information Bottleneck Perspective
title_zh: 多智能体系统何时有效？信息瓶颈视角
authors:
- Wendi Yu
- Lianhao Zhou
- Xiangjue Dong
- Sai Sudarshan Barath
- Declan Staunton
- Byung-Jun Yoon
- Xiaoning Qian
- James Caverlee
- Shuiwang Ji
affiliations:
- Texas A&M University
- Brookhaven National Laboratory
arxiv_id: '2607.16133'
url: https://arxiv.org/abs/2607.16133
pdf_url: https://arxiv.org/pdf/2607.16133
published: '2026-07-17'
collected: '2026-07-20'
category: MultiAgent
direction: 多智能体协作 · 信息瓶颈优化
tags:
- Multi-Agent Systems
- Information Bottleneck
- Single-Agent System
- LLM
- Communication Compression
- Model Capability
one_liner: 用信息瓶颈理论揭示多智能体增益源于上下文压缩与通信损失间的权衡，弱模型更难从冗余上下文中获益
practical_value: '- 在设计电商搜索推荐的多智能体架构（如多个 LLM Agent 协作进行意图解析、Query 改写、商品召回）时，需精心控制
  Agent 间传递的信息粒度：压缩冗余上下文可大幅降低 token 消耗与延迟，但必须确保传递的信息足够任务要求，避免关键信息丢失。

  - 对于能力较弱的模型（如小参数量的生成式推荐模型），采用多智能体拆分任务并传递压缩后的关键信息，效果可能显著优于单智能体全量上下文；而对于强模型，全量上下文可能已足够，多智能体引入的压缩反而可能损害性能，需针对模型规模做适配。

  - 可将多智能体通信视为一个信息瓶颈优化问题：引入一个可控的压缩率参数（类似 β），在工程实现中通过调整摘要长度、关键词提取等策略来寻找最优的压缩比，平衡效率与效果。

  - 在推荐系统中使用 Agent 协作生成推荐理由或推送文案时，每个 Agent 只向上游发送必要的结构化信息（如商品核心卖点、用户偏好标签），而不是冗长的自然语言描述，可以提升整体系统的吞吐量。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 驱动的多智能体系统（MAS）在复杂任务中表现参差不齐，其相对于单智能体系统（SAS）的优势条件尚不清晰。本文从信息瓶颈视角出发，解释何时 MAS 真正有效。

**方法**：关键洞察在于 SAS 将所有推理痕迹累积在单一共享上下文中，而 MAS 使用隔离的局部上下文，并通过有限容量的中继消息连接。首先证明，在无限中继带宽下，MAS 可以模拟任何 SAS，因此 MAS 的非平凡优势仅出现在有界中继场景。此时，压缩冗余上下文能提升效率，但也会导致任务相关信息损失，形成“压缩-损失”权衡。作者将此权衡形式化为信息瓶颈问题，引入有效参数 β，β 随模型能力变化，当上下文缩减带来的收益超过中继信息损失时，MAS 增益出现。

**结果**：在 5 个基准（包括推理、代码生成等）及 3 种模型规模（GPT-3.5、GPT-4o-mini、GPT-4o）上进行 18 组对照实验。结果显示：当中继消息近乎充足时，MAS 一致优于 SAS，尤其对弱模型增益显著；当中继信息损失增大时，强模型增益缩水甚至逆转，因为强模型已能从冗余上下文中提取有用信息，压缩反而不利。研究证实 MAS 设计本质是信息瓶颈优化，解释了有界智能体间通信的助益与损害条件。
