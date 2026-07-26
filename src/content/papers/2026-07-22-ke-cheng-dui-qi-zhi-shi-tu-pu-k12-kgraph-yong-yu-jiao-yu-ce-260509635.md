---
title: 'K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training
  Educational LLMs'
title_zh: 课程对齐知识图谱 K12-KGraph 用于教育LLM评测与训练
authors:
- Hao Liang
- Qihan Lin
- Zhaoyang Han
- Xiaochen Ma
- Zhen Hao Wong
- Meiyi Qiang
- Linzhuang Sun
- Wentao Zhang
affiliations:
- Peking University
- Institute for Advanced Algorithms Research, Shanghai
- OriginHub Technology
- Zhongguancun Academy
arxiv_id: '2605.09635'
url: https://arxiv.org/abs/2605.09635
pdf_url: https://arxiv.org/pdf/2605.09635
published: '2026-07-22'
collected: '2026-07-26'
category: Eval
direction: 教育LLM课程认知评估与图引导训练
tags:
- Knowledge Graph
- Curriculum Cognition
- Educational LLMs
- VQA
- SFT
- Benchmark
one_liner: 构建课程知识图谱并衍生多任务基准，暴露大模型在前提推理等课程认知上的短板，并以图引导数据高效微调
practical_value: '- **在电商知识图谱上复制多任务QA生成**：借鉴从领域KG自动衍生Ground/Prereq/Neighbor等任务模板的方式，为电商商品搭配、选购意图、类目归属等场景快速构建大规模评测集，低成本评估模型对商品结构化关系的认知。

  - **构建商品认知微调数据**：参考K12-Train的图引导监督微调数据生成流程（将节点与关系转为自然语言QA，包括纯文本与多模态图文对），用商品知识图谱合成训练样本，提升LLM在导购、属性问答、搭配推荐解释上的表现。

  - **领域特定SFT数据效率极高**：实验证明，在相同样本量下，结构清晰的领域SFT数据（K12-Train-Text）碾压等量的通用SFT语料，说明用少量高质量的领域知识图谱衍生数据即可获得明显收益，电商场景可效仿。

  - **多模态互补的设计**：论文发现文本与视觉监督互补，单独任一都不如联合训练好；在产品搜索推荐中，可同时使用物品图片与结构化文本描述进行对齐训练，增强模型对视觉特征与商品属性的整合能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有教育大模型评测仅关注做对题（事实记忆），忽略模型对课程知识结构化和视觉呈现的理解（课程认知），即前提链、概念层级、实验关联等。为填补这一空白，需要一套对齐课程大纲的知识图谱及配套评测。

**方法**：作者从人教版数学、物理、化学、生物教材中抽取构建K12-KGraph，包含书籍、章节、概念、技能、实验、图表等9类节点和14种关系。基于图谱，自动生成多选评测集K12-Bench（23,640题），覆盖Ground（概念定位）、Prereq（前提关系）、Neighbor（邻居推理）、Evidence（实验证据）和Locate（视觉定位）五类任务。同时合成图引导的监督微调数据K12-Train，含2,267条纯文本QA和5,068条图文VQA。

**关键结果**：最强闭源模型Gemini-3-Flash在K12-Bench准确率仅57%，开源模型Gemma-4-31B-IT为46%，Prereq和Neighbor任务尤其薄弱。在严格匹配2,300条样本下，K12-Train-Text微调在GaokaoBench和EduEval上显著超越OpenHermes、WizardLM等8种主流SFT数据的等量子集。多模态训练更优，K12-Train-Full在Gaokao-MM等基准上表现最佳，且文本与视觉相互补充。论文开源了图谱、基准、数据和构建流程。
