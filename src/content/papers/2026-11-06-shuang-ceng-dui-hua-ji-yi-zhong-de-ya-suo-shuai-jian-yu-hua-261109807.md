---
title: 'Compaction, decay and reinforcement in a two-tier conversational memory: a
  paired evaluation against retrieval-augmented generation'
title_zh: 双层对话记忆中的压缩、衰减与强化：与检索增强生成的配对评估
authors:
- Osamudiamen Edogun
- Joshua Obigwe
- Irfan Mehmood
affiliations:
- Independent researcher
- University of Bradford
arxiv_id: '2611.09807'
url: https://arxiv.org/abs/2611.09807
pdf_url: https://arxiv.org/pdf/2611.09807
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent 对话记忆压缩策略评估
tags:
- conversational memory
- compaction
- RAG
- paired evaluation
- McNemar's test
- context economy
one_liner: 在 LoCoMo 上配对比较压缩式记忆与 RAG，压缩在事实性问题上准确率高 6.8 个点且省 34% token，但需要原文措辞时落后
practical_value: '- 构建长期对话记忆时，采用双轨制：将历史对话压缩为原子事实（用户偏好、订单事实、优惠信息），同时保留近期原始 transcript
  或关键消息的引用片段；检索时优先事实，必要时回退原文，以适应需要精确措辞的任务（如比价、政策解释）。

  - 如果业务场景的答案多为事实性值（商品属性、价格、库存、用户标签），结构化抽取记忆可显著提升准确率并节省 prompt token（本论文省 34%），适合高并发在线推理成本控制。

  - 评估记忆/检索方案时采用配对设计：同一 store、同一生成器、同一 judge，每行两个预测，用 McNemar exact test 检验分歧样本，以区分模型差异；同时报告按参考答案长度的分层结果，避免评估偏差。

  - 对抗性/需要原文措辞的问题上，纯 compaction 落后，最好设置置信度：当抽取事实与查询关联不明确或需要原文时，自动回退到原文检索。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：长期对话 agent 面临存储决策，RAG 保存全部 transcript 并检索，但长上下文中间退化、无关段落有害；替代方案是将每轮压缩为原子事实并去重链接，然后检索。

**方法关键点**：在 LoCoMo 数据集上，两种记忆存储（compaction vs. RAG）回答全部 1,985 个问题，同一窗口、同一 store、同一生成器和 judge，将两个预测放在同一行，使 512 个分歧问题可用 McNemar exact test 检验显著性。

**关键结果**：在四个可比类别上，压缩得分 71.4% vs 64.6%，领先 6.8 个百分点（p=5.5e-08），且 prompt token 少 34%。加入对抗集后领先降至 2.0，不再显著，因为 baseline 在对抗集领先 14.6。分层分析显示：当参考答案需要 1-2 个源词时，压缩领先 9.6 点；超过 8 个词时落后 3.1 点，token overlap 同向变化，排除 judge 偏差。结论：压缩保留事实断言、丢弃表达方式，所以在答案是“值”时获胜，在答案是“措辞”时失败。另报告四个负结果及功效计算。
