---
title: 'ProV-Mem: Proactive Memory for Streaming Video Question Answering'
title_zh: ProV-Mem：面向流式视频问答的主动记忆框架
authors:
- Bingbing Wang
- Jing Li
- Han Gao
- Yishi Lin
- Ruifeng Xu
- Peng He
affiliations:
- The Hong Kong Polytechnic University
- Tencent Inc.
- Shenzhen Loop Area Institute
arxiv_id: '2610.23998'
url: https://arxiv.org/abs/2610.23998
pdf_url: https://arxiv.org/pdf/2610.23998
published: '2026-10-15'
collected: '2026-10-25'
category: Agent
direction: 流式视频主动问答 · 分层记忆
tags:
- StreamingVQA
- ProactiveAgent
- Memory
- VLM
- CAUC
- Training-free
one_liner: 冻结 VLM 骨干下，用三层轻量记忆解耦何时查询、说什么、是否发出，实现训练无关的主动流式问答
practical_value: '- 三层记忆架构可直接迁移到实时用户行为流监控与主动触达 Agent：将「触发时机」「生成策略」「去重发送」解耦成独立轻量层，避免每次事件都调用大模型，显著降低推理成本。

  - 冻结 VLM backbone + 外围无训练记忆模块，适合业务快速上线；用固定 prompt 先验约束生成简洁且视觉接地的内容，可类比于推荐文案、商品摘要的约束生成。

  - episodic memory 做近重复过滤对主动 push 场景尤其关键——能减少对同一用户反复推送相似商品或消息造成的打扰，提升用户体验与消息接受率。

  - CAUC 评估思路值得借鉴：在离线评估主动推荐/推送系统时，除准确率、召回外，增加对冗余、过高发送频率、过长输出的显式惩罚，更贴近真实业务收益与成本权衡。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

流式视频问答中，保留长视觉历史成本高，丢弃又会导致漏事件与重复回答。ProV-Mem 以冻结 VLM 为骨干，不进行训练，将主动决策拆成三层轻量记忆：

- temporal-trigger memory 控制何时查询骨干，并从长时间沉默中恢复；
- instructional memory 通过固定 prompt 先验引导简洁且视觉接地的生成；
- episodic memory 过滤近重复回答，决定是否发出响应。

在理想条件充分性假设下，文章推导了分解过程与全状态联合策略的分阶段近似界。评估指标上提出 CAUC，在 PAUC 基础上显式惩罚冗余、过频和过长输出。在 ProactiveVideoQA 四个场景上，ProV-Mem 在所有场景取得最佳 CAUC，在 WEB、EGO、TV 场景取得最佳 PAUC，同时保持较低的单响应推理延迟。
