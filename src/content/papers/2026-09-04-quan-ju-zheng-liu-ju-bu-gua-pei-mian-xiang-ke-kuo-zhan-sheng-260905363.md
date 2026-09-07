---
title: 'Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time
  Training for Scalable Trade-Up Recommendation'
title_zh: 全局蒸馏、局部适配：面向可扩展升级推荐的推理蒸馏与产品类型测试时训练
authors:
- Siliang Liu
- Mohammad Ghasemi
- Sapan Patel
- Amin Banitalebi-Dehkordi
affiliations:
- Amazon Everyday Essentials Technologies
arxiv_id: '2609.05363'
url: https://arxiv.org/abs/2609.05363
pdf_url: https://arxiv.org/pdf/2609.05363
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: LLM知识蒸馏与测试时适配用于商品关系推荐
tags:
- LLM Distillation
- Test-Time Training
- Trade-Up Recommendation
- E-commerce
- Reasoning Distillation
- Product Relations
one_liner: 将LLM推理蒸馏成轻量embedding对分类器，并用商品类型级测试时训练进一步适配，实现无LLM推理的高效升级推荐
practical_value: '- **离线蒸馏替代在线LLM**：在电商catalog级商品关系判定中，用LLM离线生成标注+理由，蒸馏到15.5M参数embedding-pair分类器，推理仅需两个预计算768维向量，速度提升5000倍，成本降低10000倍。该方法可直接迁移到商品替代/互补关系、query-商品匹配等大规模打分任务。

  - **保留细粒度标签比二分更有效**：蒸馏时保留LLM的四分类（similar、反向升级、升级、不相关）标签比合并成二分类更能让rationale监督发挥作用（AUC
  0.912→0.924 vs 0.911→0.911）。在业务中若关系本身有方向或等级，不要为了简化而合并类别。

  - **按品类/商品类型做轻量测试时适配**：每个product-type用少量专家标注support set（K=32）微调LoRA adapter，比全局统一adapter提升更显著（AUC
  0.940 vs 0.929），而且推理成本不变。适合新品冷启动或品类间标准差异大的场景。

  - **Support set复用降低标注成本**：同一批专家标注示例既作为LLM的few-shot演示，又作为测试时训练的梯度监督，最大化样本利用率。工程实现时可将此设计为统一的数据pipeline。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：电商中trade-up推荐需要区分有意义的升级与同层替代、变体或数量变化，方向性强且依赖品类特定标准。LLM虽能捕捉细微区别，但对数亿商品对直接推理成本过高且延迟大。本文用两阶段框架将LLM知识压缩到轻量判别模型。

**方法关键点**：
- **Level 1：全局推理蒸馏**。用检索增强的few-shot LLM teacher对每个pair生成四分类标签和自然语言理由；学生是纯embedding-pair MLP分类器，输入预计算的base/candidate 768维嵌入，无文本生成。训练目标包含任务损失（加权focal BCE或交叉熵）、理由对齐MSE、对比InfoNCE+关系KL。推理时丢弃投影头，只用15.5M参数的前向网络。
- **Level 2：产品类型测试时训练（PT-TTT）**。对每个product type，用K个专家标注support examples微调冻结学生上的LoRA adapter（只插入分类头和投影层，约67K参数），目标为task loss + optional rationale MSE。每个品类独立训练adapter，但推理时amortized，不需要LLM。

**关键实验**：
- 训练数据：1,019,241对LLM标注silver pairs；评测：8,352对human golden benchmark（29个品类）。
- 最佳Level 1模型：shallow 15.5M四分类推理蒸馏学生，AUC 0.924（95% CI[.918,.929]），优于同架构label-only（0.912）和更大deep模型（0.887）；二分类下rationale无增益。
- PT-TTT：K=32时AUC提升到0.941（+0.017），AP 0.940；label-only达到0.940，说明增益主要来自品类特定适配而非理由重用。
- 匹配人类监督控制：pooled adapter仅提升到0.929，证明product-type-specific适配有价值；macro PT-AUC从0.910升到0.925，说明并非仅跨品类分数缩放。
- 规模：100K对推理比直接LLM快~5000倍，成本低~10000倍。

**最值得记住的一句话**：细粒度标签与理由蒸馏互补，品类级测试时适配进一步释放性能，全程无推理时LLM调用。
