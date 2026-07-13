---
title: 'AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification
  of Knowledge Graphs'
title_zh: AgentKGV：双阶段训练优化知识图谱事实验证的 Agentic RAG 框架
authors:
- Yumin Heo
- Hyeon-gu Lee
- Sumin Seo
- Youngjoong Ko
affiliations:
- SungKyunKwan University
- NAVER
arxiv_id: '2607.09092'
url: https://arxiv.org/abs/2607.09092
pdf_url: https://arxiv.org/pdf/2607.09092
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 动态检索 · 知识图谱事实核查
tags:
- Agent
- RAG
- KnowledgeGraph
- FactVerification
- TwoStageTraining
- GRPO
one_liner: 结合动态路由、迭代查询改写与双阶段训练，提升 KG 事实核查准确率并大幅降低检索成本
practical_value: '- 电商商品知识图谱质检：可将该框架用于自动校验商品属性、品牌等三元组事实性，及时发现错误信息。

  - 检索成本敏感场景的 Agent 设计：借鉴 GRPO 轨迹级优化策略，训练搜索策略模型减少不必要的检索轮次，直接降低线上 API 调用成本。

  - 小模型推理稳定性：采用蒸馏 SFT 将大模型推理能力迁移至小模型，用于查询改写与路由，可在资源受限环境保持稳定的 Agent 行为。

  - 动态路由与查询改写模块可拆解复用：在推荐系统的 RAG 检索链路中，当用户查询与文档库存在表面形式不匹配时，可嵌入类似的多轮迭代改写机制。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：大规模自动构建的知识图谱常因抽取错误导致事实性谬误，手工校验成本高昂，单次检索增强生成（RAG）难以处理主语-宾语表面形式不匹配，且多次调用大模型带来高成本。

方法：提出 AgentKGV 框架，利用 LLM 作为智能体进行多轮事实核查。集成动态路由选择工具（搜索或推理）与迭代查询改写，以解决文档级检索中的实体链接偏差。为工业部署，引入双阶段训练：第一阶段用蒸馏 SFT 将大教师模型的推理与改写能力迁移到小模型，保证稳定输出；第二阶段 GRPO 在轨迹级别优化搜索策略，识别不必要检索并提前停止，减少搜索调用次数。

结果：在 T-REx 长尾谓词切分上，框架比单轮 RAG 宏 F1 提升 5.5 个百分点，两阶段训练再进一步提升 9.4 个百分点。GRPO 将平均搜索次数从 3.24 降至 1.63，且准确率无损失。
