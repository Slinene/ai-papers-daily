---
title: 'Safe Alone, Unsafe Together: Safeguarding Against Implicit Toxicity When Benign
  Images Combine'
title_zh: 单图无害，多图有害：防止普通图片组合隐含的有毒语义
authors:
- Jiaxian Lv
- Shiyao Cui
- Yingkang Wang
- Guoxin Wu
- Qingling Zhang
- Minlie Huang
affiliations:
- The Conversational AI (CoAI) Group, DCST, Tsinghua University
arxiv_id: '2607.00576'
url: https://arxiv.org/abs/2607.00576
pdf_url: https://arxiv.org/pdf/2607.00576
published: '2026-07-01'
collected: '2026-07-05'
category: Other
direction: 多模态安全 · 隐含联合语义
tags:
- MIIT
- Multi-image
- Toxicity Detection
- LLM
- Distillation
- Content Moderation
one_liner: 定义多图隐含毒性（MIIT）问题，构建数据集并训练推理蒸馏模型，在审核中超越商业API
practical_value: '- 电商场景中，用户多图晒单或商品详情页的图片组合可能隐含违规（如暗示毒品器具），可借鉴多图联合推理的审核机制，将单图无害的概念纳入模型输入，提升对组合语义的捕捉能力。

  - 训练阶段采用“渐进式蒸馏推理监督”：先让强模型生成有推理链的标注，再逐步蒸馏到小模型，产出带实体关联解释的判定结果，有助于审核人员快速确认风险。

  - 工程上可设计两阶段流水线：先快速过滤单图明显违规，再对剩余多图组合进行联合编码推断隐性风险，平衡延迟与召回。

  - 数据集构造的自动化流程（利用LLM生成危险组合描述、图生成模型合成图像）可作为扩充审核负样本的手段，缓解组合风险样本稀缺问题。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

社交媒体中多图内容日益流行，催生了新的安全隐患：多图隐含毒性（MIIT），即单张图片各自无害，但组合出现时产生伤害性语义。现有内容审核API和模型因缺乏单图明显风险特征而难以检测此类组合威胁。

本文首先形式化定义MIIT，并分析其检测面临的三个主要挑战：语义关联隐蔽、缺乏标注数据、模型需具备推理能力。为解决数据稀缺，作者设计自动化生成流水线构建了MIIT-dataset，覆盖七种代表性风险类别（如暴力、色情、违法暗示），所有样本仅含图像且单张均无害。

方法核心是训练MiShield模型，利用强语言模型生成带有推理链的“渐进式蒸馏监督”，使最终的8B参数模型不仅能输出安全判定，还能给出导致危害的相关实体分析。实验表明，MiShield-8B在误检率控制在3%以内时，召回率比顶尖商业API和更大规模模型高出7-27个百分点，证明了其有效性与实用价值。
