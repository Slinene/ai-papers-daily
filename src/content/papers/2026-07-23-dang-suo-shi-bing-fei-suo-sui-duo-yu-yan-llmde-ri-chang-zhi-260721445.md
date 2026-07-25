---
title: 'When Trivia Is Not Trivial: Everyday Knowledge Failures in Multilingual LLMs'
title_zh: 当琐事并非琐碎：多语言LLM的日常知识缺口
authors:
- Anna Mosolova
- Djamé Seddah
affiliations:
- INRIA Paris
arxiv_id: '2607.21445'
url: https://arxiv.org/abs/2607.21445
pdf_url: https://arxiv.org/pdf/2607.21445
published: '2026-07-23'
collected: '2026-07-25'
category: Eval
direction: 多语言LLM日常知识评估
tags:
- multilingual
- benchmark
- everyday knowledge
- popular culture
- QA
one_liner: 引入多语言基准TriviaRoomQA，发现LLM在流行文化等日常知识上显著弱于学术知识，且跨语言性能不一致
practical_value: '- 电商对话式推荐或客服系统中若依赖LLM回答关于流行文化、实时新闻等长尾问题，需警惕其知识盲区，建议结合RAG或外部知识库（如商品百科）进行补充

  - 面向多语言市场的推荐文案生成或用户意图理解，同一事实可能因语言变体得到不同回复，需对低资源语言进行适配或注入本地知识

  - 评估LLM在业务场景的适用性时，不应仅依赖学术基准（如MMLU），需自建覆盖日常、长尾、时效性知识的测试集

  - 训练或微调面向消费者的生成式推荐模型时，可以考虑混入文化、娱乐等非结构化语料，以减轻流行领域知识欠缺'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有LLM基准多聚焦学术与推理任务，忽视了日常文化、流行文化、长尾事实等普通用户高频接触的知识，而这些知识在真实对话、推荐解释等场景中至关重要。

**方法**：构建多语言多选题基准**TriviaRoomQA**，覆盖288个主题、6种欧洲语言，含3,300道平行题目及5,340道法语单语题目，系统评估30个7–70B参数的开源LLM。

**关键发现**：
- 模型在历史、地理、数学等知识密集型主题表现较强，但在名人、音乐、电影、新闻等日常流行文化主题准确率大幅下降；
- 同一问题跨语言表现差异显著，表明事实知识的获取并非语言无关，大语种不等于高准确率；
- 当前流行的学术基准无法反映此类知识缺口，模型“高分”并不等同于可靠的日常知识覆盖。

该工作为多语言LLM的实用化部署提供了新的评估维度。
