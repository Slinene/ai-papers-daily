---
title: More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling,
  and Test-Time Compute in Multi-Agent LLMs
title_zh: 更多智能体、更多采样还是更多思考：厘清多智能体LLM的协调、集成与测试时计算
authors:
- Seyed Mahmoud Sajjadi Mohammadabadi
affiliations:
- University of Nevada, Reno
arxiv_id: '2611.17610'
url: https://arxiv.org/abs/2611.17610
pdf_url: https://arxiv.org/pdf/2611.17610
published: '2026-11-12'
collected: '2026-11-18'
category: Eval
direction: 多智能体LLM评估 · 测试时计算核算
tags:
- Multi-Agent LLMs
- Test-Time Compute
- Evaluation Methodology
- Resource Accounting
- Self-Consistency
- Meta-Analysis
one_liner: 对9项研究516个多智能体配置做资源核算元分析，发现样本/预算匹配后多智能体整体不优于自洽基线（-0.042）
practical_value: '- 离线评估生成式推荐/Agent流水线时，不要把多智能体与单次greedy对比；用同样本数self-consistency或同预算基线，并报告R的六维资源（reason/token/cost/latency/sample/system）。

  - 在电商商品筛选、智能客服协商、搜索意图改写等场景，先确认是否有可分区证据或外部验证器；共享同一上下文的同质多智能体往往只增加token稀释，5样本多数投票常更便宜且不差于debate。

  - 做多模型集成/多智能体投票时，用有效独立票数 Keff=K/(1+(K-1)ρ) 估计相关性损耗，优先降低模型间误差相关性（异质模型/不同视图），而不是简单堆agent数量。

  - 用阈值 p*=τ_{i→c}/(τ_{i→c}+τ_{c→i}) 与debate transcript的转移率做动态度量，判断给定任务/模型上沟通是否可能正收益；baseline准确率已较高时，多智能体更可能拖累准确率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多智能体LLM通常与单次greedy解码比较，混淆了协调机制、采样次数与测试时计算量。此前不少评测看到multi-agent“涨点”，可能只是多了采样或token预算，而不是通信/协调本身有效。需要把资源核算和baseline强度显式纳入评估。

**方法关键点**
- 提出资源向量R：thinking tokens、total tokens、monetary cost、latency、sample count、system scaffolding/tools，共六维。
- 提出Baseline Ladder四类：A单次greedy、B样本数匹配（self-consistency）、C预算匹配、D Pareto frontier。
- 形式化结论：共享同一证据时通信不增加信息；greedy baseline对多采样系统有偏；相关投票的有效独立票数 Keff=K/(1+(K-1)ρ)；scaffold token随 K、T 呈二次增长；从众转移阈值 p*=κ/(1+κ)。
- 从9项研究提取516个unique multi-agent configurations、531行原始表数据，做描述性合成与REML多水平log odds建模。

**关键实验数字**
- 相对A类单次baseline，mean Δ=−0.032；去掉最大贡献研究Zhang et al.后为−0.005。
- 相对B类样本匹配baseline，mean Δ=−0.051；相对C类预算匹配baseline为−0.012；合并B/C为−0.042（去Zhang后−0.029）。
- 在474个可比较contrasts中，multi-agent准确率等于或低于baseline的比例为74%；对采样baseline为76%。
- 5个同时报告A/B的研究中，sampling gap全部为负，study均值−0.038，说明单次greedy会系统性高看multi-agent。
- 唯一明显正向例外是Wunderlich et al.在MMLU-Pro上的Pareto对比：debate +1.3、MoA +2.7（vs 10样本self-consistency）。
- 多水平模型pooled log odds=−0.195，CR2 95% CI [−0.320,−0.070]，多项敏感性检查仍为负。

**最值得记住的一句话**
当用样本数或预算匹配的自洽/单智能体基线做对比后，多智能体协调增益整体为负；只有信息分区、外部验证或跨模型误差去相关才可能带来正向协调收益。
