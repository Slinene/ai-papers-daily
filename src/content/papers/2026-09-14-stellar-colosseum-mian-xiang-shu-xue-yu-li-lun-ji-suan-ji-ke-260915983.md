---
title: 'Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics
  and Theoretical Computer Science'
title_zh: Stellar Colosseum：面向数学与理论计算机科学长程研究的多智能体协作框架
authors:
- Honghao Lin
- David P. Woodruff
- Yuan Deng
- Jieming Mao
- Song Zuo
- Vahab Mirrokni
affiliations:
- Google Research
- Carnegie Mellon University
arxiv_id: '2609.15983'
url: https://arxiv.org/abs/2609.15983
pdf_url: https://arxiv.org/pdf/2609.15983
published: '2026-09-14'
collected: '2026-09-15'
category: MultiAgent
direction: 多智能体长程推理编排
tags:
- Multi-agent
- Theorem Proving
- Inference-time Scaling
- Tree Aggregation
- Falsification
- TCS-Bench
one_liner: 多智能体编排系统，用策略探索、反证与树聚合组织长程研究，在TCS-Bench达71.0%、Codeforces 218/222
practical_value: '- 借鉴“就绪门”控制：将长流程显式分为策略探索、就绪判定、分解、局部求解、全局验证，适合电商/Agent 中的复杂多步任务（如营销策略生成、多跳
  query 解析、自动实验设计），避免过早定型或无限探索。

  - 树聚合保留批判：候选生成后做定向反证，聚合时保留 objections 而非简单投票。可用于多路召回/排序模型集成、多 Agent 辩论，防止共享错误被多数票掩盖；尤其适合需要证据链的
  RAG 与生成式推荐评估。

  - 依赖图分解与局部重试：把大文档/大任务拆成 DAG 子问题，依赖完成才执行，失败只重试局部。推荐 pipeline 中可将检索、粗排、精排、重排解耦，线上某环节退化时只回滚/重跑局部，不改全局。

  - 共享知识目录：跨轮保存定理、失败路径、引用与观察，避免重复踩坑。在推荐用户画像、搜索 query 策略、Agent memory 中可维护历史尝试与用户反馈，形成可复用的结构化记忆。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：语言模型能写出可信的短证明，但长程研究问题中决策序列不确定且相互依赖，一个关键引理失败或后期步骤暴露假设缺失就可能导致整体失败。推理时间 scaling 可以增加采样与检查，但简单的最终答案投票会掩盖共享错误，无法定位缺口或保留失败中的有用信息。需要一套系统化地分配推理、跟踪证据并组织修订。

**方法关键点**：
- 工作流分五阶段：策略探索、就绪门、证明分解、子问题求解、全局验证；就绪门判断策略是否足够具体可分解，而不是等证明完成。
- 阶段内推理：并行生成候选，定向反证（找边界条件、错误蕴含、循环、定理误用等），再通过重叠随机采样树聚合候选与批判记录；聚合是建设性的，保留 objections，避免大 prompt 一次比较过多。
- 证明分解为有向无环依赖图，独立子问题并行求解；局部失败只重试该子问题，不影响已完成部分。
- 跨轮共享知识：保留最近一次尝试的完整证明与验证反馈，知识目录持续记录定理、失败路径、文献与观察。

**关键结果**：
- TCS-Bench（300道来自 FOCS/STOC/SODA 的研究级定理证明题）上，Colosseum 用 Gemini 3.1 Pro 和 Gemini 3.7 Flash 分别达到 54.0% 和 55.0%，交叉模型选择后达 71.0%；单独模型基线 Gemini 3.1 DeepThink 为 52.0%，GPT-5.6 Pro (max) 为 68.0%。
- Codeforces 222 题中，带执行反馈配置解决 218 题，corpus-level performance rating 4263；无执行探针配置 213 题、3918 分。
- 开放研究贡献了 5 个新结果（ℓp subspace coreset、稀疏最小二乘 condition-number barrier、最大内积嵌入维度下界、单阶段 Hadamard 量化、prefix-matrix factorization 下界），并独立复现 Erdős 单位距离突破的架构，生成 46/75 页长证明。

**最值得记住的一句话**：长程推理的关键不是生成更多候选，而是把失败证据和依赖结构保留下来，让验证反馈能定位到局部并触发修订或重新探索。
