---
title: An LLM-Powered Semantic Alignment Framework for Journal Recommendation
title_zh: 基于 LLM 语义对齐的期刊推荐框架
authors:
- Yanglin Yan
- Zicheng Xie
- Tianchen Gao
- Rui Pan
- Hansheng Wang
affiliations:
- Central University of Finance and Economics
- Peking University
arxiv_id: '2606.27930'
url: https://arxiv.org/abs/2606.27930
pdf_url: https://arxiv.org/pdf/2606.27930
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: LLM 语义对齐 · 零样本推荐
tags:
- LLM
- Semantic Alignment
- Zero-shot Recommendation
- Interpretability
- Scholarly Recommendation
one_liner: 用 LLM 将稿件内容与期刊范围进行语义匹配，实现免训练的零样本期刊推荐
practical_value: '- 在电商场景中，可将商品描述（标题、详情）与用户查询或兴趣画像进行语义对齐，直接用 LLM 做零样本商品推荐，无需训练排序模型

  - 利用 LLM 生成推荐理由，提升推荐可解释性，适合客服或导购场景下的解释性推荐

  - 冷启动场景下，无需历史交互数据，仅靠物品与用户侧文本描述即可启动推荐，适合新品或低频品类

  - 参考论文中引入“参考文献”信息可提升效果的做法，电商中可引入用户行为序列或商品关联关系作为额外上下文，进一步提升匹配质量'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统期刊推荐依赖监督学习或特征工程，泛化性和可解释性受限。该工作将推荐问题重新定义为稿件内容与期刊范围描述的语义匹配问题，利用 LLM 的内置知识直接推断，无需任务专用训练。

**方法**：构建包含文章标题、摘要、关键词的输入，并与候选期刊的范围描述配对，交于 DeepSeek-V3 进行成对语义对齐与排序。通过提示工程引导 LLM 输出推荐排名及推理理由。实验采用 49 本统计学相关期刊的 23,609 篇文章进行评估。

**结果**：仅靠语义匹配，Top-3、Top-5、Top-10 准确率分别达 40.23%、53.67%、70.05%。加入参考文献信息后效果进一步提升；多次运行稳定性高，Top-5 推荐的平均 Jaccard 相似度为 84%。输出的推理文本为推荐过程提供了可解释性。整体框架为免训练、可扩展的学术推荐提供了新范式。
