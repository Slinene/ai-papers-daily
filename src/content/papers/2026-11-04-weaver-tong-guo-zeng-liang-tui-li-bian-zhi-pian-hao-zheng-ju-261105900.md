---
title: 'Weaver: Weaving Preference Evidence through Incremental Reasoning for Personalized
  Retrieval-Augmented Generation'
title_zh: Weaver：通过增量推理编织偏好证据的个性化检索增强生成
authors:
- Linyao Zheng
- Zhifang Mao
- Xuhang Shi
affiliations:
- Xi'an Jiaotong University
- Beijing University of Posts and Telecommunications
arxiv_id: '2611.05900'
url: https://arxiv.org/abs/2611.05900
pdf_url: https://arxiv.org/pdf/2611.05900
published: '2026-11-04'
collected: '2026-11-05'
category: RAG
direction: 个性化RAG · 双层图增量检索推理
tags:
- Personalized RAG
- User Preference
- Incremental Retrieval
- Compositional Reasoning
- Memory Graph
one_liner: 提出Weaver框架，用双层检索与推理图增量组合偏好证据，在个性化RAG基准上显著超越基线
practical_value: '- 采用“意图依赖图 + 信息缺口追踪”把用户请求拆解成多个信息依赖项，动态维护缺失信息，适合对话式购物助手/Agent 在多轮交互中规划检索与追问，避免一次性无序检索。

  - 记忆条件增量检索：不把全部历史一次性塞入上下文，而是基于已确认前提逐步定位缺失证据，可借鉴到电商长会话中逐轮精炼用户需求，降低 token 成本和无关信息干扰。

  - 范围感知组合推理：判断哪些历史偏好适用于当前请求，识别互补/替代证据并区分同情境下的冲突声明，可迁移到推荐系统中的偏好冲突消解，例如用户在不同季节/场景下表达相反偏好时，选择适用偏好生成解释。

  - 实验结果（PersonaMem 86.42%，超最强基线 16 个百分点）验证其长程个性化问答有效性，可作为需要长时记忆与推理的个性化 RAG 或客服 Agent
  的架构参考。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**
个性化 RAG 需要从长期交互历史中提取并应用用户偏好，但偏好证据分散在过往对话中，且绑定特定时间和情境。孤立片段难以完整支撑回答，不同条件下表达的偏好容易混淆，导致生成质量下降。

**方法关键点**
Weaver 采用双层检索与推理图：上层为意图依赖图，通过依赖信息缺口追踪表示当前请求所需信息及其先决依赖；下层为记忆条件检索轨迹图，记录检索路径。记忆条件增量检索基于已确认前提和检索线索逐步定位缺失证据，而非一次性全量召回。范围感知组合推理联合解释累积证据，判断哪些偏好适用于当前请求，识别互补与替代支持，并区分同一时间与情境下的冲突声明。推理结论迭代更新任务前提与剩余信息缺口，引导后续检索，最终构建一致的上下文集。

**关键结果**
在个性化 RAG 基准 PersonaMem 和 PrefEval 上，Weaver 分别取得 86.42% 和 91.10% 的准确率，超过最强的评估基线 16.01 和 7.56 个百分点，证明其在证据完整性和回答质量上均有显著提升。
