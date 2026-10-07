---
title: Towards In-Parameter Memory Augmentation for Large Language Models
title_zh: 面向大语言模型的参数内记忆增强
authors:
- Haoyu Huang
- Zhongwei Xie
- Jiaxin Bai
- Yisen Gao
- Hong Ting Tsang
- Wuganjing Song
- Huihao Jing
- Yufei Li
- Yangqiu Song
affiliations:
- The Hong Kong University of Science and Technology
- Hong Kong Baptist University
arxiv_id: '2610.08630'
url: https://arxiv.org/abs/2610.08630
pdf_url: https://arxiv.org/pdf/2610.08630
published: '2026-10-05'
collected: '2026-10-07'
category: LLM
direction: LLM 参数化记忆增强综述
tags:
- In-Parameter Memory
- LLM Memory
- Adapters
- Survey
- Parametric Memory
one_liner: 以参数放置与获取时间为两个正交轴，系统梳理部署期 LLM 参数化记忆方法
practical_value: '- 在生成式推荐/对话 Agent 中，用 LoRA 或 prefix 参数封装长期用户偏好、商品知识或交互经验，替代每次拼接长历史，可显著降低
  prompt token 与重复编码成本；在线更新 LoRA 可以跨会话沉淀用户兴趣。

  - 按数据形态选择参数放置：稳定领域事实/类目属性适合固化在 FFN 或 MLP 层；时序行为、短期兴趣更适合 Attention 或 Hybrid 放置，离线训练
  adapter 作为商品/类目记忆库，请求时即插即用。

  - 与 ICL 协同：把长期稳定知识放进参数，短期促销、会话上下文仍走 ICL，减少上下文占用；多租户/多活动场景要评估 LoRA 合并时的 interference，避免用户偏好记忆互相污染。

  - 购物 Agent 可用 online LoRA/TempLora 把成功决策、用户反馈实时写入参数形成私有记忆，而非无限堆积历史消息，对长会话和跨 session
  个性化尤其有价值。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 和基于 LLM 的 Agent 需要融入预训练后知识，如领域事实、用户偏好、文档与交互经验。ICL 灵活但占上下文窗口，且随长度增加产生重复离散编码成本；参数内记忆提供互补方案，把可复用记忆表示为模型参数、adapter 或参数式对象，在推理前向过程中组合。

方法：该综述聚焦部署期参数化记忆增强，用两个正交轴组织方法：参数放置（Embedding、Attention、FFN、Hybrid）和参数获取时间（部署中 online、部署前 offline）。论文给出代表性方法地图，包括 KBLaM、AtlasKV、Doc2Lora、TempLora、SHINE、MemoryLLM、Titans 等，并讨论 interference、安全性、与 ICL 协同设计、递归自我改进等开放问题。

结果：作为 survey，没有单一量化指标，核心贡献在于分类框架和边界澄清，为工程选型提供参考。
