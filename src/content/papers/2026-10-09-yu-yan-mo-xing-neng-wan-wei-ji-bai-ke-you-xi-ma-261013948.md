---
title: Can Language Models Play the Wikipedia Game?
title_zh: 语言模型能玩维基百科游戏吗？
authors:
- Alexander Hickey
- Joanna Knight
- James Bishop
affiliations:
- The Alan Turing Institute
arxiv_id: '2610.13948'
url: https://arxiv.org/abs/2610.13948
pdf_url: https://arxiv.org/pdf/2610.13948
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM 信息检索导航能力评测
tags:
- LLM
- Information Retrieval
- Benchmark
- Graph Navigation
- Cross-lingual
- Wikipedia Game
one_liner: 构建大规模本地维基与引文图，评测 LLM 跨语言/跨领域导航检索，最佳模型与人类相当但未超越
practical_value: '- 借鉴 Wikipedia Game 评测框架，用本地构建的商品/内容链接图（如商品详情页关联、类目树、百科内链）替代依赖外部
  API，低成本评测 LLM 在业务知识图谱上的多跳导航与检索能力，提前发现跨类目/跨语言失效模式。

  - 在选型 LLM 做检索或 Agent 路径规划时，不要只看平均分：模型在不同语言/话题下排名会反转，业务上应按店铺类目、搜索语言分别评测，针对性部署或路由。

  - 把 TF-IDF 和人工导航成功率作为双 baseline：当 LLM 只是“与人类相当”时，适合做辅助或候选生成，不建议完全替代人工；工程上可设置阈值或
  human-in-the-loop 校验。

  - 若构建商品/论文/类目大规模图并导航，可复用该工作已开源的 Wikipedia 与 OpenAlex 图构建代码，作为本地 RAG/GraphRAG 的路径探索与评测数据集。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：文档集合太大无法索引时，语言模型越来越多地支撑或自动化信息检索，但涉及专业语言或科学知识时很难。用 Wikipedia Game 作为类比任务——玩家只能通过文章内链从一篇随机文章导航到目标文章，可以测试模型在非结构化文档存储中的语义导航能力。

**方法关键点**：
- 构建大规模本地 Wikipedia 页面图和 OpenAlex 论文引用图，提供代码，避免依赖第三方 API；
- 比较 sentence embedding 模型与 LLM（GPT-o3 mini、GPT-4o、QwQ:32B、DeepSeek-R1:70B 等），覆盖五种维基百科语言和五个学术文献数据集；
- 设置人类和 TF-IDF 基准，用 Wikipedia Game 格式进行跨技术、跨语言、跨领域的鲁棒对比。

**关键结果数字**：
- 没有模型显著超过人类；
- 最佳模型（GPT-o3 mini、GPT-4o、QwQ:32B、DeepSeek-R1:70B）达到与人类相当的成功率；
- 模型表现和排名因语言和话题而异，提示实践者不能依赖单一全局最优模型。
