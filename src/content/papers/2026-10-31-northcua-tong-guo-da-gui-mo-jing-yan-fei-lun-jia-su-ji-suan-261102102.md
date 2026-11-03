---
title: 'NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience
  at Scale'
title_zh: NorthCUA：通过大规模经验飞轮加速计算机使用代理
authors:
- Chaoyun Zhang
- Bingxuan Li
- Pinxue Guo
- Yangfan Gao
- Zikun Cai
- Tianci Xie
- Hui Li
- Yuqi Huang
- Yifei Cao
- Bo Mao
affiliations:
- Shanghai Qiji Zhifeng Co., Ltd.
arxiv_id: '2611.02102'
url: https://arxiv.org/abs/2611.02102
pdf_url: https://arxiv.org/pdf/2611.02102
published: '2026-10-31'
collected: '2026-11-03'
category: Agent
direction: Agent 经验飞轮与强化学习
tags:
- Computer-Use Agent
- Experience Flywheel
- Reinforcement Learning
- GUI Grounding
- Staged Learning
- Open-source
one_liner: 用经验飞轮、分级学习与桌面-网页联合强化学习，训练出开源SOTA的计算机使用代理模型族
practical_value: '- 借鉴经验飞轮机制：在电商/搜索推荐 agent 中，将用户交互轨迹作为经验，通过结果校验（转化、点击、任务完成）筛选高质量轨迹，持续扩充训练数据，形成数据闭环。

  - 对未成功任务采用递归自改进：保存已验证的里程碑，让后续尝试在已有进展上继续。适合长程多轮推荐/导购场景，避免每次从零开始，提升任务完成率。

  - 分级学习策略：先 mid-training 注入 grounding 数据（如商品/页面结构化信息）建立基础能力，再 long-horizon SFT 学习完整任务轨迹，最后用在线
  RL 在真实环境中闭环优化。可复用为：领域继续预训练 → 人工标注 SFT → 在线策略迭代。

  - Ultrafast 的思路：直接动作选择与开放生成结合，在低延迟场景（实时推荐、搜索响应）可用混合解码策略，牺牲少量质量换取显著响应速度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
缩放计算机使用代理需要把决策与完整结果连接的经验，而现有方法缺乏可持续生成、验证和复用轨迹的闭环系统。

**方法关键点**
NorthCUA 由 Experience Flywheel 和 Harness 组成。Flywheel 供给多样化可执行任务；Harness 支持长时交互、记录决策并校验任务结果。Flywheel 据此筛选已验证轨迹，对未解决任务执行递归自改进，演化可复用技能并保存已验证里程碑，使后续尝试可继承进展。Staged Learning 结合这些经验与 grounding 数据，通过 mid-training 和 long-horizon SFT 建立 GUI 能力，再在同一 Harness 中进行桌面-网页联合强化学习，形成经验生产与策略改进闭环。

**关键结果**
Nano、Mini、Pro 模型族在开源模型中达到 SOTA：ScreenSpot-Pro 准确率 93.3%，OSWorld-G 91.0%，OSWorld-Verified 88.6%，WebArena-Verified 73.9%，OSWorld 2.0 Partial 66.8%，WebTestBench F1 60.3%。Ultrafast 变体在 pre-RL Nano 上采用直接动作选择与开放生成，提供质量-延迟权衡。
