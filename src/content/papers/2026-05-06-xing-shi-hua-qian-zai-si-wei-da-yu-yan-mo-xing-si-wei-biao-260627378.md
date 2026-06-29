---
title: 'Formalizing Latent Thoughts: Four Axioms of Thought Representation in LLMs'
title_zh: 形式化潜在思维：大语言模型思维表征的四条公理
authors:
- Fahd Seddik
- Fatemeh Fard
affiliations:
- University of British Columbia
arxiv_id: '2606.27378'
url: https://arxiv.org/abs/2606.27378
pdf_url: https://arxiv.org/pdf/2606.27378
published: '2026-05-06'
collected: '2026-06-29'
category: Eval
direction: LLM 思维表征的公理化评估
tags:
- LLM
- Representation Evaluation
- Axiomatic Framework
- Reasoning
- Latent Thought
one_liner: 提出四条表征公理并审计发现现有LLM的潜在思维表征均无法同时满足，显露出结构性缺陷
practical_value: '- 若在电商搜索/推荐中引入LLM处理查询或生成推荐理由，可借鉴四条公理（因果性、极小性、可分离性、稳定性）自评模型内部表征，诊断其是否真正编码了任务相关信息而非表面统计

  - 面对Agent规划时，评估隐状态是否对不同子目标具备可分离性、对同任务扰动是否稳定，从而在部署前定位结构性问题，避免仅凭下游任务指标误判

  - 在生成式推荐模型中，检查生成item的隐向量是否满足因果性（关键输入token促成了表征）、极小性（冗余信息少），可帮助优化编码器结构

  - 该框架提供了一套与基准分数解耦的表征评测量化方法，可直接嵌入内部模型评估管线，用于对比不同训练策略或架构对表征质量的影响'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有对LLM连续思维表征的评估完全依赖下游任务准确率，无法区分是表征质量差还是模型处理能力不足。不同工作发现表征在早期层坍塌但准确率不变，因此迫切需要功能性的表征评估框架。

**方法**：作者形式化四条功能性公理——**因果性**（表征应由相关的输入token导致）、**极小性**（表征应丢弃无关信息）、**可分离性**（不同任务的表征应可区分）、**稳定性**（同任务不同输入的表征应相似），并为每条公理定义直接作用于表征的量化度量，与下游准确率完全解耦。

**结果**：审计多个开源LLM在23个推理任务（如空间推理、事实QA）上的隐层表征，发现：没有模型同时满足全部公理；表征能可靠地区分任务类型，却无法区分同一任务内的不同问题；表征编码的信息几乎不超出输入嵌入已有的内容。这一缺陷在密集、推理蒸馏和RL训练模型家族中一致出现，表明是结构性的，而非模型规模或训练过程所致。
