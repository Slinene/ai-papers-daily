---
title: 'Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence
  Scoring and Abstention'
title_zh: 多跳检索可预测失效：分数分布置信度评分与弃权
authors:
- Andre Bacellar
arxiv_id: '2609.22056'
url: https://arxiv.org/abs/2609.22056
pdf_url: https://arxiv.org/pdf/2609.22056
published: '2026-09-18'
collected: '2026-09-21'
category: RAG
direction: RAG 多跳检索 · 置信度评分与弃权
tags:
- multi-hop retrieval
- confidence scoring
- abstention
- RAG
- calibration
- selective prediction
one_liner: 提出基于检索分数分布特征的轻量级置信度评分RCS，实现多跳RAG的校准弃权，降低高置信错误率
practical_value: '- 利用检索分数分布特征（top-k最大分数、margin、lift、top3均值、熵）构建零额外LLM推理的置信度评分RCS，可在电商搜索/推荐召回后实时判断结果可信度（<1ms），对低置信query触发精排兜底或人工介入，避免高置信错误。

  - 定义CWAR并采用弃权策略：在覆盖率-准确率曲线上根据业务目标选择阈值，可在规定错误率下最大化自动回答覆盖率，适合电商导购Agent中控制高成本错误。

  - 特征互补性结论：不同领域的数据集中主导置信度特征不同（如query长度 vs hop-1分数集中度），提示我们不要依赖单一检索分数阈值，应使用多特征逻辑回归融合，增强跨场景稳健性。

  - 跨域迁移性：该置信度模型跨数据集迁移仅损失0.5pp AUC，说明这些结构性特征领域无关，电商多品类场景可通过少量标注数据训练得到通用置信度模型，降低标注成本。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
多跳检索失败并非均匀分布，而是聚集在结构性可预测的子群体中。现有RAG系统总是返回top-k结果，即使证据不完整也没有信号告知下游。例如在MuSiQue测试中，39.5%的查询未能检索到全部gold passages，却仍被系统自信地输出。这种高置信错误在事实核查、问答等场景代价很高，因此需要支持第三种动作——弃权（abstention），在检索质量低时返回低置信信号。

**方法关键点**  
- 定义 **CWAR**（Confident-Wrong-Answer Rate）度量高置信回答中的错误率，并定义 **AUC-AC**（准确率-覆盖率曲线下面积）评估置信度排序能力。  
- 提出 **RCS**（Retrieval Confidence Score），一个逻辑回归函数，输入9个从ANN分数分布中提取的查询-特征：hop1-max、hop1-margin、hop1-top3均值、hop1熵、hop1-lift、hop2-max、hop2-margin、hop2熵、query长度；这些特征均在检索后立即可得，无需额外LLM调用。  
- 训练使用二分类交叉熵，阈值选择基于验证集上达到目标CWAR的最小阈值，保证校准性。  
- 理论证明：CWAR可约减当且仅当检索特征与成功有互信息；且没有单一ANN分数特征在所有失效体制中最佳，存在特征互补性。  

**关键实验**  
在三个多跳基准（MuSiQue, 2WikiMultiHopQA, HoVer）和两种检索架构（LLM-judge与dense-only）共五种失效体制上，与8个基线（random, entropy, max-score, margin, lift, query-len-inv, temp-scaled, MLP）对比。RCS在所有五个条件下取得最佳或并列最佳AUC-AC。在MuSiQue LLM-judge pipeline上，RCS AUC-AC=0.790，50%覆盖率时CWAR从39.5%降至20.6%（相对下降47.8%），ECE=0.035。跨数据集迁移：在MuSiQue训练、2Wiki测试AUC仅降0.5pp。特征重要性：MuSiQue主导特征是query长度，HoVer是hop1-top3。  

**最值得记住的一句话**  
检索分数分布中蕴含的轻量级结构特征足以构建校准的弃权决策，且这些特征跨领域迁移性极好，无需额外LLM推理即可在检索阶段拦截大概率失败的多跳查询。
