---
title: 'From Clicks to Intent: Cross-Platform Session Embeddings with LLM-Distilled
  Taxonomy for Financial Services Recommendations'
title_zh: 点击到意图：金融推荐中跨平台会话嵌入与LLM意图蒸馏
authors:
- Dianjing Fan
- Yao Li
- Kyaw Hpone Myint
- Dwipam Katariya
- Alexandre G. R. Day
- Pranab Mohanty
- Giri Iyengar
affiliations:
- Capital One
arxiv_id: '2606.26277'
url: https://arxiv.org/abs/2606.26277
pdf_url: https://arxiv.org/pdf/2606.26277
published: '2026-06-24'
collected: '2026-06-26'
category: RecSys
direction: 跨平台会话嵌入与LLM意图蒸馏
tags:
- Session Embedding
- Clickstream
- Intent Taxonomy
- Knowledge Distillation
- Sequential Recommendation
- Financial Services
one_liner: 自监督Transformer编码多模态点击流生成会话嵌入，并蒸馏LLM意图分类器，提升跨平台推荐与可解释性
practical_value: '- **跨平台预登录信号复用**：在电商中可借鉴类似架构，将匿名用户浏览行为（商品查看、停留时间、页面内容）通过自监督Transformer编码为固定维度会话向量，登陆后与已认证用户关联，直接作为召回或排序模型的输入特征，弥补通常被丢弃的预登录意图。

  - **LLM蒸馏提供可解释意图标签**：用聚类采样让LLM迭代生成意图分类体系，再将LLM标注蒸馏为轻量MLP，实现毫秒级意图预测。推荐系统可将蒸馏出的意图标签用于用户分群、冷启动策略（如“正在比较信用卡的用户”），或是作为可解释特征注入排序层，比粗糙的页面计数特征富含更强语义。

  - **双输出设计兼顾性能与分析**：同一嵌入空间既产出高精度稠密向量用于排序/转化预测，又可蒸馏出人可读的意图标签用于业务分析、归因解释，工程上可复用一个Transformer编码器，在损失极小准确率（7%）的前提下大幅降低推理成本与延迟（3000+倍加速）。

  - **无标注自监督预训练**：序列预测任务（预测下一页标题或URL）无标注，简单有效，适合利用大规模浏览点击日志进行预训练，后续可微调用于具体业务目标，降低标注依赖。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
金融服务推荐中，用户预登录网页浏览行为承载着最重要的意图信号，但登录后传统推荐系统往往丢弃这些未认证的行为，原因在于跨平台实体匹配困难，且原有意图表示过于粗糙（如简单页面计数）。同时，金融业对可解释性要求高，现有方法无法同时服务定量推荐任务与定性分析。为此，该工作提出一个双用途系统，从预登录点击流中同时产出稠密会话嵌入和可解释意图标签，实现跨平台个性化。

### 方法要点
- **多模态会话编码**：将预登录点击流事件序列化为特征（页面URL、HTML文本经过Sentence-BERT编码、驻留时间、事件类型等），每个事件经可学习嵌入表和MLP融合，加位置编码，送入Transformer编码器，通过自监督预测页面标题/URL进行训练，最终以平均池化得到64维会话嵌入。
- **聚类增强的LLM意图分类生成**：对会话嵌入做K-Means聚类，从每个簇采样代表性会话，由LLM通过分批次迭代（生成-更新-审核）生成固定数量的意图类别（如“信用卡预审批”“定期利率比较”），再让LLM对采样会话进行多标签标注，得到置信度。所得分类体系通过人工审核保证质量。
- **嵌入空间意图蒸馏**：将LLM标注的置信度作为软标签，训练一个轻量MLP直接从会话嵌入预测意图概率，避免每次推理调用LLM，实现3,000+倍的推理加速，仅损失7%的标注性能。

### 关键结果
在金融服务真实数据（日千万级会话）上验证两个任务：
- **移动首页瓷砖排序**：加入会话嵌入后，最优变体（双向注意力+平均池化）较仅用页面计数特征的基线提升 macro Recall@1 1.88%，降低 Log Loss 13.38%。
- **用户转化预测**：会话嵌入（64维）超越 LLM 教师标签（35维）4.3% micro F1；蒸馏学生模型保留教师 93% 性能，且推理一秒钟处理100K会话，延迟从LLM的2-4秒/会话降至亚毫秒级。

一句话：自监督Transformer学到的点击流会话嵌入能同时驱动高性能排序与可解释意图分类，为推荐系统的定量与定性需求提供了统一方案。
