---
title: Omni-Streaming Thinking
title_zh: 全模态流式思考：跨模态证据校验与反驳更新
authors:
- Enjun Du
- Siyi Liu
- Ziyu Zheng
- Jingyu Li
- Yiwen Guo
- Yongqi Zhang
- Difan Zou
affiliations:
- The University of Hong Kong
- The Hong Kong University of Science and Technology (Guangzhou)
- LIGHTSPEED
- University of Sussex
- Independent Researcher
arxiv_id: '2609.15128'
url: https://arxiv.org/abs/2609.15128
pdf_url: https://arxiv.org/pdf/2609.15128
published: '2026-09-13'
collected: '2026-09-15'
category: Multimodal
direction: 流式全模态推理与证据核查
tags:
- Streaming Multimodal
- Evidence Verification
- Hallucination Reduction
- Audio-Visual Reasoning
- Answer Gating
one_liner: 通过待定声明、分模态证据校验与反驳更新，缓解流式全模态模型过早跨模态固化，5个基准平均相对提升超10%
practical_value: '- 在直播电商、视频客服、实时内容审核等流式多模态场景中，可借鉴「pending claim + verification interval」机制：先对用户意图或商品属性打待定标签，绑定未来验证窗口，到期用指定模态证据校验，避免视觉线索过早固化为事实。

  - 多模态 RAG / Agent 记忆管理可分离存储不同模态证据，对每个 claim 指定验证模态，防止视觉信息覆盖音频等冲突信号，降低幻觉和错误推理。

  - 引入 answer gate：仅当关键 claim 通过验证后才允许输出回答，可迁移到实时推荐/对话助手的置信度控制，减少过早错误推荐。

  - 冻结大模型骨干 + 轻量适配即可获得显著流式全模态推理提升，适合业务方低成本复用 Qwen-Omni 等开源骨干。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：流式全模态模型需从已观察到的视频块和同步音频中决定何时回答。视觉证据常先于语音事件成熟，导致模型过早把视觉解释固化为事实，后续音频出现矛盾时仍沿用错误认知，作者称之为「premature cross-modal commitment」。

**方法关键点**：OST 生成结构化输出，包含已观察证据、未来证据预测和基于证据的声明。每个声明初始标记为 pending，并绑定未来验证区间；音视频证据分开存储，到期后从指定模态核对声明。检测到矛盾时，反驳过程降低该声明及其依赖状态的影响，并用新证据更新状态。最后通过 answer gate 判断回答关键声明是否满足置信条件。方法基于冻结的 Qwen3-Omni-30B-A3B-Instruct 骨干，仅做轻量适配。

**关键结果**：在 5 个流式与音视频基准上，OST 比最强开源基线平均相对提升超过 10%。新提出的 OST-DiagBench 固定视频、编辑音频以测试一致、缺失、矛盾、共存和字幕语音冲突，OST 达到 d'=2.95，开源基线最高为 1.38，同时减少视觉诱发的听觉幻觉。
