---
title: Self-Evolving World Models for LLM Agent Planning
title_zh: 自我进化的世界模型用于 LLM 智能体规划
authors:
- Xuan Zhang
- Wenxuan Zhang
- See-Kiong Ng
- Yang Deng
affiliations:
- National University of Singapore
- Singapore University of Technology and Design
- Singapore Management University
arxiv_id: '2606.30639'
url: https://arxiv.org/abs/2606.30639
pdf_url: https://arxiv.org/pdf/2606.30639
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: 世界模型与记忆自进化增强 LLM Agent 规划
tags:
- LLM Agent
- World Model
- Memory
- Self-evolving
- Planning
- Foresight
one_liner: 提出 WorldEvolver：部署时通过记忆修订增强世界模型预测与规划，无需更新参数
practical_value: '- 在搜索推荐系统中，可构建“世界模型”模拟用户对推荐结果的响应（点击、购买等），替代真实环境试错，加速策略优化。

  - 分层记忆（情景记忆 + 语义记忆）可分别存储实时交互序列与长期行为规则，用于用户兴趣建模和动态策略提升。

  - 选择性前瞻机制过滤低置信预测，避免劣质生成内容污染推荐或排序结果，可迁移至生成式推荐的幻觉控制。

  - 自进化框架支持模型参数冻结下的在线适应性提升，适合电商/广告场景中对延迟敏感的大规模部署。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 LLM Agent 世界模型能预测动作后果，但不可靠预测常被忽略或误导决策；离线微调则面临分布偏移。需要一种部署时自我进化的世界模型。

**方法**：提出 WorldEvolver，保持 agent 和世界模型参数冻结，通过三个模块在测试时修订上下文：(1) **情景记忆**基于检索的真实动作转换进行模拟；(2) **语义记忆**从预测-观测不匹配中提取持久启发式规则；(3) **选择性前瞻**过滤低置信度预测，仅将高置信预测整合进 agent 推理。

**结果**：在 ALFWorld 和 ScienceWorld 上，Word2World 预测准确率和 AgentBoard 下游成功率均优于现有基线，跨越三种 backbone，证明测试时记忆修订同时提升预测保真度与规划性能。
