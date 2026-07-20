---
title: 'CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted
  Fine-Tuning Data'
title_zh: 'CRAFT: 聚类评分标准诊断LLM弱点并生成定向微调数据'
authors:
- Vipul Gupta
- Zihao Wang
- Razvan-Gabriel Dumitru
- MohammadHossein Rezaei
- Aakash Sabharwal
- Yunzhong He
affiliations:
- Scale AI
arxiv_id: '2607.16122'
url: https://arxiv.org/abs/2607.16122
pdf_url: https://arxiv.org/pdf/2607.16122
published: '2026-07-17'
collected: '2026-07-20'
category: Training
direction: 评估驱动的弱能力诊断与定向数据生成
tags:
- CRAFT
- capability diagnosis
- fine-tuning data
- rubric clustering
- model evaluation
one_liner: 将评分标准视为能力探针，聚类构建能力树诊断模型薄弱能力，针对性生成微调数据，在专业领域显著提升性能。
practical_value: '- **用评分标准（rubric）定位能力缺口**：在电商搜索/推荐系统的模型评估中，将人工或自动评分规则（如“查询意图识别是否准确”“推荐多样性是否达标”）转化为能力探针，提取能力描述并聚类，自动发现模型在哪一类子能力上薄弱，而不仅是哪个样本出错。

  - **定向生成微调数据**：针对诊断出的弱能力节点，利用LLM批量生成针对性训练样本，避免全量数据收集的盲目性，提升数据迭代效率。例如，若诊断出“对长尾查询的语义理解弱”，可定向生成该类查询的标注数据。

  - **层次能力树动态选择粒度**：参考CRAFT的层次聚类与动态节点选择策略，在能力诊断时自适应地选择最明显的失败层级，避免过细或过粗导致的噪声，使微调更聚焦关键短板。

  - **可嵌入持续学习流水线**：在Agent或推荐系统上线后，周期性对线上badcase进行rubric标注 -> 能力诊断 -> 生成微调数据 -> 模型更新的闭环，实现持续自我改进。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有LLM评估能找出模型出错的样本或话题，但无法解释底层能力缺陷（即“为何错”），导致后续微调缺乏明确方向。

**方法**：CRAFT将评估数据集中的每个评分标准（rubric）作为能力探针。首先从prompt与对应rubric中提取能力描述，然后对这些描述进行层次聚类，构建一棵能力树。对目标模型在树上每个节点进行性能评分，再动态地从不同层次中选出表现最差的节点（选择最清晰的失败粒度）。最后，基于这些弱能力节点，定向生成监督微调数据。

**结果**：在金融和法律两个专业领域、4个开源模型、13个独立基准测试上，CRAFT均优于基于prompt聚类的EvalTree方法和随机数据生成。金融领域平均得分全面领先；法律领域在3个模型上最优，第4个模型上也在方差范围内持平。这表明在评分标准粒度上诊断能力，能更精准地发现并弥补模型短板。
