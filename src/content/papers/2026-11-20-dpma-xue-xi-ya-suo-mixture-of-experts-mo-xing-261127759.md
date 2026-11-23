---
title: 'DPMA: Learning to Compress Mixture-of-Experts Models'
title_zh: DPMA：学习压缩 Mixture-of-Experts 模型
authors:
- Jon Irureta
- Jon Imaz
- Philipp Wiesner
- Gorka Azkune
- Javier Fernandez-Marques
- Alex Iacob
- Andrej Jovanović
- Aizea Lojo
- Nicholas D. Lane
affiliations:
- Ikerlan Technology Research Center
- University of the Basque Country UPV/EHU
- University of Cambridge
- Science of Fundamental AI Research Lab (SOFAIR)
- Flower Labs
arxiv_id: '2611.27759'
url: https://arxiv.org/abs/2611.27759
pdf_url: https://arxiv.org/pdf/2611.27759
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: MoE 模型压缩 · 可微分剪枝合并
tags:
- MoE
- Model Compression
- Pruning
- Merging
- Routing
- Global Budget
one_liner: 提出可微分联合优化剪枝、合并与路由吸收的 MoE 压缩方法，在全局专家预算下实现层级自适应分配
practical_value: '- 部署 MoE 大模型（如 Mixtral、DeepSeek-MoE）到资源受限环境时，可借鉴 DPMA 的**全局专家预算
  + 层级自适应分配**：不再每层等比例压缩，而是根据各层对输出匹配的重要性动态决定保留专家数，实际显存节省更高效。

  - **冻结原有权重、仅用校准集优化压缩系数**的思路很适合业务迭代：无需重新训练，只做少量前向和梯度更新，即可快速产出压缩版本，风险可控，适合线上 A/B 测试不同压缩比的模型。

  - **路由吸收（absorb routing contributions）** 技巧：将剪枝专家的路由权重转发给保留专家，避免硬删专家导致路由分布突变，可减少压缩后的性能损失，在自研
  MoE 推荐/广告模型压缩时可直接复用。

  - 如果业务中使用 MoE 架构的 LLM 做特征抽取或生成，可先压缩再上线，降低 GPU 常驻显存，提升单卡吞吐，尤其适合多模型共存的推理服务场景。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：MoE 架构计算高效，但所有专家必须常驻内存，限制了在资源受限硬件上的部署。现有免训练压缩方法要么单一剪枝、要么单一合并，且通常对所有层施加统一压缩比，缺乏灵活性。

**方法关键点**：DPMA 在全局专家预算下，通过梯度下降联合学习压缩操作和逐层专家分配。引入三类可学习系数：剪枝、合并、吸收（将剪枝专家的路由权重转发给保留专家）。优化目标是最小化压缩模型与原始模型在校准集上的输出差异，原始权重完全冻结。压缩过程无需重训练，只需少量校准数据和梯度更新。

**关键结果**：在 4 个 MoE 模型、8 个多选题基准、5 种压缩比下，DPMA 在每个模型上平均准确率均超过所有对比方法。在 75% 专家削减时，DPMA 在每个模型上都优于最强基线，最大提升达 6.7 个百分点。
