---
title: 'AgentWebRec: Compact Evidence Fusion over the Agent Web for Personalized Recommendation'
title_zh: AgentWebRec：在用户代理网络中通过紧凑证据融合实现个性化推荐
authors:
- Haoran Qiang
- Guannan Liu
- Liang Zhang
- Junjie Wu
affiliations:
- Beihang University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.01705'
url: https://arxiv.org/abs/2610.01705
pdf_url: https://arxiv.org/pdf/2610.01705
published: '2026-10-01'
collected: '2026-10-02'
category: MultiAgent
direction: Agent Web 多智体协作推荐
tags:
- LLM Agents
- Agent Web
- Recommendation
- Multi-Agent Collaboration
- Evidence Fusion
one_liner: 将推荐重构为 Agent Web 上的任务时证据获取与融合，通过 query-response 交互与置信度门控协作，在不集中代理记忆的情况下提升个性化推荐
practical_value: '- 用户侧 Agent 记忆管理：在不汇聚原始交互数据的前提下，通过 query-response 接口获得紧凑任务证据，适合跨平台/合规场景下的用户偏好建模；可把私有记忆检索改为候选语义锚定
  + 时间衰减 + 预算控制，降低无关上下文稀释。

  - 条件协作机制：用本地决策置信度 κ 作为门控，只有低置信才请求邻居代理提供偏好模式，并将每个邻居返回的 pattern 通过 RefineLLM 融合；这能避免无差别引入噪声，控制推理成本和延迟，适合电商推荐中稀疏用户或长尾场景。

  - 平台侧 item 语义增强：利用语义邻居构造支持集并用 AbstractLLM 丰富候选商品描述，可以作为后续检索的 anchor；对描述不完整、长尾商品尤其有益，可直接借鉴到商品理解、query
  改写或广告创意生成中。

  - 用户代理网络拓扑构建：实验表明基于 item 共现构建用户边优于 persona 相似度或随机边，说明行为共现是更可靠的人群同质性信号；在构建用户人群、Lookalike
  或协同过滤图时可优先采用行为共现作为边权重。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 个人代理正成为用户语义的持久载体，传统的 User-Platform 关系演变为 User-Agent Web-Platform 路径。用户侧信息分散在不同的代理中，只有少部分与当前推荐决策相关，且返回响应语义异构；集中聚合不可行，因此核心问题从“聚合更多用户信息”转为“在有限证据预算下，对当前决策需要获取什么、保留什么”。

## 方法关键点
AgentWebRec 将推荐定义为 Agent Web 上的任务时证据获取与融合，由目标用户代理与平台代理、自身私有记忆、邻居用户代理交互完成，不集中代理记忆。
- 平台语义增强：查询平台代理，对候选 item 检索语义邻居（TopK），用 AbstractLLM 生成增强 item 描述，作为后续检索的语义锚点。
- 私有记忆检索与投影：用增强候选语义和用户 persona 计算语义相关性与时间衰减，选取 top K_M 交互记录，通过 ProjectLLM 投影成任务特定偏好状态，再用 MatchLLM 得到局部决策（预测、置信度、理由）。
- 置信度门控协作：当局部决策置信度低于阈值 θ_κ，将决策上下文抽象成协作查询，邻居代理检索自身相关记忆并用 PatternLLM 输出偏好模式，最后由 RefineLLM 融合，仅当协作证据相关且有补充时才更新局部判断。

## 关键实验结果
在四个 InstructRec 数据集（Books, Goodreads, MovieTV, Yelp）上，与 LightGCN、SASRec、LLMRank、AFL、AgentCF、AgentCF++、MemRec 对比，AgentWebRec 在所有指标上总体最优。典型 H@1：Books 0.5250（vs 最强基线 0.4850）、Goodreads 0.6860（vs 0.2893）、MovieTV 0.5410（vs 0.3610）、Yelp 0.3760（vs 0.3520），H@3/N@5 也有显著提升。消融显示三个证据层均有互补贡献；参数敏感性与边结构实验表明适度预算、基于 item 共现的边构建最优。

## 一句话
“推荐不是聚合更多用户信息，而是面向当前决策有选择地获取并渐进融合任务相关证据。”
