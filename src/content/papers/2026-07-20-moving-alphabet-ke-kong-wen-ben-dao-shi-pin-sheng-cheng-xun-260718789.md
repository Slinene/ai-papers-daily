---
title: 'Moving Alphabet: A Controlled Study of Training Data for Text-to-Video Generation'
title_zh: Moving Alphabet：可控文本到视频生成训练数据研究
authors:
- Amber Yijia Zheng
- Lu Liu
- Raymond A. Yeh
- Xi Yin
affiliations:
- Meta Superintelligence Labs
- Purdue University
arxiv_id: '2607.18789'
url: https://arxiv.org/abs/2607.18789
pdf_url: https://arxiv.org/pdf/2607.18789
published: '2026-07-20'
collected: '2026-07-24'
category: Multimodal
direction: 文本到视频生成 · 训练数据重要性
tags:
- text-to-video
- training data
- caption quality
- data distribution
- procedural testbed
one_liner: 用程序化字母视频揭示数据分布与标注质量对文生视频模型泛化与训练效率的关键影响。
practical_value: '- 在电商产品视频生成中，刻意保持训练数据内容（如商品品类、场景）与视频时长的均衡分布，避免偏斜，可提升模型泛化。

  - 标注质量直接决定模型上限和收敛速度；低质量caption无法被CFG或微调完全挽救，预训练阶段就应投入资源保证标注准确性。

  - 可借鉴“程序化测试床”思路，在可控环境下快速评测数据策略（如不同的文本改写、缺失信息）对生成质量的影响，降低大规模实验成本。

  - 当训练数据存在噪声时，使用高质量子集微调可部分修复，但仍需关注源头数据清洗。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：文本到视频生成近年靠模型、数据和算力规模驱动进步，但训练数据的影响未被系统研究。真实数据的采集、清洗和标注过程复杂，难以控制变量。

**方法**：提出“Moving Alphabet”程序化测试床，通过渲染不同字体、颜色、大小、位置、运动方向和速度的字母生成视频，精确控制内容分布和标注质量。利用真值元数据生成干净caption，并通过字符删除、打乱、替换等方式构造低质量caption，在隔离环境下研究数据分布和标注质量对文生视频模型的影响。

**关键结果**：1）视频内容与时长的多样且平衡分布对模型泛化至关重要；2）caption质量显著影响模型性能和训练效率，表明文生视频模型受视频理解能力限制；3）无分类器引导和在高质量数据上微调只能部分修复劣质预训练数据带来的损害，无法完全弥补。实验为大规模文生视频模型的数据策展提供了可指导的见解。
