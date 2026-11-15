---
title: 'ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research'
title_zh: ArchSpace：记录、评审与引用 LLM 架构研究的公共平台
authors:
- Jie Wang
- Tong Zhu
- JiaHao Kuang
- Zhe Xu
- Yunkai Chai
- Dehong Zheng
- Yu Cheng
- Tao Ji
- ZhouHan Lin
- Qi Zhang
affiliations:
- Shanghai AI Laboratory
- Fudan University
- Shanghai Jiao Tong University
- East China Normal University
arxiv_id: '2611.17332'
url: https://arxiv.org/abs/2611.17332
pdf_url: https://arxiv.org/pdf/2611.17332
published: '2026-11-12'
collected: '2026-11-15'
category: Training
direction: LLM 架构研究平台与 scaling laws 预测
tags:
- LLM Architecture
- Scaling Laws
- Research Platform
- Training Recipe
- Open Source
one_liner: 用 scaling laws 从小规模实验预测大模型损失，降低 LLM 架构创新验证成本
practical_value: '- **用 scaling laws 做预筛选**：在电商/广告/搜索的大模型训练中，新架构（如 MoE 替代 dense、注意力变体、新
  positional encoding）先在小规模、多组超参下跑通，用 scaling law 拟合外推预测 target 规模 loss，只对预测有增益的候选投入全量训练，可大幅降低试错算力。

  - **建立内部架构实验记录库**：模仿 ArchSpace 的 recording/reviewing 机制，把已尝试的模型改动、失败原因、训练配方沉淀为可检索条目，避免团队重复踩坑；尤其适合算力有限但需要频繁迭代
  LLM 底座的业务团队。

  - **直接复用基线配方**：平台提供的 Qwen3.5 / OLMo3 基线及 scaling law 拟合结果可作为自研 LLM 的参照系，对比自身架构修改是否在等
  loss 下带来推理效率或训练稳定性收益。

  - **关注工业界 vs 学术界引用落差**：论文数据显示工业界论文仅约 60-77%，但引用占比高达 87-96%，业务团队应更重视工业界架构报告和开源实现，而非只跟学术顶会。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 架构决定 scaling 行为、训练效率和推理成本，但工业界（DeepSeek、Qwen、Kimi 等）很少公开哪些架构创新成功/失败及原因；学术界因算力有限、基线不一致，只能做小规模单点比较，难以判断改进能否在更大规模成立。

**方法关键点**：ArchSpace 定位为公共平台，对每个架构提案记录实验与推理、由社区评审、供后续工作引用。为避免昂贵的大规模训练，平台采用业界广泛使用的 scaling laws，从小规模实验预测大模型 loss，从而低成本筛选候选架构。平台初始提供 Qwen3.5 和 OLMo3 两个 baseline collection、拟合好的 scaling laws、以及可复用的训练配方，验证通过的 idea 可成为新基线，形成闭环。

**关键结果**：平台统计了 23Q4-26Q3 的 LLM 架构论文数量与引用情况，工业界论文占比约 60.7%-77.5%，但工业界引用占比高达 87%-96.2%，说明工业界工作影响力更大但公开记录不足。ArchSpace 通过开放记录机制试图弥合这一缺口。
