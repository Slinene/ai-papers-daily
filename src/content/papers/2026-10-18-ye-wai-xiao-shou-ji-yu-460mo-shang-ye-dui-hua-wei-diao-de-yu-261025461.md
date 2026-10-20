---
title: 'Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent
  Trained on Commercial Conversations'
title_zh: 野外销售：基于460万商业对话微调的销售Agent基准与随机现场实验
authors:
- Benjamin Tannenbaum
affiliations:
- Javo, AISO Boost Ltd.
arxiv_id: '2610.25461'
url: https://arxiv.org/abs/2610.25461
pdf_url: https://arxiv.org/pdf/2610.25461
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: 对话式销售Agent训练与在线随机实验
tags:
- Sales Agent
- Conversational AI
- Fine-tuning
- A-B Testing
- Commercial Conversations
- LLM
one_liner: 用460万真实商业对话微调Qwen3-32B销售Agent，在100个网站随机试验中比无Agent提升10%收入，比前沿模型提升21.6%转化
practical_value: '- 真实商业对话微调是提升销售/导购Agent业绩的关键：SFT学完整对话（需求挖掘、推荐、异议处理、下一步提议），DPO用购买进展信号做偏好优化；可直接迁移到电商客服、导购对话训练。

  - 模型隔离评估设计值得借鉴：固定界面、检索、工具、prompt、guardrails，只换模型权重，才能干净归因训练数据的价值；业务方上线Agent前应做类似消融。

  - 在线实验协议可复用：ITT收入/访客 + engaged conversion + 非劣性对比人工 + 安全守卫指标（退货率、投诉、未支持声明、未授权优惠），并采用CUPED、sample
  ratio check、顺序检验等。

  - 成本效率结论：对话Agent推理成本仅为人工的1.8%（0.06美元 vs 3.40美元），且转化非劣性，可优先在咨询密集品类（美妆、家具、旅游）部署自动化销售助手。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：通用LLM被后训练为“帮忙而非销售”，在销售基准上表现出被动问答而非主动销售倾向；商业对话数据稀缺，现有证据要么基于模拟器不可靠，要么早于当前模型；站点决策者需要可部署的增量收益数字。

**方法关键点**：
- 收集4.6M条真实商业对话（58.4M轮，覆盖14行业），去除评估站点和基准重叠，17.4%有购买结果标签。
- 两阶段训练：SFT让模型根据完整对话生成卖家回复（挖掘需求、推荐、异议处理、提议下一步）；DPO利用购买进展信号构造偏好对（进展 vs 停滞/退出）；额外3.4万约束样本强化合规（无政策外折扣/声明、AI披露、转人工）。
- 统一scaffold：界面、检索、目录工具、prompt、guardrails、响应时限完全相同，仅模型权重不同，用于隔离训练效果。

**关键实验与结果**：
- 离线基准：Javo在SalesLLM-EN上得分7.01，超过最佳前沿模型6.21和初级销售6.13，接近资深销售6.88；SmartSalesBench 0.79；τ-bench retail 73.0（未牺牲工具策略遵循）。
- 100个网站14.8M访客随机试验：相对无Agent，收入/访客+10.0%（95% CI +5.1至+14.9），转化+8.0%；相对前沿模型GPT-5.2（相同scaffold），engaged conversion +21.6%（+16.9至+26.3），ITT收入/访客+16.9%。
- 与20家站点真实人工对比：engaged conversion 11.26% vs 11.20%，非劣性成立（margin -7%，单侧p=0.004），无显著优越，每对话成本仅为人工的1.8%（0.06 vs 3.40美元）。
- 安全守卫：退货率、取消率、投诉率、未支持声明、未授权优惠、压力策略全部满足预设边际。

**最值得记住的一句话**：真实商业对话训练数据，而非模型规模，决定了销售Agent在真实流量中的营收效果。
