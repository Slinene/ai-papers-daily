---
title: 'SVD-Surgeon: Optimal Singular-Value Surgery for Large Language Model Compression'
title_zh: SVD-Surgeon：大语言模型的最优奇异值压缩手术
authors:
- Mahmoud Safari
- Frank Hutter
affiliations:
- University of Freiburg
- Prior Labs
- ELLIS Institute Tübingen
arxiv_id: '2606.23568'
url: https://arxiv.org/abs/2606.23568
pdf_url: https://arxiv.org/pdf/2606.23568
published: '2026-06-22'
collected: '2026-06-23'
category: LLM
direction: 低秩压缩 · 二阶损失补偿
tags:
- SVD
- model compression
- LLM
- OBS
- training-free
- pruning
one_liner: 将OBS框架引入SVD压缩，闭式更新保留奇异值以补偿截断损失，无需重训练
practical_value: '- 将OBS补偿思想直接用于LLM的SVD压缩，无需微调即可提升压缩后模型质量，适合对延迟敏感的在线推荐或Agent系统快速迭代部署

  - 奇异值重要性评估可指导结构化剪枝决策，例如在广告召回模型中按重要度保留关键秩，平衡吞吐与精度

  - 方法即插即用，可叠加到现有SVD-LLM等压缩器上，工程实现成本低，可直接复用以压缩推荐系统中的语义编码器或生成模型

  - 闭式更新公式仅需二阶导数信息，计算开销小，适合在大规模模型压缩流水线中作为后处理步骤'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM部署面临显存和计算瓶颈，SVD低秩压缩有效但现有方法只关注如何分解或保留哪些分量，忽略了被截断奇异值对损失的影响。

方法：将OBS框架迁移到奇异值域，将每个奇异值视为可训练参数，通过二阶泰勒展开推导出保留奇异值的闭式补偿更新，理论上等价于最小化压缩带来的损失增量。同时，利用二阶导数信息计算每个奇异值的显著度，指导截断选择。整个过程无需任何重训练或梯度下降。

结果：在SVD-LLM基础上叠加该方法，OPT-6.7B和LLaMA 2-7B上困惑度在同等压缩率下平均降低0.3-0.5点，提升压缩效率10-15%，且完全训练无关。
