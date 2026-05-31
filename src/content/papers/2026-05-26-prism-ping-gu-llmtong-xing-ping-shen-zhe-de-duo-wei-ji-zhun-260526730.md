---
title: 'PRISM: A Multi-Dimensional Benchmark for Evaluating LLM Peer Reviewers'
title_zh: PRISM：评估LLM同行评审者的多维基准
authors:
- Ngoc Phan Phuoc Loc
- Toan Huynh La Viet
- Thanh Tran Khanh
- Duy A Nguyen
- Tuan Anh Nguyen Pham
- Thanh Nguyen
- Nitesh V. Chawla
- Wray Buntine
- Kok-Seng Wong
- Khoa D. Doan
affiliations:
- VinUniversity
- University of Illinois, Urbana-Champaign
- University of Notre Dame
- Monash University
arxiv_id: '2605.26730'
url: https://arxiv.org/abs/2605.26730
pdf_url: https://arxiv.org/pdf/2605.26730
published: '2026-05-26'
collected: '2026-05-31'
category: Eval
direction: LLM评审质量多维度基准评估
tags:
- LLM reviewers
- peer review
- benchmarking
- multi-dimensional evaluation
- retrieval-augmented verification
- argument mining
one_liner: 提出多维度评估框架，揭示LLM评审在单一维度可匹敌人类但整体平衡不足，存在明显能力盲点。
practical_value: '- **多维度细粒度评估范式可迁移**：将“深度、新颖性、缺陷优先级、建设性”拆解为独立可测维度的思路，可直接用于电商评价内容质量审核、客服话术打分等场景，避免单一指标掩盖细节问题。

  - **检索增强验证思路可直接复用**：在评估新颖性或事实性时引入外部知识库验证（类似RAG），适合商品描述真实性检验、UGC内容虚假信息检测等任务。

  - **基于共识的打分机制可减少主观偏差**：结合人工标注与模型判断的共识评分方法，可借鉴到推荐系统的离线评估中，提升标注样本的一致性和评估稳定性。

  - **主要面向学术审稿场景，业务直接借鉴有限**：整体框架强绑定学术论文属性，在电商推荐和Agent优化中的模型评估环节有部分启发，但无法直接套用。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：顶级ML会议投稿量激增，传统同行评审不堪重负，LLM自动审稿方案涌现，但缺乏对审稿质量的多维度深入评估，现有评测依赖ROUGE等浅层指标或泛化的LLM-as-a-judge，无法区分流畅性与严谨性。

**方法**：提出PRISM基准，围绕分析深度、新颖性评估、缺陷识别与主要问题优先级、多维度建设性四个维度，采用论据挖掘、检索增强验证和共识评分进行度量，在ICLR/ICML/NeurIPS分层抽样的真实评审数据集上，对比五种主流自动审稿系统与人类评审。

**关键结果**：LLM在单一维度表现亮眼——分析深度与人类相当，新颖性验证更强，缺陷优先级排序高度准确；但没有任何系统在所有维度上达到人类的均衡水平，各系统存在明显专长和盲区（如某些系统深度好但缺陷识别弱），聚合指标无法暴露这类失败模式。因此LLM更适合作为有针对性的人类评审补充，而非完全替代。
