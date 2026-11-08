---
title: 'VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents'
title_zh: VisSearch-Bench：评估多模态智能体的长程视觉搜索
authors:
- ZhengXian Wu
- Qianhao Nie
- Zhuohong Chen
- Junjie Gao
- Yuyao Zhang
- Yunyao Yu
- Hangrui Xu
- Cheng Cheng
- Guiyu Ma
- Jin Zhang
affiliations:
- Tsinghua University
- Ant Group
- Renmin University of China
arxiv_id: '2611.04894'
url: https://arxiv.org/abs/2611.04894
pdf_url: https://arxiv.org/pdf/2611.04894
published: '2026-11-02'
collected: '2026-11-08'
category: Eval
direction: 多模态 Agent 视觉搜索基准与评估
tags:
- VisSearch-Bench
- Multimodal Agents
- Visual Search
- Benchmark
- Long Horizon
- Process Score
one_liner: 提出 VisSearch-Bench 基准，用 204 个人工任务评估多模态 Agent 的视觉上下文管理与跨图像搜索能力
practical_value: '- 引入 Process Score 评估中间检索结果和子问题答案，而不仅看最终准确率，能更细粒度定位多模态 Agent 在视觉搜索中的上下文断裂点；电商商品搜索中可借鉴该思路，对「找相似款」「局部细节匹配」「空间关系筛选」等中间步骤单独评分。

  - 任务类型覆盖集合式视觉搜索、顺序视觉搜索、混合广深搜索、竞争视觉消歧、视觉结构引导搜索，这些可以直接映射到电商场景：从候选商品集合中找目标、跨多级详情页追踪信息、在相似商品中消歧、按版面/位置结构定位卖点。

  - 每个任务提供可追溯证据和评分规则，便于回归测试与调试；业务中构建多模态搜索 Agent 时可以引入类似可追溯链路，记录每一步图像/文本证据，避免 Agent
  仅靠文本检索偏离视觉目标。

  - 结果提示即使接入搜索工具，多模态模型仍难将视觉证据与搜索结果完整链接；建议在 Agent 状态中显式维护视觉上下文，而不是仅在初始阶段识别实体后完全转向文本检索。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有多模态 Agent 搜索任务中，图像大多只用于初始实体识别，后续依赖文本检索，无法反映跨图像、对象和搜索步骤的视觉信息组织与关联能力。论文聚焦「视觉上下文管理」，即如何在长程搜索中持续使用视觉信息并与其他发现关联。

**方法关键点**：构建 VisSearch-Bench，包含 204 个人工编写任务，跨越 7 大领域、25 个子域，覆盖五类任务：集合式视觉搜索、顺序视觉搜索、混合广深搜索、竞争视觉消歧、视觉结构引导搜索。每个任务配有参考答案、可追溯证据和评分规则。评估采用两个指标：Accuracy 衡量任务完全解决比例；Process Score 衡量中间结果和子问题答案的正确性与完整性。

**关键结果**：在 16 个多模态模型上测试，包括直接回答和接入 ReAct、DeerFlow 搜索框架的 Agent 配置。最好系统仅完全解决 26.47% 的任务，平均准确率约 8.58%。即使使用搜索工具，模型仍难以将视觉证据与搜索结果有效链接以产生完整答案。
