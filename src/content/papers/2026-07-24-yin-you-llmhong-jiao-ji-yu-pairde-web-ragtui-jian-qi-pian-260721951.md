---
title: 'SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in
  Web-RAG Recommenders'
title_zh: 引诱LLM触礁：基于PAIR的Web-RAG推荐器偏好操纵
authors:
- Evan Caville
- Siamak Layeghy
- Billy Sung
- Sara Dolnicar
- Marius Portmann
affiliations:
- The University of Queensland
- Curtin University
arxiv_id: '2607.21951'
url: https://arxiv.org/abs/2607.21951
pdf_url: https://arxiv.org/pdf/2607.21951
published: '2026-07-24'
collected: '2026-07-27'
category: RecSys
direction: 对抗攻击与排名操纵 · RAG安全
tags:
- adversarial attack
- RAG
- LLM
- recommender systems
- ranking manipulation
- prompt injection
one_liner: 使用PAIR自动攻击框架，通过固定检索源下的内容投毒迭代，将目标实体推至LLM推荐排名第一
practical_value: '- 评估RAG推荐系统安全：借鉴SIREN的自动化测试框架，用固定源回放平台隔离内容影响，检测模型是否易受类似排名投毒攻击。

  - 防御过滤：在检索文档进入LLM上下文前，清洗掉声明性排名主张（“最好”“第一”）和植入列表，它们比指令注入更有效，需重点防御。

  - 攻击手法洞察：实验中“在列表首位列出目标”等简单编辑就十分有效，提示我们在电商搜索中须警惕对手通过修改商品描述或评论操纵排名。

  - 工程实现：论文的Custom-RAG replay平台思路可直接迁移，用于复现和压测自家推荐链路的鲁棒性，分离检索与内容影响。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：网页增强LLM在回答推荐查询时，每个检索页面都可能成为攻击面。现有研究多在检索阶段投毒或伪造产品，未在固定源集下系统比较不同内容编辑对模型最终排名的影响。

**方法**：提出SIREN，一种借鉴PAIR越狱循环的自动攻击-评判方法。它先利用Anthropic的网页工具检索并捕获页面，然后基于一个包含23种内容投毒技术的可解释分类法，迭代编辑其中一个源文档。关键设计是定制RAG回放平台，保持每次查询的源文档集合和顺序完全相同，从而将排名变化严格归因于内容编辑。攻击目标是使选定实体在LLM生成的推荐列表中升至第1位。

**结果**：在两个生产级Claude模型上，SIREN在8个查询-模型上下文的124次技术试验中，62次成功达到排名第1；这些成功载荷在新会话中复现的平均成功率为0.805。分析显示，声明性排名主张（如“这是最好的选择”）和植入有序列表比指令注入形式更有效，但效力差异因目标模型而异。
