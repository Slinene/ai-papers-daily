---
title: 'Sci-Surf: Navigating Scientific Literature Discovery through Human Feedback
  and Intelligent Summarizatio'
title_zh: Sci-Surf：基于人类反馈与智能摘要的科学文献发现导航
authors:
- Fang Guo
- Qi Zhu
- Rongcan Pei
- Shuqi He
- Hui Chen
- Yue Zhang
affiliations:
- Zhejiang University
- Tongji University
- Google Cloud
- Westlake University
arxiv_id: '2608.11973'
url: https://arxiv.org/abs/2608.11973
pdf_url: https://arxiv.org/pdf/2608.11973
published: '2026-08-12'
collected: '2026-08-13'
category: RecSys
direction: LLM用户画像驱动的个性化推荐
tags:
- User Profiling
- Personalization
- LLM
- Human Feedback
- Multimodal Summarization
- Online Evaluation
one_liner: 集成LLM用户画像与多模态论文摘要的意图中心型学术推荐系统，在线评估提升10.4%
practical_value: '- **LLM verbalized profile 可迁移到电商用户画像**：将用户行为序列用 LLM 总结成自然语言画像，作为召回/排序模型的额外特征或
  prompt 上下文，捕捉静态标签难以表达的 nuanced intent。

  - **反馈驱动的画像迭代机制**：真实用户反馈持续 refine profiles，类似在线学习。电商推荐中可设计定期批量更新用户画像，用 LLM 总结近期交互生成动态兴趣描述。

  - **多模态内容理解**：论文图文生成结构化博客式摘要，可借鉴用于商品详情页优化、feed 流内容描述生成、广告创意文案自动生成。

  - **在线评估指标**：采用 predictive alignment 衡量画像与真实偏好的对齐度，比单纯离线 AUC 更有说服力，业务中可引入类似指标评估画像质量。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：科学出版物爆炸式增长，研究人员难以高效发现相关新研究并深入理解。现有学术发现平台依赖静态主题订阅或嵌入相似度，仅提供摘要或短总结，对 nuanced intent modeling 和深度论文总结支持不足。

**方法关键点**：Sci-Surf 提出以意图为中心的知识发现系统，整合反馈驱动的个性化推荐与多模态博客风格论文消化。通过 LLM 生成 verbalized user profile 细化用户意图表示；同时生成结构化摘要，融合全文文本与图表信息，提升论文阅读理解效率。

**关键结果**：端到端 demo 展示完整学术发现流程，真实用户评估表明推荐质量和消化质量均有提升。在一个月在线评估中，集成 verbalized profiles 使预测与现实用户偏好的对齐度平均提高 10.4%。
