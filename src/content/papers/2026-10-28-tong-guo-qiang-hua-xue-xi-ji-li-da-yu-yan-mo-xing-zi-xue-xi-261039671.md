---
title: Incentivizing Self-Learning in Large Language Models via Reinforcement Learning
title_zh: 通过强化学习激励大语言模型自学习
authors:
- Lingkai Kong
- Yuzhe Gu
- Haiteng Zhao
- Zijian Wu
- Youqing Fang
- Zhouqi Hua
- Yanan Sun
- Kai Chen
- Wenwei Zhang
affiliations:
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
- MMLab, The Chinese University of Hong Kong
- University of Science and Technology of China
- Fudan University
arxiv_id: '2610.39671'
url: https://arxiv.org/abs/2610.39671
pdf_url: https://arxiv.org/pdf/2610.39671
published: '2026-10-28'
collected: '2026-11-12'
category: Training
direction: RL自学习 · 长上下文推理
tags:
- reinforcement learning
- self-learning
- long-context
- LLM
- reasoning
- RAG
one_liner: 用RL与细粒度奖励训练LLM在长文教科书中自主导航学习，证明准确率从51.5%提升至79.5%
practical_value: '- 可借鉴 BookNavigator 式交互：在电商/Agent 长文档问答或导购中，给模型提供可浏览的目录/章节接口，让模型自主选择阅读路径，而不是一次性把整篇商品手册或政策文档塞进上下文；配合
  RL 训练能学到更高效的检索与信息利用策略

  - 细粒度奖励设计：将最终答案奖励分解为“定位到相关章节/引用了正确原理/中间步骤正确”等子奖励，可稳定长上下文 RL 训练；在业务中可对应把推荐理由或商品对比任务拆解为证据定位、属性提取、答案匹配等环节分别给奖励

  - RL 训练出的自学习策略具有领域泛化性：论文显示对未见教科书和不同任务基准有提升，说明模型学到的是“如何学习”而非死记知识，适合电商知识库频繁更新的场景，可训练
  Agent 动态查阅新产品资料而非频繁重训

  - 在复杂长上下文任务中（如浏览大量用户评论、商品详情、政策文档做决策）用 RL 替代固定检索 RAG，可能获得更鲁棒表现'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 解决陌生领域问题需要紧密结合知识获取与推理，而传统 RAG 只做事实检索/聚合，模型无法像人一样在长文资料中自主学习并应用新原理。

方法：构造基于教科书的数学证明任务，参考答案被隐藏；提出 BookNavigator 接口，让模型能够浏览教科书目录、章节和内容，自主决定阅读路径；用 RL 训练，设计细粒度奖励（如定位相关章节、引用正确原理、证明步骤正确等），激励自学习行为而非仅看最终答案。

关键结果：在 Intern-S2-Preview-35B 上，证明准确率由 51.5% 提升至 79.5%，超过无教科书和固定检索的 RL 基线；在 BrowseComp-Plus 和 CL-bench 长上下文复杂任务上，分别比基座提升 1.7 和 2.3 个百分点；跨领域/跨教科书也有提升，表明 RL 学到的是一种领域无关的自学习策略。
