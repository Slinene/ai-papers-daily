---
title: Harnessing Domain Specialists in Multimodal Mixture-of-Experts for Efficient
  Adaptation
title_zh: 在多模态MoE中利用领域专家实现高效适配
authors:
- Damiano Marsili
- Raphi Kang
- Aditya Mehta
- Pietro Perona
- Georgia Gkioxari
affiliations:
- California Institute of Technology
arxiv_id: '2610.02123'
url: https://arxiv.org/abs/2610.02123
pdf_url: https://arxiv.org/pdf/2610.02123
published: '2026-10-01'
collected: '2026-10-04'
category: Training
direction: MoE领域专家选择与高效适配
tags:
- MoE
- Multimodal
- Expert Specialization
- Parameter-Efficient Fine-tuning
- Selective Fine-tuning
one_liner: 发现多模态MoE专家自发语义专精，ExpertLens解码路由权重定位专家并选择性微调，仅更新21.7-47%参数达4倍加速
practical_value: '- 对已有的多模态 MoE backbone（商品图/文、视频、广告创意理解等），可直接复用 ExpertLens 思路：无需新增标注数据，从
  router 权重解码出与目标域相关的专家，再做选择性微调；比全参微调便宜、比 LoRA 更稳，适合电商域迁移（如从通用视觉语言模型适配到美妆/3C 商品理解）。

  - 在需要频繁接入新业务/新类目的推荐与广告系统中，可把“专家定位—选择性更新”作为增量适配流程：只更新约 1/4~1/2 参数，训练加速约 4 倍，节省 GPU
  成本，同时保持旧任务能力。

  - 当标签稀缺或受隐私限制时，这种 data-free 的专家识别可先于标注构建领域路由，后续再小样本微调；对搜索词改写、商品属性抽取、多模态 embeddings
  等任务具有工程可行性。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

动机：MoE 的稀疏路由主要是为效率，不是为模块化；这里考察多模态 MoE 是否自发出现领域/模态专精。

方法关键点：
- 发现专家确实发展出跨模态和领域的强语义专精。
- 设计 ExpertLens：不经数据，直接从预训练 router 权重解码成语义词汇 token，定位目标领域相关专家。
- 只对相关专家做选择性微调，以获得高效多模态适配。

关键结果：
- 在 math、medical、remote sensing 任务上，ExpertLens 达到或超过全参微调。
- 仅更新 21.7–47.0% 参数，平均训练加速 4.0x。
- 适配性能和训练效率均优于 LoRA。
