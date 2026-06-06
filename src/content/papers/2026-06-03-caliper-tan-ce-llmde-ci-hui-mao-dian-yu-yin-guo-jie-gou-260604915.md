---
title: 'Caliper: Probing Lexical Anchors versus Causal Structure in LLMs'
title_zh: Caliper：探测LLM的词汇锚点与因果结构
authors:
- Zhenyu Yu
- Shuigeng Zhou
affiliations:
- Fudan University
arxiv_id: '2606.04915'
url: https://arxiv.org/abs/2606.04915
pdf_url: https://arxiv.org/pdf/2606.04915
published: '2026-06-03'
collected: '2026-06-06'
category: Reasoning
direction: 因果推理评估 · 词汇锚点探针
tags:
- causal reasoning
- lexical anchors
- LLM evaluation
- benchmark perturbation
- placeholder tokens
one_liner: 通过替换变量名为占位符，揭示LLM的因果推理高度依赖词汇锚点而非结构推理，导致性能显著下降。
practical_value: '- 在电商推荐中，若用LLM生成解释或因果发现，需警惕模型可能仅匹配预训练中的表面词汇（如“因为促销所以购买”），而非真正理解因果结构。可借鉴Caliper的匿名化测试来验证解释模型的鲁棒性。

  - 为多Agent协作中的因果推理模块设计评估时，可采用变量名替换为占位符的方法，检查Agent是否依赖特定实体名称而非因果图，避免被虚假词汇相关误导。

  - 在生成式推荐的场景中，如果利用LLM进行用户行为因果建模，应考虑在训练或微调时引入匿名化样本，以提升对未见变量名的泛化能力，减少对词汇锚点的过拟合。

  - 该方法提供了一种通用的“压力测试”范式：任何依赖LLM做结构化推理的业务（如规则挖掘、归因分析），都可通过剥离语义词汇来探测模型是否学到了真正的结构，从而避免过度信任模型的表面表现。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM在因果推理基准（如CLadder）上可达50-70%的准确率，但不确定是真正进行了结构因果推理，还是仅利用了自然语言中常见的词汇共现（如“吸烟”→“癌症”）。为区分这两种假设，需要一种剥离表面语义的评估方法。

**方法**：提出Caliper扰动，将因果问题中的语义变量名（如“smoking”）替换为无意义的占位符（如“A”、“B”），同时完整保留因果图结构及概率规范。在9个指令微调模型（3.8B至671B参数）和3个基准（包括CRASS、e-CARE）上进行零样本测试，并进一步考察结构化脚手架和少样本上下文学习的影响。

**关键结果**：词汇匿名化后，所有模型性能大幅下降：在CRASS上平均下降29.6个百分点，e-CARE上下降18.0个百分点；在40个模型-基准组合中，39个出现正差距（匿名化后准确率更低）。CLadder的伪词子集上该差距缩小17倍，表明原始基准中的变量名提供了大量表面线索。结构化脚手和少样本ICL虽能略微缩小差距，但主要通过降低匿名化后的基线准确率实现，而非恢复原始准确率。结论：在零样本条件下，当前指令微调LLM几乎不具备结构因果推理能力，其表现高度依赖词汇锚点。
