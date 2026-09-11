---
title: 'Agentic Share-of-Search: A Multi-Agent AI System for Competitive Decision-Making
  in LLM-Mediated E-Commerce'
title_zh: 面向 LLM 电商的 Agentic 可见份额测量与竞争诊断系统
authors:
- Spandan Ghose Chowdhury
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.11190'
url: https://arxiv.org/abs/2609.11190
pdf_url: https://arxiv.org/pdf/2609.11190
published: '2026-09-10'
collected: '2026-09-11'
category: MultiAgent
direction: 多 Agent 竞争情报 · ASoS 指标
tags:
- Agentic Share-of-Search
- Multi-Agent Systems
- Root Cause Analysis
- LLM-Mediated E-Commerce
- Generative Recommender Systems
- Competitive Intelligence
one_liner: 提出 ASoS 指标与多 Agent 系统，测量并诊断卖家在 LLM 生成式推荐中的可见性差距
practical_value: '- **借鉴 ASoS 指标设计**：用 rank-discounted share 衡量商品/店铺在 LLM 回答中的可见份额，分母只计入可解析到竞争集内的零售商；重复提及取最好
  rank，多零售商归因均分权重，优先使用回答中的零售商归因而非目录解析。可直接迁移到电商团队监测 ChatGPT/Perplexity/Gemini 回答中的
  SKU 级曝光。

  - **架构分层可复用**：uniform platform client + 可插拔 entity resolver + mock client 注入噪声做离线
  CI，能降低多 LLM 平台监控的接入成本与 API 开销。QLoRA 微调小模型做商品名/SKU 归一化（93.7% top-1，不到 1% frontier
  API 成本）适合作为实体链接的轻量方案。

  - **诊断任务选型 ReAct 而非 AutoGen/LangGraph**：单轮 RCA/归因场景下 ReAct 的 thought–act–observe
  循环足够，可审计 trace 且避免对话状态机开销；priority score = |r| × gap 按业务影响排序，比按异常度排序更贴近 merchandising
  分析师的决策逻辑。

  - **原型验证用 synthetic signal ablation**：在缺乏因果 ground truth 时，通过随机消融信号看诊断 agent 是否
  top-1 恢复，并报告无条件/条件精度与随机基线对比，可作为 agent 诊断能力可行性验证的轻量模板；但业务落地仍需人工审核和干预实验闭环。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：AI 购物助手正在取代确定性搜索排名，成为商品发现的新入口。传统 SEO/品牌监测工具无法测度 LLM 回答中的 SKU 级零售商可见性，卖家侧缺乏竞争诊断与干预的量化手段，需要一个能测量“我的产品在生成式推荐中相对竞品出现多少、差在哪、该改什么”的决策支持系统。

方法关键点：
- **ASoS 指标**：rank-discounted share（权重 1/log2(k+1)），分母仅包含可解析到竞争集内零售商的提及；重复提及去重取 best rank；多零售商归因按权重均分；优先使用回答中的零售商归因字符串，目录解析仅作 fallback。
- **多 Agent 查询执行**：coordinator 分发 query-platform 对，query agent 对每个 query 重复 3 次；extraction LLM 解析产品名、品牌/零售商归因、排名、情感与购买链接；实体解析提供 embedding baseline 与 QLoRA opt-in 两种实现。
- **竞争信号数据库**：价格、内容质量、评论、目录覆盖、发货等；定量信号用确定性解析，定性信号用 gpt-4o-mini 零样本 JSON 输出。
- **诊断 Agent**：ReAct 单轮，计算 per-SKU 出现率与各信号的 Pearson 相关，按 priority score = |r| × observed gap 排序，经 SOP 验证后输出结构化干预建议。

关键结果：100 次合成信号消融试验中总体 Precision@1 = 39.0%（95% CI 30.0–48.8，5.5× 随机基线）；消融信号位于 top-3 相关时条件精度 63.9%；最强相关信号 has_qa 精度 100%。QLoRA resolver 在对抗测试上 93.7% top-1 vs embedding 91.1%。Gemini live pilot 抽取成功率 70.0%。

最值得记住：把生成式推荐中的卖家可见性变成可测量、可诊断的 ASoS，并用关联性诊断按业务影响排序干预项，但结论是关联性而非因果，需人工审核和干预实验验证。
