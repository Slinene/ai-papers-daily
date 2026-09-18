---
title: 'RiskChainBench: A Benchmark for Obfuscated Platform Message Restoration and
  Evidence-Grounded Web Investigation'
title_zh: RiskChainBench：混淆平台消息恢复与证据支撑的网页调查基准
authors:
- ZhuoXin Liu
- Zhiming Ma
- Ying Zhang
- Mengzheng Yang
- Yifan Wang
- Zhengqi Huang
- Yanhan Zhou
- Zekun Lin
- Jun Zhang
- Shun Zhang
affiliations:
- Baidu
- SmartFlowAI
- People’s Public Security University of China
- Tsinghua University
- JD Technology
arxiv_id: '2609.16900'
url: https://arxiv.org/abs/2609.16900
pdf_url: https://arxiv.org/pdf/2609.16900
published: '2026-09-14'
collected: '2026-09-18'
category: Eval
direction: 风险内容检测基准 · Web Agent 调查
tags:
- Benchmark
- Obfuscated text
- Web agent
- Risk detection
- Evidence-grounded
- Multimodal
one_liner: 提出配对混淆消息恢复与本地网页调查的基准，评估模型恢复风险指令并执行证据引证网页调查的能力
practical_value: '- **混淆文本恢复技巧可迁移至电商内容审核与 query 清洗**：论文针对 emoji、谐音、字符拆分、冗余符号的恢复流程，可直接用于处理电商平台中规避风控的违禁商品描述、广告文案或搜索
  query 变体，提升召回与安全性。

  - **Agent 系统瓶颈定位方法值得借鉴**：将任务拆解为消息恢复（入口预测）与网页调查（证据获取）并离线 gate 组合，清晰分离模型在不同子任务上的表现；可复用于搜索推荐
  Agent 的评估，定位是 query 理解错误还是后续执行不稳定。

  - **证据引证报告设计可增强推荐理由可信度**：强制模型输出带证据引用的风险报告并设计 faithfulness/sufficiency/completeness/consistency
  多维度裁判，在电商推荐解释、广告合规审查中可要求 Agent 提供可追溯依据，减少幻觉。

  - **工程实现中优先强化稳定探索和工具调用鲁棒性**：研究发现执行失败占网页运行 31.9%，而决策后类型错误仅 0.9%，提示在构建多步 Agent 时，应优先优化重试机制、页面解析容错和状态恢复，而非过度微调决策模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：平台滥用信息常通过 emoji、谐音、字符拆分等手段隐藏跳转指令，将用户引向色情、欺诈、赌博等风险服务。现有基准分别评估混淆文本和风险网页，忽视从消息恢复到下游证据获取的完整链路。

**方法关键点**：构建 RiskChainBench，包含 3,600 个合成 token-text 恢复输入（来自 600 个源会话）与 600 个对应人工标注的本地网页环境。模型先恢复消息、操作意图和目的地；同一模型作为 VLM 驱动的 web agent 调查正确关联的网站，生成冻结的、带证据引用的风险报告，且不依赖消息语义或域名信誉线索。评估分离恢复与正确路由的网页调查，并通过离线组合：将冻结的入口预测作为门控应用到同一任务 2 结果。人工标签决定任务正确性，固定多模态证据裁判评估 faithfulness、sufficiency、completeness、consistency。

**关键结果数字**：十个模型中，Entry Top-1 从 35.2% 到 95.2%，网页决策准确率从 26.3% 到 62.8%；不同子任务领先系统不同。执行失败占网页运行的 31.9%，而决策后类型错误仅占 0.9%，表明稳定探索和风险判断是主要瓶颈。
