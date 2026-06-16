---
title: How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability
  to Web Content Manipulation
title_zh: LLM搜索代理对抗Web内容操纵的背书脆弱性评估
authors:
- Yimeng Chen
- Zhe Ren
- Firas Laakom
- Yu Li
- Dandan Guo
- Jürgen Schmidhuber
affiliations:
- Center of Excellence for Generative AI, KAUST
- Jilin University
- Zhejiang University
- The Swiss AI Lab, IDSIA-USI/SUPSI
- NNAISENSE
arxiv_id: '2606.16821'
url: https://arxiv.org/abs/2606.16821
pdf_url: https://arxiv.org/pdf/2606.16821
published: '2026-06-15'
collected: '2026-06-16'
category: Other
direction: LLM搜索代理安全评估
tags:
- LLM search agents
- endorsement vulnerability
- web content manipulation
- adversarial attack
- safety evaluation
one_liner: 提出SearchGEO框架，系统评估13种LLM搜索代理被恶意网页内容操纵后给出错误推荐的攻击成功率
practical_value: '- 在电商/推荐系统中部署搜索型LLM Agent时，需引入类似SearchGEO的对抗性评估流程，测试不同模型后端对网页证据操纵的脆弱性，避免因恶意SEO内容导致错误推荐。

  - 攻击成功率在不同模型家族差异显著（如Claude几乎免疫，Gemini高达31.4%），选型时必须将对抗鲁棒性作为核心指标，而非仅考虑基准性能。

  - 高风险场景（如自动执行安装命令）应设计额外的安全护栏：观察到Claude过度拒绝而GPT过度信任，可根据业务容忍度选择模型或设置强制拦截规则。

  - 同一部署脚手架在不同后端上可能放大或消减ASR，提示工程实现需针对具体模型调优，简单复用可能引入漏洞。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM搜索代理直接整合开放网页证据生成推荐回答，但攻击者可通过发布恶意内容操纵这些推荐，形成“背书劫持”。目前缺乏系统评估这种威胁的框架。

**方法**：提出SearchGEO评估框架，构建了一个Web证据操纵流水线，定义五种攻击模式（如插入、重写、窃取上下文等），并从多个输出层面度量攻击成功率。在统一场景下测试了13个主流LLM后端（含GPT、Claude、Gemini等系列），每个模型处理308个精心构造的操纵案例。

**关键结果**：
- 整体攻击成功率（ASR）跨模型差异极大：Claude-Sonnet-4.6为0.0%，Gemini-3-Flash高达31.4%。
- 最强攻击模式随模型家族而变化，无单一攻击范式普遍生效。
- 同一部署脚手架（如LangChain）在不同后端上可能放大或降低ASR。
- 辅助技能探测（将背书转为安装命令）揭示稳健模型的极端分化：Claude过度拒绝良性请求，GPT则过度信任恶意指令。

结论：将推荐可靠性在对抗搜索内容下的表现列为LLM后端安全评估的首要维度。
