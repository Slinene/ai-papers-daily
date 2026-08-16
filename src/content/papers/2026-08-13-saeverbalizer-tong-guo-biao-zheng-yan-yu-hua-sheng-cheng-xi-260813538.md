---
title: 'SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via
  Representation Verbalization'
title_zh: SAEVerbalizer：通过表征言语化生成稀疏自编码器特征解释
authors:
- Weihan Meng
- Hongzhu Guo
- Yi Jing
- Dewen Liu
- Zijun Yao
- Xiaozhi Wang
- Lei Hou
- Juanzi Li
affiliations:
- Tsinghua University
- Peking University
- Fudan University
arxiv_id: '2608.13538'
url: https://arxiv.org/abs/2608.13538
pdf_url: https://arxiv.org/pdf/2608.13538
published: '2026-08-13'
collected: '2026-08-16'
category: LLM
direction: LLM 可解释性 · 表征言语化
tags:
- Sparse Autoencoder
- Interpretability
- Verbalization
- Feature Explanation
- Controllable Generation
one_liner: 注入 SAE 解码方向并微调下游层，将 SAE 特征直接言语化为自然语言解释，摆脱外部行为观察
practical_value: '- 可将 SAE 特征言语化范式迁移到推荐/搜索的内部表征：对用户或商品 embedding 的稀疏特征生成自然语言解释，帮助理解模型捕获的隐式偏好（如价格敏感、品牌忠诚），用于特征
  Debug 和可解释推荐。

  - 训练一个 verbalizer 后即可直接解释 decoder 方向，无需为每个特征收集行为证据，显著降低大规模特征解释的工程成本；在电商场景可批量解释召回/排序模型中的稀疏特征，加速模型审计。

  - 多方向注入产生组合语义、反转方向产生相反语义，可用于可控文本生成：例如在广告文案或推荐理由生成中，通过注入/反转特定语义方向实现属性编辑（如风格、情感、卖点控制）。

  - 跨模型迁移只需轻量 adapter，不重新训练完整解释器，适合业务中多 LLM 版本快速适配；在生成式推荐或 Agent 决策解释模块中可复用该迁移策略。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**
Sparse autoencoders (SAEs) 能从 LLM 表征中提取大量可解释特征，但特征解释仍主要依赖外部观察模型行为。这种方式得到的解释浅层，且大规模收集行为证据计算效率低。

**方法关键点**
SAEVerbalizer 将 SAE decoder 方向注入 LLM 表征，并微调 LLM 的下游层，使其根据注入方向生成自然语言解释。训练时使用固定 verbalization prompt 和对应 decoder 方向，让模型学会直接从表征方向“读出”特征含义，无需再跑外部语料收集行为证据。

**关键结果**
实验表明，学到的 verbalization 能力泛化到未见过的 SAE 特征；可迁移到不同随机种子训练的 SAE 字典；配合轻量 adapter 可扩展到不同 LLM 的 SAE 特征。干预实验显示，注入多个 decoder 方向会生成融合多个语义的解释，而反转单个方向则产生对应的语义反转，验证了表征方向与语义的可控对应关系。
