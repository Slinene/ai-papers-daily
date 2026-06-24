---
title: 'Unified Multi-Task Relevance Modeling for E-Commerce: Comparing Task Routing
  Architectures Across LLMs and Cross-Encoders'
title_zh: 电商统一多任务相关度建模：对比LLM与Cross-Encoder的任务路由架构
authors:
- Md Omar Faruk Rokon
- Jhalak Nilesh Acharya
- Shasvat Desai
- Hong Yao
- Kuang-chih Lee
affiliations:
- Walmart Global Tech
arxiv_id: '2606.23919'
url: https://arxiv.org/abs/2606.23919
pdf_url: https://arxiv.org/pdf/2606.23919
published: '2026-06-22'
collected: '2026-06-24'
category: RecSys
direction: 多任务相关度建模 · 任务路由架构
tags:
- Multi-Task Learning
- Relevance Modeling
- Task Routing
- LoRA
- Cross-Encoder
- E-Commerce Search
one_liner: 首次对比三种任务路由架构在LLM和Cross-Encoder上的效果，发现解码器仅靠文本前缀时若去掉前缀会崩塌，私有层可完全恢复，多任务训练提升低资源任务最高+14%。
practical_value: '- **多任务框架设计**: 将6种实体对关系（query-ad, query-query, ad-ad等）统一用三点相关度分级联合训练，利用数据丰富任务（如query-ad）的知识转移到低资源任务（如product-type-product-type），直接提升低资源任务准确率最高14%，适合电商搜索推荐中多种相关性场景的统一建模。

  - **任务路由选择**: 对于Cross-Encoder，用文本前缀就够了，去掉前缀换成多分类头几乎无损失（~1%）；对于decoder-only LLM，**必须加私有Transformer层**（MHP），否则去掉文本前缀后模型会崩塌（Gemma-2-2b从87.14%掉到55.59%）。如果用LoRA微调LLM做多任务，务必配套私有层。

  - **集成方案**: 将LLM和Cross-Encoder的MHP模型做多数投票，利用两类模型的错误多样性（如LLM在抽象任务上更强，Cross-Encoder在词汇丰富任务上更强），在453K测试集上达到89.96%准确率，比文本前缀集成高1.92%，且MHP私有层训练出的模型多样性更强，适合构建高精度离线标注或线上集成。

  - **工程效率权衡**: Gemma-2-2b（2B）用LoRA（~2M可训参数）搭配MHP后准确率88.04%，接近Llama-3-8b（88.27%），且推理速度快于大模型，适合低延迟线上场景；ModernBERT（396M）用于批量离线标注效果最好（97.81%在ad-ad任务），但泛化到抽象任务弱，可按任务类型选模型。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商平台需要同时评估多种实体对的相关度（query-ad, query-query, ad-ad等六种），传统做法为每种任务单独训练模型，推理成本高且无法知识迁移。本文试图用一个统一多任务模型覆盖所有关系类型，利用数据量不同实现从富裕任务到稀缺任务的正迁移，并探讨如何将任务身份告知共享模型（任务路由），发现encoder与decoder模型对此存在不对称性。

**方法关键点**
- 将六种任务统一为三分类（Irrelevant, Partially Relevant, Relevant），共享同一个模型骨干。
- 任务路由架构比较： (1) 文本前缀（SH）：在输入前拼接任务描述字符串； (2) 多头分类（MH）：去掉前缀，用任务ID选择各自线性分类头； (3) 私有层+多头（MHP）：在共享编码器后、分类头前插入两层任务私有Transformer层。
- 模型家族：LoRA微调的decoder-only LLM（Gemma-2-2b, Llama-3-8b）和全参数微调的Cross-Encoder（ModernBERT, ELECTRA等）。
- 数据构造：以80万人工标注query-ad对为种子，通过共相关、分类层级和embedding相似度衍生出其余5个任务（共227万样例），并经人工验证（Cohen’s κ≥0.76）。

**关键实验与结果**
- 在453K测试集上，MHP集成（Gemma+Llama+ModernBERT的多数投票）达到89.96%准确率，超越最强单模型（89.26%）和文本前缀集成（88.04%）。
- 多任务训练带来显著提升：低资源任务T5（PT-PT）提升+14.07%，T2（Q-Q）提升+7.22%，但最大任务T1（Q-Ad）有轻微负迁移。
- 任务路由不对称：Cross-Encoder切换为MH仅损失~1%，而Gemma-2-2b掉落31.55%至55.59%（训练崩塌），添加两层私有后完全恢复并略超基线。
- 部分相关（Partially Relevant）类别最难，调高该类损失权重可提升其召回但牺牲其他类。

**核心洞察**：Decoder-only LLM依赖输入前缀进行任务条件化，而Cross-Encoder的[CLS]汇总全局上下文，任务身份传达方式需因模制宜；私有层是LLM多任务路由的安全选择。
