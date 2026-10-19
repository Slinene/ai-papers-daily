---
title: Learning Personalized Memory Gating from Delayed One-Sided Feedback
title_zh: 从延迟单侧反馈中学习个性化记忆门控
authors:
- Kaixuan Ji
- Zixiang Chen
- Wenting Zhao
- Cheng Qian
- Heng Wang
- Weizhi Zhang
- Jielin Qiu
- Liangwei Yang
- Quanquan Gu
- Silvio Savarese
affiliations:
- Salesforce AI Research
- University of California, Los Angeles
- University of Illinois at Urbana-Champaign
- University of Illinois Chicago
arxiv_id: '2610.23812'
url: https://arxiv.org/abs/2610.23812
pdf_url: https://arxiv.org/pdf/2610.23812
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 长期记忆 · 个性化门控
tags:
- Memory Gating
- Personalization
- Contextual Bandit
- Delayed Feedback
- LLM Agents
- Online Learning
one_liner: 将 Agent 记忆门控建模为延迟单侧反馈的 contextual apple tasting，提出 Warm-Start UCB 实现用户级个性化选择
practical_value: '- 在电商客服/导购 Agent 的记忆系统中，不要使用全局统一的重要性阈值；可以按用户做个性化门控，用“该 fact 后续是否被检索并用于回复”作为弱标签，低成本构造训练数据。

  - 把记忆写入决策当作 contextual bandit 问题处理：只有保存下来的 fact 才能观察到后续复用信号（单边反馈），且复用有延迟；可采用 Warm-Start
  UCB 的思路，先用离线数据初始化策略，再对当前用户在线微调，比纯离线或纯在线更稳。

  - 工程实现上，设置合理的延迟窗口：理论显示延迟窗口在 O(√T) 内时 regret 有上界，延迟过长时应截断或异步更新，避免在线学习退化。

  - 业务可复用结论：用户对 fact 的复用模式差异大，个性化门控在 memory budget 小、history 长时优势更明显，适合需要长期用户记忆的电商推荐/客服场景。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：语言模型 Agent 的长期记忆库容量有限，无法保存所有抽取的 fact；现有记忆门控策略通常跨用户共享，忽略不同用户未来复用模式的差异，导致记忆利用率低。

**方法关键点**：
- 提出基于检索的标注策略，将每个 fact 是否在后续被检索并用于回复作为价值标签，把记忆门控下沉到 fact 级在线决策。
- 将在线记忆门控形式化为 contextual apple tasting with delayed one-sided feedback：只有被保存的 fact 才能观察到后续复用信号，未保存的无法观察，且反馈存在延迟。
- 提出 Warm-Start UCB，先用离线已有数据学习初始化策略，再对当前用户进行在线自适应；相比纯离线或纯在线算法，能同时利用历史数据和个体实时信号。
- 理论分析给出高概率 regret 上界为 \(\tilde{O}(T\epsilon \wedge d\sqrt{T})\)，其中 T 为总轮数，ε 为初始化误差，d 为特征映射维度，且要求延迟窗口最多为 \(O(\sqrt{T})\)。

**关键结果**：实验在不同 memory budget 和 history length 设置下均优于所有基线，表明个性化记忆门控策略在长期交互场景中具有明显优势。
