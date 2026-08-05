---
title: 'MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce
  Operations'
title_zh: MerchantBench：电商运营中LLM智能体长期连贯性基准
authors:
- Qiming Shi
- Yulong Tao
- Linbo Jin
- Zhaolu Kang
- Yibo Dou
- Jiawen Zhu
- Tianjun Pan
- Shaokang Fu
- Chengyu Wang
- Siyue Li
affiliations:
- Alibaba Group
- State Key Lab of CAD&CG, Zhejiang University
- School of Software Technology, Zhejiang University
- School of Software and Microelectronics, Peking University
- College of Computer Science and Artificial Intelligence, Fudan University
arxiv_id: '2607.28956'
url: https://arxiv.org/abs/2607.28956
pdf_url: https://arxiv.org/pdf/2607.28956
published: '2026-07-30'
collected: '2026-08-05'
category: Agent
direction: Agent 长期连贯性评估
tags:
- Agent
- Benchmark
- E-commerce
- Long-Term Planning
- Delayed Feedback
- Simulation
one_liner: 提出首个电商卖家长期运营模拟基准，评估LLM智能体在365天中维持连贯决策的能力，揭示LLM远逊于人类
practical_value: '- **长期模拟环境构建**：可借鉴其365天订单级模拟设定，将“供应商事件-采购-上架-定价-订单-现金流”时序闭环用于训练或评估搜推广场景中的Agent，尤其适合需要多步决策且反馈延迟的任务（如选品、动态定价）。

  - **决策依赖与现金流的约束设计**：采购、定价、现金流之间形成硬性依赖，当前行为会影响未来选择空间，这对设计推荐Agent的“预算受限序列决策”有很大启发，例如广告竞价中的预算分配与出价调整。

  - **混合延迟反馈的处理框架**：MerchantBench区分上游即时事件与下游延迟订单结果，这种双通道反馈模式可复用于搜索推荐系统，帮助Agent学会在延迟转化数据下的自适应策略。

  - **评估指标与人类对照**：用最终净资产等累计指标衡量长期连贯性，并引入人类基线，这种做法可迁移到业务Agent评测中，避免仅看短期收益忽视长期效果，从而设计更鲁棒的线上评估体系。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM智能体评测多聚焦于有限步数的即时成功任务，而真实电商运营需要长期连贯性——在跨越多天的时间跨度内保持目标导向行为，同时根据累积证据动态调整决策。卖家侧运营涉及产品采购、上架定价、现金流管理、延迟反馈适应等环环相扣的序列决策，天然适合评估长期连贯性。

**方法**：构建MerchantBench，基于98843条真实商品记录，模拟365天订单级卖家经营环境，提供26种操作工具。环境包含即时可观测的上游供应商事件（如补货提醒）和延迟到达的下游订单成果（如客户收货付款），强制Agent跟踪订单生命周期并回溯早期决定。实验评测8个主流LLM在两类Agent框架下的表现，共48次运行，并与人类参与者的平均表现对比。

**结果**：目前最强LLM配置的最终净资产均值仅为人类参与者的27.3%，揭示出LLM在处理需要长期记忆、约束推断和动态规划的连贯决策任务上存在巨大短板。
