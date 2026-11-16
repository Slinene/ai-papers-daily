---
title: 'JFinBench: A Continuously Refreshable Japanese Financial Benchmark from the
  Latest Certification Exams'
title_zh: JFinBench：来自最新认证考试的日本金融可刷新基准
authors:
- Issa Sugiura
- Taro Makino
- Takashi Ishida
affiliations:
- Sakana AI
- Institute of Science Tokyo
arxiv_id: '2611.18130'
url: https://arxiv.org/abs/2611.18130
pdf_url: https://arxiv.org/pdf/2611.18130
published: '2026-11-12'
collected: '2026-11-16'
category: Eval
direction: 金融 LLM 评估基准 · 可刷新数据管道
tags:
- financial benchmark
- Japanese
- LLM evaluation
- human-in-the-loop
- agentic pipeline
- data contamination
one_liner: 构建可周期刷新的日本金融基准 JFinBench，用 human-in-the-loop agentic pipeline 处理异构考试格式并评估
  12 个 LLM
practical_value: '- 构建领域评测集的 human-in-the-loop agentic pipeline 可迁移到电商/广告场景：用 coding
  agent 编写针对不同数据源（商品属性、活动规则、政策文档）的转换代码和审核页面，人类只做校验和反馈，显著降低多源异构数据的结构化成本。

  - 定期刷新评测集、纳入最新版本以对抗训练数据污染，适合需要跟踪模型在快速变化的业务知识（如平台规则、广告合规、促销玩法）上表现的团队。

  - 同时报告无工具和有工具（终端/网络）两种设置下的结果；实验显示工具使用普遍提升但模型排名基本不变，说明在 RAG/工具增强的推荐 Agent 评测中，模型自身知识仍是关键因素，不能只依赖外部检索。

  - 闭源与开源模型存在约 12 个百分点的领域知识差距，选择基座模型时应重点考察其在目标垂直领域的认证/考试级知识覆盖。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有金融基准对国家特定金融体系覆盖不足，且题目泄露进入训练数据导致过时，需要可刷新、覆盖日本金融认证的评估集。

方法：发布 JFinBench，包含 321 个样本，来自 2026 年版六种认证考试（会计、税务、财务规划、银行）。构建采用 human-in-the-loop agentic pipeline：先用通用 VLM 对 PDF 转录音频并做字符级校验，再由 coding agent 为每个考试编写转换代码和审核页面，将异构格式转为结构化样本（问题、选项、答案、图表裁剪），人类验证每个样本并将修正反馈给 agent。该 pipeline 支持纳入新考试版本，周期刷新以缓解数据污染。

结果：评估 12 个近期 LLM，Claude Fable 5 和 GPT-6 Astra 综合得分超 93%，最佳开源模型 Kimi K3.1 Pro 落后 Claude Fable 5 约 12 个百分点；当模型额外使用终端和网络访问时，所有模型均提升，差距缩小至约 4 个百分点但模型排名基本不变，表明即使有工具，模型自身知识仍具价值。
