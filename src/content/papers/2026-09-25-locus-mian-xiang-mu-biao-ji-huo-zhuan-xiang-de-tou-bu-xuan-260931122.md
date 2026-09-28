---
title: 'LocUS: Head Selection and Subspace Projection for Targeted Activation Steering'
title_zh: LocUS：面向目标激活转向的头部选择与子空间投影
authors:
- Irene Tallini
- Lorenzo Basile
- Valentino Maiorca
- Francesco Locatello
- Alberto Cazzaniga
affiliations:
- Area Science Park, Trieste, Italy
- Institute of Science and Technology Austria
- Université Côte d'Azur, Inria, LJAD, Maasai Project Team, Nice, France
arxiv_id: '2609.31122'
url: https://arxiv.org/abs/2609.31122
pdf_url: https://arxiv.org/pdf/2609.31122
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM 推理时激活转向 · 低秩子空间
tags:
- Activation Steering
- LLM
- Inference-time Intervention
- Subspace Projection
- Head Selection
- Safety
one_liner: LocUS 将激活转向约束到输出词汇子空间并稀疏选择注意力头，以干预<6%参数匹配或超越 SOTA 并更好保持通用能力
practical_value: '- 在电商客服/导购 Agent 中，可用 LocUS 做实时安全/合规控制：基于对比数据估计转向方向，但通过 unembedding
  子空间投影和稀疏头部选择，仅干预 <6% 参数，避免大幅损害商品推荐能力。

  - 利用模型原始 unembedding 矩阵作为属性子空间来源，无需额外训练即可定位特定属性（如“负评倾向”）对应的输出方向，并在局部修正，此法可复用于生成式推荐中的风格/属性控制。

  - 对 LLM 生成推荐理由或商品描述的场景，可对生成的语义属性（如情绪、说服力）做 targeted steering，同时不改变物品 ID 或事实准确性，保持通用能力不下降。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：标准激活转向在推理时控制 LLM 行为，但通常从对比数据估计每层方向并作用于整个表示空间，容易耦合无关属性、损害通用能力。

方法关键点：LocUS（Localized Unembedding Steering）将激活转向建立在模型自身的输出词汇子空间上。具体地，在 unembedding 矩阵中识别特定属性的线性子空间，施加几何约束，使转向变换仅在该子空间内进行；同时将干预局部化到稀疏的注意力头子集，而非整个层。这种设计不仅限制干预范围，还显著减少需要修改的参数。

关键结果：在三个模型家族上针对毒性缓解、情感重定向和谄媚抑制任务评估，LocUS 匹配或超越了现有最优基线，同时只干预不到 6% 的参数，并更好地保持一般能力。
