---
title: 'Cleo: A Transparent and Controllable Chatbot for Conversational Commerce'
title_zh: Cleo：面向对话商务的透明可控聊天机器人系统
authors:
- Kevin Schott
- Jan Lattenkamp
- Daniel Hienert
- Dagmar Kern
affiliations:
- GESIS – Leibniz Institute for the Social Sciences
arxiv_id: '2608.06068'
url: https://arxiv.org/abs/2608.06068
pdf_url: https://arxiv.org/pdf/2608.06068
published: '2026-08-06'
collected: '2026-08-07'
category: RecSys
direction: 透明可控的对话式推荐系统
tags:
- Conversational Commerce
- Hybrid Architecture
- Transparent Ranking
- LLM
- Decision Support
- Explainability
one_liner: 通过混合架构分离确定性排序与 LLM 生成，实现可审计的产品推荐与决策支持。
practical_value: '- **混合架构的解耦设计**：将排序逻辑与对话生成严格分离，Ranker 执行确定性多属性过滤与损失计算，LLM 仅负责结构化需求抽取和自然语言响应，可有效防止
  LLM 幻觉或劝说性内容影响推荐结果。电商场景中可直接复用该架构，在保持对话流畅性的同时确保推荐可靠可控。

  - **可审计的透明排序**：通过暴露每个属性的损失值（price/RAM/storage/screen size）和整体评分，用户可点击“为什么这样排序”查看详细解释。这为推荐系统中的算法透明度与可解释性提供了低门槛实现思路，可直接作为功能模块嵌入商品推荐对话界面。

  - **结构化需求抽取与后处理**：用 LLM 进行需求槽位抽取（JSON 输出），配合规则化的单位换算、离散值对齐和非法过滤，显著提升抽取鲁棒性。在电商对话搜索、智能客服中可参考该管线，降低
  LLM 输出不可控带来的风险。

  - **比较与亮点功能的约束生成**：多产品对比和单产品亮点均先用规则计算指标差异，再交由 LLM 格式化输出，避免生成虚假规格。对于需要展示商品对比或卖点总结的推荐场景，这是一种低成本高效率的幻觉防御手段。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：对话式商务中，LLM 存在不透明、难以预测、易产生幻觉或劝说性内容等问题，同时用户在多属性商品（如笔记本电脑）的对比决策中面临认知负荷。现有方案要么是缺少对话能力的传统分面搜索，要么是黑箱的端到端 LLM 推荐器。本文致力于在对话流畅性与算法透明度之间取得平衡。

**方法关键点**：
- **混合架构**：管理层（Conversation Manager）协调 AI Manager 与 Ranker。Ranker 执行确定性排序，AI Manager 负责结构化需求抽取和约束生成，二者严格解耦。
- **需求抽取**：用 LLM 将用户自然语言转为 JSON 结构化需求（如 "casual gaming" → {"gpu": "dedicated", "ram": 32}），并通过后处理清洗（单位换算、离散对齐、无效值过滤）保证可查询性。
- **确定性排序**：基于 3,638 条笔记本电脑规格，依次进行类别过滤（品牌、GPU 类型）、数值损失计算（价格、RAM、存储、屏幕尺寸）、综合损失排序，损失值完全可审计并通过前端展示。
- **约束生成与决策支持**：响应生成要求 LLM 基于当前需求和排序结果进行解释（如“因为视频编辑需要，已更新为独立显卡”），避免幻觉；产品对比和亮点功能先由规则计算规格差异与需求匹配，再由 LLM 格式化为自然语言。

**关键结果**：作者未进行正式用户实验，但展示了演示系统原型，支持多轮混合主导对话、实时重排序、可解释排序面板、AI 驱动的多产品对比与个性化推荐。未来研究中计划对比混合架构、纯 LLM 和传统分面搜索的效果，并评估解释对决策信心的影响。该系统为对话推荐系统的透明性与可控性提供了一个可扩展的实验平台。

**核心记忆**："通过硬编码的排序与约束生成将 LLM 的角色限定为‘格式化器’而非‘决策者’，是当前阶段在电商推荐中安全使用 LLM 的一套务实方案。"
