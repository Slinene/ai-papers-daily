---
title: 'Ask the Tool, Don''t Guess: Agent Tool Calls Hold Their Progress, and the
  Serving System Should Read It'
title_zh: 工具调用进度自报：Agent 服务系统应读取而非猜测
authors:
- Yipeng Liu
- Yingqiang Zhang
- Feifei Li
- Huanchen Zhang
affiliations:
- Tsinghua University
- Alibaba Cloud Computing
- Zhejiang University
arxiv_id: '2609.18849'
url: https://arxiv.org/abs/2609.18849
pdf_url: https://arxiv.org/pdf/2609.18849
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent 工具调用 · KV cache 调度
tags:
- Agent
- Tool Call
- KV Cache
- Serving
- Progress Reporting
- TTFT
one_liner: 让工具调用上报剩余进度，比预估算更准，可将 p90 TTFT 降低约 20%
practical_value: '- 在电商/搜索 Agent 中，对长耗时工具（SQL 查询、库存 API、商品爬虫、订单处理）增加 progress 上报字段，如剩余比例或“即将完成”信号，服务层可用它做
  KV cache 驱逐/恢复决策，而不是靠工具名或历史均值猜时长。

  - 工程实现上，progress 信号通过 harness 旁路采集，不改变 Agent 可见的输入输出，对 benchmark 分数无损耗；这可以直接迁移到现有多
  Agent 编排框架，无需修改模型 prompt。

  - 在推理引擎侧，把工具 progress 作为轻量 hint 接入 KV cache 管理，作者在 LRU 上仅做小改动就接近 oracle，说明该信号比复杂预估器更有投产价值；如果业务受
  TTFT p90 波动困扰，可优先采工具真实进度而非加预测模型。

  - 进度信号在环境变化时仍然准确，适合电商大促、突发流量等场景；对多租户 GPU 资源调度，长工具调用按真实剩余时间释放/保留缓存，能提升 HBM 利用率。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**
Agent 请求在等待工具执行时占用 GPU 的 KV cache，而服务系统需要决定这些缓存是保留、逐出还是回迁。现有做法依赖工具名、历史时长、调用前声明时长或引擎负载来猜测工具运行时间。作者发现，调用开始前固定预估无法得知真实时长，甚至连调用之间按耗时排序都做不到。与此同时，运行中的工具其实已经掌握自身进度，但 Agent 栈与工具本身没有暴露这个信号。

**方法关键点**
提出让工具调用在运行中显式上报进度，并测量可获取性。对四个公开 Agent 语料的普查显示，多数工具时间中存在可读信号，分为两类：剩余工作比例，或接近结束的准确提示。一个 harness 在不改变 Agent 所见内容的前提下恢复这些信号，对 benchmark 分数没有可测影响。在 KV cache 需要决策的时间点，上报的进度比已发表的最好预估器准确数倍至一个数量级，且在环境变化时保持稳定。将进度信号以少量 hints 形式接入生产推理引擎，用于 KV cache 管理。

**关键结果**
相对 LRU，基于工具进度的方法将工具调用后的 p90 time-to-first-token (TTFT) 降低 20.7%（仅 HBM）和 20.8%（HBM + DRAM），接近 oracle 性能。
