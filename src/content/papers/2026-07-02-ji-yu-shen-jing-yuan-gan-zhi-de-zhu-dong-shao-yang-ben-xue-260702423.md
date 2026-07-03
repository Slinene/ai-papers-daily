---
title: Neuron-Aware Active Few-Shot Learning for LLMs
title_zh: 基于神经元感知的主动少样本学习用于大语言模型
authors:
- Zhuowei Chen
- Liwei Chen
- Christian Schunn
- Raquel Coelho
- Xiang Lorraine Li
affiliations:
- University of Pittsburgh
arxiv_id: '2607.02423'
url: https://arxiv.org/abs/2607.02423
pdf_url: https://arxiv.org/pdf/2607.02423
published: '2026-07-02'
collected: '2026-07-03'
category: LLM
direction: LLM少样本选择 · 内部表征利用
tags:
- Active Few-Shot Learning
- Neuron Activation
- Hallucination
- In-Context Learning
- Dual-Criteria Selection
- Domain Adaptation
one_liner: 通过神经元激活模式替代输出层信号，同时考虑多样性和易幻觉样本，更有效地挑选少样本标注数据
practical_value: '- 电商/搜索推荐场景中，若需用少样本示例将通用LLM适配到特定垂直领域（如商品分类、Query意图识别），可借鉴NeuFS的神经元激活模式筛选样本：用激活向量聚类保证样例多样性覆盖领域知识，同时通过神经元共识度量化样本的“易幻觉”程度，优先标注这类高信息量样本，减少人工标注量。

  - 内部神经元信号比外部embedding（如SimCSE）更能捕捉模型自身知识缺口，在做LLM评测或诊断时，可以分析神经元激活分歧来定位模型在哪些Query/商品上更容易产生幻觉，进而针对性补充训练数据。

  - 该方法依赖对LLM神经元激活的访问，对于仅提供API的黑盒模型不适用；但在自有部署的开源LLM上（如LLaMA），可将其集成到数据飞轮流程中，实现持续、低成本的模型垂直调优。

  - 双准则选择策略（多样性+幻觉倾向）可解耦后单独使用：多样性准则可迁移到推荐系统的物品表征学习或Review示例选取；幻觉倾向量化可为对话式推荐Agent的回复可靠性评估提供信号参考。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：通用LLM在垂直领域（教育、医疗、法律）仅靠标准ICL效果有限，主动少样本学习（AFSL）通过挑选最有价值的未标注样本来降低人工成本。现有方法依赖输出层信号（预测熵、外部语义嵌入）而忽略模型内部动态，无法精准定位知识缺口。

**方法**：提出NeuFS，改用LLM内部神经元激活模式表征样本：
1. **多样性保障**：对未标注池的样本用激活向量聚类，选取簇中心样例，保证覆盖广泛知识。
2. **幻觉样本识别**：引入“神经元共识”指标——神经元激活模式中独特激活的数量，共识度低的样本对应模型知识薄弱点，更易产生幻觉，优先挑选标注。
双准则结合，实现既多样又具挑战性的少样本选择。

**结果**：在三个数据集的推理与文本分类任务上，NeuFS均超越现有AFSL基线；消融实验证实内部神经元激活比外部嵌入（如SimCSE）更有效，选择信号更原则性和高效。
