---
title: 'What Comes Next and Why: Interpretable Next-Event Prediction with Neuro-Symbolic
  Rules'
title_zh: 可解释下一事件预测：神经符号序列规则与残差网络
authors:
- Tim Nico Bauerschmidt
- Isabel Valera
- Jilles Vreeken
affiliations:
- Saarland University
- CISPA Helmholtz Center for Information Security
arxiv_id: '2610.31114'
url: https://arxiv.org/abs/2610.31114
pdf_url: https://arxiv.org/pdf/2610.31114
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 神经符号规则 · 可解释事件预测
tags:
- Neuro-symbolic
- Sequential Rules
- Next-Event Prediction
- Interpretability
- Residual Network
- Event Sequences
one_liner: 学习序列规则 RULES，并与残差网络组成 RUNES，在保持精度同时提供可解释规则与残差调整
practical_value: '- 电商行为序列预测可用学到的规则如「搜索→点击→加购 ⇒ 购买」作为可解释基础层，配合残差网络提升精度；规则部分直接给运营/风控提供可读理由。

  - 架构上采用规则+残差加性组合，线上可单独审计或配置规则部分，残差网络吸收长尾和非规则模式，适合需要业务可解释与合规审计的场景。

  - 用于搜索词/query 推荐时，可将 query 和用户行为离散化为事件，学习「query A 后 query B」类规则，为推荐生成可解释理由。

  - 规则集可作为冷启动先验或模型诊断工具：先在合成/历史数据上验证规则恢复能力，再接入残差模型，避免黑盒覆盖关键业务规则。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**
实际序列事件预测中，可解释性往往与精度同等重要。现有神经序列模型预测准但内部不透明；神经符号方法可学习符号规则，但延伸到带时序依赖的下一事件预测较困难。

**方法关键点**
提出 RULES，直接从数据学习顺序规则，表达形如 A⇒B 的事件依赖；进一步与残差网络组合为 RUNES：规则部分提供透明、可解释的预测基底，残差网络以加性方式修正规则预测，从而保留神经网络对复杂模式的拟合能力。推理时可查看哪些规则被激活，以及残差如何调整最终预测。

**关键结果**
在合成数据上 RULES 能准确恢复 ground-truth 规则；在真实数据上发现紧凑、可解释的规则集。RUNES 在保持与神经基线有竞争力的预测精度同时，提供对规则和残差调整的透明访问。代码已开源。
