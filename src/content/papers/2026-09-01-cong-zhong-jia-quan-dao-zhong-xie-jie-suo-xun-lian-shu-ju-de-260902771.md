---
title: 'From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential
  Samples in Training Data Attribution'
title_zh: 从重加权到重写：解锁训练数据归因中高影响样本的干预效应
authors:
- Yuzhang Luo
- Chenpeng Wang
- Jianhui Chen
- Liangming Pan
affiliations:
- Peking University
- YiXin-AI Lab
- Beijing Academy of Artificial Intelligence
arxiv_id: '2609.02771'
url: https://arxiv.org/abs/2609.02771
pdf_url: https://arxiv.org/pdf/2609.02771
published: '2026-09-01'
collected: '2026-09-12'
category: Training
direction: 训练数据归因 · 影响力函数干预
tags:
- Training Data Attribution
- Influence Functions
- Response Rewriting
- LLM
- Intervention
- Safety
one_liner: 影响力函数选中的样本在重加权下干预有限，但对其响应进行重写可实现更强、持久且双向的行为改变
practical_value: '- 在 LLM 微调治理中，若需修正拒答/过度生成、安全合规、商品属性表达等行为，用影响力函数（IF）选出的少量高杠杆样本，直接重写其
  response（而非 instruction），比调整样本权重或随机改样本更有效且效果更持久、双向可控。

  - 可把 IF 作为数据清洗/标注预算分配工具：优先重标注 IF 分数高的训练样本，用行为对齐/对抗的监督信号做定向改写，能通过极小样本集实现行为翻转，避免大量重训。

  - 重加权在评估 TDA 时会低估样本干预价值，实际落地评估归因方法时应区分“局部重加权效应”与“重写干预杠杆”，不要仅用 weight-based 干预去验证归因质量。

  - 针对电商/搜索场景的 LLM 应用（如商品问答、广告文案、政策拒答），可构建行为探针（如 epistemic abstention、safety refusal），用
  IF 定位问题样本并重写响应来快速修复 badcase。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：训练数据归因（TDA）常用影响力函数（IF）估计样本对模型行为的影响。但 IF 选出的样本在传统重加权干预下常与随机选择无显著差异，引发疑问：高影响样本本身没有干预价值，还是重加权这种干预方式无法释放其行为杠杆？

方法：提出 influence-guided response rewriting：用 IF 识别干预目标，保持 instruction 不变，仅将样本 response 替换为行为对齐或行为相反的监督信号，并以 epistemic abstention 作为主要测试床，在四个开源权重 LLM 上对比 response rewriting 与 reweighting 对同一批 IF 选出样本的干预效果。

结果：response rewriting 带来更强、更持久且双向的行为偏移；对同样样本做 reweighting 则效果弱且不稳定。进一步分析显示，IF 选出的样本在 rewriting 下的干预杠杆高于其他选择器，行为变化集中在目标相关行为上；这一对比同样适用于 safety refusal 场景。研究区分了影响力估计所刻画的局部重加权效应与样本本身的更广泛干预杠杆，推动 TDA 方法走向 intervention-aware 评估。
