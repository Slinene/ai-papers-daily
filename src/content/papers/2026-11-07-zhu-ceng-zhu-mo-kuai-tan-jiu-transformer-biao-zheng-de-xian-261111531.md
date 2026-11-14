---
title: Probing Transformer Representations Layer by Layer, Module by Module
title_zh: 逐层逐模块探究 Transformer 表征的线性探针选择
authors:
- Ambroise Odonnat
- Theo Gnassounou
- Laetitia Chapel
- Romain Tavenard
- Ievgen Redko
affiliations:
- Noah's Ark Lab
- Inria
- EPFL
- IRISA (Univ. Rennes 2)
- Schneider Electric
arxiv_id: '2611.11531'
url: https://arxiv.org/abs/2611.11531
pdf_url: https://arxiv.org/pdf/2611.11531
published: '2026-11-07'
collected: '2026-11-14'
category: LLM
direction: Transformer 表征探针选择与层/模块联合分析
tags:
- probing
- representation
- transformer
- layer-module
- vision-language
- foundation-models
one_liner: 通过 14.4 万次 probing 评估，发现层与模块需联合选择，固定策略 Act@100 与 LN2@60 可恢复大部分增益
practical_value: '- 用 LLM 提取商品/用户/会话表征做下游分类、检索或相似度匹配时，不要默认取最后一层残差流；直接尝试 LN2@60（第二层
  LayerNorm，约 60% 深度）往往比最后层更好，且少一套超参搜索。

  - 做视觉/多模态特征表示时，可优先取最后一层的前馈激活（Act@100），它在大多数探测任务中稳定优于 final residual stream，尤其当预训练到业务数据的迁移难度较大时优势更明显。

  - 如果需要在模型中间层做多尺度表征融合，不要只沿深度均匀采样；模块选择同样重要，不同层的最优模块（MLP / attention / LN）会变化，建议对候选层-模块对做小规模
  probing 验证。

  - 评估表征质量时，线性 probing 仍很有效，但固定 probe 位置（如 Act@100 / LN2@60）能显著降低搜索成本，适合快速迭代推荐模型中的特征抽取器。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：常规 probing 习惯取 Transformer 最后一层残差流，但已有工作表明中间层表征常更优；然而现有研究只沿深度观察，把每个 Transformer block 当作原子单元，忽略了内部模块（MLP、attention、LayerNorm、残差连接）的表征差异。

**方法**：对视觉基础模型（VFM）和 LLM 进行超过 144,000 次线性 probing，逐层、逐模块评估表征质量；定义“层-模块对”的最优频率，并对比固定选择策略与最优层-模块对。

**关键结果**：层和模块选择必须联合考虑——最佳层-模块对相比固定残差流的最优层，在增益上显著更大；同一层内不同模块的 probing 性能存在大幅波动，仅用深度无法刻画表征质量。简单固定策略表现良好：视觉上用最后一层前馈激活 Act@100，语言上用 60% 深度处的第二个 LayerNorm LN2@60；它们分别在多数评估中超过 probing 基线，平均恢复最佳层-模块对增益的 42% 和 86%。对 VFM，该优势随预训练到下游任务的迁移难度增加而增大。
