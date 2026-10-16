---
title: 'HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration'
title_zh: HTN-Orchestrate：面向多智能体编排的分层任务网络框架
authors:
- Yanchen Deng
- Jianguo Huang
- Yao Long Teng
- Yixuan Li
- Handuo Zhang
- Ning Wang
- Liangcai Su
- Xinyu Wang
- Bo An
affiliations:
- Nanyang Technological University
- Apodex
arxiv_id: '2610.22195'
url: https://arxiv.org/abs/2610.22195
pdf_url: https://arxiv.org/pdf/2610.22195
published: '2026-10-15'
collected: '2026-10-16'
category: MultiAgent
direction: 多智能体编排 · 分层任务网络规划
tags:
- Multi-Agent Orchestration
- Hierarchical Task Network
- Result-Informed Planning
- LLM Agents
- Task Decomposition
- Replanning
one_liner: 两层 HTN 解耦全局规划与局部多智能体执行，结果驱动增量分解与重建，在多个 benchmark 超 Agent Team
practical_value: '- **长链路电商/广告调研任务改造成双层 HTN**：上层 Planner 只维护任务树和 sibling prerequisites（例如“先锁定竞品列表/人群画像
  → 再生成文案/定价策略”），不要把整个 campaign 静态拆完；把满足 Ready 条件的叶子交给局部 Orchestrator，减少全局单点规划误差。

  - **结果驱动分解，别一开始拆全量**：对依赖前置结果的节点，等前置返回成功证据后再展开下游 prompt/worker；这能减少无效检索和 token 成本，论文消融显示可降低
  worker invocations 和 Orchestrator rounds，同时精度更好。

  - **失败重建带证据，而不是裸 retry**：设置 epoch 上限和 CollectEvidence，把已验证候选、排除项、部分结论写入 evidence
  summary 再重建任务网络；适合搜推中的归因排查、商品信息补全、竞品调研等长链路任务。

  - **叶子内多 worker 调度模式可直接复用**：局部 Orchestrator 采用 dispatch/wait/finish，支持报告渐进收集、verifier
  校验、并发上限和轮次上限，适合需要“并行检索 + 交叉验证”的推荐解释或广告素材生成。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多智能体 orchestration 存在两难：静态 workflow 能显式建模任务层级和依赖，但分解在运行前固定，中间发现不能改变后续规划；动态派发更灵活，但往往把 decomposition、dispatch、synthesis 耦合在单一 orchestrator，缺少 sibling dependencies 建模。论文用 HTN 分离全局任务规划与局部多智能体执行。

### 方法关键点
- Planner 维护任务网络 T=(V, Eh, Ed)：Eh 表示父子层级，Ed 表示兄弟节点间的 precedence dependencies；Ready(v) 要求 pending 且所有 prerequisites completed。
- 结果驱动规划：Planner 不一次性展开全部子任务，而是在依赖节点的前置结果返回后，才生成该节点的子任务和依赖边。
- 每个可执行叶子交给独立 Orchestrator：调度 researcher/verifier 等 workers，基于上下文、已返回报告和活跃任务做 dispatch/wait/finish；报告渐进收集，支持 evidence-driven follow-up，leaf 级合成 summary/outcome/evidence refs。
- AND 语义向上合成：父节点在所有 child 完成后才 synthesize；当 root unresolved 或失败时，CollectEvidence 提取 supported findings，构建新 epoch 任务网络，最多 1 次 rebuild。

### 关键结果数字
以 DeepSeek-V4.1-Flash 为 backbone，在 BrowseComp、FrontierScience-Research/Olympiad、SUPERChem、PRL-Bench 五个 benchmark 上均超过 ReAct、Agent Team、DeepSeek Harness。BrowseComp 89.73%，比 Agent Team 高 2.45 个百分点；SUPERChem 73.44%，高 4.69 个百分点；FSR 43.33% success，PRL-Bench 46.00 rubric 分。200 题消融中，完整系统 92.0%，去掉结果驱动规划/局部多智能体执行/重建分别降至 90.5%、89.5%、89.5%；共同答对题上中位完成时间只有 Agent Team 的 0.699。

### 最值得记住的一句话
把全局任务结构和局部执行解耦，并让 prerequisite 结果参与后续 decomposition，是同 backbone 小模型超过更大固定流程的关键。
