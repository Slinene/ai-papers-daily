---
title: 'SEER: Self-Evolving Event Reasoning and Retrieval for Time Series Forecasting'
title_zh: SEER：面向时序预测的自进化事件推理与检索
authors:
- Mingtian Tan
- Palash Goyal
- Mihir Parmar
- Sarkar Snigdha Sarathi Das
- Chun-Liang Li
- Nanyun Peng
- Thomas Hartvigsen
- Jinsung Yoon
- Tomas Pfister
affiliations:
- Google Cloud AI Research
- University of Virginia
arxiv_id: '2610.04109'
url: https://arxiv.org/abs/2610.04109
pdf_url: https://arxiv.org/pdf/2610.04109
published: '2026-10-01'
collected: '2026-10-07'
category: Agent
direction: 自进化 Agent · 事件检索增强时序预测
tags:
- Self-Evolving
- RAG
- Time Series Forecasting
- LLM Agent
- Causal Knowledge
- Memory
one_liner: 用预测误差驱动检索记忆与因果知识库更新，显著提升事件驱动时序预测的准确性与可解释性
practical_value: '- 在电商需求预测/广告转化预估中，把动态外部事件（价格调整、大促、供应链、热搜）作为可更新的文本上下文，而不是静态特征；用 retrieval
  memory 生成搜索 query 扩展候选，再用 selection memory 做噪声过滤，两个组件解耦，避免信息过载。

  - 闭环反思机制可用于推荐/搜索的在线学习：将预测残差（销量/CTR 偏差）和推荐理由对比，更新「检索记忆」与「因果规则库」，离线回放、线上冻结，避免直接更新模型参数；尤其适合已有
  LLM 推荐理由或文案生成场景。

  - 严格时间边界与 fact-check 约束对推荐系统外部特征同样关键，确保只用截至请求时刻的商品新闻/库存/价格，防止特征穿越导致线上翻车。

  - 蒸馏 IF-THEN 因果规则不仅提升可解释性，还能让 Agent 主动拒答/过滤高噪声样本（如选择性股票预报、选品），提升精度；电商中可迁移到「是否推荐、推什么品类」的不确定性决策。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：真实业务时序常受外生事件（供应链中断、政策、突发新闻）驱动，纯数值历史预测不足。现有 LLM+RAG 方案有三类失败模式：原始新闻流信噪比低、仅语义相似度检索缺少因果归因、开环不利用预测误差调整上下文。

**方法关键点**：
- SEER 冻结 LLM 预测器，只优化文本上下文空间 Ω_t = (E_t, K_t)：外部事件池 E_t 与持久因果知识库 K_t。
- 上下文构造 R = (ρ∘σ(E_t), K_t)；σ 用 retrieval memory Mret 生成搜索 query 扩展事件，ρ 用 selection memory Msel 过滤噪声。
- 观察真实 y_t 后，用轨迹 ξ_t 反思，把预测误差解耦为两个反馈：Φmem 更新检索/选择记忆；Φknow 蒸馏可迁移的因果规则；C 做容量压缩合并，控制上下文长度。
- 所有检索事件经 LEAF fact-checking 限制时间戳 ≤ t，严格防止 look-ahead bias。
- 实现覆盖四个 LLM backbone：Gemini 3.1 Pro/Flash、Claude 4.6 Sonnet/4.8 Opus。

**关键实验**：
- 六个领域：Memory、SSD、Stock、Weather、Electricity、Polymarket；对比 15 个基线，包括 DL 预报器、LLM 预报器和 TSFM（TimesFM 3.0、Chronos-2）。
- 主要结果：Memory 6M MSE 187.2，比最佳基线降低约 50.2%；Electricity MSE 4340.5，比最佳基线降低 16.4%；Weather MAE 2.547；Stock 方向准确率 38.25%。
- 消融显示：完整 SEER 比 LLM(no events) 平均提升 +19.5%，比 LLM(Event RAG) 平均提升 +10.5%；移除因果知识后明显下降。
- 泛化到 Selective Stock Forecasting（51.39% vs 38.10%）与 Polymarket（Brier 0.2167 vs 0.3115）。

**最值得记住的一句话**：在冻结 LLM 的前提下，用预测残差同时优化「去哪检索」和「信什么规则」，比单纯多检索几条新闻更能提升事件驱动预测。
