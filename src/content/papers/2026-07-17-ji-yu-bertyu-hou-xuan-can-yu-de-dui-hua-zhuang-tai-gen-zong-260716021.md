---
title: Candidate Attended Dialogue State Tracking Using BERT
title_zh: 基于BERT与候选参与的对话状态跟踪
authors:
- Junyuan Zheng
- Onkar Salvi
- John Chan
affiliations:
- OneConnect US Research Institute
arxiv_id: '2607.16021'
url: https://arxiv.org/abs/2607.16021
pdf_url: https://arxiv.org/pdf/2607.16021
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 对话状态跟踪 · 零样本迁移
tags:
- Dialogue State Tracking
- BERT
- Zero-shot
- Multi-domain
- Schema-based
- Scalability
one_liner: 利用预训练BERT和候选注意力实现多领域零样本对话状态跟踪，显著提升可扩展性
practical_value: '- **零样本领域迁移**：在电商客服或购物助手中，新产品类别（如新增家电品类）无需重新标注对话状态数据，直接用预训练BERT编码schema即可上线，大幅降低冷启动成本。

  - **候选注意力机制**：对schema中的每一个槽位候选值进行打分，该设计可复用于推荐系统的多意图识别或槽位填充，例如在商品搜索中同时判断用户指定的品牌、价格区间等约束条件。

  - **轻量工程实现**：整个模型仅基于BERT微调，不依赖复杂本体或额外知识库，适合快速集成到现有对话Agent架构中，作为可插拔的DST模块。

  - **跨域泛化验证**：在SGD数据集上平均目标槽准确率达到**88.7%**，较基线提升**15个点以上**，证明预训练语言模型在结构化对话理解上的迁移潜力，可推广至任务型搜索代理（如机票/酒店比价Agent）。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：任务型对话系统需要支持大量服务与API，传统DST依赖领域特定训练，难以快速扩展到新领域。针对零训练数据场景，需要一种可零样本迁移的多领域DST框架。

**方法**：提出基于BERT的候选注意对话状态跟踪模型。将对话历史和schema定义拼接后输入BERT，获得上下文表示；对每个槽位，从schema中生成候选值列表，通过候选注意力机制计算每个候选的得分，选择最高分作为状态预测。该设计使得模型不依赖领域特定的槽位名称，仅通过schema文本描述即可泛化。训练时在多个源领域联合学习，推理时直接应用到未见过的目标领域，无需任何微调。

**结果**：在Schema-Guided Dialogue (SGD) 数据集上评估，零样本设置下平均目标槽准确率达到**88.7%**，相比基线方法提升超15个百分点，证明了预训练语言模型在结构化对话状态跟踪中的强泛化能力。
