---
title: 'Scaling Dense Retrieval with LLM-Annotated Training Data: Structured Mining
  and Progressive Curriculum for E-Commerce Sponsored Search'
title_zh: 利用LLM标注训练数据扩展稠密检索：电商赞助搜索的结构化挖掘与渐进课程
authors:
- Md Omar Faruk Rokon
- Shasvat Desai
- Jhalak Nilesh Acharya
- Isha Shah
- Kumar Priyam
- Brahanyaa Somasundaram
- Vamsee Tangirala
- Minuteresa Thomas
- Vivek Arora
- Vijay Manchi
affiliations:
- Walmart Global Tech
arxiv_id: '2606.23911'
url: https://arxiv.org/abs/2606.23911
pdf_url: https://arxiv.org/pdf/2606.23911
published: '2026-06-22'
collected: '2026-06-24'
category: RecSys
direction: 稠密检索 · LLM标注 · 课程学习
tags:
- Dense Retrieval
- LLM Annotation
- Curriculum Learning
- Hard Negative Mining
- E-Commerce Search
- Distant Supervision
one_liner: 用多通道检索分歧和LLM级联生成240M+结构化样本，配合三阶段课程训练，使稠密检索在Walmart线上NDCG@10提升5.1%
practical_value: '- **多通道分歧挖掘正负样本**：利用词典/BM25/现有ANN系统间的低重叠（13%-15%），自动生成easy positives（三通道共识）、hard
  positives（词汇系统命中但ANN遗漏）和hard negatives（仅单通道高分但无关），无需人工标注。任何有多路召回的业务可直接套用。

  - **校准级联减少标注成本**：Cross-Encoder(184M) → LoRA 2B LLM → LoRA 8B LLM，每类别做isotonic calibration，高置信度提前接受，含糊样本升级，在保持89.1%人类一致率下节省约50%计算。可迁移到需要大规模打分/标注的场景，尤其适合用成本换取准确率权衡。

  - **三阶段渐进课程设计**：Stage1 BCE训练“容易正+随机负”打基础，Stage2 MNR引入hard negatives学排序，Stage3 Triplet用token-similar
  negatives学语义区分。直接混合训练比课程低9.5% NDCG@10；必须严格按BCE→MNR→Triplet顺序，以BCE结尾会毁掉细粒度表征。

  - **硬标签远监督代替软蒸馏**：LLM级联离线生成hard labels，缓存复用，升级独立，不增加线上延迟。适合需要解耦标注与训练的场景，但需容忍~11%的标签噪声；文中指出当数据量足够大时深度模型可容噪改善。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商赞助搜索中，点击信号受位置偏差、尾部查询稀疏困扰，人工标注240M+对不可扩展。关键在于：多个异质检索通道（词典、BM25、现有ANN）在Top-500内重叠仅13-15%，这种分歧可被转化为结构化训练信号——全部通道一致的易正例、词汇系统命中但ANN遗漏的难正例、仅单系统高分但无关的难负例。

**方法关键点**：
- **结构化数据挖掘**：从三个生产通道收集检索结果与排名，结合LLM标注的5级相关性，将每对（query, item）分为5个难度级别：Easy Positives（三通道共识且标注相关）、Hard Positives（词汇通道前50但ANN未召回且相关）、Hard Negatives（仅单通道前100且标注无关）、Token-Similar Negatives（TF-IDF相似但未召回且无关）、Random Negatives。清洗后得240M+训练样本。
- **校准级联标注**：使用Cross-Encoder(184M)→LoRA 2B→LoRA 8B三级分类器，每类单独isotonic校准；高置信度预测提前接受，模糊样本向上传递，在5类任务上与人类评注者达89.1%一致，且比全跑所有模型节省约50%计算。
- **渐进课程训练**：Stage1用BCE损失训练Easy Positives+Random Negatives，建立基础二分类能力；Stage2用MNR损失训练Hard Positives+Hard Negatives，学习排序去混淆系统；Stage3用Triplet损失训练Token-Similar Negatives，迫使模型超越关键词匹配。顺序至关重要：以BCE结尾会破坏细粒度表征，BCE→MNR→Triplet比单阶段混合训练NDCG@10高9.5%。

**关键结果**：在30K独立人类标注查询上，模型V3（本文方案）相比点击训练的生产基线V2，NDCG@10从0.878提升至0.923（+5.1%），其中尾部查询提升最大（+6.8%），尴尬结果从8.7%降至3.5%。线上A/B测试（两周，百万级请求/臂）显示广告花费+2.80%、eCPM+2.8%、点击转化率+2.9%。消融显示：三阶段课程贡献+9.5%，多通道挖掘占+5.2%，token-similar负样本占+4.0%，per-class isotonic校准比Platt缩放提升2.1%。
