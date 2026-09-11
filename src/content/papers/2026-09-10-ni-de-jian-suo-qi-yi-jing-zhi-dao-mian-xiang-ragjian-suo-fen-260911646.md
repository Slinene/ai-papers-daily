---
title: 'Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency'
title_zh: 你的检索器已经知道：面向RAG检索充分性的分布形状QPP
authors:
- Matyáš Veselý
- Michal Průšek
- Jiří Franc
affiliations:
- Department of Mathematics, FNSPE CTU in Prague
- Institute of Information Theory and Automation, Czech Academy of Sciences
arxiv_id: '2609.11646'
url: https://arxiv.org/abs/2609.11646
pdf_url: https://arxiv.org/pdf/2609.11646
published: '2026-09-10'
collected: '2026-09-11'
category: RAG
direction: RAG检索充分性预测 · 分布形状QPP
tags:
- Query Performance Prediction
- RAG
- Retrieval Sufficiency
- Distribution Shape
- Abstention
- Vision Document Retrieval
one_liner: 24个分布形状特征2ms预测RAG检索充分性，AUROC 0.856超过LLM judge 0.649
practical_value: '- 在电商/搜索推荐RAG链路中，可以用检索/召回分数向量的分布形状特征（top1-top2 gap、top-10 std、decay
  slope、bimodal gap、gap concentration等）构造轻量「检索充分性/置信度」模型，判断top-k是否含可回答结果；无需读商品内容或调用LLM，2ms级在线可自动触发query改写、扩大召回或直接生成答案。

  - LLM judge不要单独做置信度，把其分数作为额外特征加入小分类器（Logistic/Ridge/MLP）形成hybrid：在安全关键/对抗query上AUROC更高（SÚJB
  adversarial-detection 0.954），且误答率从12–16%压到6–7%；若LLM推理已在链路中，这种as-feature组合比单独judge更值得用。

  - 多领域/多站点迁移建议用lean特征子集：全量24特征LODO从0.856掉到0.706，而13特征S1-Lean（8分布+5query-surface）恢复到0.719并改善校准；跨域部署优先选lean子集而非全量模型。

  - 对无答案/对抗query检测，分数分布形状尤其有效：unanswerable query的top-k分数分布平坦，S1在SÚJB对抗检测AUROC 0.934
  vs MaxSim 0.489；可作为推荐系统防冷启动、防误导、防幻觉的置信度开关。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机：** RAG推理时缺少可靠的检索成功信号，模糊或域外query下生成易幻觉；安全关键部署（如捷克核监管SÚJB）禁止第三方LLM API，需要本地、极低延迟、便宜的pre-generation检索充分性预测。

**方法关键点：**
- 比较三种范式：score-based（S0–S4）、content-based LLM judge（C1）、hybrid（H1–H3）。
- GeneralQPP（S1）只用24个非词法特征：15个分数分布形状（top1–p99 gap、top-10 std、decay slope、bimodal gap、exp decay rate、top-50 skewness、gap concentration等）、5个query-surface（字符/词数、数字、标点、平均词长）、4个全局相似度统计；不读文档内容。
- 训练轻量分类器（Logistic / Ridge / MLP），3-fold CV选架构；标签为Hit@k（top-k中是否含self-sufficient page）。
- LLM judge C1为Qwen3.5-35B-A3B-FP8多模态MoE，读页面图像输出0–100分和sufficient flag；混合方案H2把LLM分数作为第25个特征输入分类器。

**关键结果：**
- ViDoRe 8域14,514 queries：S1加权AUROC 0.856，高于经典QPP池S4 0.835、C1 0.649；S1比C1快约3000倍（2ms vs 6.3s）。
- SÚJB部署case：H2 Hit@5 AUROC 0.911、adversarial-detection 0.954；H2在100条对抗unanswerable上误答率仅6–7%，明显低于S4 12–16%。
- LODO跨域：S1从0.856掉到0.706；13特征S1-Lean恢复到0.719，并改善校准。
- 不同数据集方法排名一致，Spearman ρ=0.90。

**值得记住：** 检索分数分布形状本身足以在2ms内可靠预测检索充分性，超过单独LLM judge；本地LLM判断作为额外特征比作为独立预测器更有价值。
